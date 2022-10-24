#include "asttransformer.h"
#include "astbuilder.h"

namespace Python
{

template <>
QString AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    PyObject *v = PyObject_GetAttrString(obj, attr);
    // qDebug() << "getattr<str>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr;;
    Q_ASSERT(v); // attr missing
    if (PyUnicode_Check(v))
        return PyUnicodeObjectToQString(v);
    Py_XDECREF(v);
    return "";
}

template <>
bool AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    PyObject *v = PyObject_GetAttrString(obj, attr);
    // qDebug() << "getattr<bool>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr;;
    Q_ASSERT(v); // attr missing
    bool r = PyObject_IsTrue(v) == 1;
    Py_XDECREF(v);
    return r;
}

template <>
int AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    int result;
    PyObject *v = PyObject_GetAttrString(obj, attr);
    // qDebug() << "getattr<int>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr;;
    Q_ASSERT(v); // attr missing
    if (PyLong_Check(v)) {
        result = PyLong_AsLong(v);
    } else {
        result = 0;
    }
    Py_XDECREF(v);
    return result;
}

template <>
PyObject* AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    // qDebug() << "getattr<obj>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr;;
    PyObject* v = PyObject_GetAttrString(obj, attr);
    Q_ASSERT(v); // attr missing
    return v;
}

template <>
ExpressionAst::Context AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    ExpressionAst::Context result;
    PyObject *v = PyObject_GetAttrString(obj, attr);
    if (PyObject_IsInstance(v, grammar.ast_Load))
        result = ExpressionAst::Context::Load;
    else if (PyObject_IsInstance(v, grammar.ast_Store))
        result = ExpressionAst::Context::Store;
    else if (PyObject_IsInstance(v, grammar.ast_Delete))
        result = ExpressionAst::Context::Delete;
    else
        result = ExpressionAst::Context::Invalid;
    Py_XDECREF(v);
    return result;
}

template <>
Ast::OperatorTypes  AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    Ast::OperatorTypes result;
    PyObject *op = PyObject_GetAttrString(obj, attr);
    if (PyObject_IsInstance(op, grammar.ast_Add))
        result = Ast::OperatorAdd;
    else if (PyObject_IsInstance(op, grammar.ast_BitAnd))
        result = Ast::OperatorBitwiseAnd;
    else if (PyObject_IsInstance(op, grammar.ast_BitOr))
        result = Ast::OperatorBitwiseOr;
    else if (PyObject_IsInstance(op, grammar.ast_BitXor))
        result = Ast::OperatorBitwiseXor;
    else if (PyObject_IsInstance(op, grammar.ast_Div))
        result = Ast::OperatorDiv;
    else if (PyObject_IsInstance(op, grammar.ast_FloorDiv))
        result = Ast::OperatorFloorDivision;
    else if (PyObject_IsInstance(op, grammar.ast_LShift))
        result = Ast::OperatorLeftShift;
    else if (PyObject_IsInstance(op, grammar.ast_Mod))
        result = Ast::OperatorMod;
    else if (PyObject_IsInstance(op, grammar.ast_Mult))
        result = Ast::OperatorMult;
    else if (PyObject_IsInstance(op, grammar.ast_MatMult))
        result = Ast::OperatorMatMult;
    else if (PyObject_IsInstance(op, grammar.ast_Pow))
        result = Ast::OperatorPow;
    else if (PyObject_IsInstance(op, grammar.ast_RShift))
        result = Ast::OperatorRightShift;
    else if (PyObject_IsInstance(op, grammar.ast_Sub))
        result = Ast::OperatorSub;
    else
        result = Ast::OperatorInvalid;
    Py_XDECREF(op);
    return result;
}

Ast* AstTransformer::visitModuleNode(PyObject* node, Ast* parent)
{
    Q_UNUSED(parent);
    if (!PyObject_IsInstance(node, grammar.ast_Module)) return nullptr;
    CodeAst* ast = new CodeAst();
    {
        // qDebug() << "Visit module: " << PyUnicodeObjectToQString(PyObject_Str(node));
        PyObject* body = getattr<PyObject*>(node, "body");
        ast->body = visitNodeList<Ast>(body, ast);
        Py_DECREF(body);
    }
    return ast;
}

template<typename K>
QList<K*> AstTransformer::visitNodeList(PyObject* node, Ast* parent)
{
    // qDebug() << "visit list: " << PyUnicodeObjectToQString(PyObject_Str(node));
    QList<K*> nodelist;
    Q_ASSERT(PyList_Check(node));
    for ( int i=0; i < PyList_Size(node); i++ )
    {
        PyObject* currentNode = PyList_GetItem(node, i);
        Ast* result = visitNode(currentNode, parent);
        K* transformedNode = static_cast<K*>(result);
        nodelist.append(transformedNode);
    }
    // qDebug() << "  size: " << nodelist.size();
    return nodelist;
}

Ast* AstTransformer::visitNode(PyObject* node, Ast* parent)
{
    if ( ! node || node == Py_None ) return nullptr;
    // qDebug() << "visit node: " << PyUnicodeObjectToQString(PyObject_Str(node));

    if (PyObject_IsInstance(node, grammar.ast_expr))
        return visitExprNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_stmt))
        return visitStmtNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_arg))
        return visitArgNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_comprehension))
        return visitComprehensionNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_arguments))
        return visitArgumentsNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_keyword))
        return visitKeywordNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_alias))
        return visitAliasNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_withitem))
        return visitWithItemNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_excepthandler))
        return visitExceptHandlerNode(node, parent);
    if (PyObject_IsInstance(node, grammar.ast_mod))
        return visitModuleNode(node, parent);
    qWarning() << "Unsupported AST type: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_UNREACHABLE();
}

Ast* AstTransformer::visitAliasNode(PyObject* node, Ast* parent)
{
    if (!node) return nullptr;
    // qDebug() << "visit alias: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_alias));
    AliasAst* v = new  AliasAst(parent);
    v->name = new Python::Identifier(getattr<QString>(node, "name"));
    QString asname = getattr<QString>(node, "asname");
    v->asName = asname.size() ? new Python::Identifier(asname) : nullptr;
    return v;
}


Ast* AstTransformer::visitArgNode(PyObject* node, Ast* parent)
{
    if (!node || node == Py_None) return nullptr;
    // qDebug() << "visit arg: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_arg));
    ArgAst* v = new  ArgAst(parent);
    QString arg = getattr<QString>(node, "arg");
    if (arg.size()) {
        v->argumentName = new Python::Identifier(arg);
        v->argumentName->startCol = getattr<int>(node, "col_offset");
        v->argumentName->startLine = tline(getattr<int>(node, "lineno"));
        v->argumentName->endCol = v->argumentName->startCol + arg.size() - 1;
        v->argumentName->endLine = v->argumentName->startLine;

        v->startCol = v->argumentName->startCol;
        v->startLine = v->argumentName->startLine;
        v->endCol = v->argumentName->endCol;
        v->endLine = v->argumentName->endLine;
    } else {
        v->argumentName = nullptr;
    }
    {
        PyObject* annotation = getattr<PyObject*>(node, "annotation");
        v->annotation = static_cast<ExpressionAst*>(visitExprNode(annotation, v));
        Py_DECREF(annotation);
    }
    return v;
}

Ast* AstTransformer::visitArgumentsNode(PyObject* node, Ast* parent)
{
    if (!node || node == Py_None) return nullptr;
    // qDebug() << "visit args: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_arguments));
    ArgumentsAst* v = new  ArgumentsAst(parent);
    {
        PyObject *vararg = getattr<PyObject*>(node, "vararg");
        v->vararg = static_cast<ArgAst*>(visitArgNode(vararg, v));
        Py_DECREF(vararg);
    }
    {
        PyObject *kwarg = getattr<PyObject*>(node, "kwarg");
        v->kwarg = static_cast<ArgAst*>(visitArgNode(kwarg, v));
        Py_DECREF(kwarg);
    }
    {
        PyObject *args = getattr<PyObject*>(node, "args");
        v->arguments = visitNodeList<ArgAst>(args, v);
        Py_DECREF(args);
    }

    {
        PyObject *defaults = getattr<PyObject*>(node, "defaults");
        v->defaultValues = visitNodeList<ExpressionAst>(defaults, v);
        Py_DECREF(defaults);
    }

    {
        PyObject *kwonlyargs = getattr<PyObject*>(node, "kwonlyargs");
        v->kwonlyargs = visitNodeList<ArgAst>(kwonlyargs, v);
        Py_DECREF(kwonlyargs);
    }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    {
        PyObject *posonlyargs = getattr<PyObject*>(node, "posonlyargs");
        v->posonlyargs = visitNodeList<ArgAst>(posonlyargs, v);
        Py_DECREF(posonlyargs);
    }

    // TODO: kw_defaults?
    //{
    //    PyObject *kw_defaults = getattr<PyObject*>(node, "kw_defaults");
    //    v->kw_defaults = visitNodeList<ArgAst>(kw_defaults, v);
    //    Py_DECREF(kw_defaults);
    //}
#endif

    return v;
}

Ast* AstTransformer::visitComprehensionNode(PyObject* node, Ast* parent) {
    if ( ! node || node == Py_None ) return nullptr; // TODO: Type check?
    // qDebug() << "visit comp: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_comprehension));
    ComprehensionAst* v = new  ComprehensionAst(parent);
    {
        PyObject* target = getattr<PyObject*>(node, "target");
        v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
        Py_DECREF(target);
    }
    {
        PyObject* iter = getattr<PyObject*>(node, "iter");
        v->iterator = static_cast<ExpressionAst*>(visitExprNode(iter, v));
        Py_DECREF(iter);
    }
    {
        PyObject* ifs = getattr<PyObject*>(node, "ifs");
        v->conditions = visitNodeList<ExpressionAst>(ifs, v);
        Py_DECREF(ifs);
    }
    return v;
}

Ast* AstTransformer::visitExceptHandlerNode(PyObject* node, Ast* parent)
{
    if ( !node || node == Py_None ) return nullptr;
    // qDebug() << "visit except hdlr: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_excepthandler));
    ExceptionHandlerAst* v = new  ExceptionHandlerAst(parent);
    {
        PyObject* type = getattr<PyObject*>(node, "type");
        v->type = static_cast<ExpressionAst*>(visitExprNode(type, v));
        Py_DECREF(type);
    }

    QString name = getattr<QString>(node, "name");
    if (name.size())
    {
        v->name = new Python::Identifier(name);
        v->name->startCol = getattr<int>(node, "col_offset");
        v->name->startLine = tline(getattr<int>(node, "lineno"));
        v->name->endCol = v->name->startCol + name.size() - 1;
        v->name->endLine = v->name->startLine;

        v->startCol = v->name->startCol;
        v->startLine = v->name->startLine;
        v->endCol = v->name->endCol;
        v->endLine = v->name->endLine;
    } else {
        v->name = nullptr;
    }

    {
        PyObject* body = getattr<PyObject*>(node, "body");
        v->body = visitNodeList<Ast>(body, v);
        Py_DECREF(body);
    }

    //TODO: WHat is this??
    Ast* result = v;
    // Walk through the tree and set proper end columns and lines, as the python parser sadly does not do this for us
    if ( result->hasUsefulRangeInformation ) {
        Ast* parent = v->parent;
        while ( parent ) {
            if ( parent->endLine < v->endLine ) {
                parent->endLine = v->endLine;
                parent->endCol = v->endCol;
            }
            if ( ! parent->hasUsefulRangeInformation && parent->startLine == -99999 ) {
                parent->startLine = v->startLine;
                parent->startCol = v->startCol;
            }
            parent = parent->parent;
        }
    }

    if ( v && v->astType == Ast::NameAstType ) {
        NameAst* r = static_cast<NameAst*>(result);
        r->startCol = r->identifier->startCol;
        r->endCol = r->identifier->endCol;
        r->startLine = r->identifier->startLine;
        r->endLine = r->identifier->endLine;
    }
    return v;
}

Ast* AstTransformer::visitExprNode(PyObject* node, Ast* parent)
{
    if (!node || node == Py_None) return nullptr;
    // qDebug() << "visit expr: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_expr));
    Ast* result = nullptr;

    bool ranges_copied = false;

    if (PyObject_IsInstance(node, grammar.ast_Await)) {
        AwaitAst* v = new  AwaitAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_BoolOp)) {
        BooleanOperationAst* v = new  BooleanOperationAst(parent);
        {
            PyObject* op = getattr<PyObject*>(node, "op");
            if (PyObject_IsInstance(op, grammar.ast_And))
                v->type = Ast::BooleanAnd;
            else if (PyObject_IsInstance(op, grammar.ast_Or))
                v->type = Ast::BooleanOr;
            else
                v->type = Ast::BooleanInvalidOperation;
            Py_DECREF(op);
        }
        {
            PyObject* values = getattr<PyObject*>(node, "values");
            v->values = visitNodeList<ExpressionAst>(values, v);
            Py_DECREF(values);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_BinOp)) {
        BinaryOperationAst* v = new  BinaryOperationAst(parent);
        v->type = getattr<Ast::OperatorTypes>(node, "op");
        {
            PyObject *left = getattr<PyObject*>(node, "left");
            v->lhs = static_cast<ExpressionAst*>(visitNode(left, v));
            Py_DECREF(left);
        }
        {
            PyObject *right = getattr<PyObject*>(node, "right");
            v->rhs = static_cast<ExpressionAst*>(visitExprNode(right, v));
            Py_DECREF(right);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_UnaryOp)) {
        UnaryOperationAst* v = new  UnaryOperationAst(parent);
        {
            PyObject *op = getattr<PyObject*>(node, "op");
            if (PyObject_IsInstance(node, grammar.ast_Invert))
                v->type = Ast::UnaryOperatorInvalid;
            else if (PyObject_IsInstance(node, grammar.ast_Not))
                v->type = Ast::UnaryOperatorNot;
            else if (PyObject_IsInstance(node, grammar.ast_Add))
                v->type = Ast::UnaryOperatorAdd;
            else if (PyObject_IsInstance(node, grammar.ast_Sub))
                v->type = Ast::UnaryOperatorSub;
            else
                v->type = Ast::UnaryOperatorInvalid;
            Py_DECREF(op);
        }
        {
            PyObject *operand = getattr<PyObject*>(node, "operand");
            v->operand = static_cast<ExpressionAst*>(visitExprNode(operand, v));
            Py_DECREF(operand);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Lambda)) {
        LambdaAst* v = new  LambdaAst(parent);
        {
            PyObject* args = getattr<PyObject*>(node, "args");
            v->arguments = static_cast<ArgumentsAst*>(visitArgumentsNode(args, v));
            Py_DECREF(args);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = static_cast<ExpressionAst*>(visitExprNode(body, v));
            Py_DECREF(body);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_IfExp)) {
        IfExpressionAst* v = new  IfExpressionAst(parent);
        {
            PyObject* test = getattr<PyObject*>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
            Py_DECREF(test);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = static_cast<ExpressionAst*>(visitExprNode(body, v));
            Py_DECREF(body);
        }
        {
            PyObject* orelse = getattr<PyObject*>(node, "orelse");
            v->orelse = static_cast<ExpressionAst*>(visitExprNode(orelse, v));
            Py_DECREF(orelse);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Dict)) {
        DictAst* v = new  DictAst(parent);
        {
            PyObject* keys = getattr<PyObject*>(node, "keys");
            v->keys = visitNodeList<ExpressionAst>(keys, v);
            Py_DECREF(keys);
        }
        {
            PyObject* values = getattr<PyObject*>(node, "values");
            v->values = visitNodeList<ExpressionAst>(values, v);
            Py_DECREF(values);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Set)) {
        SetAst* v = new  SetAst(parent);
        {
            PyObject* elts = getattr<PyObject*>(node, "elts");
            v->elements = visitNodeList<ExpressionAst>(elts, v);
            Py_DECREF(elts);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_ListComp)) {
        ListComprehensionAst* v = new  ListComprehensionAst(parent);
        {
            PyObject* elt = getattr<PyObject*>(node, "elt");
            v->element = static_cast<ExpressionAst*>(visitExprNode(elt, v));
            Py_DECREF(elt);
        }
        {
            PyObject* generators = getattr<PyObject*>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
            Py_DECREF(generators);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_SetComp)) {
        SetComprehensionAst* v = new  SetComprehensionAst(parent);
        {
            PyObject* elt = getattr<PyObject*>(node, "elt");
            v->element = static_cast<ExpressionAst*>(visitExprNode(elt, v));
            Py_DECREF(elt);
        }
        {
            PyObject* generators = getattr<PyObject*>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
            Py_DECREF(generators);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_DictComp)) {
        DictionaryComprehensionAst* v = new  DictionaryComprehensionAst(parent);
        {
            PyObject* key = getattr<PyObject*>(node, "key");
            v->key = static_cast<ExpressionAst*>(visitExprNode(key, v));
            Py_DECREF(key);
        }
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitNode(value, v));
            Py_DECREF(value);
        }
        {
            PyObject* generators = getattr<PyObject*>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
            Py_DECREF(generators);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_GeneratorExp)) {
        GeneratorExpressionAst* v = new  GeneratorExpressionAst(parent);
        {
            PyObject* elt = getattr<PyObject*>(node, "elt");
            v->element = static_cast<ExpressionAst*>(visitExprNode(elt, v));
            Py_DECREF(elt);
        }
        {
            PyObject* generators = getattr<PyObject*>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
            Py_DECREF(generators);

        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Yield)) {
        YieldAst* v = new  YieldAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Compare)) {
        CompareAst* v = new  CompareAst(parent);
        {
            PyObject* left = getattr<PyObject*>(node, "left");
            v->leftmostElement = static_cast<ExpressionAst*>(visitExprNode(left, v));
            Py_DECREF(left);
        }

        {
            PyObject* ops = getattr<PyObject*>(node, "ops");
            // TODO? Check list?
            for ( int _i = 0; _i < PyList_Size(ops); _i++ ) {
                PyObject* elt = PyList_GET_ITEM(ops, _i); // borrowed
                ExpressionAst::ComparisonOperatorTypes cmp;
                if (PyObject_IsInstance(elt, grammar.ast_Eq))
                    cmp = Ast::ComparisonOperatorEquals;
                else if (PyObject_IsInstance(elt, grammar.ast_NotEq))
                    cmp = Ast::ComparisonOperatorNotEquals;
                else if (PyObject_IsInstance(elt, grammar.ast_Lt))
                    cmp = Ast::ComparisonOperatorLessThan;
                else if (PyObject_IsInstance(elt, grammar.ast_LtE))
                    cmp = Ast::ComparisonOperatorLessThanEqual;
                else if (PyObject_IsInstance(elt, grammar.ast_Gt))
                    cmp = Ast::ComparisonOperatorGreaterThan;
                else if (PyObject_IsInstance(elt, grammar.ast_GtE))
                    cmp = Ast::ComparisonOperatorGreaterThanEqual;
                else if (PyObject_IsInstance(elt, grammar.ast_Is))
                    cmp = Ast::ComparisonOperatorIs;
                else if (PyObject_IsInstance(elt, grammar.ast_IsNot))
                    cmp = Ast::ComparisonOperatorIsNot;
                else if (PyObject_IsInstance(elt, grammar.ast_In))
                    cmp = Ast::ComparisonOperatorIn;
                else if (PyObject_IsInstance(elt, grammar.ast_NotIn))
                    cmp = Ast::ComparisonOperatorNotIn;
                else
                    cmp = Ast::ComparisonOperatorInvalid;
                v->operators.append(cmp);
            }
            Py_DECREF(ops);
        }

        {
            PyObject* comparators = getattr<PyObject*>(node, "comparators");
            v->comparands = visitNodeList<ExpressionAst>(comparators, v);
            Py_DECREF(comparators);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Call)) {
        CallAst* v = new  CallAst(parent);
        {
            PyObject* func = getattr<PyObject*>(node, "func");
            v->function = static_cast<ExpressionAst*>(visitNode(func, v));
            Py_DECREF(func);
        }
        {
            PyObject* args = getattr<PyObject*>(node, "args");
            v->arguments = visitNodeList<ExpressionAst>(args, v);
            Py_DECREF(args);
        }
        {
            PyObject* keywords = getattr<PyObject*>(node, "keywords");
            v->keywords = visitNodeList<KeywordAst>(keywords, v);
            Py_DECREF(keywords);
        }
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 5, 0)
        /* Convert 3.4 unpacked-args AST to match the new format from 3.5+ */
        // TODO
#endif
        result = v;
    }
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Num)) {
        NumberAst* v = new  NumberAst(parent);
        {
            PyObject* n = getattr<PyObject*>(node, "n");
            v->isInt = PyLong_Check(n);
            v->value = PyLong_AsLong(n);
            Py_DECREF(n);
        }
        result = v;
    }
#endif
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Str)) {
        StringAst* v = new  StringAst(parent);
        v->value = getattr<QString>(node, "s");
        result = v;
    }
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    else if (PyObject_IsInstance(node, grammar.ast_JoinedStr)) {
        JoinedStringAst* v = new  JoinedStringAst(parent);
        {
            PyObject* values = getattr<PyObject*>(node, "values");
            v->values = visitNodeList<ExpressionAst>(values, v);
            Py_DECREF(values);
        }
        result = v;
    }
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    else if (PyObject_IsInstance(node, grammar.ast_FormattedValue)) {
        FormattedValueAst* v = new  FormattedValueAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);

        }
        v->conversion = getattr<int>(node, "conversion");
        {
            PyObject* format_spec = getattr<PyObject*>(node, "format_spec");
            v->formatSpec = static_cast<ExpressionAst*>(visitExprNode(format_spec, v));
            Py_DECREF(format_spec);
        }
        result = v;
    }
#endif
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Bytes)) {
        BytesAst* v = new  BytesAst(parent);
        v->value = getattr<QString>(node, "s");
        result = v;
    }
#endif
    else if (PyObject_IsInstance(node, grammar.ast_Attribute)) {
        AttributeAst* v = new  AttributeAst(parent);
        QString attr = getattr<QString>(node, "attr");
        if (attr.size()) {
            v->attribute = new Python::Identifier(attr);
            v->attribute->startCol = getattr<int>(node, "col_offset");
            v->attribute->startLine = tline(getattr<int>(node, "lineno"));
            v->attribute->endCol = v->attribute->startCol + attr.size() - 1;
            v->attribute->endLine = v->attribute->startLine;

            v->startCol = v->attribute->startCol;
            v->startLine = v->attribute->startLine;
            v->endCol = v->attribute->endCol;
            v->endLine = v->attribute->endLine;
            ranges_copied = true;
        } else {
            v->attribute = nullptr;
        }
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Subscript)) {
        SubscriptAst* v = new  SubscriptAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        {
            PyObject* slice = getattr<PyObject*>(node, "slice");
            v->slice = static_cast<SliceAst*>(visitNode(slice, v));
            Py_DECREF(slice);
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Starred)) {
        StarredAst* v = new  StarredAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitNode(value, v));
            Py_DECREF(value);
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Name)) {
        NameAst* v = new  NameAst(parent);
        QString id = getattr<QString>(node, "id");
        if ( id.size() ) {
            v->identifier = new Python::Identifier(id);
            v->identifier->startCol = getattr<int>(node, "col_offset");
            v->identifier->startLine = tline(getattr<int>(node, "lineno"));
            v->identifier->endCol = v->identifier->startCol + id.size() - 1;
            v->identifier->endLine = v->identifier->endLine;
            v->startCol = v->identifier->startCol;
            v->startLine = v->identifier->startLine;
            v->endCol = v->identifier->endCol;
            v->endLine = v->identifier->endLine;
            ranges_copied = true;
        } else {
            v->identifier = nullptr;
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_List)) {
        ListAst* v = new  ListAst(parent);
        {
            PyObject* elts = getattr<PyObject*>(node, "elts");
            v->elements = visitNodeList<ExpressionAst>(elts, v);
            Py_DECREF(elts);
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Tuple)) {
        TupleAst* v = new  TupleAst(parent);
        {
            PyObject* elts = getattr<PyObject*>(node, "elts");
            v->elements = visitNodeList<ExpressionAst>(elts, v);
            Py_DECREF(elts);
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Ellipsis)) {
        EllipsisAst* v = new  EllipsisAst(parent);
        result = v;
    }
#endif
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_NameConstant)) {
        NameConstantAst* v = new NameConstantAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            if (value == Py_None)
                v->value = NameConstantAst::None;
            else if (value == Py_false)
                v->value = NameConstantAst::False;
            else
                v->value = NameConstantAst::True;
            Py_DECREF(value);
        }
        result = v;
    }
#endif
    else if (PyObject_IsInstance(node, grammar.ast_YieldFrom)) {
        YieldFromAst* v = new  YieldFromAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Constant)) {
        PyObject* value = getattr<PyObject*>(node, "value");
        if (value == Py_None) {
            NameConstantAst* v = new NameConstantAst(parent);
            v->value = NameConstantAst::None;
            result = v;

        } else if (value == Py_True) {
            NameConstantAst* v = new  NameConstantAst(parent);
            v->value = NameConstantAst::True;
            result = v;

        } else if (value == Py_False) {
            NameConstantAst* v = new  NameConstantAst(parent);
            v->value = NameConstantAst::False;
            result = v;

        } else if (value->ob_type == &PyLong_Type) {
            NumberAst* v = new NumberAst(parent);
            v->isInt = true;
            v->value = PyLong_AsLong(value);
            result = v;
        } else if (value->ob_type == &PyFloat_Type || value->ob_type == &PyComplex_Type) {
            result = new NumberAst(parent);

        } else if (value->ob_type == &PyUnicode_Type) {
            StringAst* v = new StringAst(parent);
            v->value = PyUnicodeObjectToQString(value);
            result = v;
        } else if (value->ob_type == &PyBytes_Type) {
            result = new BytesAst(parent);
        } else if (value->ob_type == &PyEllipsis_Type) {
            result = new EllipsisAst(parent);
        } else {
            qWarning() << "Unhandled constant type: " << value->ob_type->tp_name;
            Q_ASSERT(false);

        };
        Py_DECREF(value);
    }
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    else if (PyObject_IsInstance(node, grammar.ast_NamedExpr)) {
        AssignmentExpressionAst* v = new  AssignmentExpressionAst(parent);
        {
            PyObject* target = getattr<PyObject*>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
            Py_DECREF(target);
        }
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 9, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Slice)) {
        SliceAst* v = new  SliceAst(parent);
        {
            PyObject* lower = getattr<PyObject*>(node, "lower");
            v->lower = static_cast<ExpressionAst*>(visitExprNode(lower, v));
            Py_DECREF(lower);
        }
        {
            PyObject* upper = getattr<PyObject*>(node, "upper");
            v->upper = static_cast<ExpressionAst*>(visitExprNode(upper, v));
            Py_DECREF(upper);
        }
        {
            PyObject* step = getattr<PyObject*>(node, "step");
            v->step = static_cast<ExpressionAst*>(visitExprNode(step, v));
            Py_DECREF(step);
        }
        result = v;
    }
#endif
    else {
        qWarning() << "Unsupported _expr AST type: " << PyUnicodeObjectToQString(PyObject_Str(node));
        Q_ASSERT(false);
    }

    if ( ! result ) return nullptr;
    if ( ! ranges_copied ) {
        result->startCol = getattr<int>(node, "col_offset");
        result->endCol = getattr<int>(node, "end_col_offset");
        result->startLine = tline(getattr<int>(node, "lineno"));
        result->endLine = tline(getattr<int>(node, "end_lineno"));
        result->hasUsefulRangeInformation = true;
    }
    else {
        result->hasUsefulRangeInformation = true;
    }

    // Walk through the tree and set proper end columns and lines, as the python parser sadly does not do this for us
    if ( result->hasUsefulRangeInformation ) {
        Ast* parent = result->parent;
        while ( parent ) {
            if ( parent->endLine < result->endLine ) {
                parent->endLine = result->endLine;
                parent->endCol = result->endCol;
            }
            if ( ! parent->hasUsefulRangeInformation && parent->startLine == -99999 ) {
                parent->startLine = result->startLine;
                parent->startCol = result->startCol;
            }
            parent = parent->parent;
        }
    }

    if ( result && result->astType == Ast::NameAstType ) {
        NameAst* r = static_cast<NameAst*>(result);
        r->startCol = r->identifier->startCol;
        r->endCol = r->identifier->endCol;
        r->startLine = r->identifier->startLine;
        r->endLine = r->identifier->endLine;
    }
    return result;
}


Ast* AstTransformer::visitSliceNode(PyObject* node, Ast* parent) {
    if ( ! node || node == Py_None ) return nullptr;
    // Q_ASSERT(PyObject_IsInstance(node, grammar.ast_slice));
    Ast* result = nullptr;
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 9, 0)
    if (PyObject_IsInstance(node, grammar.ast_Slice)) {
        SliceAst* v = new  SliceAst(parent);
        {
            PyObject* lower = getattr<PyObject*>(node, "lower");
            v->lower = static_cast<ExpressionAst*>(visitExprNode(lower, v));
            Py_DECREF(lower);
        }
        {
            PyObject* upper = getattr<PyObject*>(node, "upper");
            v->upper = static_cast<ExpressionAst*>(visitExprNode(upper, v));
            Py_DECREF(upper);
        }
        {
            PyObject* step = getattr<PyObject*>(node, "step");
            v->step = static_cast<ExpressionAst*>(visitExprNode(step, v));
            Py_DECREF(step);
        }
        result = v;
    }
#endif
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 9, 0)
    if (PyObject_IsInstance(node, grammar.ast_ExtSlice)) {
        TupleAst* v = new  TupleAst(parent);
        {
            PyObject* dims = getattr<PyObject*>(node, "dims");
            v->elements = visitNodeList<ExpressionAst>(dims, parent);
            Py_DECREF(dims);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Index)) {
        PyObject* value = getattr<PyObject*>(node, "value");
        return visitNode(value, parent);
    }
#endif
    else {
        qWarning() << "Unsupported _slice AST type: " << PyUnicodeObjectToQString(PyObject_Str(node));
        Q_ASSERT(false);
    }

    // Walk through the tree and set proper end columns and lines, as the python parser sadly does not do this for us
    if ( result->hasUsefulRangeInformation ) {
        Ast* parent = result->parent;
        while ( parent ) {
            if ( parent->endLine < result->endLine ) {
                parent->endLine = result->endLine;
                parent->endCol = result->endCol;
            }
            if ( ! parent->hasUsefulRangeInformation && parent->startLine == -99999 ) {
                parent->startLine = result->startLine;
                parent->startCol = result->startCol;
            }
            parent = parent->parent;
        }
    }

    if ( result && result->astType == Ast::NameAstType ) {
        NameAst* r = static_cast<NameAst*>(result);
        r->startCol = r->identifier->startCol;
        r->endCol = r->identifier->endCol;
        r->startLine = r->identifier->startLine;
        r->endLine = r->identifier->endLine;
    }
    return result;
}

Ast* AstTransformer::visitStmtNode(PyObject* node, Ast* parent) {
    if ( !node || node == Py_None ) return nullptr;
    // qDebug() << "visit stmt: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_stmt));
    bool ranges_copied = false;
    Ast* result = nullptr;
    if (PyObject_IsInstance(node, grammar.ast_Expr)) {
        ExpressionAst* v = new  ExpressionAst(parent);
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_FunctionDef)
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
             || PyObject_IsInstance(node, grammar.ast_AsyncFunctionDef)
#endif
            ) {
        FunctionDefinitionAst* v = new  FunctionDefinitionAst(parent);
        QString name = getattr<QString>(node, "name");
        if ( name.size() ) {
            v->name = new Python::Identifier(name);
            v->name->startCol = getattr<int>(node, "col_offset");
            v->name->startLine = tline(getattr<int>(node, "lineno"));
            v->name->endCol = v->name->startCol + name.size() - 1;
            v->name->endLine = v->name->startLine;

            v->startCol = v->name->startCol;
            v->startLine = v->name->startLine;
            v->endCol = v->name->endCol;
            v->endLine = v->name->endLine;
            ranges_copied = true;
        }
        else {
            v->name = nullptr;
        }

        {
            PyObject* args = getattr<PyObject*>(node, "args");
            v->arguments = static_cast<ArgumentsAst*>(visitArgumentsNode(args, v));
            Py_DECREF(args);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
            Py_DECREF(body);
        }
        {
            PyObject* decorator_list = getattr<PyObject*>(node, "decorator_list");
            v->decorators = visitNodeList<ExpressionAst>(decorator_list, v);
            Py_DECREF(decorator_list);
        }
        {
            PyObject* returns = getattr<PyObject*>(node, "returns");
            v->returns = static_cast<ExpressionAst*>(visitExprNode(returns, v));
            Py_DECREF(returns);
        }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        v->async = PyObject_IsInstance(node, grammar.ast_AsyncFunctionDef);
#endif
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_ClassDef)) {
        ClassDefinitionAst* v = new  ClassDefinitionAst(parent);
        QString name = getattr<QString>(node, "name");
        if ( name.size() ) {
            v->name = new Python::Identifier(name);
            v->name->startCol = getattr<int>(node, "col_offset");
            v->name->startLine = tline(getattr<int>(node, "lineno"));
            v->name->endCol = v->name->startCol + name.size() - 1;
            v->name->endLine = v->name->startLine;

            v->startCol = v->name->startCol;
            v->startLine = v->name->startLine;
            v->endCol = v->name->endCol;
            v->endLine = v->name->endLine;
            ranges_copied = true;
        }
        else {
            v->name = nullptr;
        }

        {
            PyObject* bases = getattr<PyObject*>(node, "bases");
            v->baseClasses = visitNodeList<ExpressionAst>(bases, v);
            Py_DECREF(bases);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
            Py_DECREF(body);
        }
        {
            PyObject* decorator_list = getattr<PyObject*>(node, "decorator_list");
            v->decorators = visitNodeList<ExpressionAst>(decorator_list, v);
            Py_DECREF(decorator_list);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Return)) {
        ReturnAst* v = new  ReturnAst(parent);
        PyObject* value = getattr<PyObject*>(node, "value");
        v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        Py_DECREF(value);
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Delete)) {
        DeleteAst* v = new  DeleteAst(parent);
        PyObject* targets = getattr<PyObject*>(node, "targets");
        v->targets = visitNodeList<ExpressionAst>(targets, v);
        Py_DECREF(targets);
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Assign)) {
        AssignmentAst* v = new  AssignmentAst(parent);
        {
            PyObject* targets = getattr<PyObject*>(node, "targets");
            v->targets = visitNodeList<ExpressionAst>(targets, v);
            Py_DECREF(targets);
        }
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_AugAssign)) {
        AugmentedAssignmentAst* v = new  AugmentedAssignmentAst(parent);
        {
            PyObject* target = getattr<PyObject*>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
            Py_DECREF(target);
        }
        v->op = getattr<Ast::OperatorTypes>(node, "op");
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    else if (PyObject_IsInstance(node, grammar.ast_AnnAssign)) {
        AnnotationAssignmentAst* v = new  AnnotationAssignmentAst(parent);
        {
            PyObject* target = getattr<PyObject*>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
            Py_DECREF(target);
        }
        {
            PyObject* annotation = getattr<PyObject*>(node, "annotation");
            v->annotation = static_cast<ExpressionAst*>(visitExprNode(annotation, v));
            Py_DECREF(annotation);
        }
        {
            PyObject* value = getattr<PyObject*>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
            Py_DECREF(value);
        }
        result = v;
    }
#endif
    else if (PyObject_IsInstance(node, grammar.ast_For)
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        || PyObject_IsInstance(node, grammar.ast_AsyncFor)
#endif
    ) {
        ForAst* v = new  ForAst(parent);
        {
            PyObject* target = getattr<PyObject*>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
            Py_DECREF(target);
        }
        {
            PyObject* iter = getattr<PyObject*>(node, "iter");
            v->iterator = static_cast<ExpressionAst*>(visitExprNode(iter, v));
            Py_DECREF(iter);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
            Py_DECREF(body);
        }
        {
            PyObject* orelse = getattr<PyObject*>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
            Py_DECREF(orelse);
        }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        v->async = PyObject_IsInstance(node, grammar.ast_AsyncFor);
#endif
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_While)) {
        WhileAst* v = new  WhileAst(parent);
        {
            PyObject* test = getattr<PyObject*>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
            Py_DECREF(test);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
            Py_DECREF(body);
        }
        {
            PyObject* orelse = getattr<PyObject*>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
            Py_DECREF(orelse);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_If)) {
        IfAst* v = new  IfAst(parent);
        {
            PyObject* test = getattr<PyObject*>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
            Py_DECREF(test);
        }
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
            Py_DECREF(body);
        }
        {
            PyObject* orelse = getattr<PyObject*>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
            Py_DECREF(orelse);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_With)
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        || PyObject_IsInstance(node, grammar.ast_AsyncWith)
#endif
    ) {
            WithAst* v = new  WithAst(parent);
            {
                PyObject* body = getattr<PyObject*>(node, "body");
                v->body = visitNodeList<Ast>(body, v);
                Py_DECREF(body);
            }
            {
                PyObject* items = getattr<PyObject*>(node, "items");
                v->items = visitNodeList<WithItemAst>(items, v);
                Py_DECREF(items);
            }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
            v->async = PyObject_IsInstance(node, grammar.ast_AsyncWith);
#endif
            result = v;
    }

    else if (PyObject_IsInstance(node, grammar.ast_Raise)) {
        RaiseAst* v = new  RaiseAst(parent);
        {
            PyObject* exc = getattr<PyObject*>(node, "exc");
            v->type = static_cast<ExpressionAst*>(visitExprNode(exc, v));
            Py_DECREF(exc);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Try)) {
        TryAst* v = new  TryAst(parent);
        {
            PyObject* body = getattr<PyObject*>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
            Py_DECREF(body);
        }
        {
            PyObject* handlers = getattr<PyObject*>(node, "handlers");
            v->handlers = visitNodeList<ExceptionHandlerAst>(handlers, v);
            Py_DECREF(handlers);

        }
        {
            PyObject* orelse = getattr<PyObject*>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
            Py_DECREF(orelse);
        }
        {
            PyObject* finalbody = getattr<PyObject*>(node, "finalbody");
            v->finally = visitNodeList<Ast>(finalbody, v);
            Py_DECREF(finalbody);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Assert)) {
        AssertionAst* v = new  AssertionAst(parent);
        {
            PyObject* test = getattr<PyObject*>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
            Py_DECREF(test);
        }
        {
            PyObject* msg = getattr<PyObject*>(node, "msg");
            v->message = static_cast<ExpressionAst*>(visitExprNode(msg, v));
            Py_DECREF(msg);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Import)) {
        ImportAst* v = new  ImportAst(parent);
        {
            PyObject* names = getattr<PyObject*>(node, "names");
            v->names = visitNodeList<AliasAst>(names, v);
            Py_DECREF(names);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_ImportFrom)) {
        ImportFromAst* v = new  ImportFromAst(parent);
        QString module = getattr<QString>(node, "module");
        if ( module.size() ) {
            v->module = new Python::Identifier(module);
            v->module->startCol = getattr<int>(node, "col_offset");
            v->module->startLine = tline(getattr<int>(node, "lineno"));
            v->module->endCol = v->module->startCol + module.size() - 1;
            v->module->endLine = v->module->startLine;

            v->startCol = v->module->startCol;
            v->startLine = v->module->startLine;
            v->endCol = v->module->endCol;
            v->endLine = v->module->endLine;
            ranges_copied = true;
        } else {
            v->module = nullptr;
        }
        {
            PyObject* names = getattr<PyObject*>(node, "names");
            v->names = visitNodeList<AliasAst>(names, v);
            Py_DECREF(names);
        }
        v->level = getattr<int>(node, "level");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Global)) {
        GlobalAst* v = new  GlobalAst(parent);

        PyObject* names = getattr<PyObject*>(node, "names");
        for ( int _i = 0; _i < PyList_Size(names); _i++ ) {
            Python::Identifier* id = new Python::Identifier(PyUnicodeObjectToQString(
                            static_cast<PyObject*>(PyList_GET_ITEM(names, _i))
                    ));
            v->names.append(id);
        }

        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Break)) {
        BreakAst* v = new  BreakAst(parent);
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Continue)) {
        ContinueAst* v = new  ContinueAst(parent);
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Pass)) {
        PassAst* v = new  PassAst(parent);
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Nonlocal)) {
        NonlocalAst* v = new  NonlocalAst(parent);
        result = v;
    }
    else {
        qWarning() << "Unsupported _stmt AST type: " << PyUnicodeObjectToQString(PyObject_Str(node));
        Q_ASSERT(false);
    }

    if ( ! result ) return nullptr;
    if ( ! ranges_copied ) {
        result->startCol = getattr<int>(node, "col_offset");
        result->endCol = getattr<int>(node, "end_col_offset");
        result->startLine = tline(getattr<int>(node, "lineno"));
        result->endLine = tline(getattr<int>(node, "end_lineno"));
        result->hasUsefulRangeInformation = true;
    }
    else {
        result->hasUsefulRangeInformation = true;
    }

    // Walk through the tree and set proper end columns and lines, as the python parser sadly does not do this for us
    if ( result->hasUsefulRangeInformation ) {
        Ast* parent = result->parent;
        while ( parent ) {
            if ( parent->endLine < result->endLine ) {
                parent->endLine = result->endLine;
                parent->endCol = result->endCol;
            }
            if ( ! parent->hasUsefulRangeInformation && parent->startLine == -99999 ) {
                parent->startLine = result->startLine;
                parent->startCol = result->startCol;
            }
            parent = parent->parent;
        }
    }

    if ( result && result->astType == Ast::NameAstType ) {
        NameAst* r = static_cast<NameAst*>(result);
        r->startCol = r->identifier->startCol;
        r->endCol = r->identifier->endCol;
        r->startLine = r->identifier->startLine;
        r->endLine = r->identifier->endLine;
    }
    return result;
}

Ast* AstTransformer::visitKeywordNode(PyObject* node, Ast* parent)
{
    if ( !node || node == Py_None ) return nullptr;
    // qDebug() << "visit keyword: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_keyword));
    KeywordAst* v = new  KeywordAst(parent);
    QString arg = getattr<QString>(node, "arg");
    v->argumentName = arg.size() ? new Python::Identifier(arg) : nullptr;
    {
        PyObject* value = getattr<PyObject*>(node, "value");
        v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        Py_DECREF(value);
    }
    return v;
}


Ast* AstTransformer::visitWithItemNode(PyObject* node, Ast* parent) {
    if ( !node || node == Py_None ) return nullptr;
    // qDebug() << "visit with item: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_withitem));
    WithItemAst* v = new  WithItemAst(parent);
    {
        PyObject* context_expr = getattr<PyObject*>(node, "context_expr");
        v->contextExpression = static_cast<ExpressionAst*>(visitExprNode(context_expr, v));
        Py_DECREF(context_expr);
    }
    {
        PyObject* optional_vars = getattr<PyObject*>(node, "optional_vars");
        v->optionalVars = static_cast<ExpressionAst*>(visitExprNode(optional_vars, v));
        Py_DECREF(optional_vars);
    }
    return v;
}

} // end namespace Python
