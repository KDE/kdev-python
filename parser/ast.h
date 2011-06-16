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

namespace Python {
    class StatementAst;
    class FunctionDefinitionAst;
    class AssignmentAst;
    class PrintAst;
    class PassAst;
    class ExpressionAst;
    class NameAst;
    class CallAst;
    class AttributeAst;
    class ArgumentsAst;
    class KeywordAst;
    
    class ExpressionAst;
    class StatementAst;
    class Ast;
    class ExceptionHandlerAst;
    class AliasAst;
    class ComprehensionAst;
    class SliceAstBase;
    class SliceAst;
}

namespace Python
{


// Base class for all other Abstract Syntax Tree classes
class KDEVPYTHONPARSER_EXPORT Ast
{
public:
    enum AstType
    {
        FunctionDefinitionAstType,
        AssignmentAstType,
        PrintAstType,
        PassAstType,
        NameAstType,
        CallAstType,
        AttributeAstType,
        ArgumentsAstType,
        KeywordAstType,
        ClassDefinitionAstType,
        ReturnAstType,
        DeleteAstType,
        ForAstType,
        WhileAstType,
        IfAstType,
        WithAstType,
        RaiseAstType,
        TryExceptAstType,
        TryFinallyAstType,
        ImportAstType,
        ImportFromAstType,
        ExecAstType,
        GlobalAstType,
        BreakAstType,
        ContinueAstType,
        AssertionAstType,
        AugmentedAssignmentAstType,
        DictionaryComprehensionAstType,
        ExtendedSliceAstType,
        CodeAstType,
        StatementAstType,
        ExpressionAstType,
        
        BooleanOperationAstType,
        BinaryOperationAstType,
        UnaryOperationAstType,
        LambdaAstType,
        IfExpressionAstType, // the short one, if a then b else c
        DictAstType,
        SetAstType,
        ListComprehensionAstType,
        SetComprehensionAstType,
        GeneratorExpressionAstType,
        YieldAstType,
        CompareAstType,
        ReprAstType,
        NumberAstType,
        StringAstType,
        SubscriptAstType,
        ListAstType,
        TupleAstType,
        
        SliceAstType,
        EllipsisAstType,
        IndexAstType,
        
        ComprehensionAstType,
        ExceptionHandlerAstType,
        AliasAstType // for imports
    };
    
    enum BooleanOperationTypes {
        BooleanAnd,
        BooleanOr,
        BooleanInvalidOperation
    };
    
    enum OperatorTypes {
        OperatorAdd,
        OperatorSub,
        OperatorMult,
        OperatorDiv,
        OperatorMod,
        OperatorPow,
        OperatorLeftShift,
        OperatorRightShift,
        OperatorBitwiseOr,
        OperatorBitwiseXor,
        OperatorBitwiseAnd,
        OperatorFloorDivision,
        OperatorInvalid
    };
    
    enum UnaryOperatorTypes {
        UnaryOperatorInvert,
        UnaryOperatorNot,
        UnaryOperatorAdd,
        UnaryOperatorSub,
        UnaryOperatorInvalid
    };
    
    enum ComparisonOperatorTypes {
        ComparisonOperatorEquals,
        ComparisonOperatorNotEquals,
        ComparisonOperatorLessThan,
        ComparisonOperatorLessThanEqual,
        ComparisonOperatorGreaterThan,
        ComparisonOperatorGreaterThanEqual,
        ComparisonOperatorIs,
        ComparisonOperatorIsNot,
        ComparisonOperatorIn,
        ComparisonOperatorNotIn,
        ComparisonOperatorInvalid
    };

    Ast(Ast* parent, AstType type);
    Ast();
    virtual ~Ast();
    Ast* parent;
    AstType astType;

    qint64 startCol;
    qint64 startLine;
    qint64 endCol;
    qint64 endLine;
    
    bool hasUsefulRangeInformation;
    
    KDevelop::DUContext* context;
};

class KDEVPYTHONPARSER_EXPORT Identifier : public Ast {
public:
    Identifier(QString value);
    QString value;
};

// this replaces ModuleAst
class KDEVPYTHONPARSER_EXPORT CodeAst : public Ast {
public:
    CodeAst();
    QList<Ast*> body;
    Identifier* name; // module name
};

/** Statement classes **/
class KDEVPYTHONPARSER_EXPORT StatementAst : public Ast {
public:
    StatementAst(Ast* parent, AstType type);
};

class KDEVPYTHONPARSER_EXPORT FunctionDefinitionAst : public StatementAst {
public:
    FunctionDefinitionAst(Ast* parent);
    Identifier* name;
    ArgumentsAst* arguments;
    QList<NameAst*> decorators;
    QList<Ast*> body;
};

class KDEVPYTHONPARSER_EXPORT ClassDefinitionAst : public StatementAst {
public:
    ClassDefinitionAst(Ast* parent);
    Identifier* name;
    QList<ExpressionAst*> baseClasses;
    QList<Ast*> body;
    QList<ExpressionAst*> decorators;
};

class KDEVPYTHONPARSER_EXPORT ReturnAst : public StatementAst {
public:
    ReturnAst(Ast* parent);
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT DeleteAst : public StatementAst {
public:
    DeleteAst(Ast* parent);
    QList<ExpressionAst*> targets;
};

class KDEVPYTHONPARSER_EXPORT AssignmentAst : public StatementAst {
public:
    AssignmentAst(Ast* parent);
    QList<ExpressionAst*> targets;
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT AugmentedAssignmentAst : public StatementAst {
public:
    AugmentedAssignmentAst(Ast* parent);
    ExpressionAst* target;
    Ast::OperatorTypes op;
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT ForAst : public StatementAst {
public:
    ForAst(Ast* parent);
    ExpressionAst* target;
    ExpressionAst* iterator;
    QList<Ast*> body;
    QList<Ast*> orelse;
};

class KDEVPYTHONPARSER_EXPORT WhileAst : public StatementAst {
public:
    WhileAst(Ast* parent);
    ExpressionAst* condition;
    QList<Ast*> body;
    QList<Ast*> orelse;
};

class KDEVPYTHONPARSER_EXPORT IfAst : public StatementAst {
public:
    IfAst(Ast* parent);
    ExpressionAst* condition;
    QList<Ast*> body;
    QList<Ast*> orelse;
};

class KDEVPYTHONPARSER_EXPORT WithAst : public StatementAst {
public:
    WithAst(Ast* parent);
    ExpressionAst* contextExpression;
    ExpressionAst* optionalVars;
    QList<Ast*> body;
};

class KDEVPYTHONPARSER_EXPORT RaiseAst : public StatementAst {
public:
    RaiseAst(Ast* parent);
    ExpressionAst* type;
    // TODO check what the other things in the grammar actually are and add them
};

class KDEVPYTHONPARSER_EXPORT TryExceptAst : public StatementAst {
public:
    TryExceptAst(Ast* parent);
    QList<Ast*> body;
    QList<ExceptionHandlerAst*> handlers;
    QList<Ast*> orelse;
};

class KDEVPYTHONPARSER_EXPORT TryFinallyAst : public StatementAst {
public:
    TryFinallyAst(Ast* parent);
    QList<Ast*> body;
    QList<Ast*> finalbody;
};

class KDEVPYTHONPARSER_EXPORT AssertionAst : public StatementAst {
public:
    AssertionAst(Ast* parent);
    ExpressionAst* condition;
    ExpressionAst* message;
};

class KDEVPYTHONPARSER_EXPORT ImportAst : public StatementAst {
public:
    ImportAst(Ast* parent);
    QList<AliasAst*> names;
};

class KDEVPYTHONPARSER_EXPORT ImportFromAst : public StatementAst {
public:
    ImportFromAst(Ast* parent);
    Identifier* module;
    QList<AliasAst*> names;
    int level;
};

class KDEVPYTHONPARSER_EXPORT ExecAst : public StatementAst {
public:
    ExecAst(Ast* parent);
    ExpressionAst* body;
    ExpressionAst* globals;
    ExpressionAst* locals;
};

class KDEVPYTHONPARSER_EXPORT GlobalAst : public StatementAst {
public:
    GlobalAst(Ast* parent);
    QList<Identifier*> names;
};

// TODO what's stmt::Expr(expr value) in the grammar and what do we need it for?

class KDEVPYTHONPARSER_EXPORT BreakAst : public StatementAst {
public:
    BreakAst(Ast* parent);
};

class KDEVPYTHONPARSER_EXPORT ContinueAst : public StatementAst {
public:
    ContinueAst(Ast* parent);
};

class KDEVPYTHONPARSER_EXPORT PrintAst : public StatementAst {
public:
    PrintAst(Ast* parent);
    ExpressionAst* destination;
    QList<ExpressionAst*> values;
    bool newline;
};

class KDEVPYTHONPARSER_EXPORT PassAst : public StatementAst {
public:
    PassAst(Ast* parent);
};


/** Expression classes **/
class KDEVPYTHONPARSER_EXPORT ExpressionAst : public Ast {
public:
    ExpressionAst(Ast* parent, AstType type = Ast::ExpressionAstType);
    enum Context {
        Load = 1, // the object is read
        Store = 2, // the object is written
        Delete = 3, // the object is deleted
        Parameter = 6, // the object is passed as a parameter
        AugLoad = 4, AugStore = 5, // Augmented assignments, like a += 1
        Invalid = -1
    };
    ExpressionAst* value; // WARNING this is not set in most cases!
    CallAst* belongsToCall;
};

class KDEVPYTHONPARSER_EXPORT BooleanOperationAst : public ExpressionAst {
public:
    BooleanOperationAst(Ast* parent);
    Ast::BooleanOperationTypes type;
    QList<ExpressionAst*> values;
};

class KDEVPYTHONPARSER_EXPORT BinaryOperationAst : public ExpressionAst {
public:
    BinaryOperationAst(Ast* parent);
    Ast::OperatorTypes type;
    ExpressionAst* lhs;
    ExpressionAst* rhs;
};

class KDEVPYTHONPARSER_EXPORT UnaryOperationAst : public ExpressionAst {
public:
    UnaryOperationAst(Ast* parent);
    Ast::UnaryOperatorTypes type;
    ExpressionAst* operand;
};

class KDEVPYTHONPARSER_EXPORT LambdaAst : public ExpressionAst {
public:
    LambdaAst(Ast* parent);
    ArgumentsAst* arguments;
    ExpressionAst* body;
};

class KDEVPYTHONPARSER_EXPORT IfExpressionAst : public ExpressionAst {
public:
    IfExpressionAst(Ast* parent);
    ExpressionAst* condition;
    ExpressionAst* body;
    ExpressionAst* orelse;
};

class KDEVPYTHONPARSER_EXPORT DictAst : public ExpressionAst {
public:
    DictAst(Ast* parent);
    QList<ExpressionAst*> keys;
    QList<ExpressionAst*> values;
};

class KDEVPYTHONPARSER_EXPORT SetAst : public ExpressionAst {
public:
    SetAst(Ast* parent);
    QList<ExpressionAst*> elements;
};

class KDEVPYTHONPARSER_EXPORT ListComprehensionAst : public ExpressionAst {
public:
    ListComprehensionAst(Ast* parent);
    ExpressionAst* element;
    QList<ComprehensionAst*> generators;
};

class KDEVPYTHONPARSER_EXPORT SetComprehensionAst : public ExpressionAst {
public:
    SetComprehensionAst(Ast* parent);
    ExpressionAst* element;
    QList<ComprehensionAst*> generators;
};

class KDEVPYTHONPARSER_EXPORT DictionaryComprehensionAst : public ExpressionAst {
public:
    DictionaryComprehensionAst(Ast* parent);
    ExpressionAst* key;
    ExpressionAst* value;
    QList<ComprehensionAst*> generators;
};

class KDEVPYTHONPARSER_EXPORT GeneratorExpressionAst : public ExpressionAst {
public:
    GeneratorExpressionAst(Ast* parent);
    ExpressionAst* element;
    QList<ComprehensionAst*> generators;
};

class KDEVPYTHONPARSER_EXPORT CompareAst : public ExpressionAst {
public:
    CompareAst(Ast* parent);
    ExpressionAst* leftmostElement;
    QList<ComparisonOperatorTypes> operators;
    QList<ExpressionAst*> comparands;
};

// TODO whats this exactly?
class KDEVPYTHONPARSER_EXPORT ReprAst : public ExpressionAst {
public:
    ReprAst(Ast* parent);
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT NumberAst : public ExpressionAst {
public:
    NumberAst(Ast* parent);
    QString value; // everything else would be even more strange
};

class KDEVPYTHONPARSER_EXPORT StringAst : public ExpressionAst {
public:
    StringAst(Ast* parent);
    QString value;
};

class KDEVPYTHONPARSER_EXPORT YieldAst : public ExpressionAst {
public:
    YieldAst(Ast* parent);
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT NameAst : public ExpressionAst {
public:
    NameAst(Ast* parent);
    Identifier* identifier;
    ExpressionAst::Context context;
};

class KDEVPYTHONPARSER_EXPORT CallAst : public ExpressionAst {
public:
    CallAst(Ast* parent);
    ExpressionAst* function;
    QList<ExpressionAst*> arguments;
    QList<KeywordAst*> keywords;
    ExpressionAst* keywordArguments;
    ExpressionAst* starArguments;
};

class KDEVPYTHONPARSER_EXPORT AttributeAst : public ExpressionAst {
public:
    AttributeAst(Ast* parent);
    ExpressionAst* value;
    Identifier* attribute;
    ExpressionAst::Context context;
    int depth; // foo.bar.baz -> foo has depth 1, bar has depth 2, baz 3; needed for range analysis
};

class KDEVPYTHONPARSER_EXPORT SubscriptAst : public ExpressionAst {
public:
    SubscriptAst(Ast* parent);
    ExpressionAst* value;
    SliceAstBase* slice;
    ExpressionAst::Context context;
};

class KDEVPYTHONPARSER_EXPORT ListAst : public ExpressionAst {
public:
    ListAst(Ast* parent);
    QList<ExpressionAst*> elements;
    ExpressionAst::Context context;
};

class KDEVPYTHONPARSER_EXPORT TupleAst : public ExpressionAst {
public:
    TupleAst(Ast* parent);
    QList<ExpressionAst*> elements;
    ExpressionAst::Context context;
};

/** Slice classes **/
class KDEVPYTHONPARSER_EXPORT SliceAstBase : public Ast {
public:
    SliceAstBase(Ast* parent, AstType type);
};

class KDEVPYTHONPARSER_EXPORT EllipsisAst : public SliceAstBase {
public:
    EllipsisAst(Ast* parent);
};

class KDEVPYTHONPARSER_EXPORT SliceAst : public SliceAstBase {
public:
    SliceAst(Ast* parent);
    ExpressionAst* lower;
    ExpressionAst* upper;
    ExpressionAst* step;
};

class KDEVPYTHONPARSER_EXPORT ExtendedSliceAst : public SliceAstBase {
public:
    ExtendedSliceAst(Ast* parent);
    QList<SliceAst*> dims;
};

class KDEVPYTHONPARSER_EXPORT IndexAst : public SliceAstBase {
public:
    IndexAst(Ast* parent);
    ExpressionAst* value;
};

/** Independent classes **/
class KDEVPYTHONPARSER_EXPORT ArgumentsAst : public Ast {
public:
    ArgumentsAst(Ast* parent);
    QList<ExpressionAst*> arguments;
    QList<ExpressionAst*> defaultValues;
    Identifier* vararg;
    Identifier* kwarg;
    int arg_lineno, arg_col_offset;
    int vararg_lineno, vararg_col_offset;
};

class KDEVPYTHONPARSER_EXPORT KeywordAst : public Ast {
public:
    KeywordAst(Ast* parent);
    Identifier* argumentName;
    ExpressionAst* value;
};

class KDEVPYTHONPARSER_EXPORT ComprehensionAst : public Ast {
public:
    ComprehensionAst(Ast* parent);
    ExpressionAst* target;
    ExpressionAst* iterator;
    QList<ExpressionAst*> conditions;
};

class KDEVPYTHONPARSER_EXPORT ExceptionHandlerAst : public Ast {
public:
    ExceptionHandlerAst(Ast* parent);
    ExpressionAst* type;
    ExpressionAst* name;
    QList<Ast*> body;
};

class KDEVPYTHONPARSER_EXPORT AliasAst : public Ast {
public:
    AliasAst(Ast* parent);
    Identifier* name;
    Identifier* asName;
};

}

#endif
