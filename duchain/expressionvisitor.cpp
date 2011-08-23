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

using namespace KDevelop;
using namespace Python;
using namespace KTextEditor;

namespace Python {

REGISTER_TYPE(IntegralTypeExtended);

QHash<KDevelop::Identifier, KDevelop::AbstractType::Ptr> ExpressionVisitor::s_defaultTypes;

void ExpressionVisitor::encounter(AbstractType::Ptr type, bool merge)
{
    type = Helper::resolveType(type);
    if ( merge ) {
        m_lastType = Helper::mergeTypes(m_lastType, type);
    }
    else {
        m_lastType = type;
    }
}

template<typename T> void ExpressionVisitor::encounter(TypePtr< T > type)
{
    encounter(AbstractType::Ptr::staticCast(type));
}

Python::ExpressionVisitor::ExpressionVisitor(DUContext* ctx, PythonEditorIntegrator* editor)
    : m_lastType(0), m_ctx(ctx), m_editor(editor), m_shouldBeKnown(true)
{
    if(s_defaultTypes.isEmpty()) {
        s_defaultTypes.insert(KDevelop::Identifier("True"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("False"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("None"), AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
    }
}

void ExpressionVisitor::unknownTypeEncountered() {
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
}

void ExpressionVisitor::setTypesForEventualCall(DeclarationPointer actualDeclaration, AttributeAst* node, bool extendUnsureTypes)
{
    // if it's a function call, the result of that call will be the return type
    // TODO check whether we need to distinguish bettween foo.bar and foo.bar() here
    DUChainPointer<ClassDeclaration> classDecl = actualDeclaration.dynamicCast<ClassDeclaration>();
    DUChainPointer<FunctionDeclaration> funcDecl = actualDeclaration.dynamicCast<FunctionDeclaration>();
    kDebug() << "Determining type for eventual function call";
    
    if ( classDecl ) {
        encounter(classDecl->abstractType(), extendUnsureTypes);
        if ( extendUnsureTypes )
            m_lastAccessedReturnType.push(Helper::mergeTypes(
                m_lastAccessedReturnType.isEmpty() ? AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)) : m_lastAccessedReturnType.pop(),
                classDecl->abstractType()
            ));
        else
            m_lastAccessedReturnType.push(classDecl->abstractType());
    }
    else if ( funcDecl && funcDecl->type<FunctionType>() ) {
        if ( node->belongsToCall ) {
            AbstractType::Ptr type = funcDecl->type<FunctionType>()->returnType();
            kDebug() << "Using function return type: " << ( type ? type->toString() : "(none)" );
            // check for list content stuff
            if ( funcDecl->decoratorsSize() > 0 ) {
                kDebug() << "Got function declaration with decorators, checking for list content type...";
                if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(funcDecl.data(), "getsType") ) {
                    kDebug() << "Found decorator";
                    if ( VariableLengthContainer::Ptr t = lastType().cast<VariableLengthContainer>() ) {
                        kDebug() << "Found container, using type";
                        type = t->contentType().abstractType();
                    }
                    else {
                        m_lastAccessedReturnType.push(AbstractType::Ptr(0));
                        return unknownTypeEncountered();
                    }
                }
            }
            // otherwise, it's not a container, and the default return type will be used.
            encounter(type, extendUnsureTypes);
            if ( extendUnsureTypes ) 
                m_lastAccessedReturnType.push(Helper::mergeTypes(
                    m_lastAccessedReturnType.isEmpty() ? AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)) : m_lastAccessedReturnType.pop(),
                    type
                ));
            else
                m_lastAccessedReturnType.push(type);
        }
        else {
            encounter(funcDecl->abstractType(), extendUnsureTypes);
            if ( extendUnsureTypes )
                m_lastAccessedReturnType.push(Helper::mergeTypes(
                    m_lastAccessedReturnType.isEmpty() ? AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)) : m_lastAccessedReturnType.pop(),
                    funcDecl->abstractType()
                ));
            else
                m_lastAccessedReturnType.push(funcDecl->abstractType()); // TODO check this
        }
    }
    else {
        encounter(actualDeclaration->abstractType());
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
    QList< TypePtr< StructureType > > result;
    foreach ( const DeclarationPointer& ptr, decls ) {
        result.append(possibleStructureTypes(ptr->abstractType()));
    }
    return result;
}

void ExpressionVisitor::visitAttribute(AttributeAst* node)
{
    // check whether this is explicitly imported like "import a.b.c"
    AttributeAst* ptr = node;
    QList<Identifier*> nameComponents;
    bool success = false;
    while ( ptr && ptr->astType == Ast::AttributeAstType ) {
        nameComponents.prepend(ptr->attribute);
        if ( ptr->value && ptr->value->astType == Ast::AttributeAstType ) {
            ptr = static_cast<AttributeAst*>(ptr->value);
        }
        else if ( ptr->value && ptr->value->astType == Ast::NameAstType ) {
            nameComponents.prepend(static_cast<NameAst*>(ptr->value)->identifier);
            ptr = 0;
            success = true;
        }
        else {
            ptr = 0;
        }
    }
    
    kDebug() << "IS DOTTED: " << success;
    
    // this actually is an imported dotted name
    if ( success ) {
        RangeInRevision range = RangeInRevision(nameComponents.first()->startLine, nameComponents.first()->startCol,
                                                nameComponents.first()->endLine, nameComponents.first()->endCol);
        QStringList stringNameComponents;
        foreach ( const Identifier* i, nameComponents ) {
            stringNameComponents.append(i->value);
        }
        QString name = stringNameComponents.join(".");
        DUChainReadLocker lock(DUChain::lock());
        QList<Declaration*> found = m_ctx->findDeclarations(QualifiedIdentifier(name).first(), range.start);
        lock.unlock();
        kDebug() << "Found declarations for dotted name import: " << found;
        if ( ! found.isEmpty() ) {
            Declaration* real = Helper::resolveAliasDeclaration(found.last());
            DeclarationPointer ptr = DeclarationPointer(real);
            setLastAccessedDeclaration(ptr);
            setLastAccessedAttributeDeclaration(ptr);
            DUChainReadLocker lock(DUChain::lock());
            encounter(real->abstractType());
            setTypesForEventualCall(ptr, node);
            return;
        }
        else kDebug() << "None found, defaulting to normal behaviour";
    }
    
    // This is not an imported dotted name, proceed with normal operation
    ExpressionAst* accessingAttributeOf = node->value;
    Identifier* identifier;
    QList<DeclarationPointer> availableDeclarations;
    
    kDebug() << "Processing attribute: " << node->attribute->value;
    
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol, node->attribute->endLine, node->attribute->endCol + 1);
    
    QList<DeclarationPointer> accessingAttributeOfDeclaration;
    QList< TypePtr< StructureType > > accessingAttributeOfType;
    
    // Step 1: Find out which kind of attribute is before us in the queue, like foo.bar().baz, foo.bar.baz, foo.bar[].baz, etc.
    // Query information about its type or declaration from previously visited stuff.
    Python::AstDefaultVisitor::visitAttribute(node);
    if ( accessingAttributeOf->astType == Ast::AttributeAstType ) {
        identifier = dynamic_cast<AttributeAst*>(accessingAttributeOf)->attribute;
        // checking for "last" makes sense as the list either contains one invalid declaration,
        // or one or more valid ones (but never valid AND invalid ones)
        if ( ! m_lastAccessedAttributeDeclaration.isEmpty() && m_lastAccessedAttributeDeclaration.last() ) {
            availableDeclarations = m_lastAccessedAttributeDeclaration;
        }
        else {
            kDebug() << "No type set for accessed attribute";
            m_shouldBeKnown = false;
            return unknownTypeEncountered();
        }
    }
    else if ( accessingAttributeOf->astType == Ast::NameAstType ) {
        availableDeclarations = m_lastAccessedNameDeclaration;
    }
    else if ( accessingAttributeOf->astType == Ast::CallAstType ) {
        availableDeclarations.clear();
        accessingAttributeOfType.append(possibleStructureTypes(m_lastType));
    }
    else if ( m_lastType && m_lastType.cast<StructureType>() ) {
        accessingAttributeOfType.append(m_lastType.cast<StructureType>());
    }
    else {
        kWarning() << "Unsupported attribute access method";
        setLastAccessedAttributeDeclaration(DeclarationPointer(0));
        setLastAccessedDeclaration(DeclarationPointer(0));
        m_lastType = AbstractType::Ptr(0);
        m_shouldBeKnown = false;
        return unknownTypeEncountered();
    }
    
    // Step 2: Select a declaration from those which were found.
    if ( availableDeclarations.length() > 0 && availableDeclarations.last().data() ) {
        accessingAttributeOfDeclaration = availableDeclarations;
    }
    else if ( accessingAttributeOfType.isEmpty() ) {
        kDebug() << "No declaration found to look up type of attribute in.";
        kDebug() << "call: " << node->belongsToCall;
        setLastAccessedAttributeDeclaration(DeclarationPointer(0));
        setLastAccessedDeclaration(DeclarationPointer(0));
        m_lastType = AbstractType::Ptr(0);
        m_shouldBeKnown = false;
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
    success = false;
    bool haveOneUsefulType = false;
    DUChainReadLocker lock(DUChain::lock());
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
        actualDeclaration = DeclarationPointer(Helper::resolveAliasDeclaration(foundDecls.last()));
        m_lastAccessedAttributeDeclaration = toSharedPtrList(foundDecls);
        setLastAccessedDeclaration(toSharedPtrList(foundDecls));
        bool extendUnsure = false;
        foreach ( Declaration* decl, foundDecls ) {
            setTypesForEventualCall(DeclarationPointer(decl), node, extendUnsure);
            extendUnsure = true;
        }
    }
    else {
        kDebug() << "No declaration found for attribute";
        setLastAccessedAttributeDeclaration(DeclarationPointer(0));
        setLastAccessedDeclaration(DeclarationPointer(0));
        return unknownTypeEncountered();
    }
    kDebug() << "Last encountered type: " << ( lastType().unsafeData() ? lastType()->toString() : "<none>" );
    kDebug() << "VisitAttribute end";
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    KDEBUG_BLOCK
    kDebug();
    kDebug() << "types count BEFORE visitor call: " << m_lastAccessedReturnType.size();
    int previousSize = m_lastAccessedReturnType.size();
    Python::AstDefaultVisitor::visitCall(node);
    kDebug() << "types count AFTER visitor call: " << m_lastAccessedReturnType.size();
    // if it's not written like foo() but like foo[3](), then we don't attempt to guess a type
    if ( node->function->astType == Ast::AttributeAstType ) {
        // a bit confusing, but visitAttribute() already has taken care of this.
        kDebug() << "checking if type was provided";
        if ( m_lastAccessedReturnType.size() > previousSize ) {
            kDebug() << "type was provided";
            kDebug() << "applying type" << ( m_lastAccessedReturnType.top() ? m_lastAccessedReturnType.top()->toString() : "(none)" );
            encounter(m_lastAccessedReturnType.pop());
            return;
        }
        else {
            return unknownTypeEncountered();
        }
    }
    if ( node->function->astType != Ast::NameAstType ) {
        m_shouldBeKnown = false;
        return unknownTypeEncountered();
    }
    
    QString functionName = static_cast<NameAst*>(node->function)->identifier->value;
    kDebug() << "Visiting call of function " << functionName;
    
    DUChainReadLocker lock(DUChain::lock());
    QList<Declaration*> decls = m_ctx->topContext()->findDeclarations(QualifiedIdentifier(functionName));
    if ( decls.length() == 0 ) {
        kDebug() << "No declaration for " << functionName;
        m_shouldBeKnown = false;
        return unknownTypeEncountered();
    }
    else {
        Declaration* actualDeclaration = Helper::resolveAliasDeclaration(decls.last());
        ClassDeclaration* classDecl = dynamic_cast<ClassDeclaration*>(actualDeclaration);
        FunctionDeclaration* funcDecl = dynamic_cast<FunctionDeclaration*>(actualDeclaration);
        
        if ( classDecl ) {
            encounter(classDecl->abstractType());
        }
        else if ( funcDecl && funcDecl->type<FunctionType>() ) {
            AbstractType::Ptr type = funcDecl->type<FunctionType>()->returnType();
            encounter(type);
        }
        else {
            kDebug() << "Declaraton for " << functionName << " is not a class or function declaration";
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
        encounter(lastType());
    }
    else {
        DUChainReadLocker lock(DUChain::lock());
        kDebug() << "LAST TYPE for slice access:" << lastType() << ( lastType() ? lastType()->toString() : "<null>" );
        VariableLengthContainer::Ptr t = lastType().cast<VariableLengthContainer>();
        kDebug() << "Is container: " << t;
        if ( ! t ) {
            return unknownTypeEncountered();
        }
        encounter(t->contentType().abstractType());
    }
}

template<typename T> TypePtr<T> ExpressionVisitor::typeObjectForIntegralType(QString typeDescriptor, DUContext* ctx)
{
    DUChainReadLocker lock(DUChain::lock());
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
    encounter<VariableLengthContainer>(type);
}

void ExpressionVisitor::visitTuple(TupleAst* node) {
    AstDefaultVisitor::visitTuple(node);
    AbstractType::Ptr type = typeObjectForIntegralType<AbstractType>("tuple", m_ctx);
    encounter(type);
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    AstDefaultVisitor::visitDict(node);
    TypePtr<VariableLengthContainer> type = typeObjectForIntegralType<VariableLengthContainer>("dict", m_ctx);
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
    encounter(type);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    AbstractType::Ptr type = typeObjectForIntegralType<AbstractType>("string", m_ctx);
    encounter(type);
}

RangeInRevision nodeRange(Python::Ast* node)
{
    kDebug() << node->endLine;
    return RangeInRevision(node->startLine, node->startCol, node->endLine,node->endCol);
}

void ExpressionVisitor::visitName(Python::NameAst* node)
{
    KDevelop::Identifier id(node->identifier->value);
    QHash < KDevelop::Identifier, AbstractType::Ptr >::const_iterator defId = s_defaultTypes.constFind(id);
    if ( defId != s_defaultTypes.constEnd() ) {
        m_lastType = *defId;
        return;
    }
    
    DUChainReadLocker lock(DUChain::lock());
    QList< Declaration* > d = m_ctx->topContext()->findDeclarations(id);
    d.append(m_ctx->findDeclarations(id));
    lock.unlock();
//     Q_ASSERT(!d.isEmpty());
 
    if ( ! d.isEmpty() ) {
        DeclarationPointer ptr = DeclarationPointer(d.last());
        encounter(ptr->abstractType());
        setLastAccessedNameDeclaration(ptr);
        setLastAccessedDeclaration(ptr);
        DUChainReadLocker lock(DUChain::lock());
        kDebug() << "Found declaration: " << d.last()->toString() << d.last() << d.last()->abstractType() << dynamic_cast<VariableLengthContainer*>(d.last()->abstractType().unsafeData());
    }
    else {
        kDebug() << "VistName type not found";
        unknownTypeEncountered();
    }
}

void ExpressionVisitor::visitBinaryOperation(Python::BinaryOperationAst* node)
{
    visitNode(node->lhs);
    KDevelop::AbstractType::Ptr leftType = m_lastType;
    
    visitNode(node->rhs);
    KDevelop::AbstractType::Ptr rightType = m_lastType;
    
    if ( leftType && leftType->whichType() == AbstractType::TypeIntegral ) 
    {
        encounter(leftType);
    }
    else 
    {
        encounter(AbstractType::Ptr(new UnsureType));
    }
}

void ExpressionVisitor::visitUnaryOperation(Python::UnaryOperationAst* node)
{
    visitNode(node->operand);
    
    //FIXME: m_lastValue = m_lastValue;
}

void ExpressionVisitor::visitBooleanOperation(Python::BooleanOperationAst* node)
{
//    
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
//         if(m_lastType->whichType() != AbstractType::TypeIntegral || m_lastType.cast<IntegralType>()->dataType() != IntegralType::TypeBoolean){
//             problem = true;
//             qDebug() << "VistBooleanOperation type not match";
//             RangeInRevision r = nodeRange(expression);
//             ProblemPointer p(new Problem);
//             p->setRange(r);
//             p->setDescription(i18n("wrong type '%1'", m_lastType->toString()));
//             p->setFinalLocation(DocumentRange(m_ctx->topContext()->url(), r.castToSimpleRange()));
//             p->setSeverity(ProblemData::Error);
//             p->setSource(KDevelop::ProblemData::SemanticAnalysis);
//             m_ctx->topContext()->addProblem(p);
//         }
    }
    
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
}

}

