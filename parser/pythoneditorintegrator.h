/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
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
#ifndef PYTHONEDITORINTEGRATOR_H
#define PYTHONEDITORINTEGRATOR_H
#include <editorintegrator.h>
#include "python_lexer.h"
#include "python_parser.h"

namespace python
{
    class ast_node;
}

class ParseSession;

using namespace python;

class PythonEditorIntegrator : public KDevelop::EditorIntegrator
{
public:
    PythonEditorIntegrator(ParseSession* session);
    ParseSession* parseSession() const;

    KTextEditor::Cursor findPosition(parser::token_type const &token, Edge edge = BackEdge) const;
    KTextEditor::Cursor findPosition(std::size_t token, Edge edge = BackEdge) const;

    using KDevelop::EditorIntegrator::createRange;
    KTextEditor::Range findRange(ast_node* node, RangeEdge = OuterEdge);
    KTextEditor::Range findRange(ast_node* from, ast_node* to);
    KTextEditor::Range findRange(parser::token_type const &token);
    KTextEditor::Range findRange(std::size_t token);
    QString tokenToString(std::size_t token) const;

private:
    ParseSession* m_session;
};
#endif 
