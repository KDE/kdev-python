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
#ifndef TYPEBUILDER_H
#define TYPEBUILDER_H

#include "contextbuilder.h"
#include <typesystem.h>
#include <declaration.h>
#include "pythonduchainbuilderexport.h"

class ClassType;
class FunctionType;

typedef ContextBuilder TypeBuilderBase;

class KDEVPYTHONDUCHAINBUILDER_EXPORT TypeBuilder: public TypeBuilderBase
{
public:
    TypeBuilder(ParseSession* session, const KUrl &url);
    TypeBuilder(PythonEditorIntegrator* editor, const KUrl &url);
    virtual void supportBuild(ast_node *node, KDevelop::DUContext* context = 0);
    const QList< KDevelop::AbstractType::Ptr >& topTypes() const;
    KDevelop::DUContext* searchContext() ;
    KDevelop::AbstractType::Ptr lastType() const;
    void setLastType(KDevelop::AbstractType::Ptr ptr);
private:
    QStack<KDevelop::AbstractType::Ptr> m_typeStack;
};

#endif
