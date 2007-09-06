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
class OperatorAst;
class ClassAst;
class DecoratorAst;
class ParameterAst;
class FunctionAst;
class ExpressionListAst;
class AssignmentAst;
class AssertAst;
class KeywordStatementAst;
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
class TupleAst;
class ListAst;
class GeneratorAst;
class StringConversionAst;
class AttributeReferenceAst;
class DictionaryAst;
class SubscriptionAst;
class LambdaAst;
class KeywordArgumentAst;
class ArgumentAst;
class CallAst;
class ExpressionAst;
class UnaryOperatorAst;
class PowerAst;
class BinaryOperatorAst ;
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
    QList<StatementAst*> m_statements;;
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
    ExpressionListAst* m_expressions;
    QList<StatementAst*> m_forStatements;
    QList<StatementAst*> m_elseStatements;
};

class KDEVPYTHONPARSER_EXPORT ExceptAst : public Ast
{
public:
    ExpressionAst* m_exception;
    AssignmentAst* m_target;
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
    ExpressionListAst* m_inheritance;
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
    ParameterType m_type;
};

class KDEVPYTHONPARSER_EXPORT FunctionAst : public StatementAst
{
public:
    QList<DecoratorAst*> m_decorators;
    IdentifierAst* m_identifier;
    QList<ParameterAst*> m_parameters;
    QList<StatementAst*> m_statements;
};

class KDEVPYTHONPARSER_EXPORT ExpressionListAst : StatementAst
{
public:
    QList<ExpressionAst*> m_expressions;
};

class KDEVPYTHONPARSER_EXPORT AssertAst : StatementAst
{
public:
    ExpressionAst* m_assertOnExpression;
    ExpressionAst* m_raiseExpression;
};

class KDEVPYTHONPARSER_EXPORT AssignmentAst : StatementAst
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
    AssignmentType m_type;
    ExpressionListAst* m_expressionList;
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
    TargetType m_type;
};

// This class is for things like del, pass, continue, better name would be appreciated
class KDEVPYTHONPARSER_EXPORT KeywordStatementAst : public StatementAst
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
    KeywordType m_type;
};

class KDEVPYTHONPARSER_EXPORT DelKeywordAst : public KeywordStatementAst
{
public:
    QList<TargetAst*> m_targetList;
};

class KDEVPYTHONPARSER_EXPORT PrintKeywordAst : public KeywordStatementAst
{
public:
    ExpressionListAst* m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT ReturnKeywordAst : public KeywordStatementAst
{
public:
    ExpressionListAst* m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT YieldKeywordAst : public KeywordStatementAst
{
public:
    ExpressionListAst* m_expressionList;
};

class KDEVPYTHONPARSER_EXPORT RaiseKeywordAst : public KeywordStatementAst
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

class KDEVPYTHONPARSER_EXPORT ImportKeywordAst : public KeywordStatementAst
{
public:
    enum ImportType
    {
        FromImport,
        StarImport,
        SimpleImport
    };
    ImportType m_type;
    QList<ImportAst*> m_modules;
    QList<ImportAst*> m_imports;
};

class KDEVPYTHONPARSER_EXPORT GlobalKeywordAst : public KeywordStatementAst
{
public:
    QList<IdentifierAst*> m_globals;
};

class KDEVPYTHONPARSER_EXPORT ExecKeywordAst : public KeywordStatementAst
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
    LiteralType m_type;
};

class KDEVPYTHONPARSER_EXPORT TupleAst : public AtomAst
{
public:
    ExpressionListAst* m_expressionList;
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
    SliceItemType m_type;
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
    ArgumentType m_type;
};

class KDEVPYTHONPARSER_EXPORT KeywordArgumentAst : public ArgumentAst
{
public:
    IdentifierAst* m_identifier;
};

class KDEVPYTHONPARSER_EXPORT ExpressionAst : public Ast
{
};

class KDEVPYTHONPARSER_EXPORT OperatorAst : public ExpressionAst
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
    OperatorType m_type;
};

class KDEVPYTHONPARSER_EXPORT UnaryOperatorAst : public OperatorAst
{
public:
    UnaryOperatorAst* m_expression;
};

class KDEVPYTHONPARSER_EXPORT PowerAst : public UnaryOperatorAst
{
public:
    PrimaryAst* m_primary;
};

class KDEVPYTHONPARSER_EXPORT BinaryOperatorAst : public OperatorAst
{
public:
    UnaryOperatorAst* m_unaryExpression;
    BinaryOperatorAst* m_binaryExpression;
};

class KDEVPYTHONPARSER_EXPORT ShiftOperatorAst : public OperatorAst
{
public:
    BinaryOperatorAst* m_binaryExpression;
    ShiftOperatorAst* m_shiftExpression;
};

class KDEVPYTHONPARSER_EXPORT BitWiseOperatorAst : public OperatorAst
{
public:
    ShiftOperatorAst* m_shiftExpression;
    BitWiseOperatorAst* m_bitwiseExpression;
};

class KDEVPYTHONPARSER_EXPORT ComparisonAst : public OperatorAst
{
public:
    BooleanAst* m_firstExpression;
    ComparisonAst* m_secondExpression;
};

class KDEVPYTHONPARSER_EXPORT BooleanAst : public OperatorAst
{
public:
    BooleanAst* m_firstTest;
    BooleanAst* m_secondTest;
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
