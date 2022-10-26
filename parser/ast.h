/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2012 Patrick Spendrin <ps_ml@gmx.de>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

// The Python 3.4 Language Reference was used as basis for this AST

#ifndef PYTHON_AST_H
#define PYTHON_AST_H

#include <QList>
#include <QString>
#include <QSharedPointer>
#include <KTextEditor/Range>
#include "parserexport.h"
#include "kdevpythonversion.h"

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
        StatementAstType,
        FunctionDefinitionAstType,
        AssignmentAstType,
        PassAstType,
        NonlocalAstType,
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
        AnnotationAssignmentAstType,
        LastStatementType,
        ExpressionAstType, // everything below is an expression
        AwaitAstType,
        NameAstType,
        NameConstantAstType,
        CallAstType,
        AttributeAstType,
        DictionaryComprehensionAstType,
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
        JoinedStringAstType,
        FormattedValueAstType,
        BytesAstType,
        SubscriptAstType,
        StarredAstType,
        ListAstType,
        TupleAstType,
        YieldFromAstType,
        ComprehensionAstType,
        SliceAstType,
        EllipsisAstType,
        AssignmentExpressionAstType,
        LastExpressionType, // keep this at the end of the expr ast list

        CodeAstType,
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
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
        OperatorMatMult,
#endif
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
    virtual ~Ast() {};
    Ast* parent = nullptr;
    AstType astType;

    bool isExpression() const {
        return astType >= ExpressionAstType && astType <= LastExpressionType;
    }

    void copyRange(const Ast* other) {
        startCol = other->startCol;
        endCol = other->endCol;
        startLine = other->startLine;
        endLine = other->endLine;
    }
    
    bool appearsBefore(const Ast* other) {
        return startLine < other->startLine || ( startLine == other->startLine && startCol < other->startCol );
    }
    
    const KTextEditor::Range range() const {
        return KTextEditor::Range(startLine, startCol, endLine, endCol);
    };
    
    const KTextEditor::Cursor start() const {
        return {startLine, startCol};
    }
    
    const KTextEditor::Cursor end() const {
        return {endLine, endCol};
    }

    bool isChildOf(Ast* other) const {
        const Ast* parent = this;
        while ( parent ) {
            if ( parent == other ) {
                return true;
            }
            parent = parent->parent;
        }
        return false;
    }

    virtual QString dump() const
    {
        QString r = "Ast(astType=";
        r.append(astType);
        r.append(", startLine=");
        r.append(startLine);
        r.append(", startCol=");
        r.append(startCol);
        r.append(", endCol=");
        r.append(endCol);
        r.append(", endLine=");
        r.append(endLine);
        r.append(")");
        return r;
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

    QString dump() const override;
};

// this replaces ModuleAst
class KDEVPYTHONPARSER_EXPORT CodeAst : public Ast {
public:
    CodeAst();
    ~CodeAst();
    typedef QSharedPointer<CodeAst> Ptr;
    QList<Ast*> body;
    Identifier* name; // module name
    QString dump() const override;

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
    bool async;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ClassDefinitionAst : public StatementAst {
public:
    ClassDefinitionAst(Ast* parent);
    Identifier* name;
    QList<ExpressionAst*> baseClasses;
    QList<Ast*> body;
    QList<ExpressionAst*> decorators;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ReturnAst : public StatementAst {
public:
    ReturnAst(Ast* parent);
    ExpressionAst* value;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT DeleteAst : public StatementAst {
public:
    DeleteAst(Ast* parent);
    QList<ExpressionAst*> targets;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT AssignmentAst : public StatementAst {
public:
    AssignmentAst(Ast* parent);
    QList<ExpressionAst*> targets;
    ExpressionAst* value;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT AugmentedAssignmentAst : public StatementAst {
public:
    AugmentedAssignmentAst(Ast* parent);
    ExpressionAst* target;
    Ast::OperatorTypes op;
    ExpressionAst* value;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT AnnotationAssignmentAst : public StatementAst {
public:
    AnnotationAssignmentAst(Ast* parent);
    ExpressionAst* target;
    ExpressionAst* value;
    ExpressionAst* annotation;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ForAst : public StatementAst {
public:
    ForAst(Ast* parent);
    ExpressionAst* target;
    ExpressionAst* iterator;
    QList<Ast*> body;
    QList<Ast*> orelse;
    bool async;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT WhileAst : public StatementAst {
public:
    WhileAst(Ast* parent);
    ExpressionAst* condition;
    QList<Ast*> body;
    QList<Ast*> orelse;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT IfAst : public StatementAst {
public:
    IfAst(Ast* parent);
    ExpressionAst* condition;
    QList<Ast*> body;
    QList<Ast*> orelse;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT WithItemAst : public Ast {
public:
    WithItemAst(Ast* parent);
    ExpressionAst* contextExpression;
    ExpressionAst* optionalVars;
};

class KDEVPYTHONPARSER_EXPORT WithAst : public StatementAst {
public:
    WithAst(Ast* parent);
    QList<Ast*> body;
    QList<WithItemAst*> items;
    bool async;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT RaiseAst : public StatementAst {
public:
    RaiseAst(Ast* parent);
    ExpressionAst* type;
    // TODO check what the other things in the grammar actually are and add them
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT TryAst : public StatementAst {
public:
    TryAst(Ast* parent);
    QList<Ast*> body;
    QList<ExceptionHandlerAst*> handlers;
    QList<Ast*> orelse;
    QList<Ast*> finally;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT AssertionAst : public StatementAst {
public:
    AssertionAst(Ast* parent);
    ExpressionAst* condition;
    ExpressionAst* message;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ImportAst : public StatementAst {
public:
    ImportAst(Ast* parent);
    QList<AliasAst*> names;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ImportFromAst : public StatementAst {
public:
    ImportFromAst(Ast* parent);
    Identifier* module;
    QList<AliasAst*> names;
    int level;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT GlobalAst : public StatementAst {
public:
    GlobalAst(Ast* parent);
    QList<Identifier*> names;
    QString dump() const override;
};

// TODO what's stmt::Expr(expr value) in the grammar and what do we need it for?

class KDEVPYTHONPARSER_EXPORT BreakAst : public StatementAst {
public:
    BreakAst(Ast* parent);
    QString dump() const override { return "Break()"; }
};

class KDEVPYTHONPARSER_EXPORT ContinueAst : public StatementAst {
public:
    ContinueAst(Ast* parent);
    QString dump() const override { return "Continue()"; }
};

class KDEVPYTHONPARSER_EXPORT PassAst : public StatementAst {
public:
    PassAst(Ast* parent);
    QString dump() const override { return "Pass()"; }
};

class KDEVPYTHONPARSER_EXPORT NonlocalAst : public StatementAst {
public:
    NonlocalAst(Ast* parent);
    QString dump() const override { return "Nonlocal()"; }
};


/** Expression classes **/
class KDEVPYTHONPARSER_EXPORT ExpressionAst : public Ast {
public:
    ExpressionAst(Ast* parent, AstType type = Ast::ExpressionAstType);
    enum Context {
        Load = 1, // the object is read
        Store = 2, // the object is written
        Delete = 3, // the object is deleted
        Invalid = -1
    };
    ExpressionAst* value; // WARNING this is not set in most cases!
};

class KDEVPYTHONPARSER_EXPORT AssignmentExpressionAst : public ExpressionAst {
public:
    AssignmentExpressionAst(Ast* parent);
    ExpressionAst* target;
    ExpressionAst* value;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT AwaitAst : public ExpressionAst {
public:
    AwaitAst(Ast* parent);
    ExpressionAst* value;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT YieldFromAst : public ExpressionAst {
public:
    YieldFromAst(Ast* parent);
    ExpressionAst* value;
    QString dump() const override;
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
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
            case Python::Ast::OperatorMatMult: return QLatin1String("__matmul__");
#endif
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

    QString dump() const override;
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
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT DictAst : public ExpressionAst {
public:
    DictAst(Ast* parent);
    QList<ExpressionAst*> keys; // WARNING: Can contain null elements: `{**other}`
    QList<ExpressionAst*> values;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT SetAst : public ExpressionAst {
public:
    SetAst(Ast* parent);
    QList<ExpressionAst*> elements;
    QString dump() const override;
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
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT StringAst : public ExpressionAst {
public:
    StringAst(Ast* parent);
    QString value;
    bool usedAsComment;
    QString dump() const override { return "Str('" + value + "')"; }
};

class KDEVPYTHONPARSER_EXPORT JoinedStringAst : public ExpressionAst {
public:
    JoinedStringAst(Ast* parent);
    QList<ExpressionAst*> values;
};

class KDEVPYTHONPARSER_EXPORT FormattedValueAst : public ExpressionAst {
public:
    FormattedValueAst(Ast* parent);
    ExpressionAst* value;
    int conversion;
    ExpressionAst* formatSpec;
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
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT NameAst : public ExpressionAst {
public:
    NameAst(Ast* parent);
    Identifier* identifier;
    ExpressionAst::Context context;
    QString dump() const override;
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
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT CallAst : public ExpressionAst {
public:
    CallAst(Ast* parent);
    ExpressionAst* function;
    QList<ExpressionAst*> arguments;
    QList<KeywordAst*> keywords;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT AttributeAst : public ExpressionAst {
public:
    AttributeAst(Ast* parent);
    ExpressionAst* value;
    Identifier* attribute;
    ExpressionAst::Context context;
    int depth;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT SubscriptAst : public ExpressionAst {
public:
    SubscriptAst(Ast* parent);
    ExpressionAst* value;
    ExpressionAst* slice;
    ExpressionAst::Context context;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT StarredAst : public ExpressionAst {
public:
    StarredAst(Ast* parent);
    ExpressionAst* value;
    ExpressionAst::Context context;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ListAst : public ExpressionAst {
public:
    ListAst(Ast* parent);
    QList<ExpressionAst*> elements;
    ExpressionAst::Context context;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT TupleAst : public ExpressionAst {
public:
    TupleAst(Ast* parent);
    QList<ExpressionAst*> elements;
    ExpressionAst::Context context;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT EllipsisAst : public ExpressionAst {
public:
    EllipsisAst(Ast* parent);
    QString dump() const override { return "Ellipsis()"; }
};

class KDEVPYTHONPARSER_EXPORT SliceAst : public ExpressionAst {
public:
    SliceAst(Ast* parent);
    ExpressionAst* lower;
    ExpressionAst* upper;
    ExpressionAst* step;
    QString dump() const override;
};


/** Independent classes **/

class KDEVPYTHONPARSER_EXPORT ArgAst : public Ast {
public:
    ArgAst(Ast* parent);
    Identifier* argumentName;
    ExpressionAst* annotation;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT ArgumentsAst : public Ast {
public:
    ArgumentsAst(Ast* parent);
    QList<ArgAst*> arguments;
    QList<ArgAst*> kwonlyargs;
    QList<ArgAst*> posonlyargs;
    QList<ExpressionAst*> defaultValues;
    QList<ExpressionAst*> defaultKwValues;
    ArgAst* vararg;
    ArgAst* kwarg;
    QString dump() const override;
};

class KDEVPYTHONPARSER_EXPORT KeywordAst : public Ast {
public:
    KeywordAst(Ast* parent);
    Identifier* argumentName;
    ExpressionAst* value;
    QString dump() const override;
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
    QString dump() const override;
};

}

#endif
