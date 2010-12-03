#include "expressionvisitor.h"
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/declaration.h>

using namespace KDevelop;

Python::ExpressionVisitor::ExpressionVisitor(DUContext* ctx)
    : m_ctx(ctx)
{}

void Python::ExpressionVisitor::visitNumber(Python::NumberAst* )
{
    m_lastType = AbstractType::Ptr(new IntegralType(IntegralType::TypeFloat));
}

void Python::ExpressionVisitor::visitString(Python::StringAst* )
{
    m_lastType = AbstractType::Ptr(new IntegralType(IntegralType::TypeString));
}

void Python::ExpressionVisitor::visitName(Python::NameAst* node)
{
    qDebug() << "pepepepepe" << node->identifier->value;
    QList< Declaration* > d=m_ctx->findDeclarations(KDevelop::Identifier(node->identifier->value));
    Q_ASSERT(!d.isEmpty());
    m_lastType = d.last()->abstractType();
}

void Python::ExpressionVisitor::visitBinaryOperation(Python::BinaryOperationAst* node)
{
    visitNode(node->lhs);
    KDevelop::AbstractType::Ptr leftType = m_lastType;
    
    visitNode(node->rhs);
    KDevelop::AbstractType::Ptr rightType = m_lastType;
    
    if(leftType->whichType()==AbstractType::TypeIntegral && leftType->whichType()==AbstractType::TypeIntegral)
        m_lastType = leftType;
    else
        m_lastType = AbstractType::Ptr(new UnsureType);
}

void Python::ExpressionVisitor::visitUnaryOperation(Python::UnaryOperationAst* node)
{
    visitNode(node->operand);
    
    //FIXME: m_lastValue = m_lastValue;
}
