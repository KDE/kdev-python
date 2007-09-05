/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright (C) 2007 Andreas Pakulat <apaku@gmx.de>                     *
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

#ifndef PYTHONAST_H
#define PYTHONAST_H

namespace Python
{
class Ast
{
public:
    int m_startingColumn;
    int m_startingRow;
    int m_startingPos;
    int m_endingColumn;
    int m_endingRow;
    int m_endingPos;
};

class StatementAst : public Ast
{
};

class ValueAst : public Ast
{
public:
    QString value;
};

class SuiteAst : public Ast
{
public:
    QList<StatementAst*> m_statements;
};

class ElseIfAst : public StatementAst
{
public:
    ExpressionAst* m_expression;
    SuiteAst* m_suite;
};

class IfAst : public StatementAst
{
public:
    ExpressionAst* m_ifExpression;
    SuiteAst* m_ifSuite;
    QList<ElseIfAst* > m_elseIfSuites;
    SuiteAst* m_elseSuite;
};

class WhileAst : public StatementAst
{
public:
    ExpressionAst* m_whileExpression;
    SuiteAst* m_whileSuite;
    SuiteAst* m_elseSuite;
};

class ForAst : public StatementAst
{
public:
    QList<TargetAst*> m_forTargets;
    ExpressionListAst* m_expressions;
    SuiteAst* m_forSuite;
    SuiteAst* m_elseSuite;
};

class ExceptAst : public Ast
{
public:
    ExpressionAst* m_exception;
    AssignmentAst* m_target;
    SuiteAst* m_suite
};

class TryAst : public StatementAst
{
public:
    SuiteAst* m_trySuite;
    SuiteAst* m_elseSuite;
    SuiteAst* m_finallySuite;
    QList<ExceptAst*> m_exceptions;
};

class ClassAst : public StatementAst
{
public:
    IdentifierAst* m_identifier;
    ExpressionListAst* m_inheritance;
    SuiteAst* m_suite;
};

class DecoratorAst : public Ast
{
public:
    QList<IdentifierAst*> m_name;
    QList<ArgumentAst*> m_arguments;
};

class ParameterAst : public Ast
{
public:
    enum ParameterType
    {
        DefaultParameter,
        PositionalParameter,
        KeywordParameter
    };

public:
    IdentifierAst* m_identifier;
    QList<ParameterAst*> m_sublist;
    ExpressionAst* m_expression;
    ParameterType m_type;
};

class FunctionAst : public StatementAst
{
public:
    QList<DecoratorAst*> m_decorators;
    IdentifierAst* m_identifier;
    QList<ParameterAst*> m_parameters;
    SuiteAst* m_suite;
};

class ExpressionListAst : StatementAst
{
public:
    QList<ExpressionAst*> m_expressions;
};

class AssertAst : StatementAst
{
public:
    ExpressionAst* m_assertOnExpression;
    ExpressionAst* m_raiseExpression;
};

class AssignmentAst : StatementAst
{
public:
    enum AssignmentType
    {
        SimpleAssignment,
        PlusAssignment,
        MinusAssignment,
        StarAssignment,
        DivisionAssignment,
        ModuloAssignment,
        PowerAssignment,
        LShiftAssignment,
        RShiftAssignment,
        AndAssignment,
        XorAssignment,
        OrAssignment
    };

public:
    QList< TargetAst*> m_targetList;
    AssignmentType m_type;
    ExpressionListAst* m_expressionList;
};

class TargetAst : public Ast
{
public:
    enum TargetType
    {
        TargetList,
        IdentifierTarget,
        AttributeReferenceTarget,
        SubscriptionTarget,
        SliceTarget
    };
public:
    QList< TargetAst* > m_targetList;
    //This is either a atribute reference, a subscription or a slice
    PrimaryAst* m_primary;
    TargetType m_type;
};

// This class is for things like del, pass, continue, better name would be appreciated
class KeywordStatementAst : public StatementAst
{
    enum KeywordType
    {
        PassKeyword,
        DelKeyword,
        PrintKeyword,
        ReturnKeyword,
        YieldKeyword,
        RaiseKeyword,
        BreakKeyword,
        ContinueKeyword,
        ImportKeyword,
        GlobalKeyword,
        ExecKeyword
    };
public:
    KeywordType m_type;
};

class DelKeywordAst : public KeywordStatementAst
{
public:
    QList<TargetAst*> m_targetList;
};

class PrintKeywordAst : public KeywordStatementAst
{
public:
    ExpressionListAst* m_expressionList;
};

class ReturnKeywordAst : public KeywordStatementAst
{
public:
    ExpressionListAst* m_expressionList;
};

class YieldKeywordAst : public KeywordStatementAst
{
public:
    ExpressionListAst* m_expressionList;
};

class RaiseKeywordAst : public KeywordStatementAst
{
public:
    ExpressionAst* m_typeExpression;
    ExpressionAst* m_valueExpression;
    ExpressionAst* m_tracebackExpression;
};

class ImportAst : public Ast
{
public:
    IdentifierAst* m_import;
    ValueAst* m_alias;

class ImportKeywordAst : public KeywordStatementAst
{
public:
    enum ImportType
    {
        FromImport,
        StarImport,
        SimpleImport
    };
public:
    ImportType m_type;
    QList<ImportAst*> m_modules;
    QList<ImportAst*> m_imports;
};

class GlobalKeywordAst : public KeywordStatementAst
{
public:
    QList<IdentifierAst*> m_globals;
};

class ExecKeywordAst : public KeywordStatementAst
{
public:
    ExpressionAst* m_executeExpression;
    ExpressionAst* m_globalDictionary;
    ExpressionAst* m_localDictionary;
};

class PrimaryAst : public Ast
{
};

class AtomAst : public PrimaryAst
{
public:
    QString m_value;
};

class IdentifierAst : public AtomAst
{
};

class LiteralAst : public AtomAst
{
public:
    enum LiteralType
    {
        StringLiteral,
        IntegerLiteral,
        LongLiteral,
        FloatLiteral,
        ImaginaryLiteral
    };

public:
    LiteralType m_type;
};

class ParenthesisFormAst : public AtomAst
{
public:
    bool isTuple();

public:
    ExpressionListAst* m_expressionList;
};

class ListAst : public AtomAst
{
public:
    ExpressionListAst* m_expressionList;
    ForAst* m_listComprehension;
};

class GeneratorAst : public AtomAst
{
public:
    ExpressionAst* m_generatorExpression;
    ForAst* m_generatorLoop;
};

class StringConversionAst : public AtomAst
{
public:
    ExpressionListAst* m_expressionList;
};

class DictionaryAst : public AtomAst
{
public:
    QMap< ExpressionAst*, ExpressionAst* > m_dictionary;
};

class AttributeReferenceAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    IdentifierAst* m_identifier;
};

class SubscriptionAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    ExpressionListAst* m_expressionList;
};

class SliceAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    QList<SliceItemAst*> m_slices;
};

class SliceItemAst : public Ast
{
public:
    enum SliceItemType
    {
        Ellipsis,
        LongSlice,
        ShortSlice,
        Expression
    };

public:
    ExpressionAst* m_lowerBound;
    ExpressionAst* m_upperBound;
    ExpressionAst* m_plainExpression;
    ExpressionAst* m_stride;
    SliceItemType m_type;
};

class CallAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    QList<ArgumentAst*> m_arguments;
};

class ArgumentAst : public Ast
{
public:
    enum ArgumentType
    {
        PositionalArgument,
        KeywordArgument,
        SequenceArgument,
        DictionaryArgument,
    };

public:
    ExpressionAst* m_expression;
    ArgumentType m_type;
};

class KeywordArgumentAst : public ArgumentAst
{
public:
    IdentifierAst* m_identifier;
};

class ExpressionAst : public Ast
{
};

class OperatorAst : public ExpressionAst
{
public:
    enum OperatorType
    {
        PowerOperator,
        UnaryMinusOperator,
        UnaryPlusOperator,
        UnaryTildeOperator,
        BinaryMultiplyOperator,
        BinaryFloorDivOperator,
        BinaryDivisionOperator,
        BianryModuloOperator,
        BinaryPlusOperator,
        BinaryMinusOperator,
        LShiftOperator,
        RShiftOperator,
        BitWiseAndOperator,
        BitWiseXorOperator,
        BitWiseOrOperator,
        ComparisonLessOperator,
        ComparisonGreaterOperator,
        ComparisonEqualOperator,
        ComparisonGreaterThanOperator,
        ComparisonLessThanOperator,
        ComparisonUnequalOperator,
        ComparisonIsOperator,
        ComparisonIsNotOperator,
        ComparisonInOperator,
        ComparisonNotInOperator,
        BooleanAndOperator,
        BooleanOrOperator,
        BooleanNotOperator
    };

public:
    OperatorType m_type;
};

class UnaryOperatorAst : public OperatorAst
{
public:
    UnaryOperatorAst* m_expression;
};

class PowerAst : public UnaryOperatorAst
{
public:
    PrimaryAst* m_primary;
};

class BinaryOperatorAst : public OperatorAst
{
public:
    UnaryOperatorAst* m_unaryExpression;
    BinaryOperatorAst* m_binaryExpression;
};

class ShiftOperatorAst : public OperatorAst
{
public:
    BinaryOperatorAst* m_binaryExpression;
    ShiftOperatorAst* m_shiftExpression;
};

class BitWiseOperatorAst : public OperatorAst
{
public:
    ShiftOperatorAst* m_shiftExpression;
    BitWiseOperatorAst* m_bitwiseExpression;
};

class ComparisonAst : public OperatorAst
{
public:
    BooleanAst* m_firstExpression;
    ComparisonAst* m_secondExpression;
};

class BooleanAst : public OperatorAst
{
public:
    BooleanAst* m_firstTest;
    BooleanAst* m_secondTest;
};

class LambdaAst : public ExpressionAst
{
public:
    ParameterListAst* m_parameters;
    ExpressionAst* m_expression;
};
}

#endif

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
