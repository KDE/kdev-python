/*****************************************************************************
 * This file is part of KDDevelop                                            *
 * Copyright 2010 (c) Miquel Canes Gonzalez <miquelcanes@gmail.com>          *
 * Copyright 2011 by Sven Brauch <svenbrauch@googlemail.com>                 *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/

#include <KLocalizedString>

#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/declaration.h>
#include <language/interfaces/iproblem.h>
#include <language/duchain/types/typeregister.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>

#include "pythonduchainexport.h"
#include "expressionvisitor.h"
#include "pythoneditorintegrator.h"
#include "types/variablelengthcontainer.h"
#include "helpers.h"
#include "declarations/functiondeclaration.h"

using namespace KDevelop;
using namespace Python;
using namespace KTextEditor;

namespace Python {

REGISTER_TYPE(IntegralTypeExtended);

QHash<KDevelop::Identifier, KDevelop::AbstractType::Ptr> ExpressionVisitor::s_defaultTypes;

AbstractType::Ptr ExpressionVisitor::encounterPreprocess(AbstractType::Ptr type, bool merge)
{
    type = Helper::resolveType(type);
    AbstractType::Ptr res;
    if ( merge and not m_lastType.isEmpty() ) {
        res = Helper::mergeTypes(m_lastType.pop(), type);
    }
    else {
        res = type;
    }
    return res;
}

void ExpressionVisitor::encounter(AbstractType::Ptr type, bool merge)
{
    if ( type )
        kDebug() << "type encountered: " << type->toString();
    else
        kDebug() << "unknown type encountered";
    m_lastType.push(encounterPreprocess(type, merge));
}

template<typename T> void ExpressionVisitor::encounter(TypePtr< T > type)
{
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::encounterDeclaration(DeclarationPointer ptr)
{
    m_lastDeclaration.push(QList<DeclarationPointer>() << ptr);
}

void ExpressionVisitor::encounterDeclarations(QList< DeclarationPointer > ptrs)
{
    m_lastDeclaration.push(ptrs);
}

void ExpressionVisitor::encounterDeclaration(Declaration* ptr)
{
    m_lastDeclaration.push(QList<DeclarationPointer>() << DeclarationPointer(ptr));
}

ExpressionVisitor::ExpressionVisitor(DUContext* ctx, PythonEditorIntegrator* editor)
    : m_forceGlobalSearching(false), m_ctx(ctx), m_editor(editor), m_shouldBeKnown(true)
{
    if ( s_defaultTypes.isEmpty() ) {
        s_defaultTypes.insert(KDevelop::Identifier("True"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("False"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("None"), AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
    }
    Q_ASSERT(m_ctx);
}

AbstractType::Ptr ExpressionVisitor::unknownType()
{
    return AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
}

void ExpressionVisitor::unknownTypeEncountered() {
    encounterDeclaration(0);
    encounter(unknownType());
}

void ExpressionVisitor::setTypesForEventualCall(DeclarationPointer actualDeclaration, AttributeAst* node, bool extendUnsureTypes)
{
    // if it's a function call, the result of that call will be the return type
    DUChainPointer<ClassDeclaration> classDecl = actualDeclaration.dynamicCast<ClassDeclaration>();
    DUChainPointer<FunctionDeclaration> funcDecl = actualDeclaration.dynamicCast<FunctionDeclaration>();
    kDebug() << "Determining type for eventual function call";
    
    if ( classDecl ) {
        // we denote with this that the last call AST node was not a function, but a class "call"
        // push a null ptr to the call stack so the visitCall function doesn't change the encountered type
        m_callTypeStack.push(encounterPreprocess(classDecl->abstractType(), extendUnsureTypes));
        bool have_ctor = false;
        if ( classDecl->internalContext() ) {
            QList<Declaration*> ctors = classDecl->internalContext()->findDeclarations(QualifiedIdentifier("__init__"));
            if ( not ctors.isEmpty() ) {
                m_callStack.push(DeclarationPointer(ctors.first()));
                have_ctor = true;
            }
        }
        if ( not have_ctor ) {
            m_callStack.push(DeclarationPointer(0));
        }
        return;
    }
    else if ( funcDecl && funcDecl->type<FunctionType>() ) {
        if ( node->belongsToCall ) {
            AbstractType::Ptr type = funcDecl->type<FunctionType>()->returnType();
            kDebug() << "Using function return type: " << ( type ? type->toString() : "(none)" );
            // check for list content stuff
            if ( funcDecl->decoratorsSize() > 0 ) {
                bool decoratorFound = false;
                bool typeFound = false;
                kDebug() << "Got function declaration with decorators, checking for list content type...";
                if ( Helper::findDecoratorByName<FunctionDeclaration>(funcDecl.data(), "getsType") ) {
                    decoratorFound = true;
                    kDebug() << "Found decorator";
                    if ( VariableLengthContainer::Ptr t = lastType().cast<VariableLengthContainer>() ) {
                        kDebug() << "Found container, using type";
                        type = t->contentType().abstractType();
                        typeFound = true;
                    }
                }
                if ( Helper::findDecoratorByName<FunctionDeclaration>(funcDecl.data(), "getsList") ) {
                    decoratorFound = true;
                    kDebug() << "Got getsList decorator, checking container";
                    if ( VariableLengthContainer::Ptr t = lastType().cast<VariableLengthContainer>() ) {
                        kDebug() << "Got container:" << t->toString();
                        VariableLengthContainer::Ptr newType = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
                        newType->addContentType(t->contentType().abstractType());
                        type = newType.cast<AbstractType>();
                        typeFound = true;
                    }
                }
                if ( decoratorFound and not typeFound ) {
                    m_callStack.push(static_cast<DeclarationPointer>(funcDecl));
                    return m_callTypeStack.push(unknownType());
                }
            }
            // otherwise, it's not a container, and the default return type will be used.
            m_callStack.push(static_cast<DeclarationPointer>(funcDecl));
            return m_callTypeStack.push(encounterPreprocess(type, extendUnsureTypes));
        }
        else {
            kDebug() << "function is not being called, using function type";
            return encounter(funcDecl->abstractType(), extendUnsureTypes);
        }
    }
    else {
        return encounter(actualDeclaration->abstractType());
    }
}

QList< TypePtr< StructureType > > ExpressionVisitor::possibleStructureTypes(AbstractType::Ptr type)
{
    QList< TypePtr< StructureType > > result;
    type = Helper::resolveType(type);
    if ( ! type ) {
        return result;
    }
    if ( type->whichType() == KDevelop::AbstractType::TypeUnsure ) {
        AbstractType::Ptr current;
        UnsureType::Ptr possible = type.cast<UnsureType>();
        int amount = possible->typesSize();
        for ( int i = 0; i < amount; i++ ) {
            StructureType::Ptr current = Helper::resolveType(possible->types()[i].abstractType()).cast<StructureType>();
            if ( current ) {
                result << current;
            }
        }
    }
    else {
        StructureType::Ptr c = type.cast<StructureType>();
        if ( c ) {
            result << c;
        }
    }
    return result;
}

QList< TypePtr< StructureType > > ExpressionVisitor::typeListForDeclarationList(QList< DeclarationPointer > decls)
{
    QList<StructureType::Ptr> result;
    foreach ( const DeclarationPointer& ptr, decls ) {
        result.append(possibleStructureTypes(ptr->abstractType()));
    }
    return result;
}

void ExpressionVisitor::visitAttribute(AttributeAst* node)
{
    ExpressionAst* accessingAttributeOf = node->value;
//     Identifier* identifier = 0;
    QList<DeclarationPointer> availableDeclarations;
    
    kDebug() << "Processing attribute: " << node->attribute->value;
    
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol,
                             node->attribute->endLine, node->attribute->endCol + 1);
    
    QList<DeclarationPointer> accessingAttributeOfDeclaration;
    QList< TypePtr< StructureType > > accessingAttributeOfType;
    
    // Step 1: Find out which kind of attribute is before us in the queue, like foo.bar().baz, foo.bar.baz, foo.bar[].baz, etc.
    // Query information about its type or declaration from previously visited stuff.
    Python::AstDefaultVisitor::visitAttribute(node);
    if ( accessingAttributeOf->astType == Ast::AttributeAstType ) {
//         identifier = dynamic_cast<AttributeAst*>(accessingAttributeOf)->attribute;
        // checking for "last" makes sense as the list either contains one invalid declaration,
        // or one or more valid ones (but never valid AND invalid ones)
        if ( ! lastDeclarations().isEmpty() ) {
            availableDeclarations = lastDeclarations();
        }
        else {
            kDebug() << "No type set for accessed attribute";
            m_shouldBeKnown = false;
            return unknownTypeEncountered();
        }
    }
    else if ( accessingAttributeOf->astType == Ast::NameAstType ) {
        availableDeclarations = lastDeclarations();
    }
    else if ( accessingAttributeOf->astType == Ast::CallAstType ) {
        availableDeclarations.clear();
        accessingAttributeOfType.append(possibleStructureTypes(lastType()));
    }
    else if ( accessingAttributeOf->astType == Ast::SliceAstType ) {
        availableDeclarations = lastDeclarations();
    }
    else if ( not lastType().isNull() && lastType().cast<StructureType>() ) {
        accessingAttributeOfType.append(lastType().cast<StructureType>());
    }
    else {
        kWarning() << "Unsupported attribute access method";
        encounterDeclaration(0);
        return unknownTypeEncountered();
    }
    
    // Step 2: Select a declaration from those which were found.
    if ( availableDeclarations.length() > 0 && availableDeclarations.last().data() ) {
        accessingAttributeOfDeclaration = availableDeclarations;
    }
    else if ( accessingAttributeOfType.isEmpty() ) {
        kDebug() << "No declaration found to look up type of attribute in.";
        kDebug() << "call: " << node->belongsToCall;
        encounterDeclaration(0);
        return unknownTypeEncountered();
    }
    
    // Step 3: If no type was found previously, construct it from the Declaration.
    if ( accessingAttributeOfType.isEmpty() ) {
        accessingAttributeOfType = typeListForDeclarationList(accessingAttributeOfDeclaration);
    }
    
    QList<Declaration*> foundDecls;
    
    // Step 4: Find all matching declarations which are made inside the type of which the accessed object is.
    // Like, for A.B.C where B is an instance of foo, when processing C, find all properties of foo which are called C.
    
    // maybe our attribute isn't a class at all, then that's an error by definition for now
    bool success = false;
    bool haveOneUsefulType = false;
    if ( ! accessingAttributeOfType.isEmpty() ) {
        foreach ( StructureType::Ptr currentStructureType, accessingAttributeOfType ) {
            if ( Helper::isUsefulType(currentStructureType.cast<AbstractType>()) ) {
                haveOneUsefulType = true;
            }
            QList<DUContext*> searchContexts = Helper::inernalContextsForClass(currentStructureType, m_ctx->topContext());
            kDebug() << "Searching declarations in contexts: " << searchContexts;
            foreach ( DUContext* currentInternalContext, searchContexts ) {
                if ( currentInternalContext ) {
                    foundDecls.append(currentInternalContext->findDeclarations(QualifiedIdentifier(node->attribute->value), CursorInRevision::invalid()));
                    success = true;
                }
            }
        }
    }
    if ( ! success ) {
        foundDecls.clear();
    }
    if ( ! haveOneUsefulType ) {
        m_shouldBeKnown = false;
    }
    
    // Step 5: Construct the type of the declaration which was found.
    DeclarationPointer actualDeclaration(0);
    if ( foundDecls.length() > 0 ) {
        bool extendUnsure = false;
        // this function evaluates the previously encountered type, so only change it afterwards // |
        foreach ( Declaration* decl, foundDecls ) {                                              // |
            setTypesForEventualCall(DeclarationPointer(decl), node, extendUnsure);               // |
            extendUnsure = true;                                                                 // |
        }                                                                                        // v
        actualDeclaration = DeclarationPointer(Helper::resolveAliasDeclaration(foundDecls.last()));
        encounterDeclarations(toSharedPtrList(foundDecls));
        encounter(foundDecls.last()->abstractType());
    }
    else {
        kDebug() << "No declaration found for attribute";
        encounterDeclaration(0);
        return unknownTypeEncountered();
    }
    kDebug() << "Last encountered type: " << ( lastType().unsafeData() ? lastType()->toString() : "<none>" );
    kDebug() << "VisitAttribute end";
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    KDEBUG_BLOCK
    kDebug();
    kDebug() << "types count BEFORE visitor call: " << m_callTypeStack.size();
    int previousSize = m_callTypeStack.size();
    Python::AstDefaultVisitor::visitCall(node);
    kDebug() << "types count AFTER visitor call: " << m_callTypeStack.size();
    if ( node->function->astType == Ast::AttributeAstType ) {
        // a bit confusing, but visitAttribute() already has taken care of this.
        kDebug() << "checking if type was provided";
        if ( m_callTypeStack.size() > previousSize ) {
            kDebug() << "type was provided";
            AbstractType::Ptr typeptr = m_callTypeStack.pop();
            encounterDeclaration(m_callStack.pop());
            if ( typeptr ) {
                return encounter(typeptr);
            }
            else return unknownTypeEncountered();
        }
        else {
            return unknownTypeEncountered();
        }
    }
    if ( node->function->astType != Ast::NameAstType ) { // TODO we could fix this now
        m_shouldBeKnown = false;
        return unknownTypeEncountered();
    }
    
    NameAst* name = static_cast<NameAst*>(node->function);
    QString functionName = name->identifier->value;
    kDebug() << "Visiting call of function " << functionName;
    
    Declaration* actualDeclaration = Helper::declarationForName(
                                     name, QualifiedIdentifier(functionName), 
                                     RangeInRevision::invalid(), DUContextPointer(m_ctx));
    if ( not actualDeclaration ) {
        kDebug() << "No declaration for " << functionName;
        m_shouldBeKnown = false;
        return unknownTypeEncountered();
    }
    else {
        actualDeclaration = Helper::resolveAliasDeclaration(actualDeclaration);
        ClassDeclaration* classDecl = dynamic_cast<ClassDeclaration*>(actualDeclaration);
        QPair<FunctionDeclarationPointer, bool> d = Helper::functionDeclarationForCalledDeclaration(
                                                    DeclarationPointer(actualDeclaration));
        FunctionDeclaration* funcDecl = d.first.data();
        bool isConstructor = d.second;
        
        if ( funcDecl && funcDecl->type<FunctionType>() ) {
            AbstractType::Ptr type;
            if ( isConstructor and classDecl ) {
                type = classDecl->abstractType();
                encounterDeclaration(classDecl);
            }
            else {
                type = funcDecl->type<FunctionType>()->returnType();
                encounterDeclaration(funcDecl);
            }
            bool success = false;
            if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(
                                              funcDecl, "returnContentEqualsContentOf") ) {
                kDebug() << "Found argument dependent decorator, checking argument type";
                int argNum = d->additionalInformation().str().toInt();
                if ( node->arguments.length() > argNum ) {
                    ExpressionAst* relevantArgument = node->arguments.at(argNum);
                    ExpressionVisitor v(m_ctx);
                    v.visitNode(relevantArgument);
                    if ( v.lastType() ) {
                        VariableLengthContainer* realTarget = 0;
                        if ( VariableLengthContainer* target = dynamic_cast<VariableLengthContainer*>(type.unsafeData()) ) {
                            realTarget = target;
                        }
                        if ( VariableLengthContainer* source = dynamic_cast<VariableLengthContainer*>(v.lastType().unsafeData()) ) {
                            if ( ! realTarget ) {
                                // if the function does not force a return type, just copy the source (like for reversed())
                                realTarget = source;
                            }
                            VariableLengthContainer* newType = static_cast<VariableLengthContainer*>(realTarget->clone());
                            Q_ASSERT(newType);
                            newType->addContentType(source->contentType().abstractType());
                            success = true; // just for clarity, doesn't do anything
                            return encounter(AbstractType::Ptr(newType));
                        }
                    }
                }
            }
            if ( not success ) {
                return encounter(type);
            }
        }
        else if ( classDecl ) {
            encounter(classDecl->abstractType());
            encounterDeclaration(classDecl);
        }
        else {
            kDebug() << "Declaraton for " << functionName << " is not a class or function declaration";
            encounterDeclaration(0);
            return unknownTypeEncountered();
        }
    }
    kDebug() << "Done";
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    AstDefaultVisitor::visitNode(node->value);
    if ( node->slice && node->slice->astType != Ast::IndexAstType ) {
        kDebug() << "Found slice, will use ListType for assignment";
        kDebug() << "LAST DECLARATION:" << lastDeclaration();
        encounterDeclaration(0);
        encounter(lastType());
    }
    else {
        kDebug() << "LAST TYPE for slice access:" << lastType() << ( lastType() ? lastType()->toString() : "<null>" );
        VariableLengthContainer::Ptr t = lastType().cast<VariableLengthContainer>();
        kDebug() << "Is container: " << t;
        if ( ! t ) {
            return unknownTypeEncountered();
        }
        encounterDeclaration(0);
        encounter(t->contentType().abstractType());
    }
}

template<typename T> TypePtr<T> ExpressionVisitor::typeObjectForIntegralType(QString typeDescriptor, DUContext* ctx)
{
    QList<Declaration*> decls = ctx->topContext()->findDeclarations(
        QualifiedIdentifier("__kdevpythondocumentation_builtin_" + typeDescriptor));
    Declaration* decl = decls.isEmpty() ? 0 : dynamic_cast<Declaration*>(decls.first());
    AbstractType::Ptr type = decl ? decl->abstractType() : AbstractType::Ptr(0);
    return type.cast<T>();
}

void ExpressionVisitor::visitList(ListAst* node)
{
    AstDefaultVisitor::visitList(node);
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
    ExpressionVisitor contentVisitor(m_ctx);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            type->addContentType(contentVisitor.lastType());
        }
    }
    else {
        unknownTypeEncountered();
        kWarning() << " [ !!! ] did not get a typetrack container object when expecting one! Fix code / setup.";
    }
    encounterDeclaration(0);
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    AstDefaultVisitor::visitDictionaryComprehension(node);
    kDebug() << "visiting dictionary comprehension";
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("dict", m_ctx);
    if ( type ) {
        DUContext* comprehensionContext = m_ctx->findContextAt(CursorInRevision(node->startLine, node->startCol + 1));
        ExpressionVisitor v(comprehensionContext);
        v.visitNode(node->value);
        if ( v.lastType() ) {
            type->addContentType(v.lastType());
        }
        ExpressionVisitor k(comprehensionContext);
        k.visitNode(node->key);
        if ( v.lastType() ) {
            type->addKeyType(v.lastType());
        }
    }
    else {
        return unknownTypeEncountered();
    }
    encounterDeclaration(0);
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitSetComprehension(SetComprehensionAst* node)
{
    kDebug() << "visiting set comprehension";
    Python::AstDefaultVisitor::visitSetComprehension(node);
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("set", m_ctx);
    if ( type ) {
        DUContext* comprehensionContext = m_ctx->findContextAt(CursorInRevision(node->startLine, node->startCol+1), true);
        ExpressionVisitor v(comprehensionContext);
        v.visitNode(node->element);
        if ( v.lastType() ) {
            type->addContentType(v.lastType());
        }
    }
    encounterDeclaration(0);
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitListComprehension(ListComprehensionAst* node)
{
    kDebug() << "visiting list comprehension";
    AstDefaultVisitor::visitListComprehension(node);
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
    if ( type ) {
        DUContext* comprehensionContext = m_ctx->findContextAt(CursorInRevision(node->startLine, node->startCol + 1), true);
        ExpressionVisitor v(comprehensionContext);
        v.visitNode(node->element);
        if ( v.lastType() ) {
            type->addContentType(v.lastType());
        }
    }
    else {
        unknownTypeEncountered();
    }
    if ( type ) {
        kDebug() << "Got type for List Comprehension:" << type->toString();
    }
    encounterDeclaration(0);
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitTuple(TupleAst* node) {
    AstDefaultVisitor::visitTuple(node);
    AbstractType::Ptr type = typeObjectForIntegralType<AbstractType>("tuple", m_ctx);
    encounterDeclaration(0);
    encounter(type);
}

void ExpressionVisitor::visitIfExpression(IfExpressionAst* node)
{
    AstDefaultVisitor::visitIfExpression(node);
    if ( node->body and node->orelse ) {
        ExpressionVisitor v(m_ctx);
        v.visitNode(node->body);
        AbstractType::Ptr first = v.lastType();
        DeclarationPointer firstDecl = v.lastDeclaration();
        v.visitNode(node->orelse);
        AbstractType::Ptr second = v.lastType();
        DeclarationPointer secondDecl = v.lastDeclaration();
        encounterDeclarations(QList<DeclarationPointer>() << firstDecl << secondDecl);
        encounter(Helper::mergeTypes(first, second));
    }
}

void ExpressionVisitor::visitSet(SetAst* node)
{
    Python::AstDefaultVisitor::visitSet(node);
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("set", m_ctx);
    ExpressionVisitor contentVisitor(m_ctx);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            type->addContentType(contentVisitor.lastType());
        }
    }
    encounterDeclaration(0);
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    AstDefaultVisitor::visitDict(node);
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("dict", m_ctx);
    ExpressionVisitor contentVisitor(m_ctx);
    if ( type ) {
        foreach ( ExpressionAst* content, node->values ) {
            contentVisitor.visitNode(content);
            type->addContentType(contentVisitor.lastType());
        }
    }
    encounterDeclaration(0);
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitNumber(Python::NumberAst* number)
{
    AbstractType::Ptr type;
    if ( number->isInt ) {
        type = typeObjectForIntegralType<AbstractType>("int", m_ctx);
    }
    else {
        type = typeObjectForIntegralType<AbstractType>("float", m_ctx);
    }
    encounterDeclaration(0);
    encounter(type);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    AbstractType::Ptr type = typeObjectForIntegralType<AbstractType>("string", m_ctx);
    encounterDeclaration(0);
    encounter(type);
}

RangeInRevision nodeRange(Python::Ast* node)
{
    kDebug() << node->endLine;
    return RangeInRevision(node->startLine, node->startCol, node->endLine,node->endCol);
}

void ExpressionVisitor::visitName(Python::NameAst* node)
{
    // "True", "False", "None" etc.
    KDevelop::Identifier id(node->identifier->value);
    QHash < KDevelop::Identifier, AbstractType::Ptr >::const_iterator defId = s_defaultTypes.constFind(id);
    if ( defId != s_defaultTypes.constEnd() ) {
        return encounter(*defId);
    }
    
    kDebug() << "Finding declaration for" << node->identifier->value;
    RangeInRevision range;
    if ( ! m_forceGlobalSearching ) {
        range = RangeInRevision(node->startLine, node->startCol, node->endLine, node->endCol);
    }
    else {
        range = RangeInRevision::invalid();
    }
    Declaration* d = Helper::declarationForName(node, QualifiedIdentifier(node->identifier->value), range, DUContextPointer(m_ctx));
    
    if ( d ) {
        /** DEBUG **/
        kDebug() << "Found declaration: " << d->toString() << d
                 << d->abstractType() << dynamic_cast<VariableLengthContainer*>(d->abstractType().unsafeData());
        /** / DEBUG **/
        encounterDeclaration(DeclarationPointer(d));
        return encounter(d->abstractType());
    }
    else {
        kDebug() << "VistName type not found";
        if ( m_reportUnknownNames ) {
            m_unknownNames.append(node->identifier->value);
        }
        return unknownTypeEncountered();
    }
}

void ExpressionVisitor::visitBinaryOperation(Python::BinaryOperationAst* node)
{
    visitNode(node->lhs);
    KDevelop::AbstractType::Ptr leftType = lastType();
    
    visitNode(node->rhs);
    KDevelop::AbstractType::Ptr rightType = lastType();
    
    if ( leftType->indexed() != rightType->indexed() ) {
        return unknownTypeEncountered();
    }
    
    encounterDeclaration(0);
    encounter(leftType); // TODO this is wrong.
}

void ExpressionVisitor::visitUnaryOperation(Python::UnaryOperationAst* node)
{
    visitNode(node->operand);
    
    //FIXME: m_lastValue = m_lastValue;
}

void ExpressionVisitor::visitBooleanOperation(Python::BooleanOperationAst* node)
{
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
    }
    
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
}

}

