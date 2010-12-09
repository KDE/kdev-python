#include "expressionvisitor.h"
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/declaration.h>
#include <language/interfaces/iproblem.h>
#include <KLocalizedString>

using namespace KDevelop;
using namespace Python;

QHash<KDevelop::Identifier, KDevelop::AbstractType::Ptr> ExpressionVisitor::s_defaultTypes;

Python::ExpressionVisitor::ExpressionVisitor(DUContext* ctx)
    : m_ctx(ctx)
{
    if(s_defaultTypes.isEmpty()) {
        s_defaultTypes.insert(KDevelop::Identifier("True"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        s_defaultTypes.insert(KDevelop::Identifier("False"), AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
    }
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
    qDebug() << node->endLine;
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
 
    qDebug() << "visitName" << node->identifier->value << d;   
    if(!d.isEmpty())
        m_lastType = d.last()->abstractType();
    else {
        qDebug("VistName type not found");
        RangeInRevision r = nodeRange(node);
        
        ProblemPointer p(new Problem);
        p->setRange(r);
        p->setDescription(i18n("undefined variable '%1'", node->identifier->value));
        qDebug() << "adddProblemKiko" << m_ctx->topContext()->url().str();
        p->setFinalLocation(DocumentRange(m_ctx->topContext()->url(), r.castToSimpleRange()));
        p->setSeverity(ProblemData::Error);
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        m_ctx->topContext()->addProblem(p);
    }
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

