/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

// The Python 2.6 Language Reference was used as basis for this AST

#ifndef PYTHON_AST_H
#define PYTHON_AST_H

#include <QList>
#include <QMap>
#include <QString>
#include <QStringList>
#include <QPair>

#include "parserexport.h"

namespace KDevelop
{
    class DUContext;
}

namespace Python
{
    
class KDEVPYTHONPARSER_EXPORT Identifier {
public:
    Identifier(QString value);
    QString value;
};

// Abstract StatementAst class
class KDEVPYTHONPARSER_EXPORT StatementAst : public Ast {
public:
    virtual StatementAst(Ast* parent, Ast::AstType type) = 0;
};

class KDEVPYTHONPARSER_EXPORT FunctionDefinitionAst : public StatementAst {
public:
    FunctionDefinitionAst(Ast* parent, Ast::AstType type);
    IdentifierAst* name;
    ArgumentsAst* arguments;
};

class KDEVPYTHONPARSER_EXPORT AssignmentAst : public StatementAst {
public:
    AssignmentAst(Ast* parent, Ast::AstType type);
    QList<ExpressionAst*> targets;
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT PrintAst : public StatementAst {
public:
    PrintAst(Ast* parent, AstType type);
    ExpressionAst* destination;
    QList<ExpressionAst> values;
    bool newline;
};

class KDEVPYTHONPARSER_EXPORT PassAst : public StatementAst {
public:
    PassAst(Ast* parent, AstType type);
};

class KDEVPYTHONPARSER_EXPORT ExpressionAst : public Ast {
public:
    virtual ExpressionAst(Ast* parent, AstType type) = 0;
    enum Context {
        Load, // the object is read
        Store, // the object is written
        Delete, // the object is deleted
        Parameter, // the object is passed as a parameter
        AugLoad, AugStore // Apparently not used by python currently, I also dont know what they mean
    };
};

class KDEVPYTHONPARSER_EXPORT NameAst : public ExpressionAst {
public:
    NameAst(Ast* parent, AstType type);
    IdentifierAst* identifier;
    ExpressionAst::Context context;
};

class KDEVPYTHONPARSER_EXPORT CallAst : public ExpressionAst {
public:
    CallAst(Ast* parent, AstType type);
    ExpressionAst* function;
    QList<ExpressionAst*> arguments;
    QList<KeywordAst*> keywords;
    ExpressionAst* starArguments;
    ExpressionAst* keywordArguments;
};

class KDEVPYTHONPARSER_EXPORT AttributeAst : public ExpressionAst {
public:
    AttributeAst(Ast* parent, AstType type);
    ExpressionAst* value;
    IdentifierAst* attribute;
    ExpressionAst::Context context;
};



class KDEVPYTHONPARSER_EXPORT Ast
{
public:
    enum AstType
    {
    
    };

    Ast(Ast* parent, AstType type);
    virtual ~Ast();
    Ast* parent;
    AstType astType;

    qint64 start;
    qint64 end;
    qint64 startCol;
    qint64 startLine;
    qint64 endCol;
    qint64 endLine;
    
    KDevelop::DUContext* context;
};

}

#endif
