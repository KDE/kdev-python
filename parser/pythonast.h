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

#ifndef PYTHONAST_H
#define PYTHONAST_H

namespace Python
{

class Ast
{
    enum AstType
    {
        CodeAst,
        ClassDefinitionAst,
        FunctionDefinitionAst,
        SuiteAst,
        DecoratorAst,
        ParameterAst,
        ArgumentAst,
        StatementAst,
        ExpressionAst,
        WhileAst,
        IfAst,
        ForAst,
        ImportAst,
        ContinueAst,
        BreakAst,
        PassAst,
        GlobalAst,
        WithAst,
        ExecAst,
        TryAst,
        RaiseAst,
        ReturnAst,
        PrintAst,
        YieldAst,
        AssignmentAst,
        DelAst,
        AssertAst,
        ExpressionStatementAst,
        LambdaAst,
        ExpressionAst,
        BooleanAst,
        ComparisonAst,
        BinaryExpressionAst,
        UnaryExpressionAst,
        ArithmeticExpressionAst,
        CallAst,
        SliceItemAst,
        SliceAst,
        SubscriptAst,
        AttributeReferenceAst,
        PrimaryAst,
        TargetAst,
        AtomAst,
        EnclosureAst,
        ListAst,
        ListForAst,
        ListIfAst,
        GeneratorAst,
        GeneratorForAst,
        GeneratorIfAst,
        DictionaryAst
    };

public:
    Ast( Ast* parent );
    AstType astType;
    Ast* parent;
};

class CodeAst : public Ast
{

public:
    CodeAst( Ast* parent );
    QList<StatementAst*> statements;
};

class FunctionDefinitionAst : public StatementAst
{

public:
    FunctionDefinitionAst( Ast* parent );
    QString functionName;
    QList<ParameterAst*> parameters;
    QList<DecoratorAst*> decorators;
    SuiteAst* suite;
};

class DecoratorAst : public Ast
{

public:
    DecoratorAst( Ast* parent );
    QStringList names;
    QList<ArgumentAst*> arguments;
};

class ArgumentAst : public Ast
{
    enum ArgumentType
    {
        PositionalArgument,
        KeywordArgument,
        ListArgument,
        DictArgument
    };

public:
    ArgumentAst( Ast* );
    QList<ExpressionAst*> positionalArguments;
    QMap<QString, ExpressionAst*> keywordArguments;
    ExpressionAst* expression;
    ArgumentType argumentType;
};

class ParameterAst : public Ast
{
    enum ParameterType
    {
        SubListParameter,
        ListParameter,
        DictParameter,
        DefaultParameter
    };

public:
    ParameterAst( Ast* parent );
    QList<ParameterAst*> sublist;
    ExpressionAst* expression;
    QString parameterName;
    ParameterType parameterType;
};

class SuiteAst : public Ast
{
    public:
        SuiteAst( Ast* );
        QList<StatementAst*> statements;
};

class StatementAst : public Ast
{
    public:
        StatementAst( Ast* );
};

class IfAst : public StatementAst
{
    public:
        IfAst( Ast* );
        QMap<ExpressionAst*, SuiteAst*> expressionSuites;
        SuiteAst* elseSuite;
};

class WhileAst : public StatementAst
{
    public:
        WhileAst( Ast* );
        ExpressionAst* expression;
        SuiteAst* whileSuite;
        SuiteAst* elseSuite;
};

class ForAst : public StatementAst
{
    public:
        ForAst( Ast* );
        QList<TargetAst*> targets;
        QList<ExpressionAst*> expressions;
        SuiteAst* forSuite;
        SuiteAst* elseSuite;
};

class ClassDefinitionAst : public StatementAst
{

public:
    ClassDefinitionAst( Ast* parent );
    QString className;
    QList<ExpressionAst*> inheritance;
    SuiteAst* suite;
};

class TryAst : public StatementAst
{
    public:
        TryAst( Ast* );
        SuiteAst* trySuite;
        SuiteAst* elseSuite;
        SuiteAst* finallySuite;
        QList<ExceptAst*> exceptions;
};

class ExceptAst : public Ast
{
    public:
        ExceptAst( Ast* );
        ExpressionAst* expression;
        TargetAst* target;
        SuiteAst* suite;
};

class WithAst : public StatementAst
{
    public:
        WithAst( Ast* );
        ExpressionAst* expression;
        TargetAst* target;
        SuiteAst* suite;
};

class ExecAst : public StatementAst
{
    public:
        ExecAst( Ast* );
        ArithmeticExpressionAst* expression;
        DictionaryAst* globalsAndLocals;
        ExpressionAst* localsOnly;
};

class GlobalAst : public StatementAst
{
    public:
        GlobalAst( Ast* );
        QList<QString> identifiers;
};

class ImportAst : public StatementAst
{
    enum ImportType
    {
        FromImport,
        PlainImport,
        StarImport
    };
    public:
        ImportAst( Ast* );
        ImportType importType;
};

class PlainImportAst : public ImportAst
{
    public:
        PlainImportAst( Ast* );
        QMap<QStringList,QString> modulesAsName;
};

class StarImportAst : public ImportAst
{
    public:
        StarImportAst( Ast* );
        QStringList modulepath;
};

class FromImportAst : public ImportAst
{
    public:
        FromImportAst( Ast* );
        QList<QString> modulepath;
        int numLeadingDots;
        QMap<QString,QString> identifierAsName;
};

class RaiseAst : public StatementAst
{
    public:
        RaiseAst( Ast* );
        ExpressionAst* type;
        ExpressionAst* value;
        ExpressionAst* traceback;
};

class PrintAst : public StatementAst
{
    public:
        PrintAst( Ast* );
        QList<ExpressionAst*> printables;
        ExpressionAst* outfile;
};

class ReturnAst : public StatementAst
{
    public:
        ReturnAst( Ast* );
        QList<ExpressionAst*> expressions;
};

class YieldAst : public StatementAst
{
    public:
        YieldAst( Ast* );
        QList<ExpressionAst*> expressions;
};

class DelAst : public StatementAst
{
    public:
        DelAst( Ast* );
        QList<TargetAst*> targets;
};

class AssertAst : public StatementAst
{
    public:
        AssertAst( Ast* );
        ExpressionAst* assertTest;
        ExpressionAst* exceptionValue;
};

class ExpressionStatementAst : public StatementAst
{
    public:
        ExpressionStatementAst( Ast* );
        QList<ExpressionAst*> expressions;
};

class AssignmentAst : public StatementAst
{
    enum OpType
    {
        AddEqualOp,
        SubEqualOp,
        MultiplyEqualOp,
        DivideEqualOp,
        ModuloEqualOp,
        PowEqualOp,
        LeftShiftEqualOp,
        RightShiftEqualOp,
        XorEqualOp,
        OrEqualOp,
        AndEqualOp,
        AssignmentOp
    };

    public:
        AssignmentAst( Ast* );
        OpType operation;
        QList<QList<TargetAst*> > targetlists;
        QList<ExpressionAst*> expressions;
        YieldAst* yield;
};

class TargetAst : public Ast
{
    enum ListType
    {
        TupleList,
        NormalList
    };
    public:
        TargetAst( Ast* );
        QString identifier;
        QList<TargetAst*> targets;
        ListType listType;
        AttributeReferenceAst* attributeReference;
        SubscriptAst* subscript;
        SliceAst* slice;
};

class AtomAst : public Ast
{
    public:
        AtomAst( Ast* );
        QString identifier;
        QString literal;
        EnclosureAst* enclosure;
};

class EnclosureAst : public Ast
{
    public:
        EnclosureAst( Ast* );
        QList<ExpressionAst*> parenthesizedform;
        ListAst* list;
        GeneratorAst* generator;
        DictionaryAst* dict;
        QList<ExpressionAst*> stringconversion;
        YieldAst* yield;
};

class ListAst : public Ast
{
    public:
        ListAst( Ast* );
        QList<ExpressionAst*> expressions;
        ListForAst* listGenerator;
};

class ListForAst : public Ast
{
    public:
        ListForAst( Ast* );
        QList<TargetAst*> targets;
        QList<ExpressionAst*> oldExpressions;
        ListForAst* nextGenerator;
        ListIfAst* nextCondition;
};

class ListIfAst : public Ast
{
    public:
        ListIfAst( Ast* );
        ExpressionAst* expression;
        ListForAst* nextGenerator;
        ListIfAst* nextCondition;
};

class GeneratorAst : public Ast
{
    public:
        GeneratorAst( Ast* );
        ExpressionAst* expression;
        GeneratorForAst* generator;
};

class GeneratorForAst : public Ast
{
    public:
        GeneratorForAst( Ast* );
        QList<TargetAst*> targets;
        OrTestAst* inList;
        GeneratorForAst* nextGenerator;
        GeneratorIfAst* nextCondition;
};

class GeneratorIfAst : public Ast
{
    public:
        GeneratorIfAst( Ast* );
        ExpressionAst* expression;
        GeneratorForAst* nextGenerator;
        GeneratorIfAst* nextCondition;
};

class DictionaryAst : public Ast
{
    public:
        DictionaryAst( Ast* );
        QList<QMap<ExpressionAst*, ExpressionAst*> > dictionary;
};

class PrimaryAst : public Ast
{
    public:
        PrimaryAst( Ast* );
        AtomAst* atom;
        AttributeReferenceAst* attributeReference;
        SubscriptAst* subscript;
        SliceAst* slice;
        CallAst* call;
};

class AttributeReferenceAst : public Ast
{
    public:
        AttributeReferenceAst( Ast* );
        PrimaryAst* primary;
        QString identifier;
};

class SubscriptAst : public Ast
{
    public:
        SubscriptAst( Ast* );
        PrimaryAst* primary;
        QList<ExpressionAst*> expressions;
};

class SliceAst : public Ast
{
    public:
        SliceAst( Ast* );
        PrimaryAst* primary;
        QPair<ExpressionAst*,ExpressionAst*> simpleSliceBounds;
        QList<SliceItemAst*> extendedSliceList;
};

class SliceItemAst : public Ast
{
    enum SliceItemType
    {
        EllipsisSlice,
        ProperSlice,
        ExpressionSlice
    };
    public:
        SliceItemAst( Ast* );
        ExpressionAst* expression;
        SliceItemType itemType;
        QPair<ExpressionAst*,ExpressionAst*> bounds;
        ExpressionAst* stride;
};

class CallAst : public Ast
{
    public:
        CallAst( Ast* );
        PrimaryAst* callable;
        QList<ArgumentAst*> arguments;
        ExpressionAst* expression;
        GeneratorForAst* generator;
};

class ArithmeticExpressionAst : public Ast
{
    enum ArithmeticOperation
    {
        PowerOp,
        UnaryPlus,
        UnaryMinus,
        UnaryTilde,
        BinaryPlus,
        BinaryMinus,
        BinaryMultiply,
        BinaryDivide,
        BinaryModulo,
        BinaryFloor,
        BinaryLeftShift,
        BinaryRightShift,
        BinaryAnd,
        BinaryOr,
        BinaryXor,
        NoOp
    };
    public:
        ArithmeticExpressionAst( Ast* );
};

class UnaryExpressionAst : public ArithmeticExpressionAst
{
    public:
        UnaryExpressionAst( Ast* );
        PrimaryAst* primary;
        UnaryExpressionAst* nextExpression;
};

class BinaryExpressionAst : public ArithmeticExpressionAst
{
    public:
        BinaryExpressionAst( Ast* );
        BinaryExpressionAst* lhs;
        UnaryExpressionAst* rhs;
};

class ComparisonAst : public Ast
{
    enum ComparisonOperator
    {
        LessThanOp,
        GreaterThanOp,
        EqualOp,
        UnequalOp,
        LessEqualOp,
        GreaterEqualOp,
        IsOp,
        IsNotOp,
        InOp,
        NotInOp
    };
    public:
        ComparisonAst( Ast* );
        BinaryExpressionAst* firstComparator;
        QMap<ComparisonOperator,BinaryExpressionAst*> comparatorList;
};

class BooleanAst : public Ast
{
    enum BooleanOperation
    {
        NotOp,
        AndOp,
        OrOp
    };
    public:
        BooleanAst( Ast* );
        BooleanOperationAst* lhs;
        BooleanOperation opType;
        ComparisonAst* rhs;
};

class ExpressionAst : public Ast
{
    enum ExpressionType
    {
        BooleanExpression,
        IfElseExpression,
        LambdaExpression
    };
    public:
        ExpressionAst( Ast* );
        ExpressionType expressionType;
        BooleanAst* booleanExpression;
        ExpressionAst* elseExpression;
        LambdaAst* lambda;
};

class LambdaAst : public Ast
{
    public:
        LambdaAst( Ast* );
        QList<ParameterAst*> parameters;
        ExpressionAst* expression;
};

}

#endif
