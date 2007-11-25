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

#include <QList>
#include <QMap>
#include <QString>
#include <QStringList>
#include <QPair>

namespace Python
{


class Ast;
class CodeAst;
class FunctionDefinitionAst;
class DecoratorAst;
class ArgumentAst;
class ParameterAst;
class StatementAst;
class IfAst;
class WhileAst;
class ForAst;
class ClassDefinitionAst;
class TryAst;
class ExceptAst;
class WithAst;
class ExecAst;
class GlobalAst;
class ImportAst;
class PlainImportAst;
class StarImportAst;
class FromImportAst;
class RaiseAst;
class PrintAst;
class ReturnAst;
class YieldAst;
class DelAst;
class AssertAst;
class ExpressionStatementAst;
class AssignmentAst;
class TargetAst;
class AtomAst;
class EnclosureAst;
class ListAst;
class ListForAst;
class ListIfAst;
class ListParameterAst;
class GeneratorAst;
class GeneratorForAst;
class GeneratorIfAst;
class DictionaryAst;
class PrimaryAst;
class AttributeReferenceAst;
class SubscriptAst;
class SliceAst;
class ExtendedSliceAst;
class SimpleSliceAst;
class SliceItemAst;
class ProperSliceItemAst;
class ExpressionSliceAst;
class EllipsisSliceAst;
class CallAst;
class ArithmeticExpressionAst;
class UnaryExpressionAst;
class BinaryExpressionAst;
class ComparisonAst;
class BooleanOperationAst;
class ExpressionAst;
class BooleanExpressionAst;
class LambdaAst;
class ParameterAst;
class ParameterPartAst;
class DefaultParameterAst;
class IdentifierParameterPartAst;
class ListParameterPartAst;
class DictionaryParameterAst;

class Ast
{
public:
    enum AstType
    {
        ArgumentAst,
        AssertAst,
        AssignmentAst,
        AtomAst,
        AttributeReferenceAst,
        BinaryExpressionAst,
        BooleanExpressionAst,
        BooleanOperationAst,
        BreakAst,
        CallAst,
        ClassDefinitionAst,
        CodeAst,
        ComparisonAst,
        DecoratorAst,
        DefaultParameterAst,
        DelAst,
        DictionaryAst,
        DictionaryParameterAst,
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
        IdentifierParameterPartAst,
        IfAst,
        LambdaAst,
        ListAst,
        ListForAst,
        ListIfAst,
        ListParameterAst,
        ListParameterPartAst,
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

    Ast( Ast* parent );
    virtual ~Ast();
    AstType astType;
    Ast* parent;
    /**
     * This is the absolute position in the file that this Ast node starts at.
     *
     * Counting starts with 0.
     */
    qint64 start;

    /**
     * This is the absolute position in the file that this Ast node ends at.
     *
     * Counting starts with 0.
     */
    qint64 end;

    /**
     * This is the column in the starting line where this Ast node starts.
     *
     * Counting starts with 0.
     */
    qint64 startCol;

    /**
     * This is the line where this Ast node starts.
     *
     * Counting starts with 0.
     */
    qint64 startLine;

    /**
     * This is the column in the ending line where this Ast node ends.
     *
     * Counting starts with 0.
     */
    qint64 endCol;

    /**
     * This is the line where this Ast node ends.
     *
     * Counting starts with 0.
     */
    qint64 endLine;
};

class CodeAst : public Ast
{

public:
    CodeAst();
    QList<StatementAst*> statements;
};

class StatementAst : public Ast
{

public:
    StatementAst( Ast* );
};

class PrimaryAst : public Ast
{

public:
    PrimaryAst( Ast* );
};

class ParameterAst : public Ast
{
public:
    ParameterAst( Ast* parent );
};

class ParameterPartAst : public Ast
{
public:
    ParameterPartAst( Ast* );
};


class ImportAst : public StatementAst
{

public:
    ImportAst( Ast* );
};

class SliceAst : public PrimaryAst
{

public:
    SliceAst( Ast* );
    Python::PrimaryAst* primary;
};


class SliceItemAst : public Ast
{

public:
    SliceItemAst( Ast* );
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

class ExpressionAst : public Ast
{

public:
    ExpressionAst( Ast* );
};

class FunctionDefinitionAst : public StatementAst
{

public:
    FunctionDefinitionAst( Ast* parent );
    QString functionName;
    QList<Python::ParameterAst*> parameters;
    QList<Python::DecoratorAst*> decorators;
    QList<Python::StatementAst*> functionBody;
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
    QList<Python::TargetAst*> listItems;
    TargetType targetType;
    Python::AttributeReferenceAst* attributeReference;
    Python::SubscriptAst* subscript;
    Python::SliceAst* slice;
};

class DecoratorAst : public Ast
{

public:
    DecoratorAst( Ast* parent );
    QStringList dottedName;
    QList<Python::ArgumentAst*> arguments;
};

class ArgumentAst : public Ast
{

public:
    enum ArgumentType
    {
        PositionalArgument,
        KeywordArgument,
        ListArgument,
        DictArgument
    };
    ArgumentAst( Ast* );
    QList<Python::ExpressionAst*> positionalArguments;
    QMap<QString, Python::ExpressionAst*> keywordArguments;
    Python::ExpressionAst* listOrDictName;
    ArgumentType argumentType;
};

class DefaultParameterAst : public ParameterAst
{
public:
    DefaultParameterAst( Ast* );
    Python::ParameterPartAst* name;
    Python::ExpressionAst* value;
};


class IdentifierParameterPartAst : public ParameterPartAst
{
public:
    IdentifierParameterPartAst( Ast* );
    QString name;
};

class ListParameterPartAst : public ParameterPartAst
{
public:
    ListParameterPartAst( Ast* );
    QList<ParameterPartAst*> parameternames;
};

class DictionaryParameterAst : public ParameterAst
{
public:
    DictionaryParameterAst( Ast* );
    QString name;
};

class ListParameterAst : public ParameterAst
{
public:
    ListParameterAst( Ast* );
    QString name;
};

class IfAst : public StatementAst
{

public:
    IfAst( Ast* );
    QMap<Python::ExpressionAst*, QList<Python::StatementAst*> > ifElseIfBodies;
    QList<Python::StatementAst*> elseBody;
};

class WhileAst : public StatementAst
{

public:
    WhileAst( Ast* );
    Python::ExpressionAst* condition;
    QList<Python::StatementAst*> whileBody;
    QList<Python::StatementAst*> elseBody;
};

class ForAst : public StatementAst
{

public:
    ForAst( Ast* );
    QList<Python::TargetAst*> assignedTargets;
    QList<Python::ExpressionAst*> iterable;
    QList<Python::StatementAst*> forBody;
    QList<Python::StatementAst*> elseBody;
};

class ClassDefinitionAst : public StatementAst
{

public:
    ClassDefinitionAst( Ast* parent );
    QString className;
    QList<Python::ExpressionAst*> inheritance;
    QList<Python::StatementAst*> classBody;
};

class TryAst : public StatementAst
{

public:
    TryAst( Ast* );
    QList<Python::StatementAst*> tryBody;
    QList<Python::StatementAst*> elseBody;
    QList<Python::StatementAst*> finallyBody;
    QList<Python::ExceptAst*> exceptions;
};

class ExceptAst : public Ast
{

public:
    ExceptAst( Ast* );
    Python::ExpressionAst* exceptionDeclaration;
    Python::TargetAst* exceptionValue;
    QList<Python::StatementAst*> exceptionBody;
};

class WithAst : public StatementAst
{

public:
    WithAst( Ast* );
    Python::ExpressionAst* context;
    Python::TargetAst* name;
    QList<Python::StatementAst*> body;
};

class ExecAst : public StatementAst
{

public:
    ExecAst( Ast* );
    Python::ArithmeticExpressionAst* executable;
    Python::DictionaryAst* globalsAndLocals;
    Python::ExpressionAst* localsOnly;
};

class GlobalAst : public StatementAst
{

public:
    GlobalAst( Ast* );
    QList<QString> identifiers;
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
    Python::ExpressionAst* exceptionType;
    Python::ExpressionAst* exceptionValue;
    Python::ExpressionAst* traceback;
};

class PrintAst : public StatementAst
{

public:
    PrintAst( Ast* );
    QList<Python::ExpressionAst*> printables;
    Python::ExpressionAst* outfile;
};

class ReturnAst : public StatementAst
{

public:
    ReturnAst( Ast* );
    QList<Python::ExpressionAst*> returnValues;
};

class YieldAst : public StatementAst
{

public:
    YieldAst( Ast* );
    QList<Python::ExpressionAst*> yieldValue;
};

class DelAst : public StatementAst
{

public:
    DelAst( Ast* );
    QList<Python::TargetAst*> deleteObjects;
};

class AssertAst : public StatementAst
{

public:
    AssertAst( Ast* );
    Python::ExpressionAst* assertTest;
    Python::ExpressionAst* exceptionValue;
};

class ExpressionStatementAst : public StatementAst
{

public:
    ExpressionStatementAst( Ast* );
    QList<Python::ExpressionAst*> expressions;
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
    QList<QList<Python::TargetAst*> > targets;
    QList<Python::ExpressionAst*> value;
    Python::YieldAst* yieldValue;
};


class AtomAst : public PrimaryAst
{

public:
    AtomAst( Ast* );
    QString identifier;
    QString literal;
    Python::EnclosureAst* enclosure;
};

class EnclosureAst : public Ast
{

public:
    EnclosureAst( Ast* );
    QList<Python::ExpressionAst*> parenthesizedform;
    Python::ListAst* list;
    Python::GeneratorAst* generator;
    Python::DictionaryAst* dict;
    QList<Python::ExpressionAst*> stringConversion;
    Python::YieldAst* yield;
};

class ListAst : public Ast
{

public:
    ListAst( Ast* );
    QList<Python::ExpressionAst*> plainList;
    Python::ListForAst* listGenerator;
};

class ListForAst : public Ast
{

public:
    ListForAst( Ast* );
    QList<Python::TargetAst*> assignedTargets;
    QList<Python::ExpressionAst*> iterableObject;
    Python::ListForAst* nextGenerator;
    Python::ListIfAst* nextCondition;
};

class ListIfAst : public Ast
{

public:
    ListIfAst( Ast* );
    Python::ExpressionAst* condition;
    Python::ListForAst* nextGenerator;
    Python::ListIfAst* nextCondition;
};

class GeneratorAst : public Ast
{

public:
    GeneratorAst( Ast* );
    Python::ExpressionAst* generatedValue;
    Python::GeneratorForAst* generator;
};

class GeneratorForAst : public Ast
{

public:
    GeneratorForAst( Ast* );
    QList<Python::TargetAst*> assignedTargets;
    Python::BooleanExpressionAst * iterableObject;
    Python::GeneratorForAst* nextGenerator;
    Python::GeneratorIfAst* nextCondition;
};

class GeneratorIfAst : public Ast
{

public:
    GeneratorIfAst( Ast* );
    Python::ExpressionAst* condition;
    Python::GeneratorForAst* nextGenerator;
    Python::GeneratorIfAst* nextCondition;
};

class DictionaryAst : public Ast
{

public:
    DictionaryAst( Ast* );
    QMap<Python::ExpressionAst*, Python::ExpressionAst*> dictionary;
};

class AttributeReferenceAst : public PrimaryAst
{

public:
    AttributeReferenceAst( Ast* );
    Python::PrimaryAst* primary;
    QString identifier;
};

class SubscriptAst : public PrimaryAst
{

public:
    SubscriptAst( Ast* );
    Python::PrimaryAst* primary;
    QList<Python::ExpressionAst*> subscription;
};

class ExtendedSliceAst : public SliceAst
{

public:
    ExtendedSliceAst( Ast* );
    QList<Python::SliceItemAst*> extendedSliceList;
};

class SimpleSliceAst : public SliceAst
{

public:
    SimpleSliceAst( Ast* );
    QPair<Python::ExpressionAst*, Python::ExpressionAst*> simpleSliceBounds;
};

class ProperSliceItemAst : public SliceItemAst
{

public:
    ProperSliceItemAst( Ast* );
    QPair<Python::ExpressionAst*, Python::ExpressionAst*> bounds;
    Python::ExpressionAst* stride;
};

class ExpressionSliceAst : public SliceItemAst
{

public:
    ExpressionSliceAst( Ast* );
    Python::ExpressionAst* sliceExpression;
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
    Python::PrimaryAst* callable;
    QList<Python::ArgumentAst*> arguments;
    Python::ExpressionAst* callValue;
    Python::GeneratorForAst* callGenerator;
};


class UnaryExpressionAst : public ArithmeticExpressionAst
{

public:
    UnaryExpressionAst( Ast* );
    Python::PrimaryAst* primary;
    Python::UnaryExpressionAst* operand;
};

class BinaryExpressionAst : public ArithmeticExpressionAst
{

public:
    BinaryExpressionAst( Ast* );
    Python::BinaryExpressionAst* lhs;
    Python::UnaryExpressionAst* rhs;
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
    Python::BinaryExpressionAst* firstComparator;
    QMap<Python::ComparisonAst::ComparisonOperator,
         Python::BinaryExpressionAst*> comparatorList;
};

class BooleanOperationAst : public Ast
{
    enum BooleanOperation
    {
        NotOp,
        AndOp,
        OrOp
    };

public:
    BooleanOperationAst( Ast* );
    Python::BooleanOperationAst* lhs;
    BooleanOperation opType;
    Python::ComparisonAst* rhs;
};

class BooleanExpressionAst : public ExpressionAst
{

public:
    BooleanExpressionAst( Ast* );
    Python::BooleanOperationAst* mainExpression;
    Python::BooleanOperationAst* condition;
    Python::ExpressionAst* elseExpression;
};

class LambdaAst : public ExpressionAst
{

public:
    LambdaAst( Ast* );
    QList<Python::ParameterAst*> parameters;
    Python::ExpressionAst* expression;
};

}

#endif
