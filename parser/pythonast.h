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
        ArgumentAst,
        AssertAst,
        AssignmentAst,
        AtomAst,
        AttributeReferenceAst,
        BinaryExpressionAst,
        BooleanAst,
        BooleanExpressionAst,
        CallAst,
        ClassDefinitionAst,
        CodeAst,
        ComparisonAst,
        DecoratorAst,
        DelAst,
        DictionaryAst,
        EllipsisSliceAst,
        EnclosureAst,
        ExceptAst,
        ExecAst,
        ExpressionSliceAst,
        ExpressionStatementAst,
        ExtendedSliceAst,
        ForAst,
        FromImportAst,
        FunctionDefinitionAst,
        GeneratorAst,
        GeneratorForAst,
        GeneratorIfAst,
        GlobalAst,
        IfAst,
        LambdaAst,
        ListAst,
        ListForAst,
        ListIfAst,
        ParameterAst,
        PlainImportAst,
        PrintAst,
        ProperSliceItemAst,
        RaiseAst,
        ReturnAst,
        SimpleSliceAst,
        StarImportAst,
        SubscriptAst,
        TargetAst,
        TryAst,
        UnaryExpressionAst,
        WhileAst,
        WithAst,
        YieldAst
    };

public:
    Ast( Ast* parent );
    AstType astType;
    Ast* parent;
    /**
     * This is the absolute position in the file that this Ast node starts at.
     *
     * Counting starts with 0.
     */
    int start;

    /**
     * This is the absolute position in the file that this Ast node ends at.
     *
     * Counting starts with 0.
     */
    int end;

    /**
     * This is the column in the starting line where this Ast node starts.
     *
     * Counting starts with 0.
     */
    int startCol;

    /**
     * This is the line where this Ast node starts.
     *
     * Counting starts with 0.
     */
    int startLine;

    /**
     * This is the column in the ending line where this Ast node ends.
     *
     * Counting starts with 0.
     */
    int endCol;

    /**
     * This is the line where this Ast node ends.
     *
     * Counting starts with 0.
     */
    int endLine;
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
    QList<StatementAst*> functionBody;
};

class DecoratorAst : public Ast
{

public:
    DecoratorAst( Ast* parent );
    QStringList dottedName;
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
    ExpressionAst* listOrDictName;
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
    QList<ParameterAst*> parameterList;
    ExpressionAst* defaultValue;
    QString parameterName;
    ParameterType parameterType;
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
    QMap<ExpressionAst*, QList<StatementAst*> > ifElseIfList;
    QList<StatementAst*> elseBody;
};

class WhileAst : public StatementAst
{

public:
    WhileAst( Ast* );
    ExpressionAst* condition;
    QList<StatementAst*> whileBody;
    QList<StatementAst*> elseBody;
};

class ForAst : public StatementAst
{

public:
    ForAst( Ast* );
    QList<TargetAst*> assignedTargets;
    QList<ExpressionAst*> iterable;
    QList<StatementAst*> forBody;
    QList<StatementAst*> elseBody;
};

class ClassDefinitionAst : public StatementAst
{

public:
    ClassDefinitionAst( Ast* parent );
    QString className;
    QList<ExpressionAst*> inheritance;
    QList<StatementAst*> classBody;
};

class TryAst : public StatementAst
{

public:
    TryAst( Ast* );
    QList<StatementAst*> tryBody;
    QList<StatementAst*> elseBody;
    QList<StatementAst*> finallyBody;
    QList<ExceptAst*> exceptions;
};

class ExceptAst : public Ast
{

public:
    ExceptAst( Ast* );
    ExpressionAst* exceptionDeclaration;
    TargetAst* exceptionValue;
    QList<StatementAst*> exceptionBody;
};

class WithAst : public StatementAst
{

public:
    WithAst( Ast* );
    ExpressionAst* context;
    TargetAst* name;
    QList<StatementAst*> body;
};

class ExecAst : public StatementAst
{

public:
    ExecAst( Ast* );
    ArithmeticExpressionAst* executable;
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

public:
    ImportAst( Ast* );
};

class PlainImportAst : public ImportAst
{

public:
    PlainImportAst( Ast* );
    QMap<QStringList, QString> modulesAsName;
};

class StarImportAst : public ImportAst
{

public:
    StarImportAst( Ast* );
    QStringList modulePath;
};

class FromImportAst : public ImportAst
{

public:
    FromImportAst( Ast* );
    QList<QString> modulePath;
    int numLeadingDots;
    QMap<QString, QString> identifierAsName;
};

class RaiseAst : public StatementAst
{

public:
    RaiseAst( Ast* );
    ExpressionAst* exceptionType;
    ExpressionAst* exceptionValue;
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
    QList<ExpressionAst*> returnValues;
};

class YieldAst : public StatementAst
{

public:
    YieldAst( Ast* );
    QList<ExpressionAst*> yieldValue;
};

class DelAst : public StatementAst
{

public:
    DelAst( Ast* );
    QList<TargetAst*> deleteObjects;
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
    QList<QList<TargetAst*> > targets;
    QList<ExpressionAst*> value;
    YieldAst* yieldValue;
};

class TargetAst : public Ast
{
    enum TargetType
    {
        TupleTarget,
        ListTarget,
        AttributeReferenceTarget,
        SubscriptTarget,
        SliceTarget
    };

public:
    TargetAst( Ast* );
    QString identifier;
    QList<TargetAst*> listItems;
    TargetType targetType;
    AttributeReferenceAst* attributeReference;
    SubscriptAst* subscript;
    SliceAst* slice;
};

class AtomAst : public PrimaryAst
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
    QList<ExpressionAst*> stringConversion;
    YieldAst* yield;
};

class ListAst : public Ast
{

public:
    ListAst( Ast* );
    QList<ExpressionAst*> plainList;
    ListForAst* listGenerator;
};

class ListForAst : public Ast
{

public:
    ListForAst( Ast* );
    QList<TargetAst*> assignedTargets;
    QList<ExpressionAst*> iterableObject;
    ListForAst* nextGenerator;
    ListIfAst* nextCondition;
};

class ListIfAst : public Ast
{

public:
    ListIfAst( Ast* );
    ExpressionAst* condition;
    ListForAst* nextGenerator;
    ListIfAst* nextCondition;
};

class GeneratorAst : public Ast
{

public:
    GeneratorAst( Ast* );
    ExpressionAst* generatedValue;
    GeneratorForAst* generator;
};

class GeneratorForAst : public Ast
{

public:
    GeneratorForAst( Ast* );
    QList<TargetAst*> assignedTargets;
    OrTestAst* iterableObject;
    GeneratorForAst* nextGenerator;
    GeneratorIfAst* nextCondition;
};

class GeneratorIfAst : public Ast
{

public:
    GeneratorIfAst( Ast* );
    ExpressionAst* condition;
    GeneratorForAst* nextGenerator;
    GeneratorIfAst* nextCondition;
};

class DictionaryAst : public Ast
{

public:
    DictionaryAst( Ast* );
    QMap<ExpressionAst*, ExpressionAst*> dictionary;
};

class PrimaryAst : public Ast
{

public:
    PrimaryAst( Ast* );
};

class AttributeReferenceAst : public PrimaryAst
{

public:
    AttributeReferenceAst( Ast* );
    PrimaryAst* primary;
    QString identifier;
};

class SubscriptAst : public PrimaryAst
{

public:
    SubscriptAst( Ast* );
    PrimaryAst* primary;
    QList<ExpressionAst*> subscription;
};

class SliceAst : public PrimaryAst
{

public:
    SliceAst( Ast* );
    PrimaryAst* primary;
};

class ExtendedSliceAst : public SliceAst
{

public:
    ExtendedSliceAst( Ast* );
    QList<SliceItemAst*> extendedSliceList;
};

class SimpleSliceAst : public SliceAst
{

public:
    SimpleSliceAst( Ast* );
    QPair<ExpressionAst*, ExpressionAst*> simpleSliceBounds;
};

class SliceItemAst : public Ast
{

public:
    SliceItemAst( Ast* );
};


class ProperSliceItemAst : public SliceItemAst
{

public:
    ProperSliceItemAst( Ast* );
    QPair<ExpressionAst*, ExpressionAst*> bounds;
    ExpressionAst* stride;
};

class ExpressionSliceAst : public SliceItemAst
{

public:
    ExpressionSliceAst( Ast* );
    ExpressionAst* sliceExpression;
};

class EllipsisSliceAst : public SliceItemAst
{

public:
    EllipsisSliceAst( Ast* );
};

class CallAst : public PrimaryAst
{

public:
    CallAst( Ast* );
    PrimaryAst* callable;
    QList<ArgumentAst*> arguments;
    ExpressionAst* callValue;
    GeneratorForAst* callGenerator;
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
    ArithmeticOperation opType;
};

class UnaryExpressionAst : public ArithmeticExpressionAst
{

public:
    UnaryExpressionAst( Ast* );
    PrimaryAst* primary;
    UnaryExpressionAst* operand;
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
    QMap<ComparisonOperator, BinaryExpressionAst*> comparatorList;
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

public:
    ExpressionAst( Ast* );
};

class BooleanExpressionAst : ExpressionAst
{

public:
    BooleanExpressionAst( Ast* );
    BooleanAst* mainExpression;
    BooleanAst* condition;
    ExpressionAst* elseExpression;
};

class LambdaAst : public ExpressionAst
{

public:
    LambdaAst( Ast* );
    QList<ParameterAst*> parameters;
    ExpressionAst* expression;
};

}

#endif
