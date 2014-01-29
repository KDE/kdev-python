/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *   Copyright 2012 Patrick Spendrin <ps_ml@gmx.de>                        *
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

// The Python 3.4 Language Reference was used as basis for this AST

#ifndef PYTHON_AST_H
#define PYTHON_AST_H

#include <QList>
#include <QMap>
#include <QString>
#include <QStringList>
#include <QPair>
#include <QSharedPointer>

#include <language/editor/simplerange.h>

#include "parserexport.h"

namespace KDevelop
{
    class DUContext;
}

namespace Python {
    class StatementAst;
    class FunctionDefinitionAst;
    class AssignmentAst;
    class PassAst;
    class NonlocalAst;
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
        PassAstType,
        NonlocalAstType,
        NameAstType,
        NameConstantAstType,
        CallAstType,
        AttributeAstType,
        ArgumentsAstType,
        ArgAstType,
        KeywordAstType,
        ClassDefinitionAstType,
        ReturnAstType,
        DeleteAstType,
        ForAstType,
        WhileAstType,
        IfAstType,
        WithAstType,
        WithItemAstType,
        RaiseAstType,
        TryAstType,
        ImportAstType,
        ImportFromAstType,
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
        NumberAstType,
        StringAstType,
        BytesAstType,
        SubscriptAstType,
        StarredAstType,
        ListAstType,
        TupleAstType,
        YieldFromAstType,
        
        SliceAstType,
        EllipsisAstType,
        IndexAstType,
        
        ComprehensionAstType,
        ExceptionHandlerAstType,
        AliasAstType, // for imports
        IdentifierAstType,
        LastAstType // the largest one, not valid!
    };
    
    enum BooleanOperationTypes {
        BooleanAnd = 1,
        BooleanOr,
        BooleanInvalidOperation
    };
    
    enum OperatorTypes {
        OperatorAdd = 1,
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
        UnaryOperatorInvert = 1,
        UnaryOperatorNot,
        UnaryOperatorAdd,
        UnaryOperatorSub,
        UnaryOperatorInvalid
    };
    
    enum ComparisonOperatorTypes {
        ComparisonOperatorEquals = 1,
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
    Ast* parent;
    AstType astType;
    
    void copyRange(const Ast* other) {
        startCol = other->startCol;
        endCol = other->endCol;
        startLine = other->startLine;
        endLine = other->endLine;
    }
    
    bool appearsBefore(const Ast* other) {
        return startLine < other->startLine || ( startLine == other->startLine && startCol < other->startCol );
    };
    
    const KDevelop::SimpleRange range() const {
        return KDevelop::SimpleRange(startLine, startCol, endLine, endCol);
    };

    int startCol;
    int startLine;
    int endCol;
    int endLine;
    
    bool hasUsefulRangeInformation;
    
    KDevelop::DUContext* context;
};

class KDEVPYTHONPARSER_EXPORT Identifier : public Ast {
public:
    Identifier(QString value);
    Identifier operator=(const Identifier& other) {
        value = other.value;
        startCol = other.startCol;
        endCol = other.endCol;
        startLine = other.startLine;
        endLine = other.endLine;
        parent = other.parent;
        hasUsefulRangeInformation = other.hasUsefulRangeInformation;
        return *this;
    };
    bool operator==(const Identifier& rhs) const {
        return value == rhs.value;
    };
    bool operator==(const QString& rhs) const {
        return value == rhs;
    };
    void setEndColumn() {
        endCol = startCol + value.length() - 1;
    }
    operator QString() const {
        return value;
    };
    QString value;
};

// this replaces ModuleAst
class KDEVPYTHONPARSER_EXPORT CodeAst : public Ast {
public:
    CodeAst();
    ~CodeAst();
    typedef QSharedPointer<CodeAst> Ptr;
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
    QList<ExpressionAst*> decorators;
    QList<Ast*> body;
    ExpressionAst* returns;
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

class KDEVPYTHONPARSER_EXPORT WithItemAst : public Ast {
public:
    WithItemAst(Ast* parent);
    ExpressionAst* contextExpression;
    NameAst* optionalVars;
};

class KDEVPYTHONPARSER_EXPORT WithAst : public StatementAst {
public:
    WithAst(Ast* parent);
    QList<Ast*> body;
    QList<WithItemAst*> items;
};

class KDEVPYTHONPARSER_EXPORT RaiseAst : public StatementAst {
public:
    RaiseAst(Ast* parent);
    ExpressionAst* type;
    // TODO check what the other things in the grammar actually are and add them
};

class KDEVPYTHONPARSER_EXPORT TryAst : public StatementAst {
public:
    TryAst(Ast* parent);
    QList<Ast*> body;
    QList<ExceptionHandlerAst*> handlers;
    QList<Ast*> orelse;
    QList<Ast*> finally;
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

class KDEVPYTHONPARSER_EXPORT PassAst : public StatementAst {
public:
    PassAst(Ast* parent);
};

class KDEVPYTHONPARSER_EXPORT NonlocalAst : public StatementAst {
public:
    NonlocalAst(Ast* parent);
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

class KDEVPYTHONPARSER_EXPORT YieldFromAst : public ExpressionAst {
public:
    YieldFromAst(Ast* parent);
    ExpressionAst* value;
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
    inline QString methodName() const {
        switch ( type ) {
            case Python::Ast::OperatorAdd: return QLatin1String("__add__");
            case Python::Ast::OperatorBitwiseAnd: return QLatin1String("__and__");
            case Python::Ast::OperatorBitwiseOr: return QLatin1String("__or__");
            case Python::Ast::OperatorBitwiseXor: return QLatin1String("__xor__");
            case Python::Ast::OperatorDiv: return QLatin1String("__div__");
            case Python::Ast::OperatorFloorDivision: return QLatin1String("__floordiv__");
            case Python::Ast::OperatorLeftShift: return QLatin1String("__lshift__");
            case Python::Ast::OperatorMod: return QLatin1String("__mod__");
            case Python::Ast::OperatorMult: return QLatin1String("__mul__");
            case Python::Ast::OperatorPow: return QLatin1String("__pow__");
            case Python::Ast::OperatorRightShift: return QLatin1String("__rshift__");
            case Python::Ast::OperatorSub: return QLatin1String("__sub__");
            case Python::Ast::OperatorInvalid: // fallthrough
            default: return QString();
        }
    };
    // incremental methods, for e.g. a += 3
    inline QString incMethodName() const {
        QString name = methodName();
        if ( name.size() < 3 ) {
            return name;
        }
        name.insert(2, QLatin1Char('i'));
        return name;
    }
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
    long value; // only used for ints
    bool isInt; // otherwise it's a float
};

class KDEVPYTHONPARSER_EXPORT StringAst : public ExpressionAst {
public:
    StringAst(Ast* parent);
    QString value;
};

class KDEVPYTHONPARSER_EXPORT BytesAst : public ExpressionAst {
public:
    BytesAst(Ast* parent);
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

class KDEVPYTHONPARSER_EXPORT NameConstantAst : public ExpressionAst {
public:
    NameConstantAst(Ast* parent);
    enum NameConstantTypes {
        False,
        True,
        None,
        Invalid // should not happen
    };
    NameConstantTypes value;
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
};

class KDEVPYTHONPARSER_EXPORT SubscriptAst : public ExpressionAst {
public:
    SubscriptAst(Ast* parent);
    ExpressionAst* value;
    SliceAstBase* slice;
    ExpressionAst::Context context;
};

class KDEVPYTHONPARSER_EXPORT StarredAst : public ExpressionAst {
public:
    StarredAst(Ast* parent);
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

class KDEVPYTHONPARSER_EXPORT ArgAst : public Ast {
public:
    ArgAst(Ast* parent);
    Identifier* argumentName;
    ExpressionAst* annotation;
};

class KDEVPYTHONPARSER_EXPORT ArgumentsAst : public Ast {
public:
    ArgumentsAst(Ast* parent);
    QList<ArgAst*> arguments;
    QList<ExpressionAst*> defaultValues;
    ArgAst* vararg;
    ArgAst* kwarg;
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
    Identifier* name;
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
