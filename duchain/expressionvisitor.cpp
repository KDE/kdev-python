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

#include "expressionvisitor.h"
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/declaration.h>
#include <language/interfaces/iproblem.h>
#include <KLocalizedString>

#include <language/duchain/types/typeregister.h>
#include "pythonduchainexport.h"

#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/types/functiontype.h>

using namespace KDevelop;
using namespace Python;

namespace Python {

REGISTER_TYPE(IntegralTypeExtended);

QHash<KDevelop::Identifier, KDevelop::AbstractType::Ptr> ExpressionVisitor::s_defaultTypes;

Python::ExpressionVisitor::ExpressionVisitor(DUContext* ctx)
    : m_ctx(ctx)
{
    if(s_defaultTypes.isEmpty()) {
        s_defaultTypes.insert(KDevelop::Identifier("True"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("False"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("None"), AbstractType::Ptr(new IntegralType(IntegralType::TypeNull)));
    }
}

void ExpressionVisitor::unknownTypeEncountered() {
    m_lastType = AbstractType::Ptr(new IntegralType(IntegralType::TypeNull));
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    Python::AstDefaultVisitor::visitCall(node);
    // if it's not written like foo() but like foo[3](), then we don't attempt to guess a type
    if ( ! dynamic_cast<NameAst*>(node->function) ) {
        return unknownTypeEncountered();
    }
    QList<Declaration*> decls = m_ctx->findDeclarations(QualifiedIdentifier(dynamic_cast<NameAst*>(node->function)->identifier->value));
    if ( decls.length() == 0 ) {
        kWarning() << "No declaration for " << node->function->value;
        return unknownTypeEncountered();
    }
    else {
        FunctionDeclaration* decl = dynamic_cast<FunctionDeclaration*>(decls.last());
        if ( ! decl || ! decl->isFunctionDeclaration() || ! decl->type<FunctionType>() ) {
            kWarning() << "Declaration for " << node->function->value << "is not a function declaration";
            return unknownTypeEncountered();
        }
        m_lastType = decl->type<FunctionType>()->returnType();
    }
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    if ( node->slice && node->slice->astType != Ast::IndexAstType ) {
        kDebug() << "Found slice, will use ListType for assignment";
        m_lastType = AbstractType::Ptr(new IntegralTypeExtended(IntegralTypeExtended::TypeList));
    }
    else {
        kDebug() << "No slice, defaulting to NULL type.";
        return unknownTypeEncountered();
    }
}

void ExpressionVisitor::visitList(ListAst* node)
{
    m_lastType = AbstractType::Ptr(new IntegralTypeExtended(IntegralTypeExtended::TypeList));
    AstDefaultVisitor::visitList(node);
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    m_lastType = AbstractType::Ptr(new IntegralTypeExtended(IntegralTypeExtended::TypeDict));
    AstDefaultVisitor::visitDict(node);
}

void Python::ExpressionVisitor::visitNumber(Python::NumberAst* )
{
    m_lastType = AbstractType::Ptr(new IntegralType(IntegralType::TypeFloat));
}

void Python::ExpressionVisitor::visitString(Python::StringAst* )
{
    m_lastType = AbstractType::Ptr(new IntegralType(IntegralType::TypeString));
}

RangeInRevision nodeRange(Python::Ast* node)
{
    kDebug() << node->endLine;
    return RangeInRevision(node->startLine, node->startCol, node->endLine,node->endCol);
}

void Python::ExpressionVisitor::visitName(Python::NameAst* node)
{
    KDevelop::Identifier id(node->identifier->value);
    QHash < KDevelop::Identifier, AbstractType::Ptr >::const_iterator defId = s_defaultTypes.constFind(id);
    if(defId!=s_defaultTypes.constEnd()) {
        m_lastType = *defId;
        return;
    }
    
    QList< Declaration* > d=m_ctx->findDeclarations(id);
//     Q_ASSERT(!d.isEmpty());
 
    kDebug() << "visitName" << node->identifier->value << d;   
    if(!d.isEmpty())
        m_lastType = d.last()->abstractType();
    else {
        qDebug("VistName type not found");
        RangeInRevision r = nodeRange(node);
        r.end.column += 1;
        
        ProblemPointer p(new Problem);
        p->setRange(r);
        p->setDescription(i18n("undefined variable '%1'", node->identifier->value));
        p->setFinalLocation(DocumentRange(m_ctx->topContext()->url(), r.castToSimpleRange()));
        p->setSeverity(ProblemData::Error);
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        m_ctx->topContext()->addProblem(p);
        m_lastType = 0;
    }
}

void Python::ExpressionVisitor::visitBinaryOperation(Python::BinaryOperationAst* node)
{
    visitNode(node->lhs);
    KDevelop::AbstractType::Ptr leftType = m_lastType;
    
    visitNode(node->rhs);
    KDevelop::AbstractType::Ptr rightType = m_lastType;
    
    if ( leftType && leftType->whichType() == AbstractType::TypeIntegral ) 
    {
        m_lastType = leftType;
    }
    else 
    {
        m_lastType = AbstractType::Ptr(new UnsureType);
    }
}

void Python::ExpressionVisitor::visitUnaryOperation(Python::UnaryOperationAst* node)
{
    visitNode(node->operand);
    
    //FIXME: m_lastValue = m_lastValue;
}

void Python::ExpressionVisitor::visitBooleanOperation(Python::BooleanOperationAst* node)
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
    
    m_lastType = AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean));
}

}

