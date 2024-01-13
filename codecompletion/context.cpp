/*
    SPDX-FileCopyrightText: 2011-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "context.h"

#include "items/keyword.h"
#include "items/importfile.h"
#include "items/functiondeclaration.h"
#include "items/implementfunction.h"
#include "items/missingincludeitem.h"
#include "items/replacementvariable.h"

#include "worker.h"
#include "helpers.h"
#include "duchain/pythoneditorintegrator.h"
#include "duchain/expressionvisitor.h"
#include "duchain/declarationbuilder.h"
#include "duchain/helpers.h"
#include "duchain/types/unsuretype.h"
#include "duchain/navigation/navigationwidget.h"
#include "parser/astbuilder.h"

#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/util/includeitem.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/codecompletion/codecompletionitemgrouper.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <interfaces/idocumentcontroller.h>
#include <project/projectmodel.h>

#include <QProcess>
#include <QRegularExpression>
#include <KTextEditor/View>
#include <memory>

#include <QDebug>
#include "codecompletiondebug.h"

using namespace KTextEditor;
using namespace KDevelop;

namespace Python {

PythonCodeCompletionContext::ItemTypeHint PythonCodeCompletionContext::itemTypeHint()
{
    return m_itemTypeHint;
}

PythonCodeCompletionContext::CompletionContextType PythonCodeCompletionContext::completionContextType()
{
    return m_operation;
}

std::unique_ptr<ExpressionVisitor> visitorForString(QString str, DUContext* context,
                                                    CursorInRevision scanUntil = CursorInRevision::invalid())
{
    ENSURE_CHAIN_READ_LOCKED
    if ( !context ) {
        return nullptr;
    }
    AstBuilder builder;
    CodeAst::Ptr tmpAst = builder.parse({}, str);
    if ( ! tmpAst ) {
        return nullptr;
    }
    ExpressionVisitor* v = new ExpressionVisitor(context);
    v->enableGlobalSearching();
    if ( scanUntil.isValid() ) {
        v->scanUntil(scanUntil);
        v->enableUnknownNameReporting();
    }
    v->visitCode(tmpAst.data());
    return std::unique_ptr<ExpressionVisitor>(v);
}

void PythonCodeCompletionContext::eventuallyAddGroup(QString name, int priority,
                                                     QList<CompletionTreeItemPointer> items)
{
    if ( items.isEmpty() ) {
        return;
    }
    KDevelop::CompletionCustomGroupNode* node = new KDevelop::CompletionCustomGroupNode(name, priority);
    node->appendChildren(items);
    m_storedGroups << CompletionTreeElementPointer(node);
}

QList< CompletionTreeElementPointer > PythonCodeCompletionContext::ungroupedElements()
{
    return m_storedGroups;
}

static QList<CompletionTreeItemPointer> setOmitParentheses(QList<CompletionTreeItemPointer> items) {
    for ( auto current: items ) {
        if ( auto func = dynamic_cast<FunctionDeclarationCompletionItem*>(current.data()) ) {
            func->setDoNotCall(true);
        }
    }
    return items;
};

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::shebangItems()
{
    KeywordItem::Flags f = (KeywordItem::Flags) ( KeywordItem::ForceLineBeginning | KeywordItem::ImportantItem );
    QList<CompletionTreeItemPointer> shebangGroup;
    if ( m_position.line == 0 && ( m_text.startsWith('#') || m_text.isEmpty() ) ) {
        QString i18ndescr = i18n("insert Shebang line");
        shebangGroup << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this),
                                                    "#!/usr/bin/env python\n", i18ndescr, f));
        shebangGroup << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this),
                                                    "#!/usr/bin/env python3\n", i18ndescr, f));
    }
    else if ( m_position.line <= 1 && m_text.endsWith('#') ) {
        shebangGroup << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this),
                                                    "# -*- coding:utf-8 -*-\n\n", i18n("specify document encoding"), f));
    }
    eventuallyAddGroup(i18n("Add file header"), 1000, shebangGroup);
    return ItemList();
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::functionCallItems()
{
    ItemList resultingItems;

    // gather additional items to show above the real ones (for parameters, and stuff)
    FunctionDeclaration* functionCalled = nullptr;
    DUChainReadLocker lock;
    auto v = visitorForString(m_guessTypeOfExpression, m_duContext.data());
    if ( ! v || ! v->lastDeclaration() ) {
        qCWarning(KDEV_PYTHON_CODECOMPLETION) << "Did not receive a function declaration from expression visitor! Not offering call tips.";
        qCWarning(KDEV_PYTHON_CODECOMPLETION) << "Tried: " << m_guessTypeOfExpression;
        return resultingItems;
    }
    functionCalled = Helper::functionForCalled(v->lastDeclaration().data()).declaration;

    auto current = Helper::resolveAliasDeclaration(functionCalled);
    QList<Declaration*> calltips;
    if ( current && current->isFunctionDeclaration() ) {
        calltips << current;
    }

    auto calltipItems = declarationListToItemList(calltips);
    foreach ( CompletionTreeItemPointer current, calltipItems ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Adding calltip item, at argument:" << m_alreadyGivenParametersCount+1;
        FunctionDeclarationCompletionItem* item = static_cast<FunctionDeclarationCompletionItem*>(current.data());
        item->setAtArgument(m_alreadyGivenParametersCount + 1);
        item->setDepth(depth());
    }

    resultingItems.append(calltipItems);

    // If this is the top-level calltip, add additional items for the default-parameters of the function,
    // but only if all non-default arguments (the mandatory ones) already have been provided.
    // TODO fancy feature: Filter out already provided default-parameters
    if ( depth() != 1 || ! functionCalled ) {
        return resultingItems;
    }
    if ( DUContext* args = DUChainUtils::argumentContext(functionCalled) ) {
        int normalParameters = args->localDeclarations().count() - functionCalled->defaultParametersSize();
        if ( normalParameters > m_alreadyGivenParametersCount ) {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Not at default arguments yet";
            return resultingItems;
        }
        for ( unsigned int i = 0; i < functionCalled->defaultParametersSize(); i++ ) {
            QString paramName = args->localDeclarations().at(normalParameters + i)->identifier().toString();
            resultingItems << CompletionTreeItemPointer(new KeywordItem(CodeCompletionContext::Ptr(m_child),
                                                        paramName + "=", i18n("specify default parameter"),
                                                        KeywordItem::ImportantItem));
        }
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "adding " << functionCalled->defaultParametersSize() << "default args";
    }

    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::defineItems()
{
    DUChainReadLocker lock;
    ItemList resultingItems;
    // Find all base classes of the current class context
    if ( m_duContext->type() != DUContext::Class ) {
        qCWarning(KDEV_PYTHON_CODECOMPLETION) << "current context is not a class context, not offering define completion";
        return resultingItems;
    }
    ClassDeclaration* klass = dynamic_cast<ClassDeclaration*>(m_duContext->owner());
    if ( ! klass ) {
        return resultingItems;
    }
    auto baseClassContexts = Helper::internalContextsForClass(
        klass->type<StructureType>(), m_duContext->topContext()
    );
    // This class' context is put first in the list, so all functions existing here
    // can be skipped.
    baseClassContexts.removeAll(m_duContext.data());
    baseClassContexts.prepend(m_duContext.data());
    Q_ASSERT(baseClassContexts.size() >= 1);
    QList<IndexedString> existingIdentifiers;

    bool isOwnContext = true;
    foreach ( DUContext* c, baseClassContexts ) {
        const auto declarations = c->allDeclarations(
            CursorInRevision::invalid(), m_duContext->topContext(), false
        );
        foreach ( const DeclarationDepthPair& d, declarations ) {
            if ( FunctionDeclaration* funcDecl = dynamic_cast<FunctionDeclaration*>(d.first) ) {
                // python does not have overloads or similar, so comparing the function names is enough.
                const IndexedString identifier = funcDecl->identifier().identifier();
                if ( isOwnContext ) {
                    existingIdentifiers << identifier;
                }

                if ( existingIdentifiers.contains(identifier) ) {
                    continue;
                }
                existingIdentifiers << identifier;
                QStringList argumentNames;
                DUContext* argumentsContext = DUChainUtils::argumentContext(funcDecl);
                if ( argumentsContext ) {
                    foreach ( Declaration* argument, argumentsContext->localDeclarations() ) {
                        argumentNames << argument->identifier().toString();
                    }
                    resultingItems << CompletionTreeItemPointer(new ImplementFunctionCompletionItem(
                        funcDecl->identifier().toString(), argumentNames, m_indent)
                    );
                }
            }
        }
        isOwnContext = false;
    }
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::raiseItems()
{
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Finding items for raise statement";
    DUChainReadLocker lock;
    ItemList resultingItems;
    ReferencedTopDUContext ctx = Helper::getDocumentationFileContext();
    if ( !ctx ) {
        return {};
    }
    QList< Declaration* > declarations = ctx->findDeclarations(QualifiedIdentifier("BaseException"));
    if ( declarations.isEmpty() || ! declarations.first()->abstractType() ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "No valid exception classes found, aborting";
        return resultingItems;
    }
    Declaration* base = declarations.first();
    IndexedType baseType = base->abstractType()->indexed();
    QVector<DeclarationDepthPair> validDeclarations;
    ClassDeclaration* current = nullptr;
    StructureType::Ptr type;
    auto decls = m_duContext->topContext()->allDeclarations(CursorInRevision::invalid(), m_duContext->topContext());
    foreach ( const DeclarationDepthPair d, decls ) {
        current = dynamic_cast<ClassDeclaration*>(d.first);
        if ( ! current || ! current->baseClassesSize() ) {
            continue;
        }
        FOREACH_FUNCTION( const BaseClassInstance& base, current->baseClasses ) {
            if ( base.baseClass == baseType ) {
                validDeclarations << d;
            }
        }
    }
    auto items = declarationListToItemList(validDeclarations);
    if ( m_itemTypeHint == ClassTypeRequested ) {
        // used for except <cursor>, we don't want the parentheses there
        items = setOmitParentheses(items);
    }
    resultingItems.append(items);
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::importFileItems()
{
    DUChainReadLocker lock;
    ItemList resultingItems;
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Preparing to do autocompletion for import...";
    m_maxFolderScanDepth = 1;
    resultingItems << includeItemsForSubmodule("");
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::inheritanceItems()
{
    ItemList resultingItems;
    DUChainReadLocker lock;
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "InheritanceCompletion";
    QVector<DeclarationDepthPair> declarations;
    if ( ! m_guessTypeOfExpression.isEmpty() ) {
        // The class completion is a member access
        auto v = visitorForString(m_guessTypeOfExpression, m_duContext.data());
        if ( v ) {
            auto cls = v->lastType().dynamicCast<StructureType>();
            if ( cls && cls->declaration(m_duContext->topContext()) ) {
                if ( DUContext* internal = cls->declaration(m_duContext->topContext())->internalContext() ) {
                    declarations = internal->allDeclarations(m_position, m_duContext->topContext(), false);
                }
            }
        }
    }
    else {
        declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
    }
    QVector<DeclarationDepthPair> remainingDeclarations;
    foreach ( const DeclarationDepthPair& d, declarations ) {
        Declaration* r = Helper::resolveAliasDeclaration(d.first);
        if ( r && r->topContext() == Helper::getDocumentationFileContext() ) {
            continue;
        }
        if ( r && dynamic_cast<ClassDeclaration*>(r) ) {
            remainingDeclarations << d;
        }
    }
    resultingItems.append(setOmitParentheses(declarationListToItemList(remainingDeclarations)));
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::memberAccessItems()
{
    ItemList resultingItems;
    DUChainReadLocker lock;
    auto v = visitorForString(m_guessTypeOfExpression, m_duContext.data());
    if ( v ) {
        if ( v->lastType() ) {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << v->lastType()->toString();
            resultingItems << getCompletionItemsForType(v->lastType());
        }
        else {
            qCWarning(KDEV_PYTHON_CODECOMPLETION) << "Did not receive a type from expression visitor! Not offering autocompletion.";
        }
    }
    else {
        qCWarning(KDEV_PYTHON_CODECOMPLETION) << "Completion requested for syntactically invalid expression, not offering anything";
    }

    // append eventually stripped postfix, for e.g. os.chdir|
    bool needDot = true;
    foreach ( const QChar& c, m_followingText ) {
        if ( needDot ) {
            m_guessTypeOfExpression.append('.');
            needDot = false;
        }
        if ( c.isLetterOrNumber() || c == '_' ) {
            m_guessTypeOfExpression.append(c);
        }
    }
    if ( resultingItems.isEmpty() && m_fullCompletion ) {
        resultingItems << getMissingIncludeItems(m_guessTypeOfExpression);
    }
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::stringFormattingItems()
{
    if ( ! m_fullCompletion ) {
        return ItemList();
    }
    DUChainReadLocker lock;
    ItemList resultingItems;
    int cursorPosition;
    StringFormatter stringFormatter(CodeHelpers::extractStringUnderCursor(m_text,
                                                                          m_duContext->range().castToSimpleRange(),
                                                                          m_position.castToSimpleCursor(),
                                                                          &cursorPosition));

    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Next identifier id: " << stringFormatter.nextIdentifierId();
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Cursor position in string: " << cursorPosition;

    bool insideReplacementVariable = stringFormatter.isInsideReplacementVariable(cursorPosition);
    RangeInString variablePosition = stringFormatter.getVariablePosition(cursorPosition);

    bool onVariableBoundary = (cursorPosition == variablePosition.beginIndex || cursorPosition == variablePosition.endIndex);
    if ( ! insideReplacementVariable || onVariableBoundary ) {
        resultingItems << CompletionTreeItemPointer(new ReplacementVariableItem(
            ReplacementVariable(QString::number(stringFormatter.nextIdentifierId())),
                                i18n("Insert next positional variable"), false)
        );

        resultingItems << CompletionTreeItemPointer(new ReplacementVariableItem(
            ReplacementVariable("${argument}"),
                                i18n("Insert named variable"), true)
        );

    }

    if ( ! insideReplacementVariable ) {
        return resultingItems;
    }

    const ReplacementVariable *variable = stringFormatter.getReplacementVariable(cursorPosition);

    // Convert the range relative to the beginning of the string to the absolute position
    // in the document. We can safely assume that the replacement variable is on one line,
    // because the regex does not allow newlines inside replacement variables.
    KTextEditor::Range range;
    range.setStart({m_position.line, m_position.column - (cursorPosition - variablePosition.beginIndex)});
    range.setEnd({m_position.line, m_position.column + (variablePosition.endIndex - cursorPosition)});

    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Variable under cursor: " << variable->toString();
    bool hasNumericOnlyOption =     variable->hasPrecision()
                                || (variable->hasType() && variable->type() != 's')
                                ||  variable->align() == '=';

    auto makeFormattingItem = [&variable, &range](const QChar& conversion, const QString& spec,
                                                  const QString& description, bool useTemplateEngine)
    {
        return CompletionTreeItemPointer(
            new ReplacementVariableItem(ReplacementVariable(variable->identifier(), conversion, spec),
                                                            description, useTemplateEngine, range)
        );
    };

    if ( ! variable->hasConversion() && ! hasNumericOnlyOption ) {
        auto addConversionItem = [&](const QChar& conversion, const QString& title) {
            resultingItems.append(makeFormattingItem(conversion, variable->formatSpec(), title, false));
        };
        addConversionItem('s', i18n("Format using str()"));
        addConversionItem('r', i18n("Format using repr()"));
    }

    if ( ! variable->hasFormatSpec() ) {
        auto addFormatSpec = [&](const QString& format, const QString& title, bool useTemplateEngine)
        {
            resultingItems.append(makeFormattingItem(variable->conversion(), format, title, useTemplateEngine));
        };
        addFormatSpec("<${width}", i18n("Format as left-aligned"), true);
        addFormatSpec(">${width}", i18n("Format as right-aligned"), true);
        addFormatSpec("^${width}", i18n("Format as centered"), true);

        // These options don't make sense if we've set conversion using str() or repr()
        if ( ! variable->hasConversion() ) {
            addFormatSpec(".${precision}", i18n("Specify precision"), true);
            addFormatSpec("%", i18n("Format as percentage"), false);
            addFormatSpec("c", i18n("Format as character"), false);
            addFormatSpec("b", i18n("Format as binary number"), false);
            addFormatSpec("o", i18n("Format as octal number"), false);
            addFormatSpec("x", i18n("Format as hexadecimal number"), false);
            addFormatSpec("e", i18n("Format in scientific (exponent) notation"), false);
            addFormatSpec("f", i18n("Format as fixed point number"), false);
        }
    }

    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Resulting items size: " << resultingItems.size();
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::keywordItems()
{
    ItemList resultingItems;
    QStringList keywordItems;
    keywordItems << "def" << "class" << "lambda" << "global" << "import"
                 << "from" << "while" << "for" << "yield" << "return";
    foreach ( const QString& current, keywordItems ) {
        KeywordItem* k = new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), current + " ", "");
        resultingItems << CompletionTreeItemPointer(k);
    }
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::classMemberInitItems()
{
    DUChainReadLocker lock;
    ItemList resultingItems;
    Declaration* decl = duContext()->owner();
    if ( ! decl ) {
        return resultingItems;
    }
    DUContext* args = DUChainUtils::argumentContext(duContext()->owner());
    if ( ! args ) {
        return resultingItems;
    }
    if ( ! decl->isFunctionDeclaration() || decl->identifier() != KDevelop::Identifier("__init__") ) {
        return resultingItems;
    }
    // the current context actually belongs to a constructor
    foreach ( const Declaration* argument, args->localDeclarations() ) {
        const QString argName = argument->identifier().toString();
        // Do not suggest "self.self = self"
        if ( argName == "self" ) {
            continue;
        }
        bool usedAlready = false;
        // Do not suggest arguments which already have a use in the context
        // This is uesful because you can then do { Ctrl+Space Enter Enter } while ( 1 )
        // to initialize all available class variables, without using arrow keys.
        for ( int i = 0; i < duContext()->usesCount(); i++ ) {
            if ( duContext()->uses()[i].usedDeclaration(duContext()->topContext()) == argument ) {
                usedAlready = true;
                break;
            }
        }
        if ( usedAlready ) {
            continue;
        }
        const QString value = "self." + argName + " = " + argName;
        KeywordItem* item = new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this),
                                            value, i18n("Initialize property"),
                                            KeywordItem::ImportantItem);
        resultingItems.append(CompletionTreeItemPointer(item));
    }
    return resultingItems;
}

PythonCodeCompletionContext::ItemList PythonCodeCompletionContext::generatorItems()
{
    ItemList resultingItems;
    QList<KeywordItem*> items;

    DUChainReadLocker lock;
    auto v = visitorForString(m_guessTypeOfExpression, m_duContext.data(), m_position);
    if ( ! v || v->unknownNames().isEmpty() ) {
        return resultingItems;
    }
    if ( v->unknownNames().size() >= 2 ) {
        // we only take the first two, and only two. It gets too much items otherwise.
        QStringList combinations;
        auto names = v->unknownNames().values();
        combinations << names.at(0) + ", " + names.at(1);
        combinations << names.at(1) + ", " + names.at(0);
        foreach ( const QString& c, combinations ) {
            items << new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "" + c + " in ", "");
        }
    }
    foreach ( const QString& n, v->unknownNames() ) {
        items << new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "" + n + " in ", "");
    }

    foreach ( KeywordItem* item, items ) {
        resultingItems << CompletionTreeItemPointer(item);
    }
    return resultingItems;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    m_fullCompletion = fullCompletion;
    ItemList resultingItems;
    
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Line: " << m_position.line;
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Completion type:" << m_operation;
    
    if ( m_operation != FunctionCallCompletion ) {
        resultingItems.append(shebangItems());
    }
    
    // Find all calltips recursively
    if ( parentContext() ) {
        resultingItems.append(parentContext()->completionItems(abort, fullCompletion));
    }
    
    if ( m_operation == PythonCodeCompletionContext::NoCompletion ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "no code completion";
    }
    else if ( m_operation == PythonCodeCompletionContext::GeneratorVariableCompletion ) {
        resultingItems.append(generatorItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::FunctionCallCompletion ) {
        resultingItems.append(functionCallItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::DefineCompletion ) {
        resultingItems.append(defineItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::RaiseExceptionCompletion ) {
        resultingItems.append(raiseItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportFileCompletion ) {
        resultingItems.append(importFileItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportSubCompletion ) {
        DUChainReadLocker lock;
        resultingItems.append(includeItemsForSubmodule(m_searchImportItemsInModule));
    }
    else if ( m_operation == PythonCodeCompletionContext::InheritanceCompletion ) {
        resultingItems.append(inheritanceItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::MemberAccessCompletion ) {
        resultingItems.append(memberAccessItems());
    }
    else if ( m_operation == PythonCodeCompletionContext::StringFormattingCompletion ) {
        resultingItems.append(stringFormattingItems());
    }
    else {
        // it's stupid to display a 3-letter completion item on manually invoked code completion and makes everything look crowded
        if ( m_operation == PythonCodeCompletionContext::NewStatementCompletion && ! fullCompletion ) {
            resultingItems.append(keywordItems());
        }
        if ( m_operation == PythonCodeCompletionContext::NewStatementCompletion ) {
            // Eventually suggest initializing class members from constructor arguments
            resultingItems.append(classMemberInitItems());
        }
        if ( abort ) {
            return ItemList();
        }
        DUChainReadLocker lock;
        auto declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
        foreach ( const DeclarationDepthPair& d, declarations ) {
            if ( d.first && d.first->context()->type() == DUContext::Class ) {
                declarations.removeAll(d);
            }
        }
        resultingItems.append(declarationListToItemList(declarations));
    }
    
    m_searchingForModule.clear();
    m_searchImportItemsInModule.clear();
    
    return resultingItems;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::getMissingIncludeItems(QString forString)
{
    QList<CompletionTreeItemPointer> items;

    // Find all the non-empty name components (mainly, remove the last empty one for "sys." or similar)
    QStringList components = forString.split('.');
    components.removeAll(QString());

    // Check all components are alphanumeric
    QRegularExpression alnum(QRegularExpression::anchoredPattern(QStringLiteral("\\w*")));
    foreach ( const QString& component, components ) {
        QRegularExpressionMatch match = alnum.match(component);
        if ( ! match.hasMatch() ) return items;
    }

    if ( components.isEmpty() ) {
        return items;
    }

    Declaration* existing = Helper::declarationForName(components.first(), m_position,
                                                       DUChainPointer<const DUContext>(m_duContext.data()));
    if ( existing ) {
        // There's already a declaration for the first component; no need to suggest it
        return items;
    }

    // See if there's a module called like that.
    auto found = ContextBuilder::findModulePath(components.join("."), m_workingOnDocument);

    // Check if anything was found
    if ( found.first.isValid() ) {
        // Add items for the "from" and the plain import
        if ( components.size() > 1 && found.second.isEmpty() ) {
            // There's something left for X in "from foo import X",
            // and it's not a declaration inside the module so offer that
            const QString module = QStringList(components.mid(0, components.size() - 1)).join(".");
            const QString text = QString("from %1 import %2").arg(module, components.last());
            MissingIncludeItem* item = new MissingIncludeItem(text, components.last(), forString);
            items << CompletionTreeItemPointer(item);
        }

        const QString module = QStringList(components.mid(0, components.size() - found.second.size())).join(".");
        const QString text = QString("import %1").arg(module);
        MissingIncludeItem* item = new MissingIncludeItem(text, components.last());
        items << CompletionTreeItemPointer(item);
    }

    return items;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::declarationListToItemList(const QVector<DeclarationDepthPair>& declarations, int maxDepth)
{
    QList<CompletionTreeItemPointer> items;
    
    DeclarationPointer currentDeclaration;
    Declaration* checkDeclaration = nullptr;
    int count = declarations.length();
    for ( int i = 0; i < count; i++ ) {
        if ( maxDepth && maxDepth > declarations.at(i).second ) {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Skipped completion item because of its depth";
            continue;
        }
        currentDeclaration = DeclarationPointer(declarations.at(i).first);
        
        PythonDeclarationCompletionItem* item = nullptr;
        checkDeclaration = Helper::resolveAliasDeclaration(currentDeclaration.data());
        if ( ! checkDeclaration ) {
            continue;
        }
        if ( checkDeclaration->isFunctionDeclaration()
                || (checkDeclaration->internalContext() && checkDeclaration->internalContext()->type() == DUContext::Class) ) {
            item = new FunctionDeclarationCompletionItem(currentDeclaration, KDevelop::CodeCompletionContext::Ptr(this));
        }
        else {
            item = new PythonDeclarationCompletionItem(currentDeclaration, KDevelop::CodeCompletionContext::Ptr(this));
        }
        if ( ! m_matchAgainst.isEmpty() ) {
            item->addMatchQuality(identifierMatchQuality(m_matchAgainst, checkDeclaration->identifier().toString()));
        }
        items << CompletionTreeItemPointer(item);
    }
    return items;
}

QList< CompletionTreeItemPointer > PythonCodeCompletionContext::declarationListToItemList(QList< Declaration* > declarations)
{
    QVector<DeclarationDepthPair> fakeItems;
    fakeItems.reserve(declarations.size());
    foreach ( Declaration* d, declarations ) {
        fakeItems << DeclarationDepthPair(d, 0);
    }
    return declarationListToItemList(fakeItems);
}

QList< CompletionTreeItemPointer > PythonCodeCompletionContext::getCompletionItemsForType(AbstractType::Ptr type)
{
    type = Helper::resolveAliasType(type);
    if ( type->whichType() != AbstractType::TypeUnsure ) {
        return getCompletionItemsForOneType(type);
    }

    QList<CompletionTreeItemPointer> result;
    auto unsure = type.staticCast<UnsureType>();
    int count = unsure->typesSize();
    for ( int i = 0; i < count; i++ ) {
        result.append(getCompletionItemsForOneType(unsure->types()[i].abstractType()));
    }
    // Do some weighting: the more often an entry appears, the better the entry.
    // That way, entries which are in all of the types this object could have will
    // be sorted higher up.
    QStringList itemTitles;
    QList<CompletionTreeItemPointer> remove;
    for ( int i = 0; i < result.size(); i++ ) {
        DeclarationPointer decl = result.at(i)->declaration();
        if ( ! decl ) {
            itemTitles.append(QString());
            continue;
        }
        const QString& title = decl->identifier().toString();
        if ( itemTitles.contains(title) ) {
            // there's already an item with that title, increase match quality
            int item = itemTitles.indexOf(title);
            PythonDeclarationCompletionItem* declItem = dynamic_cast<PythonDeclarationCompletionItem*>(result[item].data());
            if ( ! m_fullCompletion ) {
                remove.append(result.at(i));
            }
            if ( declItem ) {
                // Add 1 to the match quality of the first item in the list.
                declItem->addMatchQuality(1);
            }
        }
        itemTitles.append(title);
    }
    foreach ( const CompletionTreeItemPointer& ptr, remove ) {
        result.removeOne(ptr);
    }
    return result;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::getCompletionItemsForOneType(AbstractType::Ptr type)
{
    type = Helper::resolveAliasType(type);
    ReferencedTopDUContext builtinTopContext = Helper::getDocumentationFileContext();
    if ( type->whichType() != AbstractType::TypeStructure ) {
        return ItemList();
    }
    // find properties of class declaration
    auto cls = type.dynamicCast<StructureType>();
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Finding completion items for class type";
    if ( ! cls || ! cls->internalContext(m_duContext->topContext()) ) {
        qCWarning(KDEV_PYTHON_CODECOMPLETION) << "No class type available, no completion offered";
        return QList<CompletionTreeItemPointer>();
    }
    // the PublicOnly will filter out non-explictly defined __get__ etc. functions inherited from object
    auto searchContexts = Helper::internalContextsForClass(cls, m_duContext->topContext(), Helper::PublicOnly);
    QVector<DeclarationDepthPair> keepDeclarations;
    foreach ( const DUContext* currentlySearchedContext, searchContexts ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "searching context " << currentlySearchedContext->scopeIdentifier() << "for autocompletion items";
        const auto declarations = currentlySearchedContext->allDeclarations(CursorInRevision::invalid(),
                                                                                                m_duContext->topContext(),
                                                                                                false);
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "found" << declarations.length() << "declarations";

        // filter out those which are builtin functions, and those which were imported; we don't want those here
        // also, discard all magic functions from autocompletion
        // TODO rework this, it's maybe not the most elegant solution possible
        // TODO rework the magic functions thing, I want them sorted at the end of the list but KTE doesn't seem to allow that
        foreach ( const DeclarationDepthPair& current, declarations ) {
            if ( current.first->context() != builtinTopContext && ! current.first->identifier().identifier().str().startsWith("__") ) {
                keepDeclarations.append(current);
            }
            else {
                qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Discarding declaration " << current.first->toString();
            }
        }
    }
    return declarationListToItemList(keepDeclarations);
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::findIncludeItems(IncludeSearchTarget item)
{
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "TARGET:" << item.directory.path() << item.remainingIdentifiers;
    QDir currentDirectory(item.directory.path());
    QFileInfoList contents = currentDirectory.entryInfoList(QStringList(), QDir::Files | QDir::Dirs | QDir::NoDotAndDotDot);
    bool atBottom = item.remainingIdentifiers.isEmpty();
    QList<CompletionTreeItemPointer> items;
    
    QString sourceFile;
    
    if ( item.remainingIdentifiers.isEmpty() ) {
        // check for the __init__ file
        QFileInfo initFile(item.directory.path(), "__init__.py");
        if ( initFile.exists() ) {
            IncludeItem init;
            init.basePath = item.directory;
            init.isDirectory = true;
            init.name = "";
            if ( ! item.directory.fileName().contains('-') ) {
                // Do not include items which contain "-", those are not valid
                // modules but instead often e.g. .egg directories
                ImportFileItem* importfile = new ImportFileItem(init);
                importfile->moduleName = item.directory.fileName();
                items << CompletionTreeItemPointer(importfile);
                sourceFile = initFile.filePath();
            }
        }
    }
    else {
        QFileInfo file(item.directory.path(), item.remainingIdentifiers.first() + ".py");
        item.remainingIdentifiers.removeFirst();
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << " CHECK:" << file.absoluteFilePath();
        if ( file.exists() ) {
            sourceFile = file.absoluteFilePath();
        }
    }
    
    if ( ! sourceFile.isEmpty() ) {
        IndexedString filename(sourceFile);
        TopDUContext* top = DUChain::self()->chainForDocument(filename);
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << top;
        DUContext* c = internalContextForDeclaration(top, item.remainingIdentifiers);
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "  GOT:" << c;
        if ( c ) {
            // tell function declaration items not to add brackets
            items << setOmitParentheses(declarationListToItemList(c->localDeclarations().toList()));
        }
        else {
            // do better next time
            DUChain::self()->updateContextForUrl(filename, TopDUContext::AllDeclarationsAndContexts);
        }
    }
    
    if ( atBottom ) {
        // append all python files in the directory
        foreach ( QFileInfo file, contents ) {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << " > CONTENT:" << file.absolutePath() << file.fileName();
            if ( file.isFile() ) {
                if ( file.fileName().endsWith(".py") || file.fileName().endsWith(".so") ) {
                    IncludeItem fileInclude;
                    fileInclude.basePath = item.directory;
                    fileInclude.isDirectory = false;
                    fileInclude.name = file.fileName().mid(0, file.fileName().length() - 3); // remove ".py"
                    ImportFileItem* import = new ImportFileItem(fileInclude);
                    import->moduleName = fileInclude.name;
                    items << CompletionTreeItemPointer(import);
                }
            }
            else if ( ! file.fileName().contains('-') ) {
                IncludeItem dirInclude;
                dirInclude.basePath = item.directory;
                dirInclude.isDirectory = true;
                dirInclude.name = file.fileName();
                ImportFileItem* import = new ImportFileItem(dirInclude);
                import->moduleName = dirInclude.name;
                items << CompletionTreeItemPointer(import);
            }
        }
    }
    return items;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::findIncludeItems(QList< Python::IncludeSearchTarget > items)
{
    QList<CompletionTreeItemPointer> results;
    foreach ( const IncludeSearchTarget& item, items ) {
        results << findIncludeItems(item);
    }
    return results;
}

DUContext* PythonCodeCompletionContext::internalContextForDeclaration(TopDUContext* topContext, QStringList remainingIdentifiers)
{
    Declaration* d = nullptr;
    DUContext* c = topContext;
    if ( ! topContext ) {
        return nullptr;
    }
    if ( remainingIdentifiers.isEmpty() ) {
        return topContext;
    }
    do {
        QList< Declaration* > decls = c->findDeclarations(QualifiedIdentifier(remainingIdentifiers.first()));
        remainingIdentifiers.removeFirst();
        if ( decls.isEmpty() ) {
            return nullptr;
        }
        d = decls.first();
        if ( (c = d->internalContext()) ) {
            if ( remainingIdentifiers.isEmpty() ) {
                return c;
            }
        }
        else return nullptr;
        
    } while ( d && ! remainingIdentifiers.isEmpty() );
    return nullptr;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::includeItemsForSubmodule(QString submodule)
{
    auto searchPaths = Helper::getSearchPaths(m_workingOnDocument);
    
    QStringList subdirs;
    if ( ! submodule.isEmpty() ) {
        subdirs = submodule.split(".");
    }
    
    Q_ASSERT(! subdirs.contains(""));
    
    QList<IncludeSearchTarget> foundPaths;
    
    // this is a bit tricky. We need to find every path formed like /.../foo/bar for
    // a query string ("submodule" variable) like foo.bar
    // we also need paths like /foo.py, because then bar is probably a module in that file.
    // Thus, we first generate a list of possible paths, then match them against those which actually exist
    // and then gather all the items in those paths.
    
    foreach ( QUrl currentPath, searchPaths ) {
        auto d = QDir(currentPath.path());
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Searching: " << currentPath << subdirs;
        int identifiersUsed = 0;
        foreach ( const QString& subdir, subdirs ) {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << "changing into subdir" << subdir;
            if ( ! d.cd(subdir) ) {
                break;
            }
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << d.absolutePath() << d.exists();
            identifiersUsed++;
        }
        QStringList remainingIdentifiers = subdirs.mid(identifiersUsed, -1);
        foundPaths.append(IncludeSearchTarget(QUrl::fromLocalFile(d.absolutePath()), remainingIdentifiers));
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Found path:" << d.absolutePath() << remainingIdentifiers << subdirs;
    }
    return findIncludeItems(foundPaths);
}

PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& remainingText,
                                                         QString calledFunction,
                                                         int depth, int alreadyGivenParameters,
                                                         CodeCompletionContext* child)
    : CodeCompletionContext(context, remainingText, CursorInRevision::invalid(), depth)
    , m_operation(FunctionCallCompletion)
    , m_itemTypeHint(NoHint)
    , m_child(child)
    , m_guessTypeOfExpression(calledFunction)
    , m_alreadyGivenParametersCount(alreadyGivenParameters)
    , m_fullCompletion(false)
{
    ExpressionParser p(remainingText);
    summonParentForEventualCall(p.popAll(), remainingText);
}

void PythonCodeCompletionContext::summonParentForEventualCall(TokenList allExpressions, const QString& text)
{
    DUChainReadLocker lock;
    int offset = 0;
    while ( true ) {
        QPair<int, int> nextCall = allExpressions.nextIndexOfStatus(ExpressionParser::EventualCallFound, offset);
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "next call:" << nextCall;
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << allExpressions.toString();
        if ( nextCall.first == -1 ) {
            // no more eventual calls
            break;
        }
        offset = nextCall.first;
        allExpressions.reset(offset);
        TokenListEntry eventualFunction = allExpressions.weakPop();
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << eventualFunction.expression << eventualFunction.status;
        // it's only a call if a "(" bracket is followed (<- direction) by an expression.
        if ( eventualFunction.status != ExpressionParser::ExpressionFound ) {
            continue; // not a call, try the next opening "(" bracket
        }
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Call found! Creating parent-context.";
        // determine the amount of "free" commas in between
        allExpressions.reset();
        int atParameter = 0;
        for ( int i = 0; i < offset-1; i++ ) {
            TokenListEntry entry = allExpressions.weakPop();
            if ( entry.status == ExpressionParser::CommaFound ) {
                atParameter += 1;
            }
            // clear the param count for something like "f([1, 2, 3" (it will be cleared when the "[" is read)
            if ( entry.status == ExpressionParser::InitializerFound || entry.status == ExpressionParser::EventualCallFound ) {
                atParameter = 0;
            }
        }
        m_parentContext = new PythonCodeCompletionContext(m_duContext,
                                                            text.mid(0, eventualFunction.charOffset),
                                                            eventualFunction.expression, depth() + 1,
                                                            atParameter, this
                                                            );
        break;
    }
    allExpressions.reset(1);
}

// decide what kind of completion will be offered based on the code before the current cursor position
PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text,
                                                         const QString& followingText,
                                                         const KDevelop::CursorInRevision& position,
                                                         int depth, const PythonCodeCompletionWorker* /*parent*/)
    : CodeCompletionContext(context, text, position, depth)
    , m_operation(PythonCodeCompletionContext::DefaultCompletion)
    , m_itemTypeHint(NoHint)
    , m_child(nullptr)
    , m_followingText(followingText)
    , m_position(position)
{
    m_workingOnDocument = context->topContext()->url().toUrl();
    QString textWithoutStrings = CodeHelpers::killStrings(text);
    
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << text << position << context->localScopeIdentifier().toString() << context->range();
    
    QPair<QString, QString> beforeAndAfterCursor = CodeHelpers::splitCodeByCursor(text,
                                                                                  context->range().castToSimpleRange(),
                                                                                  position.castToSimpleCursor());

    // check if the current position is inside a multi-line comment -> no completion if this is the case
    CodeHelpers::EndLocation location = CodeHelpers::endsInside(beforeAndAfterCursor.first);
    if ( location == CodeHelpers::Comment ) {
        m_operation = PythonCodeCompletionContext::NoCompletion;
        return;
    }
    else if ( location == CodeHelpers::String ) {
        m_operation = PythonCodeCompletionContext::StringFormattingCompletion;
        return;
    }
    
    // The expression parser used to determine the type of completion required.
    ExpressionParser parser(textWithoutStrings);
    TokenList allExpressions = parser.popAll();
    allExpressions.reset(1);
    ExpressionParser::Status firstStatus = allExpressions.last().status;
    
    // TODO reuse already calculated information
    FileIndentInformation indents(text);
    
    DUContext* currentlyChecked = context.data();
    // This will set the line to use for the completion to the beginning of the expression.
    // In reality, the line we're in might mismatch the beginning of the current expression,
    // for example in multi-line list initializers.
    int currentlyCheckedLine = position.line - text.mid(text.length() - allExpressions.first().charOffset).count('\n');
    
    // The following code will check whether the DUContext directly at the cursor should be used, or a previous one.
    // The latter might be the case if there's code like this:
    /* class foo():
     * ..pass
     * .
     * ..# completion requested here; note that there's less indent in the previous line!
     * */
    // In that case, the DUContext of "foo" would end at line 2, but should still be used for completion.
    {
        DUChainReadLocker lock(DUChain::lock());
        while ( currentlyChecked == context.data() && currentlyCheckedLine >= 0 ) {
            currentlyChecked = context->topContext()->findContextAt(CursorInRevision(currentlyCheckedLine, 0), true);
            currentlyCheckedLine -= 1;
        }
        while ( currentlyChecked && context->parentContextOf(currentlyChecked) ) {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << "checking:" << currentlyChecked->range() << currentlyChecked->type();
            // FIXME: "<=" is not really good, it must be exactly one indent-level less
            int offset = position.line-currentlyChecked->range().start.line;
            // If the check leaves the current context, abort.
            if ( offset >= indents.linesCount() ) {
                break;
            }
            if (    indents.indentForLine(indents.linesCount()-1-offset)
                 <= indents.indentForLine(indents.linesCount()-1) )
            {
                qCDebug(KDEV_PYTHON_CODECOMPLETION) << "changing context to" << currentlyChecked->range() 
                        << ( currentlyChecked->type() == DUContext::Class );
                context = currentlyChecked;
                break;
            }
            currentlyChecked = currentlyChecked->parentContext();
        }
    }
    
    m_duContext = context;
    
    QList<ExpressionParser::Status> defKeywords;
    defKeywords << ExpressionParser::DefFound << ExpressionParser::ClassFound;
    
    if ( allExpressions.nextIndexOfStatus(ExpressionParser::EventualCallFound).first != -1 ) {
        // 3 is always the case for "def foo(" or class foo(": one names the function, the other is the keyword
        if ( allExpressions.length() >= 4 && allExpressions.at(1).status == ExpressionParser::DefFound ) {
            // The next thing the user probably wants to type are parameters for his function.
            // We cannot offer completion for this.
            m_operation = NoCompletion;
            return;
        }
        if ( allExpressions.length() >= 4 ) {
            // TODO: optimally, filter out classes we already inherit from. That's a bonus, tough.
            if ( allExpressions.at(1).status == ExpressionParser::ClassFound ) {
                // show only items of type "class" for completion
                if ( allExpressions.at(allExpressions.length()-1).status == ExpressionParser::MemberAccessFound ) {
                    m_guessTypeOfExpression = allExpressions.at(allExpressions.length()-2).expression;
                }
                m_operation = InheritanceCompletion;
                return;
            }
        }
    }
    
    // For something like "func1(3, 5, func2(7, ", we want to show all calltips recursively
    summonParentForEventualCall(allExpressions, textWithoutStrings);
    
    if ( firstStatus == ExpressionParser::MeaninglessKeywordFound ) {
        m_operation = DefaultCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::InFound ) {
        m_operation = DefaultCompletion;
        m_itemTypeHint = IterableRequested;
        return;
    }
    
    if ( firstStatus == ExpressionParser::NoCompletionKeywordFound ) {
        m_operation = NoCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::RaiseFound || firstStatus == ExpressionParser::ExceptFound ) {
        m_operation = RaiseExceptionCompletion;
        if ( firstStatus == ExpressionParser::ExceptFound ) {
            m_itemTypeHint = ClassTypeRequested;
        }
        return;
    }

    if ( firstStatus == ExpressionParser::NothingFound ) {
        m_operation = NewStatementCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::DefFound ) {
        if ( context->type() == DUContext::Class ) {
            m_indent = QString(" ").repeated(indents.indentForLine(indents.linesCount()-1));
            m_operation = DefineCompletion;
        }
        else {
            qCDebug(KDEV_PYTHON_CODECOMPLETION) << "def outside class context";
            m_operation = NoCompletion;
        }
        return;
    }
    
    // The "def in class context" case is handled above already
    if ( defKeywords.contains(firstStatus) ) {
        m_operation = NoCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::ForFound ) {
        int offset = allExpressions.length() - 2; // one for the "for", and one for the general off-by-one thing
        QPair<int, int> nextInitializer = allExpressions.nextIndexOfStatus(ExpressionParser::InitializerFound);
        if ( nextInitializer.first == -1 ) {
            // no opening bracket, so no generator completion.
            m_operation = NoCompletion;
            return;
        }
        // check that all statements in between are part of a generator initializer list
        bool ok = true;
        QStringList exprs;
        int currentOffset = 0;
        while ( ok && offset > currentOffset ) {
            ok = allExpressions.at(offset).status == ExpressionParser::ExpressionFound;
            if ( ! ok ) break;
            exprs.prepend(allExpressions.at(offset).expression);
            offset -= 1;
            ok = allExpressions.at(offset).status == ExpressionParser::CommaFound;
            // the last expression must *not* have a comma
            currentOffset = allExpressions.length() - nextInitializer.first;
            if ( ! ok && currentOffset == offset ) {
                ok = true;
            }
            offset -= 1;
        }
        if ( ok ) {
            m_guessTypeOfExpression = exprs.join(",");
            m_operation = GeneratorVariableCompletion;
            return;
        }
        else {
            m_operation = NoCompletion;
            return;
        }
    }
    
    QPair<int, int> import = allExpressions.nextIndexOfStatus(ExpressionParser::ImportFound);
    QPair<int, int> from = allExpressions.nextIndexOfStatus(ExpressionParser::FromFound);
    int importIndex = import.first;
    int fromIndex = from.first;
    
    if ( importIndex != -1 && fromIndex != -1 ) {
        // it's either "import ... from" or "from ... import"
        // we treat both in exactly the same way. This is not quite correct, as python
        // forbids some combinations. TODO fix this.
        
        // There's two relevant pieces of text, the one between the "from...import" (or "import...from"),
        // and the one behind the "import" or the "from" (at the end of the line).
        // Both need to be extracted and passed to the completion computer.
        QString firstPiece, secondPiece;
        if ( fromIndex > importIndex ) {
            // import ... from
            if ( fromIndex == allExpressions.length() ) {
                // The "from" is the last item in the chain
                m_operation = ImportFileCompletion;
                return;
            }
            firstPiece = allExpressions.at(allExpressions.length() - importIndex - 1).expression;
        }
        else {
            firstPiece = allExpressions.at(allExpressions.length() - fromIndex - 1).expression;
        }
        // might be "from foo import bar as baz, bang as foobar, ..."
        if ( allExpressions.length() > 4 && firstStatus == ExpressionParser::MemberAccessFound ) {
            secondPiece = allExpressions.at(allExpressions.length() - 2).expression;
        }
        
        if ( fromIndex < importIndex ) {
            // if it's "from ... import", swap the two pieces.
            qSwap(firstPiece, secondPiece);
        }
        
        if ( firstPiece.isEmpty() ) {
            m_searchImportItemsInModule = secondPiece;
        }
        else if ( secondPiece.isEmpty() ) {
            m_searchImportItemsInModule = firstPiece;
        }
        else {
            m_searchImportItemsInModule = firstPiece + "." + secondPiece;
        }
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << firstPiece << secondPiece;
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "Got submodule to search:" << m_searchImportItemsInModule << "from text" << textWithoutStrings;
        m_operation = ImportSubCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::FromFound || firstStatus == ExpressionParser::ImportFound ) {
        // it's either "from ..." or "import ...", which both come down to the same completion offered
        m_operation = ImportFileCompletion;
        return;
    }
    
    if ( fromIndex != -1 || importIndex != -1 ) {
        if ( firstStatus == ExpressionParser::CommaFound ) {
            // "import foo.bar, "
            m_operation = ImportFileCompletion;
            return;
        }
        if ( firstStatus == ExpressionParser::MemberAccessFound ) {
            m_operation = ImportSubCompletion;
            m_searchImportItemsInModule = allExpressions.at(allExpressions.length() - 2).expression;
            return;
        }
        // "from foo ..."
        m_operation = NoCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::MemberAccessFound ) {
        TokenListEntry item = allExpressions.weakPop();
        if ( item.status == ExpressionParser::ExpressionFound ) {
            m_guessTypeOfExpression = item.expression;
            m_operation = MemberAccessCompletion;
        }
        else {
            m_operation = NoCompletion;
        }
        return;
    }

    if ( firstStatus == ExpressionParser::EqualsFound && allExpressions.length() >= 2 ) {
        m_operation = DefaultCompletion;
        m_matchAgainst = allExpressions.at(allExpressions.length() - 2).expression;
    }
}

}
