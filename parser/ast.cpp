/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2010-2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2012 Patrick Spendrin <ps_ml@gmx.de>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#include "ast.h"
#include "astbuilder.h"
#include <language/duchain/problem.h>

namespace Python
{

static void dumpNode(QString &r, QString prefix, const Ast* node)
{
    r.append(prefix);
    r.append(node ? node->dump(): QStringLiteral("None"));
}


static void dumpContext(QString &r, QString prefix, ExpressionAst::Context context)
{
    r.append(prefix);
    switch(context) {
        case ExpressionAst::Context::Load:
            r.append(QStringLiteral("Load()"));
            break;
        case ExpressionAst::Context::Store:
            r.append(QStringLiteral("Store()"));
            break;
        case ExpressionAst::Context::Delete:
            r.append(QStringLiteral("Delete()"));
            break;
        default:
            r.append(QStringLiteral("Invalid"));
    }
}

static void dumpOperator(QString &r, QString prefix, Ast::OperatorTypes op)
{
    r.append(prefix);
    switch(op) {
        case Ast::OperatorAdd:
            r.append(QStringLiteral("Add()"));
            break;
        case Ast::OperatorSub:
            r.append(QStringLiteral("Sub()"));
            break;
        case Ast::OperatorMult:
            r.append(QStringLiteral("Mult()"));
            break;
        case Ast::OperatorMatMult:
            r.append(QStringLiteral("MatMult()"));
            break;
        case Ast::OperatorDiv:
            r.append(QStringLiteral("Div()"));
            break;
        case Ast::OperatorPow:
            r.append(QStringLiteral("Pow()"));
            break;
        case Ast::OperatorLeftShift:
            r.append(QStringLiteral("LShift()"));
            break;
        case Ast::OperatorRightShift:
            r.append(QStringLiteral("RShift()"));
            break;
        case Ast::OperatorBitwiseOr:
            r.append(QStringLiteral("BitwiseOr"));
            break;
        case Ast::OperatorBitwiseXor:
            r.append(QStringLiteral("BitwiseXor()"));
            break;
        case Ast::OperatorFloorDivision:
            r.append(QStringLiteral("FloorDivision()"));
            break;
        default:
            r.append(QStringLiteral("Invalid"));
    }
}

template<class T>
static void dumpList(QString &r, QString prefix, const T list, QString sep=QStringLiteral(", "))
{
    int i = 0;
    r.append(prefix);
    r.append(QLatin1Char('['));
    for (const Ast* node : list) {
        i += 1;
        dumpNode(r, QString(), node);
        if (i < list.size())
            r.append(sep);
    }
    r.append(QLatin1Char(']'));
}

// We never need actual constructors for AST nodes, but it seems to be required, at least for some platforms
// so we provide pseudo implementations
// there's nothing happening here, don't bother reading the code
    
Ast::Ast( Ast* parent, Ast::AstType type ) : parent(parent), astType( type ), startCol(0), startLine(-99999), endCol(0), endLine(0), hasUsefulRangeInformation(false), context(nullptr) { }
Ast::Ast() :  parent(nullptr), startCol(0), startLine(-5), endCol(0), endLine(0), hasUsefulRangeInformation(false), context(nullptr) { }

ArgumentsAst::ArgumentsAst(Ast* parent): Ast(parent, Ast::ArgumentsAstType)
{
    
}

QString ArgumentsAst::dump() const
{
    QString r = QStringLiteral("arguments(");
    dumpList(r, QStringLiteral("posonlyargs="), posonlyargs);
    dumpList(r, QStringLiteral(", args="), arguments);
    dumpList(r, QStringLiteral(", kwonlyargs="), kwonlyargs);
    dumpList(r, QStringLiteral(", defaults="), defaultValues);
    dumpList(r, QStringLiteral(", kw_defaults="), defaultKwValues);
    if (vararg)
        dumpNode(r, QStringLiteral(", vararg="), vararg);
    if (kwarg)
        dumpNode(r, QStringLiteral(", kwarg="), kwarg);
    r.append(QLatin1Char(')'));
    return r;
}

ArgAst::ArgAst(Ast* parent): Ast(parent, Ast::ArgAstType), argumentName(nullptr), annotation(nullptr)
{

}

QString ArgAst::dump() const
{
    QString r = QStringLiteral("arg(");
    dumpNode(r, QStringLiteral("name="), argumentName);
    dumpNode(r, QStringLiteral(", annotation="), annotation);
    r.append(QLatin1Char(')'));
    return r;
}

AssertionAst::AssertionAst(Ast* parent): StatementAst(parent, Ast::AssertionAstType) 
{
    
}

QString AssertionAst::dump() const
{
    QString r = QStringLiteral("Assertion(");
    dumpNode(r, QStringLiteral("condition="), condition);
    dumpNode(r, QStringLiteral(", message="), message);
    r.append(QLatin1Char(')'));
    return r;
}

AssignmentAst::AssignmentAst(Ast* parent): StatementAst(parent, Ast::AssignmentAstType), value(nullptr)
{
    
}

QString AssignmentAst::dump() const
{
    QString r = QStringLiteral("Assign(");
    dumpList(r, QStringLiteral("targets="), targets);
    dumpNode(r, QStringLiteral(", value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

AttributeAst::AttributeAst(Ast* parent): ExpressionAst(parent, Ast::AttributeAstType), value(nullptr), depth(0)
{
    
}

QString AttributeAst::dump() const
{
    QString r = QStringLiteral("Attribute(");
    dumpNode(r, QStringLiteral("value="), value);
    dumpNode(r, QStringLiteral(", attr="), attribute);
    dumpContext(r, QStringLiteral(", ctx="), context);
    r.append(QLatin1Char(')'));
    return r;
}

AugmentedAssignmentAst::AugmentedAssignmentAst(Ast* parent): StatementAst(parent, Ast::AugmentedAssignmentAstType), value(nullptr)
{
    
}

QString AugmentedAssignmentAst::dump() const
{
    QString r = QStringLiteral("AugmentedAssignment(");
    dumpNode(r, QStringLiteral("target="), target);
    dumpNode(r, QStringLiteral(", value="), value);
    dumpOperator(r, QStringLiteral(", op="), op);
    r.append(QLatin1Char(')'));
    return r;
}

AnnotationAssignmentAst::AnnotationAssignmentAst(Ast* parent): StatementAst(parent, Ast::AnnotationAssignmentAstType), target(nullptr), value(nullptr), annotation(nullptr)
{

}

QString AnnotationAssignmentAst::dump() const
{
    QString r = QStringLiteral("AnnotationAssignment(");
    dumpNode(r, QStringLiteral("target="), target);
    dumpNode(r, QStringLiteral(", value="), value);
    dumpNode(r, QStringLiteral(", annotation="), annotation);
    r.append(QLatin1Char(')'));
    return r;
}


BinaryOperationAst::BinaryOperationAst(Ast* parent): ExpressionAst(parent, Ast::BinaryOperationAstType), lhs(nullptr), rhs(nullptr)
{

}

BooleanOperationAst::BooleanOperationAst(Ast* parent): ExpressionAst(parent, Ast::BooleanOperationAstType)
{
    
}

BreakAst::BreakAst(Ast* parent): StatementAst(parent, Ast::BreakAstType)
{
    
}

CallAst::CallAst(Ast* parent): ExpressionAst(parent, Ast::CallAstType), function(nullptr)
{
    
}


QString CallAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Call("));
    dumpNode(r, QStringLiteral("func="), function);
    dumpList(r, QStringLiteral(", args="), arguments);
    dumpList(r, QStringLiteral(", keywords="), keywords);
    r.append(QLatin1Char(')'));
    return r;
}

ClassDefinitionAst::ClassDefinitionAst(Ast* parent): StatementAst(parent, Ast::ClassDefinitionAstType), name(nullptr)
{
    
}


QString ClassDefinitionAst::dump() const
{
    QString r;
    r.append(QStringLiteral("ClassDef("));
    dumpNode(r, QStringLiteral("name="), name);
    dumpList(r, QStringLiteral(", bases="), baseClasses);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n  "));
    // TODO: Keywords?
    dumpList(r, QStringLiteral(", decorator_list="), decorators);
    r.append(QLatin1Char(')'));
    return r;
}

CodeAst::CodeAst() : Ast(nullptr, Ast::CodeAstType), name(nullptr)
{
}

CodeAst::~CodeAst()
{
    free_ast_recursive(this);
}

QString CodeAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Module("));
    dumpNode(r, QStringLiteral("name="), name);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n  "));
    r.append(QLatin1Char(')'));
    return r;
}

CompareAst::CompareAst(Ast* parent): ExpressionAst(parent, Ast::CompareAstType), leftmostElement(nullptr)
{
    
}

ComprehensionAst::ComprehensionAst(Ast* parent): Ast(parent, Ast::ComprehensionAstType), target(nullptr), iterator(nullptr)
{
    
}

ContinueAst::ContinueAst(Ast* parent): StatementAst(parent, Ast::ContinueAstType)
{
    
}

DeleteAst::DeleteAst(Ast* parent): StatementAst(parent, Ast::DeleteAstType)
{
    
}

QString DeleteAst::dump() const
{
    QString r = QStringLiteral("Delete(");
    dumpList(r, QStringLiteral("targets="), targets);
    r.append(QLatin1Char(')'));
    return r;
}

DictAst::DictAst(Ast* parent): ExpressionAst(parent, Ast::DictAstType)
{

}

QString DictAst::dump() const
{
    QString r = QStringLiteral("Dict(");
    dumpList(r, QStringLiteral("keys="), keys);
    dumpList(r, QStringLiteral(", values="), values);
    r.append(QLatin1Char(')'));
    return r;
}


SliceAst::SliceAst(Ast* parent): ExpressionAst(parent, Ast::SliceAstType), lower(nullptr), upper(nullptr), step(nullptr)
{

}

QString SliceAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Slice("));
    dumpNode(r, QStringLiteral("lower="), lower);
    dumpNode(r, QStringLiteral(", upper="), upper);
    dumpNode(r, QStringLiteral(", step="), step);
    r.append(QLatin1Char(')'));
    return r;
}

DictionaryComprehensionAst::DictionaryComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::DictionaryComprehensionAstType), key(nullptr), value(nullptr)
{
    
}

ExceptionHandlerAst::ExceptionHandlerAst(Ast* parent): Ast(parent, Ast::ExceptionHandlerAstType), type(nullptr), name(nullptr)
{
    
}

ListComprehensionAst::ListComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::ListComprehensionAstType), element(nullptr)
{

}

ExpressionAst::ExpressionAst(Ast* parent, AstType type): Ast(parent, type), value(nullptr)
{
    
}

AssignmentExpressionAst::AssignmentExpressionAst(Ast* parent): ExpressionAst(parent, Ast::AssignmentExpressionAstType), value(nullptr)
{

}

QString AssignmentExpressionAst::dump() const
{
    QString r = QStringLiteral("AssignmentExpression(");
    dumpNode(r, QStringLiteral("target="), target);
    dumpNode(r, QStringLiteral(", value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

YieldFromAst::YieldFromAst(Ast* parent) : ExpressionAst(parent, Ast::YieldFromAstType)
{

}

QString YieldFromAst::dump() const
{
    QString r = QStringLiteral("YieldFrom(");
    dumpNode(r, QStringLiteral("value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

ForAst::ForAst(Ast* parent): StatementAst(parent, Ast::ForAstType), target(nullptr), iterator(nullptr)
{
    
}

QString ForAst::dump() const
{
    QString r = async ? QStringLiteral("AsyncFor(") : QStringLiteral("For(");
    dumpNode(r, QStringLiteral("target="), target);
    dumpNode(r, QStringLiteral(", iterator="), iterator);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n    "));
    if (orelse.size())
        dumpList(r, QStringLiteral(", orelse="), orelse, QStringLiteral(",\n    "));
    r.append(QLatin1Char(')'));
    return r;
}

FunctionDefinitionAst::FunctionDefinitionAst(Ast* parent): StatementAst(parent, Ast::FunctionDefinitionAstType), name(nullptr), arguments(nullptr), async(false)
{
    
}

QString FunctionDefinitionAst::dump() const
{
    QString r = async ? QStringLiteral("AsyncFuncDef(") : QStringLiteral("FuncDef(");
    dumpNode(r, QStringLiteral("name="), name);
    dumpNode(r, QStringLiteral(", args="), arguments);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n    "));
    if (decorators.size())
        dumpList(r, QStringLiteral(", decorator_list="), decorators);
    if (returns)
        dumpNode(r, QStringLiteral(", returns="), returns);
    r.append(QLatin1Char(')'));
    return r;
}

GeneratorExpressionAst::GeneratorExpressionAst(Ast* parent): ExpressionAst(parent, Ast::GeneratorExpressionAstType), element(nullptr)
{
    
}

GlobalAst::GlobalAst(Ast* parent): StatementAst(parent, Ast::GlobalAstType)
{
    
}


QString GlobalAst::dump() const
{
    QString r = QStringLiteral("Global(");
    dumpList(r, QStringLiteral("names="), names);
    r.append(QLatin1Char(')'));
    return r;
}

Identifier::Identifier(QString value) : Ast(nullptr, Ast::IdentifierAstType), value(value)
{
    
}

QString Identifier::dump() const
{
    return QStringLiteral("'") + value + QStringLiteral("'");
}

IfAst::IfAst(Ast* parent): StatementAst(parent, Ast::IfAstType), condition(nullptr)
{
    
}

QString IfAst::dump() const
{
    QString r = QStringLiteral("If(");
    dumpNode(r, QStringLiteral("condition="), condition);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n    "));
    if (orelse.size())
        dumpList(r, QStringLiteral(", orelse="), orelse, QStringLiteral(",\n    "));
    r.append(QLatin1Char(')'));
    return r;
}

IfExpressionAst::IfExpressionAst(Ast* parent): ExpressionAst(parent, Ast::IfExpressionAstType), condition(nullptr)
{
    
}

QString IfExpressionAst::dump() const
{
    QString r = QStringLiteral("IfExpr(");
    dumpNode(r, QStringLiteral("condition="), condition);
    dumpNode(r, QStringLiteral(", body="), body);
    if (orelse)
        dumpNode(r, QStringLiteral(", orelse="), orelse);
    r.append(QLatin1Char(')'));
    return r;
}

ImportAst::ImportAst(Ast* parent): StatementAst(parent, Ast::ImportAstType)
{
    
}

QString ImportAst::dump() const
{
    QString r = QStringLiteral("Import(");
    dumpList(r, QStringLiteral("names="), names);
    r.append(QLatin1Char(')'));
    return r;
}

ImportFromAst::ImportFromAst(Ast* parent): StatementAst(parent, Ast::ImportFromAstType), module(nullptr), level(0)
{
    
}

QString ImportFromAst::dump() const
{
    QString r = QStringLiteral("ImportFrom(");
    dumpNode(r, QStringLiteral("module="), module);
    dumpList(r, QStringLiteral(", names="), names);
    r.append(QLatin1Char(')'));
    return r;
}

KeywordAst::KeywordAst(Ast* parent): Ast(parent, Ast::KeywordAstType), argumentName(nullptr), value(nullptr)
{
    
}

QString KeywordAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Keyword("));
    dumpNode(r, QStringLiteral("arg="), argumentName);
    dumpNode(r, QStringLiteral(", value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

LambdaAst::LambdaAst(Ast* parent): ExpressionAst(parent, Ast::LambdaAstType), arguments(nullptr)
{
    
}

ListAst::ListAst(Ast* parent): ExpressionAst(parent, Ast::ListAstType)
{
    
}

QString ListAst::dump() const
{
    QString r = QStringLiteral("List(");
    dumpList(r, QStringLiteral("elts="), elements);
    dumpContext(r, QStringLiteral(", ctx="), context);
    r.append(QLatin1Char(')'));
    return r;
}

NameAst::NameAst(Ast* parent): ExpressionAst(parent, Ast::NameAstType), identifier(nullptr)
{
    
}

QString NameAst::dump() const
{
    QString r = QStringLiteral("Name(");
    dumpNode(r, QStringLiteral("id="), identifier);
    dumpContext(r, QStringLiteral(", ctx="), context);
    r.append(QLatin1Char(')'));
    return r;
}

AwaitAst::AwaitAst(Ast* parent): ExpressionAst(parent, Ast::AwaitAstType), value(nullptr)
{

}

QString AwaitAst::dump() const
{
    QString r = QStringLiteral("AwaitAst(");
    dumpNode(r, QStringLiteral("value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

QString NameConstantAst::dump() const
{
    switch (value) {
        case NameConstantAst::NameConstantTypes::False:
            return QStringLiteral("False");
        case NameConstantAst::NameConstantTypes::True:
            return QStringLiteral("True");
        case NameConstantAst::NameConstantTypes::None:
            return QStringLiteral("None");
        default:
            return QStringLiteral("Invalid");
    }
}

QString NumberAst::dump() const
{
    if (isInt)
        return QString::fromLatin1("Number(%1)").arg(value);
    else
        return QStringLiteral("Float()");
}

PassAst::PassAst(Ast* parent): StatementAst(parent, Ast::PassAstType)
{
    
}

NonlocalAst::NonlocalAst(Ast* parent): StatementAst(parent, Ast::NonlocalAstType)
{
    
}

RaiseAst::RaiseAst(Ast* parent): StatementAst(parent, Ast::RaiseAstType), type(nullptr)
{
    
}


QString RaiseAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Raise("));
    dumpNode(r, QStringLiteral("type="), type);
    r.append(QLatin1Char(')'));
    return r;
}

ReturnAst::ReturnAst(Ast* parent): StatementAst(parent, Ast::ReturnAstType), value(nullptr)
{
    
}

QString ReturnAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Return("));
    dumpNode(r, QStringLiteral("value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

SetAst::SetAst(Ast* parent): ExpressionAst(parent, Ast::SetAstType)
{
    
}

QString SetAst::dump() const
{
    QString r = QStringLiteral("Set(");
    dumpList(r, QStringLiteral("elts="), elements);
    r.append(QLatin1Char(')'));
    return r;
}

SetComprehensionAst::SetComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::SetComprehensionAstType), element(nullptr)
{
    
}

StatementAst::StatementAst(Ast* parent, AstType type): Ast(parent, type)
{
    
}

JoinedStringAst::JoinedStringAst(Ast* parent): ExpressionAst(parent, Ast::JoinedStringAstType), values()
{

}

FormattedValueAst::FormattedValueAst(Ast* parent): ExpressionAst(parent, Ast::FormattedValueAstType), value(nullptr), conversion(0), formatSpec(nullptr)
{

}

SubscriptAst::SubscriptAst(Ast* parent): ExpressionAst(parent, Ast::SubscriptAstType), value(nullptr), slice(nullptr)
{
    
}

QString SubscriptAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Subscript("));
    dumpNode(r, QStringLiteral("value="), value);
    dumpNode(r, QStringLiteral(", slice="), slice);
    dumpContext(r, QStringLiteral(", context="), context);
    r.append(QLatin1Char(')'));
    return r;
}

StarredAst::StarredAst(Ast* parent): ExpressionAst(parent, Ast::StarredAstType)
{
    
}

QString StarredAst::dump() const
{
    QString r;
    r.append(QStringLiteral("Starred("));
    dumpNode(r, QStringLiteral("value="), value);
    dumpContext(r, QStringLiteral(", context="), context);
    r.append(QLatin1Char(')'));
    return r;
}

TupleAst::TupleAst(Ast* parent): ExpressionAst(parent, Ast::TupleAstType)
{
    
}

QString TupleAst::dump() const
{
    QString r = QStringLiteral("Tuple(");
    dumpList(r, QStringLiteral("elts="), elements);
    dumpContext(r, QStringLiteral(", context="), context);
    r.append(QLatin1Char(')'));
    return r;
}


UnaryOperationAst::UnaryOperationAst(Ast* parent): ExpressionAst(parent, Ast::UnaryOperationAstType), operand(nullptr)
{
    
}

QString UnaryOperationAst::dump() const {
    QString r;
    r.append(QStringLiteral("Unary("));
    dumpNode(r, QStringLiteral("value="), operand);
    r.append(QStringLiteral(", op="));
    switch(type) {
       case Ast::UnaryOperatorInvert:
            r.append(QStringLiteral("Invert()"));
            break;
        case Ast::UnaryOperatorNot:
            r.append(QStringLiteral("Not()"));
            break;
        case Ast::UnaryOperatorAdd:
            r.append(QStringLiteral("UAdd()"));
            break;
        case Ast::UnaryOperatorSub:
            r.append(QStringLiteral("USub()"));
            break;
        default:
            r.append(QStringLiteral("Invalid"));
    }
    r.append(QLatin1Char(')'));
    return r;
}

TryStarAst::TryStarAst(Ast* parent): StatementAst(parent, Ast::TryStarAstType)
{

}

TryAst::TryAst(Ast* parent): StatementAst(parent, Ast::TryAstType)
{

}

QString TryAst::dump() const
{
    QString r = QStringLiteral("Try(");
    dumpList(r, QStringLiteral("body="), body, QStringLiteral(",\n    "));
    dumpList(r, QStringLiteral(", handlers="), handlers);
    if (orelse.size())
        dumpList(r, QStringLiteral(", orelse="), orelse, QStringLiteral(",\n    "));
    if (finally.size())
        dumpList(r, QStringLiteral(", finally="), finally, QStringLiteral(",\n    "));
    r.append(QLatin1Char(')'));
    return r;
}

TypeAliasAst::TypeAliasAst(Ast* parent): StatementAst(parent, Ast::TypeAliasType)
{
}

WhileAst::WhileAst(Ast* parent): StatementAst(parent, Ast::WhileAstType), condition(nullptr)
{
    
}

QString WhileAst::dump() const
{
    QString r = QStringLiteral("While(");
    dumpNode(r, QStringLiteral("condition="), condition);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n    "));
    if (orelse.size())
        dumpList(r, QStringLiteral(", orelse="), orelse, QStringLiteral(",\n    "));
    r.append(QLatin1Char(')'));
    return r;
}


WithAst::WithAst(Ast* parent): StatementAst(parent, Ast::WithAstType)
{
    
}

QString WithAst::dump() const
{
    QString r = async ? QStringLiteral("AsyncWith(") : QStringLiteral("With(");
    dumpList(r, QStringLiteral(", items="), items);
    dumpList(r, QStringLiteral(", body="), body, QStringLiteral(",\n    "));
    r.append(QLatin1Char(')'));
    return r;
}

WithItemAst::WithItemAst(Ast* parent): Ast(parent, Ast::WithItemAstType)
{

}

YieldAst::YieldAst(Ast* parent): ExpressionAst(parent, Ast::YieldAstType), value(nullptr)
{
    
}

QString YieldAst::dump() const
{
    QString r = QStringLiteral("Yield(");
    dumpNode(r, QStringLiteral("value="), value);
    r.append(QLatin1Char(')'));
    return r;
}


AliasAst::AliasAst(Ast* parent): Ast(parent, Ast::AliasAstType), name(nullptr), asName(nullptr)
{
    
}

QString AliasAst::dump() const
{
    QString r = QStringLiteral("Alias(");
    dumpNode(r, QStringLiteral("name="), name);
    dumpNode(r, QStringLiteral(", as="), asName);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchAst::dump() const
{
    QString r = QStringLiteral("Match(");
    dumpNode(r, QStringLiteral("subject="), subject);
    dumpList(r, QStringLiteral(", cases="), cases);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchCaseAst::dump() const
{
    QString r = QStringLiteral("MatchCase(");
    dumpNode(r, QStringLiteral("pattern="), pattern);
    if (guard)
        dumpNode(r, QStringLiteral(", guard="), guard);
    dumpList(r, QStringLiteral(", body="), body);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchValueAst::dump() const
{
    QString r = QStringLiteral("MatchValue(");
    dumpNode(r, QStringLiteral("value="), value);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchSingletonAst::dump() const
{
    QString r = QStringLiteral("MatchSingleton(");
    switch (value) {
        case NameConstantAst::NameConstantTypes::True:
            r.append(QStringLiteral("value=True"));
            break;
        case NameConstantAst::NameConstantTypes::False:
            r.append(QStringLiteral("value=False"));
            break;
        case NameConstantAst::NameConstantTypes::None:
            r.append(QStringLiteral("value=None"));
            break;
        default:
            r.append(QStringLiteral("value=Invalid"));
    }
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchSequenceAst::dump() const
{
    QString r = QStringLiteral("MatchSequence(");
    dumpList(r, QStringLiteral("patterns="), patterns);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchMappingAst::dump() const
{
    QString r = QStringLiteral("MatchMapping(");
    dumpList(r, QStringLiteral("keys="), keys);
    dumpList(r, QStringLiteral(", patterns="), patterns);
    dumpNode(r, QStringLiteral(", rest="), rest);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchClassAst::dump() const
{
    QString r = QStringLiteral("MatchClass(");
    dumpNode(r, QStringLiteral("cls="), cls);
    dumpList(r, QStringLiteral(", patterns="), patterns);
    dumpNode(r, QStringLiteral(", kwd_attrs="), kwdAttrs);
    dumpList(r, QStringLiteral(", kwd_patterns="), kwdPatterns);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchStarAst::dump() const
{
    QString r = QStringLiteral("MatchStar(");
    dumpNode(r, QStringLiteral("name="), name);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchAsAst::dump() const
{
    QString r = QStringLiteral("MatchAs(");
    dumpNode(r, QStringLiteral("name="), name);
    if (pattern)
        dumpNode(r, QStringLiteral(", pattern="), pattern);
    r.append(QLatin1Char(')'));
    return r;
}

QString MatchOrAst::dump() const
{
    QString r = QStringLiteral("MatchOr(");
    dumpList(r, QStringLiteral(", patterns="), patterns);
    r.append(QLatin1Char(')'));
    return r;
}


}
