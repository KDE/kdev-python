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

#include "astbuilder.h"

#include <QStringList>

#include "pythonparser.h"
#include "ast.h"
#include <kdev-pg-token-stream.h>

#include <kdebug.h>

namespace Python
{

//TODO: Check that created AST nodes are pushed onto the stack _before_ visiting subnodes to make sure their parent is correct

template <typename T> static T* safeNodeCast( Ast* node )
{
    T* ast = dynamic_cast<T*>(node);
    Q_ASSERT(ast);
    return ast;
}

static QList<TargetAst*> targetAstListFromExpressionAstList( const QList<ExpressionAst*>& list )
{
    QList<TargetAst*> l;
    foreach( ExpressionAst* ast, list )
    {
        switch( ast->astType )
        {
            case Ast::IdentifierAst:
            {
                IdentifierTargetAst* target = new IdentifierTargetAst( ast->parent );
                target->identifier = safeNodeCast<IdentifierAst>( ast );
                target->start = ast->start;
                target->end = ast->end;
                target->startCol = ast->startCol;
                target->startLine = ast->startLine;
                target->endCol = ast->endCol;
                target->endLine = ast->endLine;
                l << target;
                break;
            }
            case Ast::SubscriptAst:
            {
                SubscriptTargetAst* target = new SubscriptTargetAst( ast->parent );
                target->subscript = safeNodeCast<SubscriptAst>( ast );
                target->start = ast->start;
                target->end = ast->end;
                target->startCol = ast->startCol;
                target->startLine = ast->startLine;
                target->endCol = ast->endCol;
                target->endLine = ast->endLine;
                l << target;
                break;
            }
            case Ast::AttributeReferenceAst:
            {
                AttributeReferenceTargetAst* target = new AttributeReferenceTargetAst( ast->parent );
                target->attribute = safeNodeCast<AttributeReferenceAst>( ast );
                target->start = ast->start;
                target->end = ast->end;
                target->startCol = ast->startCol;
                target->startLine = ast->startLine;
                target->endCol = ast->endCol;
                target->endLine = ast->endLine;
                l << target;
                break;
            }
            case Ast::ExtendedSliceAst:
                //fall through
            case Ast::SimpleSliceAst:
            {
                SliceTargetAst* target = new SliceTargetAst( ast->parent );
                target->slice = safeNodeCast<SliceAst>( ast );
                target->start = ast->start;
                target->end = ast->end;
                target->startCol = ast->startCol;
                target->startLine = ast->startLine;
                target->endCol = ast->endCol;
                target->endLine = ast->endLine;
                l << target;
                break;
            }
            case Ast::AtomAst:
            {
                AtomAst* atom = dynamic_cast<AtomAst*>( ast );
                IdentifierTargetAst* target = new IdentifierTargetAst( ast->parent );
                target->identifier = atom->identifier;
                target->start = atom->start;
                target->end = atom->end;
                target->startCol = atom->startCol;
                target->endCol = atom->endCol;
                target->startLine = atom->startLine;
                target->endLine = atom->endLine;
                l << target;
                delete atom;
                break;
            }
            default:
                kDebug() << ast->astType;
                Q_ASSERT_X( false, "create_targetlist", "Ooops, found an expression that we can't convert to a target ast, check the code! " );
        }
    }
    return l;
}

template <typename T> static  QList<T*> generateSpecializedList( const QList<Ast*>& list )
{
    QList<T*> l;
    foreach( Ast* ast, list )
    {
        T* temp = safeNodeCast<T>( ast );
        l << temp;
    }
    return l;
}

IdentifierAst* AstBuilder::createIdentifier( Ast* parent, qint64 idx )
{
    IdentifierAst* ast = new IdentifierAst( parent );
    ast->start = parser->tokenStream->token( idx ).begin;
    ast->end = parser->tokenStream->token( idx ).end;
    parser->tokenStream->startPosition( idx, &ast->startLine, &ast->startCol );
    parser->tokenStream->endPosition( idx, &ast->endLine, &ast->endCol );
    ast->identifier = tokenText( idx );
    return ast;
}

QList<IdentifierAst*> AstBuilder::identifierListFromTokenList( Ast* parent, const KDevPG::ListNode<qint64>* sequence )
{
    QList<IdentifierAst*> identifiers;
    for( int i = 0; i < sequence->count(); i++ )
    {
        identifiers << createIdentifier( parent, sequence->at(i)->element );
    }
    return identifiers;
}

void AstBuilder::setStartEnd( Ast* ast, PythonParser::AstNode* node )
{
    ast->start = parser->tokenStream->token( node->startToken ).begin;
    ast->end = parser->tokenStream->token( node->endToken ).end;
    parser->tokenStream->startPosition( node->startToken, &ast->startLine, &ast->startCol );
    parser->tokenStream->endPosition( node->endToken, &ast->endLine, &ast->endCol );
}

QString AstBuilder::tokenText( qint64 tokenidx )
{
    // -1 means this is not a valid token idx and thus return an empty string;
    if( tokenidx == -1 )
        return "";
    KDevPG::TokenStream::Token token = parser->tokenStream->token( tokenidx );
    return parser->tokenText( token.begin, token.end );
}

AstBuilder::AstBuilder(PythonParser::Parser* p)
    : parser(p)
{
}

void AstBuilder::visitAndExpr(PythonParser::AndExprAst *node)
{
    kDebug() << "visitAndExpr start";
    visitNode( node->andExpr );
    if( node->anddShifExprSequence && node->anddShifExprSequence->count() > 0 )
    {
        BinaryExpressionAst* ast = createAst<BinaryExpressionAst>( node );
        ast->opType = ArithmeticExpressionAst::BinaryAnd;
        ast->lhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
        int count = node->anddShifExprSequence->count();
        BinaryExpressionAst* curast = ast;
        for( int i = 0; i < count; i++ )
        {
            visitNode( node->anddShifExprSequence->at(i)->element );
            if( i+1 < count )
            {
                BinaryExpressionAst* tmp = createAst<BinaryExpressionAst>( 
                        node->anddShifExprSequence->at(i)->element );
                curast->opType = ArithmeticExpressionAst::BinaryAnd;
                tmp->lhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
                curast->rhs = tmp;
                curast = tmp;
            }else
            {
                curast->rhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
            }
        }
        mNodeStack.push( ast );
    }
    kDebug() << "visitAndExpr end";
}

void AstBuilder::visitAndTest(PythonParser::AndTestAst *node)
{
    kDebug() << "visitAndTest start";
    visitNode( node->notTestSequence->at(0)->element );
    if( node->notTestSequence->count() > 1 )
    {
        BooleanAndOperationAst* ast = createAst<BooleanAndOperationAst>( node );
        ast->lhs = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
        int count = node->notTestSequence->count();
        BooleanAndOperationAst* curast = ast;
        for( int i = 1; i < count; i++ )
        {
            visitNode( node->notTestSequence->at(i)->element );
            if( i+1 < count )
            {
                BooleanAndOperationAst* tmp = createAst<BooleanAndOperationAst>( 
                        node->notTestSequence->at(i)->element );
                tmp->lhs = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
                curast->rhs = tmp;
                curast = tmp;
            }else
            {
                curast->rhs = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
            }
        }
        mNodeStack.push( ast );
    }
    kDebug() << "visitAndTest end";
}

void AstBuilder::visitArglist(PythonParser::ArglistAst *node)
{
    kDebug() << "visitArglist start";
    QList<Ast*> args;
    visitNode( node->argListBegin );
    if( dynamic_cast<GeneratorAst*>( mNodeStack.top() ) )
    {
        args << mNodeStack.pop();
        mListStack.push( args );
        // Early return because a Generator expression was found, thats the only
        // thing in this "argumentlist" then
        return;
    }
    if( node->argListBegin )
    {
        args += mListStack.pop();
    }
    if( node->arglistStar )
    {
        ArgumentAst* ast = createAst<ArgumentAst>( node->arglistStar );
        ast->argumentType = ArgumentAst::ListArgument;
        visitNode( node->arglistStar );
        ast->argumentExpression = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        args << ast;
    }
    if( node->arglistDoublestar )
    {
        ArgumentAst* ast = createAst<ArgumentAst>( node->arglistDoublestar );
        ast->argumentType = ArgumentAst::DictArgument;
        visitNode( node->arglistDoublestar );
        ast->argumentExpression = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        args << ast;
    }
    mListStack.push( args );
    kDebug() << "visitArglist end";
}

void AstBuilder::visitArgument(PythonParser::ArgumentAst *node)
{
    kDebug() << "visitArgument start";
    visitNode( node->argumentTest );
    if( node->argumentEqualTest )
    {
        ArgumentAst* ast = createAst<ArgumentAst>( node );
        ast->argumentType = ArgumentAst::KeywordArgument;
        ast->keywordName = safeNodeCast<IdentifierAst>( mNodeStack.pop() );
        visitNode( node->argumentEqualTest );
        ast->argumentExpression = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        mNodeStack.push( ast );
    }else if( node->genFor )
    {
        GeneratorAst* ast = createAst<GeneratorAst>( node );
        ast->generatedValue = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        visitNode( node->genFor );
        ast->generator = safeNodeCast<GeneratorForAst>( mNodeStack.pop() );
        mNodeStack.push( ast );
    }else
    {
        ArgumentAst* ast = createAst<ArgumentAst>( node );
        ast->argumentType = ArgumentAst::PositionalArgument;
        mNodeStack.push( ast );
    }
    kDebug() << "visitArgument end";
}

void AstBuilder::visitArithExpr(PythonParser::ArithExprAst *node)
{
    kDebug() << "visitArithExpr start";
    visitNode( node->arithTerm );
    if( node->arithOpListSequence && node->arithOpListSequence->count() > 0 && node->arithTermListSequence->count() > 0 )
    {
        Q_ASSERT_X( node->arithOpListSequence->count() == node->arithTermListSequence->count(),
                    "visitArithExpr", "different number of operators and operands" );
        BinaryExpressionAst* ast = createAst<BinaryExpressionAst>( node );
        ast->lhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
        BinaryExpressionAst* cur = ast;
        int count = node->arithOpListSequence->count();
        for( int i = 0; i < count; i++ )
        {
            switch( node->arithOpListSequence->at(i)->element->arithOp )
            {
                case PythonParser::PlusOp:
                    cur->opType = BinaryExpressionAst::BinaryPlus;
                    break;
                case PythonParser::MinusOp:
                    cur->opType = BinaryExpressionAst::BinaryMinus;
                    break;
                default:
                    //Should never reach here, unless somebody changed the grammer and not the builder
                    Q_ASSERT(false);
            }
            visitNode( node->arithTermListSequence->at(i)->element );
            if( i+1 < count )
            {
                BinaryExpressionAst* tmp = createAst<BinaryExpressionAst>( node->arithTermListSequence->at(i)->element );
                cur->rhs = tmp;
                cur = tmp;
                cur->lhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
            }else
            {
                cur->rhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
            }
        }
        mNodeStack.push( ast );
    }
    kDebug() << "visitArithExpr end";
}

void AstBuilder::visitAssertStmt(PythonParser::AssertStmtAst *node)
{
    kDebug() << "visitAssertStmt start";
    AssertAst* ast = createAst<AssertAst>( node );
    visitNode( node->assertNotTest );
    ast->assertTest = safeNodeCast<ExpressionAst>(mNodeStack.pop());
    if( node->assertRaiseTest )
    {
        visitNode( node->assertRaiseTest );
        ast->exceptionValue = safeNodeCast<ExpressionAst>(mNodeStack.pop());
    }
    mNodeStack.push(ast);
    kDebug() << "visitAssertStmt end";
}

void AstBuilder::visitAtom(PythonParser::AtomAst *node)
{
    kDebug() << "visitAtom start";
    AtomAst* ast = createAst<AtomAst>( node );
    if( node->atomIdentifierName >= 0 || node->number || node->stringliteralSequence->count() > 0 )
    {
        if( node->atomIdentifierName >= 0 )
        {
            IdentifierAst* id = createIdentifier( ast, node->atomIdentifierName );
            ast->identifier = id;
        }else if( node->number )
        {
            visitNode( node->number );
            ast->literal = safeNodeCast<LiteralAst>( mNodeStack.pop() );
        }else
        {
            LiteralAst* lit = createAst<LiteralAst>( node );
            lit->parent = ast;
            lit->literalType = LiteralAst::String;
            for( int i = 0; i < node->stringliteralSequence->count(); i++ )
            {
                lit->value += tokenText( node->stringliteralSequence->at(i)->element );
            }
            ast->literal = lit;
        }
    }else if( node->listmaker )
    {
        EnclosureAst* enc = createAst<EnclosureAst>( node->listmaker );
        enc->parent = ast;
        visitNode( node->listmaker );
        enc->encType = EnclosureAst::List;
        enc->list = safeNodeCast<ListAst>( mNodeStack.pop() );
        ast->enclosure = enc;
    }else if( node->codeexpr )
    {
        EnclosureAst* enc = createAst<EnclosureAst>( node->codeexpr );
        visitNode( node->codeexpr );
        enc->parent = ast;
        enc->encType = EnclosureAst::StringConversion;
        enc->stringConversion = generateSpecializedList<ExpressionAst>( mListStack.pop() );
        ast->enclosure = enc;
    }else if( node->dictmaker )
    {
        EnclosureAst* enc = createAst<EnclosureAst>( node->dictmaker );
        enc->parent = ast;
        visitNode( node->dictmaker );
        enc->encType = EnclosureAst::Dictionary;
        enc->dict = safeNodeCast<DictionaryAst>( mNodeStack.pop() );
        ast->enclosure = enc;
    }else if( node->yield )
    {
        visitNode( node->yield );
        EnclosureAst* enc = createAst<EnclosureAst>( node->yield );
        enc->parent = ast;
        enc->encType = EnclosureAst::Yield;
        enc->yield = safeNodeCast<YieldAst>( mNodeStack.pop() );
        ast->enclosure = enc;
    }else
    {
        EnclosureAst* enc;
        visitNode( node->testlist );
        if( node->genFor )
        {
            enc = createAst<EnclosureAst>( node );
            enc->encType = EnclosureAst::Generator;
            QList<ExpressionAst*> l = generateSpecializedList<ExpressionAst>( mListStack.pop() );
            GeneratorAst* gen = createAst<GeneratorAst>( node );
            gen->generatedValue = l.first();
            visitNode( node->genFor );
            gen->generator = safeNodeCast<GeneratorForAst>( mNodeStack.pop() );
            enc->generator = gen;
            enc->parent = ast;
            ast->enclosure = enc;
        }else
        {
            enc = createAst<EnclosureAst>( node );
            enc->encType = EnclosureAst::ParenthesizedForm;
            enc->parent = ast;
            enc->parenthesizedform = generateSpecializedList<ExpressionAst>( mListStack.pop() );
            ast->enclosure = enc;
        }
    }
    mNodeStack.push( ast );
    kDebug() << "visitAtom end";
}

void AstBuilder::visitBreakStmt(PythonParser::BreakStmtAst *node)
{
    kDebug() << "visitBreakStmt start";
    StatementAst* ast = createAst<StatementAst>( node, Ast::BreakAst );
    mNodeStack.push( ast );
    kDebug() << "visitBreakStmt end";
}

void AstBuilder::visitClassdef(PythonParser::ClassdefAst *node)
{
    kDebug() << "visitClassdef start";
    ClassDefinitionAst* ast = createAst<ClassDefinitionAst>( node );
    ast->className = createIdentifier( ast, node->className );
    visitNode( node->testlist );
    ast->inheritance = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    visitNode( node->classSuite );
    ast->classBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    mNodeStack.push(ast);
    kDebug() << "visitClassdef end";
}

void AstBuilder::visitComparison(PythonParser::ComparisonAst *node)
{
    kDebug() << "visitComparison start";
    visitNode( node->compExpr );
    if( node->compOpSequence && node->compOpSequence->count() > 0 && node->compOpExprSequence->count() > 0 )
    {
        ComparisonAst* ast = createAst<ComparisonAst>( node );
        ast->firstComparator = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        mNodeStack.push( ast );
        Q_ASSERT( node->compOpSequence->count() == node->compOpExprSequence->count() );
        int count = node->compOpSequence->count();
        for( int i = 0; i < count; i++ )
        {
            QPair<ComparisonAst::ComparisonOperator, ExpressionAst*> pair;
            switch( node->compOpSequence->at(i)->element->compOp )
            {
                case PythonParser::LessOp:
                    pair.first = ComparisonAst::LessThanOp;
                    break;
                case PythonParser::GreaterOp:
                    pair.first = ComparisonAst::GreaterThanOp;
                    break;
                case PythonParser::IsEqualOp:
                    pair.first = ComparisonAst::EqualOp;
                    break;
                case PythonParser::GreaterEqOp:
                    pair.first = ComparisonAst::GreaterEqualOp;
                    break;
                case PythonParser::LessEqOp:
                    pair.first = ComparisonAst::LessEqualOp;
                    break;
                case PythonParser::UnEqualOp:
                    pair.first = ComparisonAst::UnequalOp;
                    break;
                case PythonParser::InOp:
                    pair.first = ComparisonAst::InOp;
                    break;
                case PythonParser::NotInOp:
                    pair.first = ComparisonAst::NotInOp;
                    break;
                case PythonParser::IsNotOp:
                    pair.first = ComparisonAst::IsNotOp;
                    break;
                case PythonParser::IsOp:
                    pair.first = ComparisonAst::IsOp;
                    break;
                default:
                    //Should never reach here, unless somebody changed the grammer and not the builder
                    Q_ASSERT(false);
            }
            visitNode( node->compOpExprSequence->at(i)->element );
            pair.second = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            ast->comparatorList << pair;
        }
    }
    kDebug() << "visitComparison end";
}

void AstBuilder::visitCompoundStmt(PythonParser::CompoundStmtAst *node)
{
    kDebug() << "visitCompoundStmt start";
    PythonParser::DefaultVisitor::visitCompoundStmt( node );
    kDebug() << "visitCompoundStmt end";
}

void AstBuilder::visitContinueStmt(PythonParser::ContinueStmtAst *node)
{
    kDebug() << "visitContinueStmt start";
    StatementAst* ast = createAst<StatementAst>( node, Ast::ContinueAst );
    mNodeStack.push( ast );
    kDebug() << "visitContinueStmt end";
}

void AstBuilder::visitDecorator(PythonParser::DecoratorAst *node)
{
    kDebug() << "visitDecorator start";
    DecoratorAst* ast = createAst<DecoratorAst>( node );
    visitNode( node->decoratorName );
    ast->dottedName = generateSpecializedList<IdentifierAst>( mListStack.pop() );
    if( node->arguments )
    {
        visitNode( node->arguments );
        ast->arguments = generateSpecializedList<ArgumentAst>( mListStack.pop() );
    }
    mNodeStack.push( ast );
    kDebug() << "visitDecorator end";
}

void AstBuilder::visitDecorators(PythonParser::DecoratorsAst *node)
{
    kDebug() << "visitDecorators start";
    QList<Ast*> l;
    int count = node->decoratorSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->decoratorSequence->at(i)->element );
        l << safeNodeCast<DecoratorAst>( mNodeStack.pop() );
    }
    mListStack.push( l );
    kDebug() << "visitDecorators end";
}

void AstBuilder::visitDefparam(PythonParser::DefparamAst *node)
{
    
    kDebug() << "visitDefparam start";
    if( node->paramname != -1 )
    {
        IdentifierParameterPartAst* ast = createAst<IdentifierParameterPartAst>( node );
        ast->name = createIdentifier( ast, node->paramname );
        mNodeStack.push( ast );
    }else
    {
        ListParameterPartAst* ast = createAst<ListParameterPartAst>( node );
        mNodeStack.push( ast );
        visitNode( node->fplist );
        ast->parameternames = generateSpecializedList<ParameterPartAst>( mListStack.pop() );
    }
    kDebug() << "visitDefparam start";
}

void AstBuilder::visitDelStmt(PythonParser::DelStmtAst *node)
{
    kDebug() << "visitDelStmt start";
    DelAst* ast = createAst<DelAst>( node );
    visitNode( node->delList );
    ast->deleteObjects = generateSpecializedList<TargetAst>( mListStack.pop() );
    mNodeStack.push( ast );
    kDebug() << "visitDelStmt end";
}

void AstBuilder::visitDictmaker(PythonParser::DictmakerAst *node)
{
    kDebug() << "visitDictmaker start";
    DictionaryAst* ast = createAst<DictionaryAst>( node );
    mNodeStack.push(ast);
    int count = node->keyListSequence->count();
    Q_ASSERT( count = node->valueListSequence->count() );
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->keyListSequence->at(i)->element );
        ExpressionAst* key = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        visitNode( node->valueListSequence->at(i)->element );
        ast->dictionary.insert( key, safeNodeCast<ExpressionAst>( mNodeStack.pop() ) );
    }

    kDebug() << "visitDictmaker end";
}

void AstBuilder::visitExceptClause(PythonParser::ExceptClauseAst *node)
{
    kDebug() << "visitExceptClause start";
    ExceptAst* ast = createAst<ExceptAst>( node );
    mNodeStack.push( ast );
    visitNode( node->exceptTest );
    ast->exceptionDeclaration = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    visitNode( node->exceptTargetTest );
    ast->exceptionValue = safeNodeCast<TargetAst>( mNodeStack.pop() );
    kDebug() << "visitExceptClause end";
}

void AstBuilder::visitExecStmt(PythonParser::ExecStmtAst *node)
{
    kDebug() << "visitExecStmt start";
    ExecAst* ast = createAst<ExecAst>( node );
    visitNode( node->execCode );
    ast->executable = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
    if( node->globalDictExec )
    {
        visitNode( node->globalDictExec );
        ast->globalsAndLocals = safeNodeCast<DictionaryAst>( mNodeStack.pop() );
    }
    if( node->localDictExec )
    {
        visitNode( node->localDictExec );
        ast->localsOnly = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    mNodeStack.push( ast );
    kDebug() << "visitExecStmt end";
}

void AstBuilder::visitExpr(PythonParser::ExprAst *node)
{
    kDebug() << "visitExpr start";
    visitNode( node->expr );
    if( node->orrExprSequence && node->orrExprSequence->count() > 0 )
    {
        BinaryExpressionAst* ast = createAst<BinaryExpressionAst>( node );
        ast->opType = ArithmeticExpressionAst::BinaryOr;
        ast->lhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
        int count = node->orrExprSequence->count();
        BinaryExpressionAst* curast = ast;
        for( int i = 0; i < count; i++ )
        {
            visitNode( node->orrExprSequence->at(i)->element );
            if( i+1 < count )
            {
                BinaryExpressionAst* tmp = createAst<BinaryExpressionAst>( 
                        node->orrExprSequence->at(i)->element );
                curast->opType = ArithmeticExpressionAst::BinaryOr;
                tmp->lhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
                curast->rhs = tmp;
                curast = tmp;
            }else
            {
                curast->rhs = safeNodeCast<ArithmeticExpressionAst>( mNodeStack.pop() );
            }
        }
        mNodeStack.push( ast );
    }
    kDebug() << "visitExpr end";
}

void AstBuilder::visitExprStmt(PythonParser::ExprStmtAst *node)
{
    kDebug() << "visitExprStmt start";
    visitNode( node->testlist );
    if( node->augassign )
    {
        // Augmented assignments cannot have multiple targets, so the testlist needs to contain only 1 element
        Q_ASSERT( mListStack.top().count() == 1 );
        AssignmentAst* a = createAst<AssignmentAst>( node );
        QList<TargetAst*> l = targetAstListFromExpressionAstList( 
                generateSpecializedList<ExpressionAst>( mListStack.pop() ) );
        AssignmentAst::OpType op;
        switch( node->augassign->assignOp )
        {
            case PythonParser::PlusEqOp:
                op = AssignmentAst::AddEqualOp;
                break;
            case PythonParser::MinusEqOp:
                op = AssignmentAst::SubEqualOp;
                break;
            case PythonParser::StarEqOp:
                op = AssignmentAst::MultiplyEqualOp;
                break;
            case PythonParser::SlashEqOp:
                op = AssignmentAst::DivideEqualOp;
                break;
            case PythonParser::ModuloEqOp:
                op = AssignmentAst::ModuloEqualOp;
                break;
            case PythonParser::AndEqOp:
                op = AssignmentAst::AndEqualOp;
                break;
            case PythonParser::OrEqOp:
                op = AssignmentAst::OrEqualOp;
                break;
            case PythonParser::HatEqOp:
                op = AssignmentAst::XorEqualOp;
                break;
            case PythonParser::LeftShiftEqOp:
                op = AssignmentAst::LeftShiftEqualOp;
                break;
            case PythonParser::RightShiftEqOp:
                op = AssignmentAst::RightShiftEqualOp;
                break;
            case PythonParser::DoublestarEqOp:
                op = AssignmentAst::PowEqualOp;
                break;
            case PythonParser::DoubleslashEqOp:
                op = AssignmentAst::FloorEqualOp;
                break;
            default:
                //Should never reach here, unless somebody changed the grammer and not the builder
                Q_ASSERT(false);
        }
        a->targets.append( qMakePair( l, op ) );
        if( node->yield )
        {
            visitNode( node->yield );
            a->yieldValue = safeNodeCast<YieldAst>( mNodeStack.pop() );
        }else
        {
            visitNode( node->anugassignTestlist );
            a->value = generateSpecializedList<ExpressionAst>( mListStack.pop() );
        }
        mNodeStack.push( a );
    }else if( node->yield || node->equalTestlistSequence->count() > 0 )
    {
        AssignmentAst* a = createAst<AssignmentAst>( node );
        QList<TargetAst*> l = targetAstListFromExpressionAstList(
                generateSpecializedList<ExpressionAst>( mListStack.pop() ) );
        a->targets.append( qMakePair( l, AssignmentAst::AssignmentOp) );

        int count = node->equalTestlistSequence->count();
        if( count > 0 )
        {
            for( int i = 0; i < count; i++ )
            {
                if( !node->yield && i == count-1 )
                {
                    // We have no yield statement, so the last element in the 
                    // list is the actual expression for the assignment
                    break;
                }
                visitNode( node->equalTestlistSequence->at(i)->element );
                l = targetAstListFromExpressionAstList(
                        generateSpecializedList<ExpressionAst>( mListStack.pop() ) );
                a->targets.append( qMakePair( l, AssignmentAst::AssignmentOp ) );
            }
        }
        if( node->yield )
        {
            visitNode( node->yield );
            a->yieldValue = safeNodeCast<YieldAst>( mNodeStack.pop() );
        }else
        {
            visitNode( node->equalTestlistSequence->at( count-1 )->element );
            a->value = generateSpecializedList<ExpressionAst>( mListStack.pop() );
        }
        mNodeStack.push( a );
    }else
    {
        ExpressionStatementAst *ast = createAst<ExpressionStatementAst>( node );
        ast->expressions = generateSpecializedList<ExpressionAst>( mListStack.pop() );
        mNodeStack.push( ast );
    }
    kDebug() << "visitExprStmt end";
}

void AstBuilder::visitExprlist(PythonParser::ExprlistAst *node)
{
    kDebug() << "visitExprlist start";
    QList<Ast*> l;
    int count = node->exprSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->exprSequence->at(i)->element );
        l << safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    mListStack.push( l );
    kDebug() << "visitExprlist end";
}

void AstBuilder::visitFactor(PythonParser::FactorAst *node)
{
    kDebug() << "visitFactor start";
    if( node->power )
    {
        visitNode( node->power );
    }else
    {
        UnaryExpressionAst* ast = createAst<UnaryExpressionAst>( node );
        mNodeStack.push( ast );
        visitNode( node->factor );
        switch( node->factOp->op )
        {
            case PythonParser::UnaryPlusOp:
                ast->opType = ArithmeticExpressionAst::UnaryPlus;
                break;
            case PythonParser::UnaryTildeOp:
                ast->opType = ArithmeticExpressionAst::UnaryTilde;
                break;
            case PythonParser::UnaryMinusOp:
                ast->opType = ArithmeticExpressionAst::UnaryMinus;
                break;
            default:
                //Shouldn't reach this, unless someone changes the grammar and didn't update here
                Q_ASSERT(false);
        }
        ast->operand = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    kDebug() << "visitFactor end";
}

void AstBuilder::visitFlowStmt(PythonParser::FlowStmtAst *node)
{
    kDebug() << "visitFlowStmt start";
    PythonParser::DefaultVisitor::visitFlowStmt( node );
    kDebug() << "visitFlowStmt end";
}

void AstBuilder::visitForStmt(PythonParser::ForStmtAst *node)
{
    kDebug() << "visitForStmt start";
    ForAst* ast = createAst<ForAst>( node );
    visitNode( node->forExpr );
    ast->assignedTargets = generateSpecializedList<TargetAst>( mListStack.pop() );
    visitNode( node->forTestlist );
    ast->iterable = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    visitNode( node->forSuite );
    ast->forBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    if( node->forElseSuite )
    {
        visitNode( node->forElseSuite );
        ast->elseBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    }
    mNodeStack.push( ast );
    kDebug() << "visitForStmt end";
}

void AstBuilder::visitFpDef(PythonParser::FpDefAst *node)
{
    kDebug() << "visitFpDef start";
    DefaultParameterAst* ast = createAst<DefaultParameterAst>( node );
    
    mNodeStack.push( ast );
    visitNode( node->defparam );
    ast->name = safeNodeCast<ParameterPartAst>( mNodeStack.pop() );
    if( node->fpDefTest )
    {
        visitNode( node->fpDefTest );
        ast->value = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    kDebug() << "visitFpDef end";
}

void AstBuilder::visitFplist(PythonParser::FplistAst *node)
{
    kDebug() << "visitFplist start";
    int count = node->fplistFpdefSequence->count();
    QList<Ast*> l;
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->fplistFpdefSequence->at(i)->element );
        l << safeNodeCast<ParameterPartAst>( mNodeStack.pop() );
    }
    mListStack.push( l );
    kDebug() << "visitFplist end";
}

void AstBuilder::visitFuncdecl(PythonParser::FuncdeclAst *node)
{
    kDebug() << "visitFuncdecl start";
    FunctionDefinitionAst* ast = createAst<FunctionDefinitionAst>( node );
    if( node->decorators )
    {
        visitNode( node->decorators );
        ast->decorators = generateSpecializedList<DecoratorAst>( mListStack.pop() );
    }
    ast->functionName = createIdentifier( ast,  node->funcName );
    if( node->funArgs )
    {
        visitNode( node->funArgs );
        ast->parameters = generateSpecializedList<ParameterAst>( mListStack.pop() );
    }
    visitNode( node->funSuite );
    ast->functionBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    mNodeStack.push( ast );
    kDebug() << "visitFuncdecl end";
}

void AstBuilder::visitFuncDef(PythonParser::FuncDefAst *node)
{
    kDebug() << "visitFuncDef start";
    QList<Ast*> l;
    int count = node->fpDefSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->fpDefSequence->at(i)->element );
        l << safeNodeCast<ParameterAst>( mNodeStack.pop() );
    }
    mListStack.push( l );
    kDebug() << "visitFuncDef end";
}

void AstBuilder::visitGenFor(PythonParser::GenForAst *node)
{
    kDebug() << "visitGenFor start";
    GeneratorForAst* ast = createAst<GeneratorForAst>( node );
    mNodeStack.push( ast );
    visitNode( node->exprlist );
    ast->assignedTargets = generateSpecializedList<TargetAst>( mListStack.pop() );
    visitNode( node->test );
    ast->iterableObject = safeNodeCast<ConditionalExpressionAst>( mNodeStack.pop() );
    if( node->genIter )
    {
        visitNode( node->genIter );
        if( node->genIter->genFor )
        {
            ast->nextGenerator = safeNodeCast<GeneratorForAst>( mNodeStack.pop() );
        }else
        {
            ast->nextCondition = safeNodeCast<GeneratorIfAst>( mNodeStack.pop() );
        }
    }
    kDebug() << "visitGenFor end";
}

void AstBuilder::visitGenIf(PythonParser::GenIfAst *node)
{
    kDebug() << "visitGenIf start";
    GeneratorIfAst* ast = createAst<GeneratorIfAst>( node );
    mNodeStack.push( ast );
    visitNode( node->test );
    ast->condition = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    if( node->genIter )
    {
        visitNode( node->genIter );
        if( node->genIter->genFor )
        {
            ast->nextGenerator = safeNodeCast<GeneratorForAst>( mNodeStack.pop() );
        }else
        {
            ast->nextCondition = safeNodeCast<GeneratorIfAst>( mNodeStack.pop() );
        }
    }
    kDebug() << "visitGenIf end";
}

void AstBuilder::visitGenIter(PythonParser::GenIterAst *node)
{
    kDebug() << "visitGenIter start";
    PythonParser::DefaultVisitor::visitGenIter(node);
    kDebug() << "visitGenIter end";
}

void AstBuilder::visitGlobalStmt(PythonParser::GlobalStmtAst *node)
{
    kDebug() << "visitGlobalStmt start";
    GlobalAst* ast = createAst<GlobalAst>( node );
    ast->identifiers = identifierListFromTokenList( ast, node->globalNameSequence );
    mNodeStack.push( ast );
    kDebug() << "visitGlobalStmt end";
}

void AstBuilder::visitIfStmt(PythonParser::IfStmtAst *node)
{
    kDebug() << "visitIfStmt start";
    IfAst* ast = createAst<IfAst>( node );
    visitNode( node->ifTest );
    ast->ifCondition = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    visitNode( node->ifSuite );
    ast->ifBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    Q_ASSERT( node->elifTestSequence->count() == node->elifSuiteSequence->count() );
    int count = node->elifTestSequence->count();
    for( int i = 0; i < count; i++)
    {
        visitNode( node->elifTestSequence->at(i)->element );
        ExpressionAst* expr = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        visitNode( node->elifSuiteSequence->at(i)->element );
        ast->elseIfBodies.append(
                                 qMakePair( expr ,
                                            generateSpecializedList<StatementAst>(
                                                    mListStack.pop() ) ) );
    }
    if( node->ifElseSuite )
    {
        visitNode( node->ifElseSuite );
        ast->elseBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    }
    mNodeStack.push( ast );
    kDebug() << "visitIfStmt end";
}

void AstBuilder::visitImportFrom(PythonParser::ImportFromAst *node)
{
    kDebug() << "visitImportFrom start";
    if( !node->importAsNames )
    {
        StarImportAst* ast = createAst<StarImportAst>( node );
        ast->modulePath = identifierListFromTokenList( ast, node->importFromName->dottedNameSequence );
        mNodeStack.push( ast );
    }else
    {
        FromImportAst* ast = createAst<FromImportAst>( node );
        ast->modulePath = identifierListFromTokenList( ast, node->importFromName->dottedNameSequence );
        const KDevPG::ListNode<PythonParser::ImportAsNameAst*>* idNames;
        idNames = node->importAsNames->importAsNameSequence;
        int count = idNames->count();
        for(int i = 0; i < count; i++)
        {
            PythonParser::ImportAsNameAst* namenode = idNames->at(i)->element;
            kDebug() << "Fetching from-as:" << tokenText( namenode->importedName );
            ast->identifierAsName.append( qMakePair( 
                                                      createIdentifier( ast, namenode->importedName ), 
                                                      createIdentifier( ast, namenode->importedAs ) ) );
        }
        mNodeStack.push( ast );
    }
    kDebug() << "visitImportFrom end";
}

void AstBuilder::visitImportName(PythonParser::ImportNameAst *node)
{
    kDebug() << "visitImportName start";
    PlainImportAst* ast = createAst<PlainImportAst>( node );
    const KDevPG::ListNode<PythonParser::DottedAsNameAst*>* importedmodules;
    importedmodules = node->importName->dottedAsNameSequence;
    int count = importedmodules->count();
    for( int i = 0; i < count ; i++ )
    {
        PythonParser::DottedAsNameAst* import = importedmodules->at(i)->element;
        QList<IdentifierAst*> modulepath = identifierListFromTokenList( ast, import->importDottedName->dottedNameSequence );
        ast->modulesAsName.append( qMakePair( modulepath, createIdentifier( ast, import->importedAs ) ) );
    }
    mNodeStack.push( ast );
    kDebug() << "visitImportName end";
}

void AstBuilder::visitImportStmt(PythonParser::ImportStmtAst *node)
{
    kDebug() << "visitImportStmt start";
    PythonParser::DefaultVisitor::visitImportStmt( node );
    kDebug() << "visitImportStmt end";
}

void AstBuilder::visitLambdaDef(PythonParser::LambdaDefAst *node)
{
    kDebug() << "visitLambdaDef start";
    LambdaAst* ast = createAst<LambdaAst>( node );
    if( node->lambdaVarargslist )
    {
        visitNode( node->lambdaVarargslist );
        ast->parameters = generateSpecializedList<ParameterAst>( mListStack.pop() );
    }
    visitNode( node->lambdaTest );
    ast->expression = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    kDebug() << "visitLambdaDef end";
}

void AstBuilder::visitListFor(PythonParser::ListForAst *node)
{
    kDebug() << "visitListFor start";
    ListForAst* ast = createAst<ListForAst>( node );
    mNodeStack.push( ast );
    visitNode( node->exprlist );
    ast->assignedTargets = generateSpecializedList<TargetAst>( mListStack.pop() );
    visitNode( node->testlistSafe );
    ast->iterableObject = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    if( node->listIter )
    {
        visitNode( node->listIter );
        if( node->listIter->listFor )
        {
            ast->nextGenerator = safeNodeCast<ListForAst>( mNodeStack.pop() );
        }else
        {
            ast->nextCondition = safeNodeCast<ListIfAst>( mNodeStack.pop() );
        }
    }
    kDebug() << "visitListFor end";
}

void AstBuilder::visitListIf(PythonParser::ListIfAst *node)
{
    kDebug() << "visitListIf start";
    ListIfAst* ast = createAst<ListIfAst>( node );
    mNodeStack.push( ast );
    visitNode( node->test );
    ast->condition = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    if( node->listIter )
    {
        visitNode( node->listIter );
        if( node->listIter->listFor )
        {
            ast->nextGenerator = safeNodeCast<ListForAst>( mNodeStack.pop() );
        }else
        {
            ast->nextCondition = safeNodeCast<ListIfAst>( mNodeStack.pop() );
        }
    }
    
    kDebug() << "visitListIf end";
}

void AstBuilder::visitListIter(PythonParser::ListIterAst *node)
{
    kDebug() << "visitListIter start";
    PythonParser::DefaultVisitor::visitListIter( node );
    kDebug() << "visitListIter end";
}

void AstBuilder::visitListmaker(PythonParser::ListmakerAst *node)
{
    kDebug() << "visitListmaker start";
    ListAst* ast = createAst<ListAst>( node );
    mNodeStack.push( ast );
    visitNode( node->listMakerTest );
    ast->plainList = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    if( node->listFor )
    {
        //We should have only 1 expression in the listMakerTest as we're having a list_comprehension
        Q_ASSERT( node->listMakerTest->listTestSequence->count() == 1 );
        visitNode( node->listFor );
        ast->listGenerator = safeNodeCast<ListForAst>( mNodeStack.pop() );
    }
    kDebug() << "visitListmaker end";
}

void AstBuilder::visitListMakerTest(PythonParser::ListMakerTestAst *node)
{
    kDebug() << "visitListMakerTest start";
    QList<Ast*> l;
    int count = node->listTestSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->listTestSequence->at(i)->element );
        l << mNodeStack.pop();
    }
    mListStack.push( l );
    kDebug() << "visitListMakerTest end";
}

void AstBuilder::visitNotTest(PythonParser::NotTestAst *node)
{
    kDebug() << "visitNotTest start";
    if( node->notTest )
    {
        BooleanNotOperationAst* ast = createAst<BooleanNotOperationAst>( node );
        mNodeStack.push( ast );
        visitNode( node->notTest );
        ast->op = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
    }else
    {
        visitNode( node->comparison );
    }
    kDebug() << "visitNotTest end";
}

void AstBuilder::visitNumber(PythonParser::NumberAst *node)
{
    kDebug() << "visitNumber start";
    LiteralAst* ast = createAst<LiteralAst>( node );
    switch( node->numType )
    {
        case PythonParser::IntegerNumeric:
            ast->literalType = LiteralAst::Integer;
            break;
        case PythonParser::ImaginaryNumeric:
            ast->literalType = LiteralAst::ImaginaryNumber;
            break;
        case PythonParser::FloatNumeric:
            ast->literalType = LiteralAst::Float;
            break;
    }
    ast->value = tokenText( node->value );
    mNodeStack.push( ast );
    kDebug() << "visitNumber end";
}

void AstBuilder::visitPassStmt(PythonParser::PassStmtAst *node)
{
    kDebug() << "visitPassStmt start";
    StatementAst* ast = createAst<StatementAst>( node,  Ast::PassAst );
    mNodeStack.push( ast );
    kDebug() << "visitPassStmt end";
}

void AstBuilder::visitPower(PythonParser::PowerAst *node)
{
    kDebug() << "visitPower start";
    visitNode( node->atom );
    if( node->trailerSequence )
    {
        int count = node->trailerSequence->count();
        if( count > 0 )
        {
            for( int i = 0; i < count; i++ )
            {
                visitTrailer( node->trailerSequence->at( i )->element );
                PrimaryAst* ast = safeNodeCast<PrimaryAst>( mNodeStack.pop() );
                PrimaryAst* prim = safeNodeCast<PrimaryAst>( mNodeStack.pop() );
                switch( ast->astType )
                {
                    case Ast::CallAst:
                        static_cast<CallAst*>( ast )->callable = prim;
                        break;
                    case Ast::ExtendedSliceAst:
                    case Ast::SimpleSliceAst:
                        static_cast<SliceAst*>( ast )->primary = prim;
                        break;
                    case Ast::AttributeReferenceAst:
                        static_cast<AttributeReferenceAst*>( ast )->primary = prim;
                        break;
                    case Ast::SubscriptAst:
                        static_cast<SubscriptAst*>( ast )->primary = prim;
                        break;
                    default:
                        Q_ASSERT_X(false, "visitTrailer", "OOOPS visitTrailer returned a PrimaryAst that is not known to have a primary in front of it, like an AtomAst or something new.");
                        break;
                }
                mNodeStack.push( ast );
            }
        }
    }
    if( node->factor )
    {
        BinaryExpressionAst* bast = createAst<BinaryExpressionAst>( node );
        bast->opType = ArithmeticExpressionAst::Power;
        bast->lhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        visitNode( node->factor );
        bast->rhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        mNodeStack.push( bast );
    }
    kDebug() << "visitPower end";
}

void AstBuilder::visitPlainArgumentsList(PythonParser::PlainArgumentsListAst *node)
{
    kDebug() << "visitPlainArgumentsList start";
    QList<Ast*> l;
    int count = node->argumentsSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->argumentsSequence->at(i)->element );
        if( dynamic_cast<ArgumentAst*>( mNodeStack.top() ) )
        {
            l << safeNodeCast<ArgumentAst>( mNodeStack.pop() );
        }else if( dynamic_cast<GeneratorAst*>( mNodeStack.top() ) )
        {
            //Early return, we found a generator expression on the stack
            return;
        }
    }
    mListStack.push( l );
    kDebug() << "visitPlainArgumentsList end";
}

void AstBuilder::visitPrintStmt(PythonParser::PrintStmtAst *node)
{
    kDebug() << "visitPrintStmt start";
    PrintAst* ast = createAst<PrintAst>( node );
    if( node->printArgsSequence->count() > 0 )
    {
        int count = node->printArgsSequence->count();
        for( int i = 0; i < count; i++ )
        {
            visitNode( node->printArgsSequence->at(i)->element );
            ast->printables.append( safeNodeCast<ExpressionAst>( mNodeStack.pop() ) );
        }
    }else
    {
        visitNode( node->rshiftArgsSequence->at(0)->element );
        ast->outfile = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
        int count = node->rshiftArgsSequence->count();
        for( int i = 1; i < count; i++ )
        {
            visitNode( node->printArgsSequence->at(i)->element );
            ast->printables.append( safeNodeCast<ExpressionAst>( mNodeStack.pop() ) );
        }
    }
    mNodeStack.push( ast );
    kDebug() << "visitPrintStmt end";
}

void AstBuilder::visitProject(PythonParser::ProjectAst *node)
{
    kDebug() << "visitProject start";
    CodeAst* code = new CodeAst();
    setStartEnd( code, node );
    mNodeStack.push( code );
    int count = node->stmtSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->stmtSequence->at(i)->element );
        Ast* a = mNodeStack.pop();
        if( a )
            code->statements << safeNodeCast<StatementAst>( a );
    }
    kDebug() << "visitProject end";
}

void AstBuilder::visitRaiseStmt(PythonParser::RaiseStmtAst *node)
{
    kDebug() << "visitRaiseStmt start";
    RaiseAst* ast = createAst<RaiseAst>( node );
    if( node->type )
    {
        visitNode( node->type );
        ast->exceptionType = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    if( node->value )
    {
        visitNode( node->value );
        ast->exceptionValue = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    if( node->traceback )
    {
        visitNode( node->traceback );
        ast->traceback = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    mNodeStack.push( ast );
    kDebug() << "visitRaiseStmt end";
}

void AstBuilder::visitReturnStmt(PythonParser::ReturnStmtAst *node)
{
    kDebug() << "visitReturnStmt start";
    ReturnAst* ast = createAst<ReturnAst>( node );
    visitNode( node->returnExpr );
    ast->returnValues = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    mNodeStack.push( ast );
    kDebug() << "visitReturnStmt end";
}

void AstBuilder::visitShiftExpr(PythonParser::ShiftExprAst *node)
{
    kDebug() << "visitShiftExpr start";
    visitNode( node->arithExpr );
    if( node->shiftOpListSequence )
    {
        int count = node->shiftOpListSequence->count();
        if( count > 0 )
        {
            Q_ASSERT( count == node->arithExprListSequence->count() );
            BinaryExpressionAst* ast = createAst<BinaryExpressionAst>( node );
            ast->lhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            BinaryExpressionAst* cur = ast;
            for( int i = 0; i < count; i++ )
            {
                switch( node->shiftOpListSequence->at( i )->element->shiftOp )
                {
                    case PythonParser::LeftShiftOp:
                        cur->opType = ArithmeticExpressionAst::BinaryLeftShift;
                        break;
                    case PythonParser::RightShiftOp:
                        cur->opType = ArithmeticExpressionAst::BinaryRightShift;
                        break;
                    default:
                        Q_ASSERT_X(false, "visitShiftExpr", "OOOPS, shift operator was something other than left or right shifting!");
                }
                visitNode( node->arithExprListSequence->at( i )->element );
                if( i == count - 1 )
                {
                    cur->rhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
                }else
                {
                    cur->rhs = createAst<BinaryExpressionAst>( node->arithExprListSequence->at( i )->element );
                    cur = safeNodeCast<BinaryExpressionAst>( cur->rhs );
                    cur->lhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
                }
            }
            mNodeStack.push( ast );
        }
    }
    kDebug() << "visitShiftExpr end";
}

void AstBuilder::visitSimpleStmt(PythonParser::SimpleStmtAst *node)
{
    kDebug() << "visitSimpleStmt start";
    PythonParser::DefaultVisitor::visitSimpleStmt( node );
    kDebug() << "visitSimpleStmt end";
}

void AstBuilder::visitSmallStmt(PythonParser::SmallStmtAst *node)
{
    kDebug() << "visitSmallStmt start";
    PythonParser::DefaultVisitor::visitSmallStmt( node );
    kDebug() << "visitSmallStmt end";
}

void AstBuilder::visitStmt(PythonParser::StmtAst *node)
{
    kDebug() << "visitStmt start";
    if( node->simpleStmt || node->compoundStmt )
    {
        PythonParser::DefaultVisitor::visitStmt( node );
    }else
    {
        // Pushing a 0 onto the stack so that visitProject and visitSuite can 
        // test for this case
        mNodeStack.push( 0 );
        kDebug() << "Found linebreak";
    }
    kDebug() << "visitStmt end";
}

void AstBuilder::visitSubscript(PythonParser::SubscriptAst *node)
{
    kDebug() << "visitSubscript start";
    if( node->isEllipsis || node->hasColon )
    {
        if( node->isEllipsis )
        {
            EllipsisSliceItemAst* ast = createAst<EllipsisSliceItemAst>( node );
            mNodeStack.push( ast );
        }else
        {
            ProperSliceItemAst* ast = createAst<ProperSliceItemAst>( node );
            mNodeStack.push( ast );
            if( node->begin )
            {
                visitNode( node->begin );
                ast->bounds.first = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            }
            if( node->end )
            {
                visitNode( node->end );
                ast->bounds.second = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            }
            if( node->step )
            {
                visitNode( node->step );
                ast->stride = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            }
        }
    }else if( node->begin )
    {
        visitNode( node->begin );
    }
    kDebug() << "visitSubscript end";
}

void AstBuilder::visitSubscriptlist(PythonParser::SubscriptlistAst *node)
{
    kDebug() << "visitSubscriptlist start";
    
    if( node->hasComma )
    {
        int count = node->subscriptSequence->count();
        PrimaryAst* curast = createAst<SubscriptAst>( node );
        mNodeStack.push( curast );
        for( int i = 0; i < count; i++ )
        {
            visitNode( node->subscriptSequence->at( i )->element );
            if( dynamic_cast<ExpressionAst*>( mNodeStack.top() ) == 0
                && curast->astType != Ast::ExtendedSliceAst )
            {
                SubscriptAst* sast = safeNodeCast<SubscriptAst>( curast );
                curast = createAst<ExtendedSliceAst>( node );
                ExtendedSliceAst* esast = safeNodeCast<ExtendedSliceAst>( curast );
                for( int j = 0; j < sast->subscription.count(); j++ )
                {
                    ExpressionSliceItemAst* esiast = createAst<ExpressionSliceItemAst>(
                            node->subscriptSequence->at(j)->element );
                    esiast->sliceExpression = sast->subscription.at( j );
                    esast->extendedSliceList << esiast;
                }
                delete sast;
            }
            
            if( curast->astType == Ast::ExtendedSliceAst )
            {
                if( dynamic_cast<ExpressionAst*>( mNodeStack.top() ) != 0 )
                {
                    ExpressionSliceItemAst* itemast = createAst<ExpressionSliceItemAst>(
                            node->subscriptSequence->at(i)->element );
                    itemast->sliceExpression = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
                    safeNodeCast<ExtendedSliceAst>( curast )->extendedSliceList << itemast;
                }else
                {
                    safeNodeCast<ExtendedSliceAst>( curast )->extendedSliceList << 
                        safeNodeCast<SliceItemAst>( mNodeStack.pop() );
                }
            }else
            {
                safeNodeCast<SubscriptAst>( curast )->subscription 
                        << safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            }
        }
    }else
    {
        visitNode( node->subscriptSequence->at(0)->element );
        if( dynamic_cast<ExpressionAst*>( mNodeStack.top() ) )
        {
            SubscriptAst* ast = createAst<SubscriptAst>( node );
            ast->subscription << safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            mNodeStack.push( ast );
        }else
        {
            SimpleSliceAst* ast = createAst<SimpleSliceAst>( node );
            ProperSliceItemAst* extslice = safeNodeCast<ProperSliceItemAst>( mNodeStack.pop() );
            ast->simpleSliceBounds.first = extslice->bounds.first;
            ast->simpleSliceBounds.second = extslice->bounds.second;
            delete extslice;
            mNodeStack.push( ast );
        }
    }
    
    kDebug() << "visitSubscriptlist end";
}

void AstBuilder::visitSuite(PythonParser::SuiteAst *node)
{
    kDebug() << "visitSuite start";
    QList<Ast*> l;
    if( node->simpleStmt )
    {
        visitNode( node->simpleStmt );
        l << mNodeStack.pop();
    } else 
    {
        int count = node->stmtSequence->count();
        for( int i = 0; i < count; i++ )
        {
            visitNode( node->stmtSequence->at(i)->element );
            Ast* a = mNodeStack.pop();
            if( a )
                l << a;
        }
    }
    mListStack.push( l );
    kDebug() << "visitSuite end";
}

void AstBuilder::visitTerm(PythonParser::TermAst *node)
{
    kDebug() << "visitTerm start";
    visitNode( node->factor );
    if( node->factorsSequence )
    {
        int count = node->factorsSequence->count();
        if( count > 0 )
        {
            Q_ASSERT( count == node->termOpSequence->count() );
            BinaryExpressionAst* curast = createAst<BinaryExpressionAst>( node );
            curast->lhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            // put the binary expression onto the stack now, so its still on the stack
            // after the loop finishes
            mNodeStack.push( curast );
            for( int i = 0; i < count; i++ )
            {
                //Push current bin-expr on stack to be used as parent
                mNodeStack.push( curast );
                visitNode( node->factorsSequence->at(i)->element );
                if( i == count-1 )
                {
                    curast->rhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
                }else
                {
                    curast->rhs = createAst<BinaryExpressionAst>( node );
                    switch( node->termOpSequence->at(i)->element->op )
                    {
                        case PythonParser::StarOp:
                            curast->opType = ArithmeticExpressionAst::BinaryMultiply;
                            break;
                        case PythonParser::ModuloOp:
                            curast->opType = ArithmeticExpressionAst::BinaryModulo;
                            break;
                        case PythonParser::SlashOp:
                            curast->opType = ArithmeticExpressionAst::BinaryDivide;
                            break;
                        case PythonParser::DoubleSlashOp:
                            curast->opType = ArithmeticExpressionAst::BinaryFloor;
                            break;
                        default:
                            Q_ASSERT_X( false, "visitTerm", "OOPS, termop has an unknown value" );
                    }
                    curast->lhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
                    curast = safeNodeCast<BinaryExpressionAst>( curast->rhs );
                }
                //pop parent from stack
                mNodeStack.pop();
            }
        }
    }
    kDebug() << "visitTerm end";
}

void AstBuilder::visitTest(PythonParser::TestAst *node)
{
    kDebug() << "visitTest start";
    if( node->lambdaDef )
    {
        visitNode( node->lambdaDef );
    }else
    {
        visitNode( node->andTestSequence->at(0)->element );
        if( node->andTestSequence->count() > 1 )
        {
            BooleanOrOperationAst* ast = createAst<BooleanOrOperationAst>( node );
            ast->lhs = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
            int count = node->andTestSequence->count();
            mNodeStack.push( ast );
            for( int i = 1; i < count; i++ )
            {
                visitNode( node->andTestSequence->at(i)->element );
                if( i+1 < count )
                {
                    BooleanOrOperationAst* tmp = createAst<BooleanOrOperationAst>( 
                            node->andTestSequence->at(i)->element );
                    tmp->lhs = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
                    ast->rhs = tmp;
                    ast = tmp;
                }else
                {
                    ast->rhs = safeNodeCast<BooleanOperationAst>( mNodeStack.pop() );
                }
            }
        }
    }
    kDebug() << "visitTest end";
}

void AstBuilder::visitTestlist(PythonParser::TestlistAst *node)
{
    kDebug() << "visitTestlist start";
    QList<Ast*> expressions;
    int count = node->testsSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->testsSequence->at( i )->element );
        expressions << safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    mListStack.push( expressions ); 
    kDebug() << "visitTestlist end";
}

void AstBuilder::visitCodeexpr(PythonParser::CodeexprAst *node)
{
    kDebug() << "visitCodeexpr start";
    QList<Ast*> l;
    int count = node->testSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->testSequence->at(i)->element );
        l << safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    mListStack.push( l );
    kDebug() << "visitCodeexpr end";
}

void AstBuilder::visitTestlistSafe(PythonParser::TestlistSafeAst *node)
{
    kDebug() << "visitTestlistSafe start";
    QList<Ast*> expressions;
    int count = node->testSequence->count();
    for( int i = 0; i < count; i++ )
    {
        visitNode( node->testSequence->at( i )->element );
        expressions << safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    }
    mListStack.push( expressions ); 
    kDebug() << "visitTestlistSafe end";
}

void AstBuilder::visitTrailer(PythonParser::TrailerAst *node)
{
    kDebug() << "visitTrailer start";
    if( node->trailerArglist )
    {
        CallAst* ast = createAst<CallAst>( node );
        visitNode( node->trailerArglist );
        QList<Ast*> tmp = mListStack.pop();
        if( tmp.count() == 1 && tmp.at( 0 )->astType == Ast::GeneratorAst )
        {
            //generator in the call
            ast->generator = safeNodeCast<GeneratorAst>( tmp.at( 0 ) );
        }else
        {
            ast->arguments = generateSpecializedList<ArgumentAst>( tmp );
        }
        mNodeStack.push( ast );
    }else if( node->trailerDotName )
    {
        AttributeReferenceAst* ast = createAst<AttributeReferenceAst>( node );
        ast->identifier = createIdentifier( ast, node->trailerDotName );
        mNodeStack.push( ast );
    }
    kDebug() << "visitTrailer end";
}

void AstBuilder::visitTryStmt(PythonParser::TryStmtAst *node)
{
    kDebug() << "visitTryStmt start";
    TryAst* ast = createAst<TryAst>( node );
    visitNode( node->trySuite );
    ast->tryBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    if( node->finallySuite )
    {
        ast->finallyBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    }else
    {
        int count = node->exceptClauseSequence->count();
        for( int i = 1; i < count; i++ )
        {
            visitNode( node->exceptClauseSequence->at(i)->element );
            ExceptAst* ex = safeNodeCast<ExceptAst>( mNodeStack.pop() );
            visitNode( node->exceptSuiteSequence->at(i)->element );
            ex->exceptionBody = generateSpecializedList<StatementAst>( mListStack.pop() );
            ast->exceptions.append( ex );
        }
        if( node->tryElseSuite )
        {
            visitNode( node->tryElseSuite );
            ast->elseBody = generateSpecializedList<StatementAst>( mListStack.pop() );
        }
    }
    mNodeStack.push( ast );
    kDebug() << "visitTryStmt end";
}

void AstBuilder::visitVarargslist(PythonParser::VarargslistAst *node)
{
    kDebug() << "visitVarargslist start";
    QList<Ast*> l;
    if( node->funcDef )
    {
        visitNode( node->funcDef );
        l += mListStack.pop();
    }
    if( node->funPosParam )
    {
        if( node->funPosParam->starId > -1 )
        {
            ListParameterAst* ast = createAst<ListParameterAst>( node->funPosParam );
            ast->name = createIdentifier( ast, node->funPosParam->starId );
            l << ast;
        }
        if( node->funPosParam->doubleStarId > -1 )
        {
            DictionaryParameterAst* ast = createAst<DictionaryParameterAst>( node->funPosParam );
            ast->name = createIdentifier( ast, node->funPosParam->doubleStarId );
            l << ast;
        }
    }
    mListStack.push( l );
    kDebug() << "visitVarargslist end";
}

void AstBuilder::visitWhileStmt(PythonParser::WhileStmtAst *node)
{
    kDebug() << "visitWhileStmt start";
    WhileAst* ast = createAst<WhileAst>( node );
    visitNode( node->whileTest );
    ast->condition = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
    visitNode( node->whileSuite );
    ast->whileBody = generateSpecializedList<StatementAst>( mListStack.pop() );;
    if( node->whileElseSuite )
    {
        visitNode( node->whileElseSuite );
        ast->elseBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    }
    mNodeStack.push( ast );
    kDebug() << "visitWhileStmt end";
}

void AstBuilder::visitXorExpr(PythonParser::XorExprAst *node)
{
    kDebug() << "visitXorExpr start";
    visitNode( node->xorExpr );
    if( node->hatXorExprSequence && node->hatXorExprSequence->count() > 0 )
    {
        BinaryExpressionAst* curast = createAst<BinaryExpressionAst>( node );
        mNodeStack.push( curast );
        int count = node->hatXorExprSequence->count();
        for( int i = 0; i < count; i++ )
        {
            visitNode( node->hatXorExprSequence->at(i)->element );
            if( i == count - 1 )
            {
                curast->rhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
            }else
            {
                BinaryExpressionAst* bin = createAst<BinaryExpressionAst>( node->hatXorExprSequence->at(i)->element );
                bin->lhs = safeNodeCast<ExpressionAst>( mNodeStack.pop() );
                curast->rhs = bin;
                curast = bin;
            }
        }
    }
    kDebug() << "visitXorExpr end";
}

void AstBuilder::visitYieldExpr( PythonParser::YieldExprAst * node )
{
    kDebug() << "visitYieldExpr start";
    YieldAst* ast = createAst<YieldAst>( node );
    visitNode( node->expr );
    ast->yieldValue = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    mNodeStack.push( ast );
    kDebug() << "visitYieldExpr end";
}

void AstBuilder::visitYieldStmt(PythonParser::YieldStmtAst *node)
{
    kDebug() << "visitYieldStmt start";
    visitNode( node->yield );
    kDebug() << "visitYieldStmt end";
}

CodeAst* AstBuilder::codeAst()
{
    return safeNodeCast<CodeAst>( mNodeStack.top() );
}


}

