// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#include "pythondefaultvisitor.h"

namespace PythonParser
{

void DefaultVisitor::visitAndExpr(AndExprAst *node)
{
    visitNode(node->andExpr);
    if (node->anddShifExprSequence)
    {
        const KDevPG::ListNode<ShiftExprAst*> *__it = node->anddShifExprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitAndTest(AndTestAst *node)
{
    if (node->notTestSequence)
    {
        const KDevPG::ListNode<NotTestAst*> *__it = node->notTestSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitArglist(ArglistAst *node)
{
    visitNode(node->argListBegin);
    visitNode(node->arglistStar);
    visitNode(node->arglistDoublestar);
}

void DefaultVisitor::visitArgument(ArgumentAst *node)
{
    visitNode(node->argumentTest);
    visitNode(node->argumentEqualTest);
    visitNode(node->genFor);
}

void DefaultVisitor::visitArithExpr(ArithExprAst *node)
{
    visitNode(node->arithTerm);
    if (node->arithOpListSequence)
    {
        const KDevPG::ListNode<ArithOpAst*> *__it = node->arithOpListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->arithTermListSequence)
    {
        const KDevPG::ListNode<TermAst*> *__it = node->arithTermListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitArithOp(ArithOpAst *)
{
}

void DefaultVisitor::visitAssertStmt(AssertStmtAst *node)
{
    visitNode(node->assertNotTest);
    visitNode(node->assertRaiseTest);
}

void DefaultVisitor::visitAtom(AtomAst *node)
{
    visitNode(node->testlistGexp);
    visitNode(node->listmaker);
    visitNode(node->dictmaker);
    visitNode(node->codeexpr);
    visitNode(node->number);
}

void DefaultVisitor::visitAugassign(AugassignAst *)
{
}

void DefaultVisitor::visitBreakStmt(BreakStmtAst *)
{
}

void DefaultVisitor::visitClassdef(ClassdefAst *node)
{
    visitNode(node->testlist);
    visitNode(node->classSuite);
}

void DefaultVisitor::visitCodeexpr(CodeexprAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitCompOp(CompOpAst *)
{
}

void DefaultVisitor::visitComparison(ComparisonAst *node)
{
    visitNode(node->compExpr);
    if (node->compOpSequence)
    {
        const KDevPG::ListNode<CompOpAst*> *__it = node->compOpSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->compOpExprSequence)
    {
        const KDevPG::ListNode<ExprAst*> *__it = node->compOpExprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitCompoundStmt(CompoundStmtAst *node)
{
    visitNode(node->ifStmt);
    visitNode(node->whileStmt);
    visitNode(node->forStmt);
    visitNode(node->tryStmt);
    visitNode(node->funcdecl);
    visitNode(node->classdef);
}

void DefaultVisitor::visitContinueStmt(ContinueStmtAst *)
{
}

void DefaultVisitor::visitDecorator(DecoratorAst *node)
{
    visitNode(node->decoratorName);
    visitNode(node->arguments);
}

void DefaultVisitor::visitDecorators(DecoratorsAst *node)
{
    if (node->decoratorSequence)
    {
        const KDevPG::ListNode<DecoratorAst*> *__it = node->decoratorSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitDefparam(DefparamAst *node)
{
    visitNode(node->fplist);
}

void DefaultVisitor::visitDelStmt(DelStmtAst *node)
{
    visitNode(node->delList);
}

void DefaultVisitor::visitDictmaker(DictmakerAst *node)
{
    if (node->keyListSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->keyListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->valueListSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->valueListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitDottedAsName(DottedAsNameAst *node)
{
    visitNode(node->importDottedName);
}

void DefaultVisitor::visitDottedAsNames(DottedAsNamesAst *node)
{
    if (node->dottedAsNameSequence)
    {
        const KDevPG::ListNode<DottedAsNameAst*> *__it = node->dottedAsNameSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitDottedName(DottedNameAst *)
{
}

void DefaultVisitor::visitExceptClause(ExceptClauseAst *node)
{
    visitNode(node->exceptTest);
    visitNode(node->exceptTargetTest);
}

void DefaultVisitor::visitExecStmt(ExecStmtAst *node)
{
    visitNode(node->execCode);
    visitNode(node->globalDictExec);
    visitNode(node->localDictExec);
}

void DefaultVisitor::visitExpr(ExprAst *node)
{
    visitNode(node->expr);
    if (node->orrExprSequence)
    {
        const KDevPG::ListNode<XorExprAst*> *__it = node->orrExprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitExprStmt(ExprStmtAst *node)
{
    visitNode(node->testlist);
    visitNode(node->augassign);
    visitNode(node->anugassignTestlist);
    if (node->equalTestlistSequence)
    {
        const KDevPG::ListNode<TestlistAst*> *__it = node->equalTestlistSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitExprlist(ExprlistAst *node)
{
    if (node->exprSequence)
    {
        const KDevPG::ListNode<ExprAst*> *__it = node->exprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->exprlistSequence)
    {
        const KDevPG::ListNode<ExprAst*> *__it = node->exprlistSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitFactOp(FactOpAst *)
{
}

void DefaultVisitor::visitFactor(FactorAst *node)
{
    visitNode(node->factOp);
    visitNode(node->factor);
    visitNode(node->power);
}

void DefaultVisitor::visitFlowStmt(FlowStmtAst *node)
{
    visitNode(node->breakStmt);
    visitNode(node->continueStmt);
    visitNode(node->returnStmt);
    visitNode(node->raiseStmt);
    visitNode(node->yieldStmt);
}

void DefaultVisitor::visitForStmt(ForStmtAst *node)
{
    visitNode(node->forExpr);
    visitNode(node->forTestlist);
    visitNode(node->forSuite);
    visitNode(node->forElseSuite);
}

void DefaultVisitor::visitFpDef(FpDefAst *node)
{
    visitNode(node->defparam);
    visitNode(node->fpDefTest);
}

void DefaultVisitor::visitFplist(FplistAst *node)
{
    if (node->fplistFpdefSequence)
    {
        const KDevPG::ListNode<DefparamAst*> *__it = node->fplistFpdefSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitFunPosParam(FunPosParamAst *)
{
}

void DefaultVisitor::visitFuncDef(FuncDefAst *node)
{
    if (node->fpDefSequence)
    {
        const KDevPG::ListNode<FpDefAst*> *__it = node->fpDefSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitFuncdecl(FuncdeclAst *node)
{
    visitNode(node->decorators);
    visitNode(node->funArgs);
    visitNode(node->funSuite);
}

void DefaultVisitor::visitGenFor(GenForAst *node)
{
    visitNode(node->exprlist);
    visitNode(node->test);
    visitNode(node->genIter);
}

void DefaultVisitor::visitGenIf(GenIfAst *node)
{
    visitNode(node->test);
    visitNode(node->genIter);
}

void DefaultVisitor::visitGenIter(GenIterAst *node)
{
    visitNode(node->genFor);
    visitNode(node->genIf);
}

void DefaultVisitor::visitGlobalStmt(GlobalStmtAst *)
{
}

void DefaultVisitor::visitIfStmt(IfStmtAst *node)
{
    visitNode(node->ifTest);
    visitNode(node->ifSuite);
    if (node->elifTestSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->elifTestSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->elifSuiteSequence)
    {
        const KDevPG::ListNode<SuiteAst*> *__it = node->elifSuiteSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->ifElseSuite);
}

void DefaultVisitor::visitImportAsName(ImportAsNameAst *)
{
}

void DefaultVisitor::visitImportAsNames(ImportAsNamesAst *node)
{
    if (node->importAsNameSequence)
    {
        const KDevPG::ListNode<ImportAsNameAst*> *__it = node->importAsNameSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitImportFrom(ImportFromAst *node)
{
    visitNode(node->importFromName);
    visitNode(node->importAsNames);
}

void DefaultVisitor::visitImportName(ImportNameAst *node)
{
    visitNode(node->importName);
}

void DefaultVisitor::visitImportStmt(ImportStmtAst *node)
{
    visitNode(node->importImport);
    visitNode(node->importFrom);
}

void DefaultVisitor::visitLambdaDef(LambdaDefAst *node)
{
    visitNode(node->lambdaVarargslist);
    visitNode(node->lambdaTest);
}

void DefaultVisitor::visitListFor(ListForAst *node)
{
    visitNode(node->exprlist);
    visitNode(node->testlistSafe);
    visitNode(node->listIter);
}

void DefaultVisitor::visitListIf(ListIfAst *node)
{
    visitNode(node->test);
    visitNode(node->listIter);
}

void DefaultVisitor::visitListIter(ListIterAst *node)
{
    visitNode(node->listFor);
    visitNode(node->listIf);
}

void DefaultVisitor::visitListMakerTest(ListMakerTestAst *node)
{
    if (node->listTestSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->listTestSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitListmaker(ListmakerAst *node)
{
    visitNode(node->listMakerTest);
    visitNode(node->listFor);
}

void DefaultVisitor::visitNotTest(NotTestAst *node)
{
    visitNode(node->notTest);
    visitNode(node->comparison);
}

void DefaultVisitor::visitNumber(NumberAst *)
{
}

void DefaultVisitor::visitPassStmt(PassStmtAst *)
{
}

void DefaultVisitor::visitPlainArgumentsList(PlainArgumentsListAst *node)
{
    if (node->argumentSequence)
    {
        const KDevPG::ListNode<ArgumentAst*> *__it = node->argumentSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitPower(PowerAst *node)
{
    visitNode(node->atom);
    if (node->trailerSequence)
    {
        const KDevPG::ListNode<TrailerAst*> *__it = node->trailerSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->factor);
}

void DefaultVisitor::visitPrintStmt(PrintStmtAst *node)
{
    if (node->printArgsSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->printArgsSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->rshiftArgsSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->rshiftArgsSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitProject(ProjectAst *node)
{
    if (node->stmtSequence)
    {
        const KDevPG::ListNode<StmtAst*> *__it = node->stmtSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitRaiseStmt(RaiseStmtAst *node)
{
    visitNode(node->type);
    visitNode(node->value);
    visitNode(node->traceback);
}

void DefaultVisitor::visitReturnStmt(ReturnStmtAst *node)
{
    visitNode(node->returnExpr);
}

void DefaultVisitor::visitShiftExpr(ShiftExprAst *node)
{
    visitNode(node->arithExpr);
    if (node->shiftOpListSequence)
    {
        const KDevPG::ListNode<ShiftOpAst*> *__it = node->shiftOpListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->arithExprListSequence)
    {
        const KDevPG::ListNode<ArithExprAst*> *__it = node->arithExprListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitShiftOp(ShiftOpAst *)
{
}

void DefaultVisitor::visitSimpleStmt(SimpleStmtAst *node)
{
    if (node->smallStmtSequence)
    {
        const KDevPG::ListNode<SmallStmtAst*> *__it = node->smallStmtSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitSliceop(SliceopAst *node)
{
    visitNode(node->sliceTest);
}

void DefaultVisitor::visitSmallStmt(SmallStmtAst *node)
{
    visitNode(node->exprStmt);
    visitNode(node->printStmt);
    visitNode(node->delStmt);
    visitNode(node->passStmt);
    visitNode(node->flowStmt);
    visitNode(node->importStmt);
    visitNode(node->globalStmt);
    visitNode(node->execStmt);
    visitNode(node->assertStmt);
}

void DefaultVisitor::visitStmt(StmtAst *node)
{
    visitNode(node->simpleStmt);
    visitNode(node->compoundStmt);
}

void DefaultVisitor::visitSubscript(SubscriptAst *node)
{
    visitNode(node->subTest);
    visitNode(node->subColonTest);
    visitNode(node->sliceop);
}

void DefaultVisitor::visitSubscriptlist(SubscriptlistAst *node)
{
    if (node->subscriptSequence)
    {
        const KDevPG::ListNode<SubscriptAst*> *__it = node->subscriptSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitSuite(SuiteAst *node)
{
    visitNode(node->simpleStmt);
    if (node->stmtSequence)
    {
        const KDevPG::ListNode<StmtAst*> *__it = node->stmtSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTerm(TermAst *node)
{
    visitNode(node->factor);
    if (node->termOpListSequence)
    {
        const KDevPG::ListNode<TermOpAst*> *__it = node->termOpListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->factorListSequence)
    {
        const KDevPG::ListNode<FactorAst*> *__it = node->factorListSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTermOp(TermOpAst *)
{
}

void DefaultVisitor::visitTest(TestAst *node)
{
    if (node->andTestSequence)
    {
        const KDevPG::ListNode<AndTestAst*> *__it = node->andTestSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->lambdaDef);
}

void DefaultVisitor::visitTestListGexp(TestListGexpAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTestlist(TestlistAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->testlistSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testlistSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTestlistGexp(TestlistGexpAst *node)
{
    visitNode(node->testListGexp);
    visitNode(node->genFor);
}

void DefaultVisitor::visitTestlistSafe(TestlistSafeAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTrailer(TrailerAst *node)
{
    visitNode(node->trailerArglist);
    visitNode(node->subscriptlist);
}

void DefaultVisitor::visitTryStmt(TryStmtAst *node)
{
    visitNode(node->trySuite);
    if (node->exceptClauseSequence)
    {
        const KDevPG::ListNode<ExceptClauseAst*> *__it = node->exceptClauseSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->exceptSuiteSequence)
    {
        const KDevPG::ListNode<SuiteAst*> *__it = node->exceptSuiteSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->tryElseSuite);
    visitNode(node->finallySuite);
}

void DefaultVisitor::visitVarargslist(VarargslistAst *node)
{
    visitNode(node->funcDef);
    visitNode(node->funPosParam);
}

void DefaultVisitor::visitWhileStmt(WhileStmtAst *node)
{
    visitNode(node->whileTest);
    visitNode(node->whileSuite);
    visitNode(node->whileElseSuite);
}

void DefaultVisitor::visitXorExpr(XorExprAst *node)
{
    visitNode(node->xorExpr);
    if (node->hatXorExprSequence)
    {
        const KDevPG::ListNode<AndExprAst*> *__it = node->hatXorExprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitYieldStmt(YieldStmtAst *node)
{
    visitNode(node->yieldExpr);
}


} // end of namespace PythonParser

