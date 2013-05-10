/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2010 (c) Miquel Canes Gonzalez <miquelcanes@gmail.com>          *
 * Copyright 2011-2013 by Sven Brauch <svenbrauch@googlemail.com>            *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#include "expressionvisitor.h"
#include "types/indexedcontainer.h"
#include "types/variablelengthcontainer.h"
#include "declarations/functiondeclaration.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"
#include "helpers.h"

#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/typeregister.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/ducontext.h>
#include <language/interfaces/iproblem.h>

#include <KLocalizedString>

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

void ExpressionVisitor::encounter(AbstractType::Ptr type, EncounterFlags flags)
{
//     if ( type )
//         kDebug() << "type encountered: " << type->toString();
//     else
//         kDebug() << "unknown type encountered";
    if ( flags & AutomaticallyDetermineDeclaration ) {
        StructureType::Ptr t = type.cast<StructureType>();
        if ( t ) {
            encounterDeclaration(t->declaration(m_ctx->topContext()));
        }
        else {
            encounterDeclaration(0);
        }
    }
    m_lastType.push(encounterPreprocess(type, flags & MergeTypes));
}

template<typename T> void ExpressionVisitor::encounter(TypePtr< T > type, EncounterFlags flags)
{
    encounter(AbstractType::Ptr::staticCast(type), flags);
}

void ExpressionVisitor::encounterDeclaration(DeclarationPointer ptr, bool isAlias)
{
    m_isAlias = isAlias;
    m_lastDeclaration.push(QList<DeclarationPointer>() << ptr);
}

void ExpressionVisitor::encounterDeclarations(QList< DeclarationPointer > ptrs, bool isAlias)
{
    m_isAlias = isAlias;
    m_lastDeclaration.push(ptrs);
}

void ExpressionVisitor::encounterDeclaration(Declaration* ptr, bool isAlias)
{
    m_isAlias = isAlias;
    m_lastDeclaration.push(QList<DeclarationPointer>() << DeclarationPointer(ptr));
}

ExpressionVisitor::ExpressionVisitor(DUContext* ctx, PythonEditorIntegrator* editor)
    : m_forceGlobalSearching(false)
    , m_reportUnknownNames(false)
    , m_scanUntilCursor(CursorInRevision::invalid())
    , m_isAlias(false)
    , m_ctx(ctx)
    , m_editor(editor)
    , m_shouldBeKnown(true)
    , m_parentVisitor(0)
    , m_depth(0)
{
    if ( s_defaultTypes.isEmpty() ) {
        s_defaultTypes.insert(KDevelop::Identifier("True"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("False"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("None"), AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
    }
    Q_ASSERT(m_ctx);
    Q_ASSERT(m_ctx->topContext());
}

ExpressionVisitor::ExpressionVisitor(ExpressionVisitor* parent)
    : m_forceGlobalSearching(parent->m_forceGlobalSearching)
    , m_reportUnknownNames(parent->m_reportUnknownNames)
    , m_scanUntilCursor(parent->m_scanUntilCursor)
    , m_isAlias(false)
    , m_ctx(parent->m_ctx)
    , m_editor(parent->m_editor)
    , m_shouldBeKnown(true)
    , m_parentVisitor(parent)
    , m_depth(parent->m_depth + 1)
{

}

AbstractType::Ptr ExpressionVisitor::unknownType()
{
    return AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
}

void ExpressionVisitor::unknownTypeEncountered() {
    m_isAlias = false;
    encounterDeclaration(0);
    encounter(unknownType());
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
    DUChainReadLocker lock;
    foreach ( const DeclarationPointer& ptr, decls ) {
        result.append(possibleStructureTypes(ptr->abstractType()));
    }
    return result;
}

void ExpressionVisitor::visitAttribute(AttributeAst* node)
{
    ExpressionAst* accessingAttributeOf = node->value;

    ExpressionVisitor v(this);
    v.visitNode(accessingAttributeOf);
    AbstractType::Ptr accessedType = v.lastType();
    QList<AbstractType::Ptr> accessingAttributeOfType;
    if ( accessedType && accessedType->whichType() == AbstractType::TypeUnsure ) {
        UnsureType::Ptr unsure = accessedType.cast<UnsureType>();
        int size = unsure->typesSize();
        DUChainReadLocker lock;
        for ( int i = 0; i < size; i++ ) {
            accessingAttributeOfType << unsure->types()[i].abstractType();
        }
    }
    else {
        accessingAttributeOfType << accessedType;
    }
    
    QList<Declaration*> foundDecls;
    
    // Step 1: Find all matching declarations which are made inside the type of which the accessed object is.
    // Like, for A.B.C where B is an instance of foo, when processing C, find all properties of foo which are called C.
    
    // maybe our attribute isn't a class at all, then that's an error by definition for now
    bool success = false;
    bool haveOneUsefulType = false;
    if ( ! accessingAttributeOfType.isEmpty() ) {
        foreach ( AbstractType::Ptr current, accessingAttributeOfType ) {
            if ( current && current->whichType() != AbstractType::TypeStructure ) {
                continue;
            }
            StructureType::Ptr currentStructure = current.cast<StructureType>();
            if ( Helper::isUsefulType(current) ) {
                haveOneUsefulType = true;
            }
            DUChainReadLocker lock;
            QList<DUContext*> searchContexts = Helper::internalContextsForClass(currentStructure, m_ctx->topContext());
            foreach ( DUContext* currentInternalContext, searchContexts ) {
                if ( currentInternalContext ) {
                    foundDecls.append(currentInternalContext->findDeclarations(QualifiedIdentifier(node->attribute->value),
                                                                               CursorInRevision::invalid(), AbstractType::Ptr(),
                                                                               0, DUContext::DontSearchInParent));
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
    
    // Step 2: Construct the type of the declaration which was found.
    Declaration* d;
    if ( foundDecls.length() > 0 ) {
        DUChainReadLocker lock;
        d = DeclarationPointer(Helper::resolveAliasDeclaration(foundDecls.last())).data();
        if ( ! d ) {
            return unknownTypeEncountered();
        }
        bool isAlias =     dynamic_cast<AliasDeclaration*>(d) || d->isFunctionDeclaration()
                        || dynamic_cast<ClassDeclaration*>(d);
        encounterDeclarations(toSharedPtrList(foundDecls), isAlias);
        encounter(foundDecls.last()->abstractType());
    }
    else {
        return unknownTypeEncountered();
    }
    DUChainReadLocker lock;
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    foreach ( ExpressionAst* c, node->arguments ) {
        AstDefaultVisitor::visitNode(c);
    }
    AstDefaultVisitor::visitNode(node->keywordArguments);
    AstDefaultVisitor::visitNode(node->starArguments);
    
    ExpressionVisitor v(this);
    v.visitNode(node->function);
    Declaration* actualDeclaration = 0;
    FunctionType::Ptr unidentifiedFunctionType;
    if ( ! v.m_isAlias ) {
        if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeFunction ) {
            unidentifiedFunctionType = v.lastType().cast<FunctionType>();
        }
    }
    else {
        actualDeclaration = v.lastDeclaration().data();
    }
    
    if ( unidentifiedFunctionType ) {
        encounter(unidentifiedFunctionType->returnType());
        encounterDeclaration(0);
        return;
    }
    else if ( not actualDeclaration ) {
        m_shouldBeKnown = false;
        return unknownTypeEncountered();
    }
    else {
        DUChainReadLocker lock;
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
            
            bool decoratorFound = false;
            bool typeFound = false;
            if ( funcDecl->decoratorsSize() > 0 ) {
                if ( Helper::findDecoratorByName<FunctionDeclaration>(funcDecl, "getsType") ) {
                    decoratorFound = true;
                    if ( node->function->astType == Ast::AttributeAstType ) {
                        lock.unlock();
                        ExpressionVisitor baseTypeVisitor(this);
                        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
                        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
                        lock.lock();
                        if ( VariableLengthContainer::Ptr t = baseTypeVisitor.lastType().cast<VariableLengthContainer>() ) {
                            AbstractType::Ptr newType = t->contentType().abstractType();
                            return encounter(newType);
                        }
                    }
                }
                if ( Helper::findDecoratorByName<FunctionDeclaration>(funcDecl, "getsList")
                    or Helper::findDecoratorByName<FunctionDeclaration>(funcDecl, "getsListOfKeys")
                ) {
                    decoratorFound = true;
                    if ( node->function->astType == Ast::AttributeAstType ) {
                        lock.unlock();
                        ExpressionVisitor baseTypeVisitor(this);
                        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
                        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
                        lock.lock();
                        if ( VariableLengthContainer::Ptr t = baseTypeVisitor.lastType().cast<VariableLengthContainer>() ) {
                            VariableLengthContainer::Ptr newType = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
                            if ( newType ) {
                                AbstractType::Ptr contentType;
                                if ( Helper::findDecoratorByName<FunctionDeclaration>(funcDecl, "getsList") ) {
                                    contentType = t->contentType().abstractType();
                                }
                                else {
                                    contentType = t->keyType().abstractType();
                                }
                                newType->addContentType(contentType);
                                AbstractType::Ptr resultingType = newType.cast<AbstractType>();
                                return encounter(resultingType);
                            }
                            else return unknownTypeEncountered();
                        }
                    }
                }
                if ( Helper::findDecoratorByName<FunctionDeclaration>(funcDecl, "getsListOfBoth") ) {
                    decoratorFound = true;
                    if ( node->function->astType == Ast::AttributeAstType ) {
                        lock.unlock();
                        ExpressionVisitor baseTypeVisitor(this);
                        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
                        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
                        lock.lock();
                        if ( VariableLengthContainer::Ptr t = baseTypeVisitor.lastType().cast<VariableLengthContainer>() ) {
                            VariableLengthContainer::Ptr newType = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
                            IndexedContainer::Ptr newContents = typeObjectForIntegralType<IndexedContainer>("tuple", m_ctx);
                            if ( newType && newContents ) {
                                AbstractType::Ptr contentType, keyType;
                                contentType = t->contentType().abstractType();
                                if ( ! contentType ) {
                                    contentType = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
                                }
                                keyType = t->keyType().abstractType();
                                if ( ! keyType ) {
                                    keyType = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
                                }
                                newContents->addEntry(keyType);
                                newContents->addEntry(contentType);
                                newType->addContentType(newContents.cast<AbstractType>());
                                AbstractType::Ptr resultingType = newType.cast<AbstractType>();
                                return encounter(resultingType);
                            }
                            else return unknownTypeEncountered();
                        }
                    }
                }
                if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(
                                              funcDecl, "returnContentEqualsContentOf") )
                {
                    decoratorFound = true;
                    int argNum = d->additionalInformation().str().toInt();
                    if ( node->arguments.length() > argNum ) {
                        ExpressionAst* relevantArgument = node->arguments.at(argNum);
                        lock.unlock();
                        ExpressionVisitor v(this);
                        v.visitNode(relevantArgument);
                        lock.lock();
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
                                typeFound = true;
                                return encounter(AbstractType::Ptr(newType));
                            }
                            else if ( type ) {
                                return encounter(type);
                            }
                        }
                    }
                    else if ( type ) {
                        return encounter(type);
                    }
                }
                if ( decoratorFound and not typeFound ) {
                    return unknownTypeEncountered();
                }
            }
            
            // if none of the above decorator-finding methods worked, just use the ordinary return type.
            return encounter(type);
        }
        else if ( classDecl ) {
            encounter(classDecl->abstractType());
            encounterDeclaration(classDecl);
        }
        else {
            if ( actualDeclaration ) {
                kDebug() << "Declaraton " << actualDeclaration->toString() << " is not a class or function declaration";
            }
            return unknownTypeEncountered();
        }
    }
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    AstDefaultVisitor::visitNode(node->value);
    if ( node->slice && node->slice->astType != Ast::IndexAstType ) {
        DUChainReadLocker lock; // only for debug output
        encounterDeclaration(0);
        encounter(lastType());
    }
    else if ( node->slice ) {
        DUChainReadLocker lock;
        if ( IndexedContainer::Ptr indexed = lastType().cast<IndexedContainer>() ) {
            encounterDeclaration(0);
            if ( IndexAst* sliceIndexAst = static_cast<IndexAst*>(node->slice) ) {
                if ( sliceIndexAst->value && sliceIndexAst->value->astType == Ast::NumberAstType ) {
                    NumberAst* number = static_cast<NumberAst*>(sliceIndexAst->value);
                    int sliceIndex = number->value;
                    if ( sliceIndex < 0 && sliceIndex + indexed->typesCount() > 0 ) {
                        sliceIndex += indexed->typesCount();
                    }
                    if ( sliceIndex < indexed->typesCount() && sliceIndex >= 0 ) {
                        return encounter(indexed->typeAt(sliceIndex).abstractType());
                    }
                }
            }
            // the exact index is unknown, use unsure
            encounter(indexed->asUnsureType().cast<AbstractType>());
        }
        else if ( VariableLengthContainer::Ptr variableLength = lastType().cast<VariableLengthContainer>() ) {
            encounterDeclaration(0);
            encounter(variableLength->contentType().abstractType());
        }
    }
    else {
        return unknownTypeEncountered();
    }
}

template<typename T> TypePtr<T> ExpressionVisitor::typeObjectForIntegralType(QString typeDescriptor, DUContext* ctx)
{
    QList<Declaration*> decls = ctx->topContext()->findDeclarations(QualifiedIdentifier(typeDescriptor));
    Declaration* decl = decls.isEmpty() ? 0 : dynamic_cast<Declaration*>(decls.first());
    AbstractType::Ptr type = decl ? decl->abstractType() : AbstractType::Ptr(0);
    return type.cast<T>();
}

void ExpressionVisitor::visitList(ListAst* node)
{
    AstDefaultVisitor::visitList(node);
    DUChainReadLocker lock;
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
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
    encounter<VariableLengthContainer>(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    AstDefaultVisitor::visitDictionaryComprehension(node);
    DUChainReadLocker lock;
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("dict", m_ctx);
    if ( type ) {
        DUContext* comprehensionContext = m_ctx->findContextAt(CursorInRevision(node->startLine, node->startCol + 1));
        lock.unlock();
        Q_ASSERT(comprehensionContext);
        ExpressionVisitor v(this);
        v.m_ctx = m_forceGlobalSearching ? m_ctx->topContext() : comprehensionContext;
        v.visitNode(node->value);
        if ( v.lastType() ) {
            type->addContentType(v.lastType());
        }
        ExpressionVisitor k(this);
        v.m_ctx = m_forceGlobalSearching ? m_ctx->topContext() : comprehensionContext;
        k.visitNode(node->key);
        if ( k.lastType() ) {
            type->addKeyType(k.lastType());
        }
    }
    else {
        return unknownTypeEncountered();
    }
    encounter<VariableLengthContainer>(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitSetComprehension(SetComprehensionAst* node)
{
    Python::AstDefaultVisitor::visitSetComprehension(node);
    DUChainReadLocker lock;
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("set", m_ctx);
    if ( type ) {
        DUContext* comprehensionContext = m_ctx->findContextAt(CursorInRevision(node->startLine, node->startCol+1), true);
        lock.unlock();
        ExpressionVisitor v(this);
        v.m_ctx = m_forceGlobalSearching ? m_ctx->topContext() : comprehensionContext;
        v.visitNode(node->element);
        if ( v.lastType() ) {
            type->addContentType(v.lastType());
        }
    }
    encounter<VariableLengthContainer>(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitListComprehension(ListComprehensionAst* node)
{
    AstDefaultVisitor::visitListComprehension(node);
    DUChainReadLocker lock;
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("list", m_ctx);
    if ( type && ! m_forceGlobalSearching ) { // TODO fixme
        DUContext* comprehensionContext = m_ctx->findContextAt(CursorInRevision(node->startLine, node->startCol + 1), true);
        lock.unlock();
        ExpressionVisitor v(this);
        v.m_ctx = comprehensionContext;
        Q_ASSERT(comprehensionContext);
        v.visitNode(node->element);
        if ( v.lastType() ) {
            type->addContentType(v.lastType());
        }
    }
    else {
        return unknownTypeEncountered();
    }
    encounter<VariableLengthContainer>(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitTuple(TupleAst* node) {
    DUChainReadLocker lock;
    IndexedContainer::Ptr type = typeObjectForIntegralType<IndexedContainer>("tuple", m_ctx);
    if ( type ) {
        foreach ( ExpressionAst* expr, node->elements ) {
            ExpressionVisitor v(this);
            v.visitNode(expr);
            if ( v.lastType() ) {
                type->addEntry(v.lastType());
            }
            else {
                type->addEntry(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
            }
        }
        encounter(type.cast<AbstractType>(), AutomaticallyDetermineDeclaration);
    }
    else {
        kWarning() << "tuple type object is not available";
        return unknownTypeEncountered();
    }
}

void ExpressionVisitor::visitIfExpression(IfExpressionAst* node)
{
    AstDefaultVisitor::visitIfExpression(node);
    if ( node->body and node->orelse ) {
        ExpressionVisitor v(this);
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
    DUChainReadLocker lock;
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("set", m_ctx);
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            type->addContentType(contentVisitor.lastType());
        }
    }
    encounter<VariableLengthContainer>(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    DUChainReadLocker lock;
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("dict", m_ctx);
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    ExpressionVisitor keyVisitor(this);
    if ( type ) {
        Q_ASSERT(type->hasKeyType());
        foreach ( ExpressionAst* content, node->values ) {
            contentVisitor.visitNode(content);
            type->addContentType(contentVisitor.lastType());
        }
        foreach ( ExpressionAst* key, node->keys ) {
            keyVisitor.visitNode(key);
            type->addKeyType(keyVisitor.lastType());
        }
    }
    encounter<VariableLengthContainer>(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitNumber(Python::NumberAst* number)
{
    AbstractType::Ptr type;
    DUChainReadLocker lock;
    if ( number->isInt ) {
        type = typeObjectForIntegralType<AbstractType>("int", m_ctx);
    }
    else {
        type = typeObjectForIntegralType<AbstractType>("float", m_ctx);
    }
    encounter(type, AutomaticallyDetermineDeclaration);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    DUChainReadLocker lock;
    StructureType::Ptr type = typeObjectForIntegralType<StructureType>("str", m_ctx);
    encounter(type, AutomaticallyDetermineDeclaration);
}

RangeInRevision nodeRange(Python::Ast* node)
{
    kDebug() << node->endLine;
    return RangeInRevision(node->startLine, node->startCol, node->endLine,node->endCol);
}

void ExpressionVisitor::addUnknownName(const QString& name)
{
    if ( m_parentVisitor ) {
        m_parentVisitor->addUnknownName(name);
    }
    else {
        if ( ! m_unknownNames.contains(name) ) {
            m_unknownNames.append(name);
        }
    }
}

void ExpressionVisitor::visitName(Python::NameAst* node)
{
    // "True", "False", "None" etc.
    KDevelop::Identifier id(node->identifier->value);
    QHash < KDevelop::Identifier, AbstractType::Ptr >::const_iterator defId = s_defaultTypes.constFind(id);
    if ( defId != s_defaultTypes.constEnd() ) {
        return encounter(*defId);
    }
    
    RangeInRevision range;
    if ( m_scanUntilCursor.isValid() ) {
        range = RangeInRevision(CursorInRevision(0, 0), m_scanUntilCursor);
    }
    else if ( m_forceGlobalSearching ) {
        range = RangeInRevision::invalid();
    }
    else {
        range = RangeInRevision(0, 0, node->endLine, node->endCol);
    }
    DUChainReadLocker lock;
    Declaration* d = Helper::declarationForName(node, QualifiedIdentifier(node->identifier->value),
                                                range, DUContextPointer(m_ctx));
    
    if ( d ) {
        bool isAlias = dynamic_cast<AliasDeclaration*>(d) || d->isFunctionDeclaration() || dynamic_cast<ClassDeclaration*>(d);
        encounterDeclaration(d, isAlias);
        return encounter(d->abstractType());
    }
    else {
        if ( m_reportUnknownNames ) {
            addUnknownName(node->identifier->value);
        }
        return unknownTypeEncountered();
    }
}

void ExpressionVisitor::visitCompare(CompareAst* node)
{
    Python::AstDefaultVisitor::visitCompare(node);
    
    encounterDeclaration(0);
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
}

void ExpressionVisitor::visitBinaryOperation(Python::BinaryOperationAst* node)
{
    QList<Ast::BooleanOperationTypes> booleanOperators;
    
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
    
    encounterDeclaration(0);
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
}

}

