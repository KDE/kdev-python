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
class IdentifierAst;
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
class ConditionalExpressionAst;
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
        ArgumentAst = 0,
        AssertAst = 1,
        AssignmentAst = 2,
        AtomAst = 3,
        AttributeReferenceAst = 4,
        BinaryExpressionAst = 5,
        BooleanAndOperationAst = 6,
        BooleanNotOperationAst = 7,
        BooleanOrOperationAst = 8,
        BreakAst = 9,
        CallAst = 10,
        ClassDefinitionAst = 11,
        CodeAst = 12,
        ComparisonAst = 13,
        ConditionalExpressionAst = 14,
        ContinueAst = 15,
        DecoratorAst = 16,
        DefaultParameterAst = 17,
        DelAst = 18,
        DictionaryAst = 19,
        DictionaryParameterAst = 20,
        EllipsisSliceItemAst = 21,
        EnclosureAst = 22,
        ExceptAst = 23,
        ExecAst = 24,
        ExpressionSliceItemAst = 25,
        ExpressionStatementAst = 26,
        ExtendedSliceAst = 27,
        ForAst = 28,
        FromImportAst = 29,
        FunctionDefinitionAst = 30,
        GeneratorAst = 31,
        GeneratorForAst = 32,
        GeneratorIfAst = 33,
        GlobalAst = 34,
        IdentifierAst = 35,
        IdentifierParameterPartAst = 36,
        IfAst = 37,
        LambdaAst = 38,
        ListAst = 39,
        ListForAst = 40,
        ListIfAst = 41,
        ListParameterAst = 42,
        ListParameterPartAst = 43,
        LiteralAst = 44,
        PassAst = 45,
        PlainImportAst = 46,
        PrintAst = 47,
        ProperSliceItemAst = 48,
        RaiseAst = 49,
        ReturnAst = 50,
        SimpleSliceAst = 51,
        StarImportAst = 52,
        SubscriptAst = 53,
        TargetAst = 54,
        TryAst = 55,
        UnaryExpressionAst = 56,
        WhileAst = 57,
        WithAst = 58,
        YieldAst = 59
    };

    Ast( Ast* parent, AstType type );
    virtual ~Ast();
    Ast* parent;
    AstType astType;
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
    StatementAst( Ast*, Ast::AstType type );
};

class ParameterAst : public Ast
{
public:
    ParameterAst( Ast* parent, Ast::AstType type );
};

class ParameterPartAst : public Ast
{
public:
    ParameterPartAst( Ast*, Ast::AstType type );
};


class ImportAst : public StatementAst
{

public:
    ImportAst( Ast*, Ast::AstType type );
};

class ExpressionAst : public Ast
{

public:
    ExpressionAst( Ast*, Ast::AstType type );
};

class PrimaryAst : public ExpressionAst
{

public:
    PrimaryAst( Ast*, Ast::AstType type );
};

class SliceAst : public PrimaryAst
{

public:
    SliceAst( Ast*, Ast::AstType type );
    Python::PrimaryAst* primary;
};


class SliceItemAst : public Ast
{

public:
    SliceItemAst( Ast*, Ast::AstType type );
};


class ArithmeticExpressionAst : public ExpressionAst
{
public:
    enum ArithmeticOperation
    {
        Power,
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
        BinaryXor
    };

    ArithmeticExpressionAst( Ast*, Ast::AstType type );
    ArithmeticOperation opType;
};

class BooleanOperationAst : public Ast
{
public:
    BooleanOperationAst( Ast* parent, Ast::AstType type );
};


class FunctionDefinitionAst : public StatementAst
{

public:
    FunctionDefinitionAst( Ast* parent );
    Python::IdentifierAst* functionName;
    QList<Python::ParameterAst*> parameters;
    QList<Python::DecoratorAst*> decorators;
    QList<Python::StatementAst*> functionBody;
};

class TargetAst : public Ast
{
public:

    enum TargetType
    {
        TupleTarget,
        ListTarget,
        AttributeReferenceTarget,
        SubscriptTarget,
        SliceTarget
    };
    TargetAst( Ast* );
    Python::IdentifierAst* identifier;
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
    QList<Python::IdentifierAst*> dottedName;
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
    Python::ExpressionAst* argumentExpression;
    Python::IdentifierAst* keywordName;
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
    Python::IdentifierAst* name;
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
    Python::IdentifierAst* name;
};

class ListParameterAst : public ParameterAst
{
public:
    ListParameterAst( Ast* );
    Python::IdentifierAst* name;
};

class IfAst : public StatementAst
{

public:
    IfAst( Ast* );
    ExpressionAst* ifCondition;
    QList<Python::StatementAst*> ifBody;
    QList<QPair<Python::ExpressionAst*, QList<Python::StatementAst*> > > elseIfBodies;
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
    Python::IdentifierAst* className;
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
    QList<Python::IdentifierAst*> identifiers;
};

class PlainImportAst : public ImportAst
{

public:
    PlainImportAst( Ast* );
    QList< QPair< QList<Python::IdentifierAst*>, Python::IdentifierAst*> > modulesAsName;
};

class StarImportAst : public ImportAst
{

public:
    StarImportAst( Ast* );
    QList<Python::IdentifierAst*> modulePath;
};

class FromImportAst : public ImportAst
{

public:
    FromImportAst( Ast* );
    QList<Python::IdentifierAst*> modulePath;
    int numLeadingDots;
    QList< QPair<Python::IdentifierAst*, Python::IdentifierAst*> > identifierAsName;
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
public:

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
        FloorEqualOp,
        AssignmentOp
    };
    AssignmentAst( Ast* );
    OpType operation;
    QList<QList<Python::TargetAst*> > targets;
    QList<Python::ExpressionAst*> value;
    Python::YieldAst* yieldValue;
};

class LiteralAst : public Ast
{
public:
    enum LiteralType
    {
        String,
        Float,
        Integer,
        ImaginaryNumber
    };
    LiteralAst( Ast* );
    QString value;
    LiteralType literalType;
};

class AtomAst : public PrimaryAst
{

public:
    AtomAst( Ast* );
    Python::IdentifierAst* identifier;
    Python::LiteralAst* literal;
    Python::EnclosureAst* enclosure;
};

class EnclosureAst : public Ast
{

public:
    enum EnclosureType
    {
        ParenthesizedForm,
        List,
        Generator,
        Dictionary,
        StringConversion,
        Yield
    };
    EnclosureAst( Ast* );
    QList<Python::ExpressionAst*> parenthesizedform;
    Python::ListAst* list;
    Python::GeneratorAst* generator;
    Python::DictionaryAst* dict;
    QList<Python::ExpressionAst*> stringConversion;
    Python::YieldAst* yield;
    EnclosureType encType;
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
    Python::ConditionalExpressionAst * iterableObject;
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
    Python::IdentifierAst* identifier;
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

class ExpressionSliceItemAst : public SliceItemAst
{

public:
    ExpressionSliceItemAst( Ast* );
    Python::ExpressionAst* sliceExpression;
};

class EllipsisSliceItemAst : public SliceItemAst
{

public:
    EllipsisSliceItemAst( Ast* );
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
    Python::ExpressionAst* operand;
};

class BinaryExpressionAst : public ArithmeticExpressionAst
{

public:
    BinaryExpressionAst( Ast* );
    Python::ExpressionAst* lhs;
    Python::ExpressionAst* rhs;
};

class ComparisonAst : public BooleanOperationAst
{
public:

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
    ComparisonAst( Ast* );
    Python::ArithmeticExpressionAst* firstComparator;
    QList< QPair<Python::ComparisonAst::ComparisonOperator,
         Python::ArithmeticExpressionAst*> > comparatorList;
};

class BooleanAndOperationAst : public BooleanOperationAst
{
public:
    BooleanAndOperationAst( Ast* );
    Python::BooleanOperationAst* lhs;
    Python::BooleanOperationAst* rhs;
};

class BooleanOrOperationAst : public BooleanOperationAst
{
public:
    BooleanOrOperationAst( Ast* );
    Python::BooleanOperationAst* lhs;
    Python::BooleanOperationAst* rhs;
};

class BooleanNotOperationAst : public BooleanOperationAst
{
public:
    BooleanNotOperationAst( Ast* );
    Python::BooleanOperationAst* op;
};

class ConditionalExpressionAst : public ExpressionAst
{

public:
    ConditionalExpressionAst( Ast* );
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

class IdentifierAst : public ExpressionAst
{
public:
    IdentifierAst( Ast* );
    QString identifier;
};


}

#endif
