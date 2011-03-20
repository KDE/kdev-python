/*****************************************************************************
 * Copyright 2010 (c) Miquel Canes Gonzalez <miquelcanes@gmail.com>          *
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

#include "pythonduchainexport.h"
#include "expressionvisitor.h"
#include "pythoneditorintegrator.h"

using namespace KDevelop;
using namespace Python;
using namespace KTextEditor;

namespace Python {

REGISTER_TYPE(IntegralTypeExtended);

QHash<KDevelop::Identifier, KDevelop::AbstractType::Ptr> ExpressionVisitor::s_defaultTypes;

void ExpressionVisitor::encounter(AbstractType::Ptr type)
{
    m_lastType = type;
}

Python::ExpressionVisitor::ExpressionVisitor(DUContext* ctx, PythonEditorIntegrator* editor)
    : m_ctx(ctx), m_editor(editor)
{
    if(s_defaultTypes.isEmpty()) {
        s_defaultTypes.insert(KDevelop::Identifier("True"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("False"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("None"), AbstractType::Ptr(new IntegralType(IntegralType::TypeNull)));
    }
}

void ExpressionVisitor::unknownTypeEncountered() {
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeNull)));
}

void ExpressionVisitor::visitAttribute(AttributeAst* node)
{
    Python::AstDefaultVisitor::visitAttribute(node);
    ExpressionAst* accessingAttributeOf = node->value;
    Identifier* identifier;
    QList<DeclarationPointer> availableDeclarations;
    
    kDebug() << "Processing attribute: " << node->attribute->value;
    
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol, node->attribute->endLine, node->attribute->endCol + 1);
    
    DeclarationPointer accessingAttributeOfDeclaration;
    TypePtr<StructureType> accessingAttributeOfType;
    
    // Step 1: Find out which kind of attribute is before us in the queue, like foo.bar().baz, foo.bar.baz, foo.bar[].baz, etc.
    // Query information about its type or declaration from previously visited stuff.
    if ( accessingAttributeOf->astType == Ast::AttributeAstType ) {
        identifier = dynamic_cast<AttributeAst*>(accessingAttributeOf)->attribute;
        if ( m_lastAccessedAttributeDeclaration.data() ) {
            availableDeclarations << m_lastAccessedAttributeDeclaration;
        }
        else {
            kWarning() << "No type set for accessed attribute";
            return unknownTypeEncountered();
        }
    }
    else if ( accessingAttributeOf->astType == Ast::NameAstType ) {
        availableDeclarations = QList<DeclarationPointer>() << m_lastAccessedNameDeclaration;
    }
    else if ( accessingAttributeOf->astType == Ast::CallAstType ) {
        availableDeclarations.clear();
        accessingAttributeOfType = dynamic_cast<StructureType*>(m_lastAccessedReturnType.unsafeData());
    }
    else {
        kWarning() << "Unsupported attribute access method";
        return;
    }
    
    // Step 2: Select a declaration from those which were found.
    if ( availableDeclarations.length() > 0 && availableDeclarations.last().data() ) {
        accessingAttributeOfDeclaration = availableDeclarations.last();
    }
    else if ( ! accessingAttributeOfType.unsafeData() ) {
        kWarning() << "No declaration found to look up type of attribute in.";
        m_lastAccessedAttributeDeclaration = DeclarationPointer(0);
        return unknownTypeEncountered();
    }
    
    // Step 3: If no type was found previously, construct it from the Declaration.
    if ( ! accessingAttributeOfType.unsafeData() ) {
        accessingAttributeOfType = accessingAttributeOfDeclaration.data()->type<StructureType>();
    }
    
    QList<Declaration*> foundDecls;
    
    // Step 4: Find all matching declarations which are made inside the type of which the accessed object is.
    // Like, for A.B.C where B is an instance of foo, when processing C, find all properties of foo which are called C.
    
    // maybe our attribute isn't a class at all, then that's an error by definition for now
    bool success = false;
    DUChainReadLocker lock(DUChain::lock());
    if ( accessingAttributeOfType.unsafeData() ) {
        Declaration* foundContainerDeclaration = accessingAttributeOfType.unsafeData()->declaration(m_ctx->topContext());
        if ( foundContainerDeclaration ) {
            DUContext* searchAttrInContext = foundContainerDeclaration->internalContext();
            if ( searchAttrInContext ) {
                foundDecls = searchAttrInContext->findDeclarations(QualifiedIdentifier(node->attribute->value), CursorInRevision::invalid(), 
                                                                   KDevelop::AbstractType::Ptr(), searchAttrInContext->topContext());
                success = true;
            }
        }
    }
    if ( ! success ) foundDecls.clear();
    
    // Step 5: Construct the type of the declaration which was found.
    if ( foundDecls.length() > 0 ) {
        m_lastAccessedAttributeDeclaration = DeclarationPointer(foundDecls.last());
        kDebug() << "Last accessed declaration: " << m_lastAccessedAttributeDeclaration->identifier().toString() << m_lastAccessedAttributeDeclaration.data();
        
        // if it's a function call, the result of that call will be the return type
        // TODO check weather we need to distinguish bettween foo.bar and foo.bar() here
        Declaration* decl = foundDecls.last();
        ClassDeclaration* classDecl = dynamic_cast<ClassDeclaration*>(decl);
        FunctionDeclaration* funcDecl = dynamic_cast<FunctionDeclaration*>(decl);
        
        if ( classDecl ) {
            encounter(classDecl->abstractType());
            m_lastAccessedReturnType = classDecl->abstractType();
        }
        else if ( funcDecl && funcDecl->type<FunctionType>() ) {
            Ast* parent = node;
            while ( dynamic_cast<ExpressionAst*>(parent->parent) ) parent = parent->parent;
            if ( parent->astType == Ast::CallAstType ) {
                encounter(funcDecl->type<FunctionType>()->returnType());
                m_lastAccessedReturnType = funcDecl->type<FunctionType>()->returnType();
            }
            else {
                encounter(funcDecl->abstractType());
                m_lastAccessedReturnType = funcDecl->abstractType(); // TODO check this
            }
        }
        else {
            encounter(foundDecls.last()->abstractType());
        }
    }
    else {
        kWarning() << "No declaration found for attribute";
        m_lastAccessedAttributeDeclaration = DeclarationPointer(0);
        return unknownTypeEncountered();
    }
    kDebug() << "VisitAttribute end";
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    Python::AstDefaultVisitor::visitCall(node);
    // if it's not written like foo() but like foo[3](), then we don't attempt to guess a type
    if ( node->function->astType == Ast::AttributeAstType ) {
        // a bit confusing, but visitAttribute() already has taken care of this.
        return;
    }
    if ( ! ( node->function->astType == Ast::NameAstType ) ) {
        return unknownTypeEncountered();
    }
    
    QString functionName = dynamic_cast<NameAst*>(node->function)->identifier->value;
    kDebug() << "Visiting call of function " << functionName;
    
    DUChainReadLocker lock(DUChain::lock());
    QList<Declaration*> decls = m_ctx->findDeclarations(QualifiedIdentifier(functionName));
    if ( decls.length() == 0 ) {
        kWarning() << "No declaration for " << functionName;
        return unknownTypeEncountered();
    }
    else {
        ClassDeclaration* classDecl = dynamic_cast<ClassDeclaration*>(decls.last());
        FunctionDeclaration* funcDecl = dynamic_cast<FunctionDeclaration*>(decls.last());
        
        if ( classDecl ) {
            encounter(classDecl->abstractType());
            m_lastAccessedReturnType = classDecl->abstractType();
        }
        else if ( funcDecl && funcDecl->type<FunctionType>() ) {
            encounter(funcDecl->type<FunctionType>()->returnType());
            m_lastAccessedReturnType = funcDecl->type<FunctionType>()->returnType();
        }
        else {
            kDebug() << "Declaraton for " << functionName << " is not a class or function declaration";
            return unknownTypeEncountered();
        }
    }
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    if ( node->slice && node->slice->astType != Ast::IndexAstType ) {
        kDebug() << "Found slice, will use ListType for assignment";
        encounter(AbstractType::Ptr(new IntegralTypeExtended(IntegralTypeExtended::TypeList)));
    }
    else {
        kDebug() << "No slice, defaulting to NULL type.";
        return unknownTypeEncountered();
    }
}

AbstractType::Ptr ExpressionVisitor::typeObjectForIntegralType(QString typeDescriptor)
{
    DUChainReadLocker lock(DUChain::lock());
    QList<Declaration*> decls = m_ctx->topContext()->findDeclarations(QualifiedIdentifier("__kdevpythondocumentation_builtin_" + typeDescriptor));
    Declaration* decl = decls.isEmpty() ? 0 : decls.first();
    AbstractType::Ptr type = decl ? decl->abstractType() : AbstractType::Ptr(0);
    return type;
}

void ExpressionVisitor::visitList(ListAst* node)
{
    AstDefaultVisitor::visitList(node);
    AbstractType::Ptr type = typeObjectForIntegralType("list");
    encounter(type);
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    AstDefaultVisitor::visitDict(node);
    AbstractType::Ptr type = typeObjectForIntegralType("dict");
    encounter(type);
}

void ExpressionVisitor::visitNumber(Python::NumberAst* )
{
    AbstractType::Ptr type = typeObjectForIntegralType("float");
    encounter(type);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    AbstractType::Ptr type = typeObjectForIntegralType("string");
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
 
    kDebug() << "visitName" << node->identifier->value << d.count();   
    if ( ! d.isEmpty() ) {
        encounter(d.last()->abstractType());
        m_lastAccessedNameDeclaration = d.last();
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

