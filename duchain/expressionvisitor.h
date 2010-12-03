#ifndef EXPRESSIONVISITOR_H
#define EXPRESSIONVISITOR_H

#include <astdefaultvisitor.h>
#include <language/duchain/types/abstracttype.h>

namespace Python
{

class ExpressionVisitor : public AstDefaultVisitor
{
    public:
        ExpressionVisitor(KDevelop::DUContext* ctx);
        
        virtual void visitBinaryOperation(BinaryOperationAst* node);
        virtual void visitUnaryOperation(UnaryOperationAst* node);
        
        virtual void visitString(StringAst* node);
        virtual void visitNumber(NumberAst* node);
        virtual void visitName(NameAst* node);
    
        KDevelop::AbstractType::Ptr lastType() const { return m_lastType; }
    private:
        KDevelop::AbstractType::Ptr m_lastType;
        KDevelop::DUContext* m_ctx;
};

}

#endif // EXPRESSIONVISITOR_H
