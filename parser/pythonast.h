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

#include "parserexport.h"
#include <QList>
#include <QMap>
#include <QString>

namespace Python
{

class ExpressionAst;
class ValueAst;
class StatementAst;
class ElseIfAst;
class IfAst;
class WhileAst;
class ForAst;
class ExceptAst;
class TryAst;
class ClassAst;
class DecoratorAst;
class ParameterAst;
class FunctionAst;
class ExpressionListAst;
class AssignmentAst;
class AssertAst;
class TargetAst;
class DelKeywordAst;
class PrintKeywordAst;
class ReturnKeywordAst;
class YieldKeywordAst;
class RaiseKeywordAst;
class ImportAst;
class ImportKeywordAst;
class ExecKeywordAst;
class PrimaryAst;
class GlobalKeywordAst;
class AtomAst;
class LiteralAst;
class ParenthesizedExpressionListAst;
class ListAst;
class GeneratorAst;
class StringConversionAst;
class AttributeReferenceAst;
class DictionaryAst;
class SubscriptionAst;
class LambdaAst;
class ArgumentAst;
class CallAst;
class UnaryOperatorAst;
class PowerAst;
class BinaryOperatorAst;
class ShiftOperatorAst;
class BitWiseOperatorAst;
class ComparisonAst;
class BooleanAst;
class SliceAst;
class SliceItemAst;
class IdentifierAst;

namespace KDevelop
{
class DUContext;
}

/**
 * This is the base class of all Ast nodes, it provides information about
 * the start and end of the Ast node - as column/row and also absolute offset.
 *
 * Also allows to set the active DUChain context for the Ast
 */
class KDEVPYTHONPARSER_EXPORT Ast
{
public:

    enum AstType
    {
        Pass,
        Del,
        Print,
        Return,
        Yield,
        Raise,
        Break,
        Continue,
        Import,
        Global,
        Exec,
        Value,
        ElseIf,
        If,
        While,
        For,
        Except,
        Try,
        Class,
        Decorator,
        Parameter,
        Function,
        Assignment,
        Assert,
        Target,
        Primary,
        Atom,
        Literal,
        ParenthesizedExpressionList,
        List,
        Generator,
        StringConversion,
        AttributeReference,
        Dictionary,
        Subscription,
        Lambda,
        Argument,
        Call,
        UnaryOperator,
        Power,
        BinaryOperator,
        ShiftOperator,
        BitWiseOperator,
        Comparison,
        Boolean,
        Slice,
        SliceItem,
        Identifier
    };

    /**
     * The column in which the first part of this node starts
     */
    int m_startingColumn;

    /**
     * The row in which the first part of this node starts
     */
    int m_startingRow;

    /**
     * The offset in which the first part of this node starts
     */
    int m_startingOffset;

    /**
     * The column in which the last part of this node starts
     */
    int m_endingColumn;

    /**
     * The row in which the last part of this node starts
     */
    int m_endingRow;

    /**
     * The pffset in which the last part of this node starts
     */
    int m_endingOffset;

    /**
     * The DUChain Context to which this Ast belongs
     */
    KDevelop::DUContext* m_context;

    AstType m_type;
};

/**
 * Abstract base for all statements in the language, this Ast doesn't differ
 * betwen compound and simple statement as there's no need to do so
 */
class KDEVPYTHONPARSER_EXPORT StatementAst : public Ast
{
};

/**
 * Simple values, like aliases for imports, plain QString is
 * not sufficient because we need the context and also the
 * position information
 */
class KDEVPYTHONPARSER_EXPORT ValueAst : public Ast
{
public:
    /**
     * the value of the underlying token
     */
    QString value;
};

/**
 * Encapsulates the expression and the statements of an elif
 * This is a bit nicer than a QPair<>
 */
class KDEVPYTHONPARSER_EXPORT ElseIfAst : public StatementAst
{
public:
    ExpressionAst* m_expression;
    QList<StatementAst*> m_statements;
};

/**
 * An if statement
 *
 * the members m_elseIfList and m_elseStatements may be empty lists
 * Neither the m_ifExpression nor the m_ifStatements can be 0 or empty
 */
class KDEVPYTHONPARSER_EXPORT IfAst : public StatementAst
{
public:
    ExpressionAst* m_ifExpression;
    QList<StatementAst*> m_ifStatements;
    QList<ElseIfAst* > m_elseIfList;
    QList<StatementAst*> m_elseStatements;
};

class KDEVPYTHONPARSER_EXPORT WhileAst : public StatementAst
{
public:
    ExpressionAst* m_whileExpression;
    QList<StatementAst*> m_whileStatements;
    QList<StatementAst*> m_elseStatements;
};

class KDEVPYTHONPARSER_EXPORT ForAst : public StatementAst
{
public:
    QList<TargetAst*> m_forTargets;
    QList<ExpressionAst*> m_forExpressions;
    QList<StatementAst*> m_forStatements;
    QList<StatementAst*> m_elseStatements;
};

class KDEVPYTHONPARSER_EXPORT ExceptAst : public Ast
{
public:
    ExpressionAst* m_exception;
    TargetAst* m_target;
    QList<StatementAst*> m_statements;
};

class KDEVPYTHONPARSER_EXPORT TryAst : public StatementAst
{
public:
    QList<StatementAst*> m_tryStatements;
    QList<StatementAst*> m_elseStatements;
    QList<StatementAst*> m_finallyStatements;
    QList<ExceptAst*> m_exceptions;
};

class KDEVPYTHONPARSER_EXPORT ClassAst : public StatementAst
{
public:
    IdentifierAst* m_identifier;
    QList<ExpressionAst*> m_inheritance;
    QList<StatementAst*> m_statements;
};

class KDEVPYTHONPARSER_EXPORT DecoratorAst : public Ast
{
public:
    QList<IdentifierAst*> m_name;
    QList<ArgumentAst*> m_arguments;
};

class KDEVPYTHONPARSER_EXPORT ParameterAst : public Ast
{
public:
    enum ParameterType
    {
        DefaultParameter,
        PositionalParameter,
        KeywordParameter
    };
    IdentifierAst* m_identifier;
    QList<ParameterAst*> m_sublist;
    ExpressionAst* m_expression;
    ParameterType m_parameterType;
};

class KDEVPYTHONPARSER_EXPORT FunctionAst : public StatementAst
{
public:
    QList<DecoratorAst*> m_decorators;
    IdentifierAst* m_identifier;
    QList<ParameterAst*> m_parameters;
    QList<StatementAst*> m_statements;
};

class KDEVPYTHONPARSER_EXPORT AssertAst : public StatementAst
{
public:
    ExpressionAst* m_assertOnExpression;
    ExpressionAst* m_raiseExpression;
};

class KDEVPYTHONPARSER_EXPORT AssignmentAst : public StatementAst
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
    QList< TargetAst*> m_targetList;
    AssignmentType m_assignmentType;
    QList<ExpressionAst*> m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT TargetAst : public Ast
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
    QList< TargetAst* > m_targetList;
    //This is either a attribute reference, a subscription or a slice
    PrimaryAst* m_primary;
    TargetType m_targetType;
};

class KDEVPYTHONPARSER_EXPORT DelKeywordAst : public StatementAst
{
public:
    QList<TargetAst*> m_targetList;
};

class KDEVPYTHONPARSER_EXPORT PrintKeywordAst : public StatementAst
{
public:
    QList<ExpressionAst*> m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT ReturnKeywordAst : public StatementAst
{
public:
    QList<ExpressionAst*> m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT YieldKeywordAst : public StatementAst
{
public:
    QList<ExpressionAst*> m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT RaiseKeywordAst : public StatementAst
{
public:
    ExpressionAst* m_typeExpression;
    ExpressionAst* m_valueExpression;
    ExpressionAst* m_tracebackExpression;
};

class KDEVPYTHONPARSER_EXPORT ImportAst : public Ast
{
public:
    IdentifierAst* m_import;
    ValueAst* m_alias;
};

class KDEVPYTHONPARSER_EXPORT ImportKeywordAst : public StatementAst
{
public:
    enum ImportType
    {
        FromImport,
        StarImport,
        SimpleImport
    };
    ImportType m_importType;
    QList<ImportAst*> m_modules;
    QList<ImportAst*> m_imports;
};

class KDEVPYTHONPARSER_EXPORT GlobalKeywordAst : public StatementAst
{
public:
    QList<IdentifierAst*> m_globals;
};

class KDEVPYTHONPARSER_EXPORT ExecKeywordAst : public StatementAst
{
public:
    ExpressionAst* m_executeExpression;
    ExpressionAst* m_globalDictionary;
    ExpressionAst* m_localDictionary;
};

class KDEVPYTHONPARSER_EXPORT PrimaryAst : public Ast
{
};

class KDEVPYTHONPARSER_EXPORT AtomAst : public PrimaryAst
{
public:
    QString m_value;
};

class KDEVPYTHONPARSER_EXPORT IdentifierAst : public AtomAst
{
};

class KDEVPYTHONPARSER_EXPORT LiteralAst : public AtomAst
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
    LiteralType m_literalType;
};

class KDEVPYTHONPARSER_EXPORT ParenthesizedExpressionListAst : public AtomAst
{
public:
    bool m_isTuple;
    QList<ExpressionAst*> m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT ListAst : public AtomAst
{
public:
    ExpressionListAst* m_expressionList;
    ForAst* m_listComprehension;
};

class KDEVPYTHONPARSER_EXPORT GeneratorAst : public AtomAst
{
public:
    ExpressionAst* m_generatorExpression;
    ForAst* m_generatorLoop;
};

class KDEVPYTHONPARSER_EXPORT StringConversionAst : public AtomAst
{
public:
    ExpressionListAst* m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT DictionaryAst : public AtomAst
{
public:
    QMap< ExpressionAst*, ExpressionAst* > m_dictionary;
};

class KDEVPYTHONPARSER_EXPORT AttributeReferenceAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    IdentifierAst* m_identifier;
};

class KDEVPYTHONPARSER_EXPORT SubscriptionAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    ExpressionListAst* m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT SliceAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    QList<SliceItemAst*> m_slices;
};

class KDEVPYTHONPARSER_EXPORT SliceItemAst : public Ast
{
public:
    enum SliceItemType
    {
        Ellipsis,
        LongSlice,
        ShortSlice,
        Expression
    };
    ExpressionAst* m_lowerBound;
    ExpressionAst* m_upperBound;
    ExpressionAst* m_plainExpression;
    ExpressionAst* m_stride;
    SliceItemType m_sliceType;
};

class KDEVPYTHONPARSER_EXPORT CallAst : public PrimaryAst
{
public:
    PrimaryAst* m_primary;
    QList<ArgumentAst*> m_arguments;
};

class KDEVPYTHONPARSER_EXPORT ArgumentAst : public Ast
{
public:
    enum ArgumentType
    {
        PositionalArgument,
        KeywordArgument,
        SequenceArgument,
        DictionaryArgument
    };
    ExpressionAst* m_expression;
    IdentifierAst* m_identifier;
    ArgumentType m_argumentType;
};

class KDEVPYTHONPARSER_EXPORT ExpressionAst : public Ast
{
};

class KDEVPYTHONPARSER_EXPORT UnaryOperatorAst : public ExpressionAst
{
public:
    enum UnaryOperatorType
    {
        UnaryMinusOperator,
        UnaryPlusOperator,
        UnaryTildeOperator
    };

    UnaryOperatorAst* m_expression;
    UnaryOperatorType m_opType;
};

class KDEVPYTHONPARSER_EXPORT PowerAst : public UnaryOperatorAst
{
public:
    PrimaryAst* m_primary;
};

class KDEVPYTHONPARSER_EXPORT BinaryOperatorAst : public ExpressionAst
{
public:
    enum BinaryOperatorType
    {
        BinaryMultiplyOperator,
        BinaryFloorDivOperator,
        BinaryDivisionOperator,
        BianryModuloOperator,
        BinaryPlusOperator,
        BinaryMinusOperator
    };
    UnaryOperatorAst* m_unaryExpression;
    BinaryOperatorAst* m_binaryExpression;
    BinaryOperatorType m_opType;
};

class KDEVPYTHONPARSER_EXPORT ShiftOperatorAst : public ExpressionAst
{
public:
    enum ShiftOperatorType
    {
        LShiftOperator,
        RShiftOperator
    };
    BinaryOperatorAst* m_binaryExpression;
    ShiftOperatorAst* m_shiftExpression;
    ShiftOperatorType m_opType;
};

class KDEVPYTHONPARSER_EXPORT BitWiseOperatorAst : public ExpressionAst
{
public:
    enum BitWiseOperatorType
    {
        BitWiseAndOperator,
        BitWiseXorOperator,
        BitWiseOrOperator
    };
    ShiftOperatorAst* m_shiftExpression;
    BitWiseOperatorAst* m_bitwiseExpression;
    BitWiseOperatorType m_opType;
};

class KDEVPYTHONPARSER_EXPORT ComparisonAst : public ExpressionAst
{
public:
    enum ComparisonOperatorType
    {
        ComparisonLessOperator,
        ComparisonGreaterOperator,
        ComparisonEqualOperator,
        ComparisonGreaterThanOperator,
        ComparisonLessThanOperator,
        ComparisonUnequalOperator,
        ComparisonIsOperator,
        ComparisonIsNotOperator,
        ComparisonInOperator,
        ComparisonNotInOperator
    };
    BooleanAst* m_firstExpression;
    ComparisonAst* m_secondExpression;
    ComparisonOperatorType m_opType;
};

class KDEVPYTHONPARSER_EXPORT BooleanAst : public ExpressionAst
{
public:
    enum BooleanOperatorType
    {
        BooleanAndOperator,
        BooleanOrOperator,
        BooleanNotOperator
    };
    BooleanAst* m_firstTest;
    BooleanAst* m_secondTest;
    BooleanOperatorType m_opType;
};

class KDEVPYTHONPARSER_EXPORT LambdaAst : public ExpressionAst
{
public:
    QList<ParameterAst*> m_parameters;
    ExpressionAst* m_expression;
};
}

#endif

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
