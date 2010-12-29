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

#ifndef EXPRESSIONVISITOR_H
#define EXPRESSIONVISITOR_H

#include <astdefaultvisitor.h>
#include <language/duchain/types/abstracttype.h>
#include <QHash>

namespace KDevelop {
class Identifier;
}

namespace Python
{

class ExpressionVisitor : public AstDefaultVisitor
{
    public:
        ExpressionVisitor(KDevelop::DUContext* ctx);
        
        virtual void visitBinaryOperation(BinaryOperationAst* node);
        virtual void visitUnaryOperation(UnaryOperationAst* node);
        virtual void visitBooleanOperation(BooleanOperationAst* node);
        
        virtual void visitString(StringAst* node);
        virtual void visitNumber(NumberAst* node);
        virtual void visitName(NameAst* node);
        
        KDevelop::AbstractType::Ptr lastType() const { return m_lastType; }
    private:
        static QHash<KDevelop::Identifier, KDevelop::AbstractType::Ptr> s_defaultTypes;
        
        KDevelop::AbstractType::Ptr m_lastType;
        KDevelop::DUContext* m_ctx;
};

}

#endif // EXPRESSIONVISITOR_H
