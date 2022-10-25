#include "asttransformer.h"
#include "astbuilder.h"

namespace Python
{

template <>
QString AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    PyObject *v = PyObject_GetAttrString(obj, attr);
    // qDebug() << "getattr<str>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr << "v=" << PyUnicodeObjectToQString(PyObject_Str(v));
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
    // qDebug() << "getattr<bool>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr;
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
    // qDebug() << "getattr<int>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr << "v=" << PyUnicodeObjectToQString(PyObject_Str(v));
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
PyObjectRef AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    return getattr<PyObject*>(obj, attr);
}

template <>
ExpressionAst::Context AstTransformer::getattr(PyObject *obj, const char *attr) const
{
    ExpressionAst::Context result;
    PyObject *v = PyObject_GetAttrString(obj, attr);
    // qDebug() << "getattr<expr:ctx>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr<< "ctx: " << PyUnicodeObjectToQString(PyObject_Str(v));
    Q_ASSERT(v); // attr missing
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
    // qDebug() << "getattr<expr:ctx>: " << PyUnicodeObjectToQString(PyObject_Str(obj)) << "." << attr<< "op: " << PyUnicodeObjectToQString(PyObject_Str(op));
    Q_ASSERT(op); // attr missing
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
        PyObjectRef body = getattr<PyObjectRef>(node, "body");
        ast->body = visitNodeList<Ast>(body, ast);
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
    if (PyObject_IsInstance(node, grammar.ast_slice))
        return visitSliceNode(node, parent);
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
        PyObjectRef annotation = getattr<PyObjectRef>(node, "annotation");
        v->annotation = static_cast<ExpressionAst*>(visitExprNode(annotation, v));
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
        PyObjectRef vararg = getattr<PyObjectRef>(node, "vararg");
        v->vararg = static_cast<ArgAst*>(visitArgNode(vararg, v));
    }
    {
        PyObjectRef kwarg = getattr<PyObjectRef>(node, "kwarg");
        v->kwarg = static_cast<ArgAst*>(visitArgNode(kwarg, v));
    }
    {
        PyObjectRef args = getattr<PyObjectRef>(node, "args");
        v->arguments = visitNodeList<ArgAst>(args, v);
    }

    {
        PyObjectRef defaults = getattr<PyObjectRef>(node, "defaults");
        v->defaultValues = visitNodeList<ExpressionAst>(defaults, v);
    }

    {
        PyObjectRef kwonlyargs = getattr<PyObjectRef>(node, "kwonlyargs");
        v->kwonlyargs = visitNodeList<ArgAst>(kwonlyargs, v);
    }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    {
        PyObjectRef posonlyargs = getattr<PyObjectRef>(node, "posonlyargs");
        v->posonlyargs = visitNodeList<ArgAst>(posonlyargs, v);
    }

    // TODO: kw_defaults?
    //{
    //    PyObject *kw_defaults = getattr<PyObjectRef>(node, "kw_defaults");
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
        PyObjectRef target = getattr<PyObjectRef>(node, "target");
        v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
    }
    {
        PyObjectRef iter = getattr<PyObjectRef>(node, "iter");
        v->iterator = static_cast<ExpressionAst*>(visitExprNode(iter, v));
    }
    {
        PyObjectRef ifs = getattr<PyObjectRef>(node, "ifs");
        v->conditions = visitNodeList<ExpressionAst>(ifs, v);
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
        PyObjectRef type = getattr<PyObjectRef>(node, "type");
        v->type = static_cast<ExpressionAst*>(visitExprNode(type, v));
    }
    bool ranges_copied = false;
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
        ranges_copied = true;
    } else {
        v->name = nullptr;
    }

    {
        PyObjectRef body = getattr<PyObjectRef>(node, "body");
        v->body = visitNodeList<Ast>(body, v);
    }
    updateRanges(node, v, ranges_copied);
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
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_BoolOp)) {
        BooleanOperationAst* v = new  BooleanOperationAst(parent);
        {
            PyObjectRef op = getattr<PyObjectRef>(node, "op");
            if (PyObject_IsInstance(op, grammar.ast_And))
                v->type = Ast::BooleanAnd;
            else if (PyObject_IsInstance(op, grammar.ast_Or))
                v->type = Ast::BooleanOr;
            else
                v->type = Ast::BooleanInvalidOperation;
        }
        {
            PyObjectRef values = getattr<PyObjectRef>(node, "values");
            v->values = visitNodeList<ExpressionAst>(values, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_BinOp)) {
        BinaryOperationAst* v = new  BinaryOperationAst(parent);
        v->type = getattr<Ast::OperatorTypes>(node, "op");
        {
            PyObjectRef left = getattr<PyObjectRef>(node, "left");
            v->lhs = static_cast<ExpressionAst*>(visitExprNode(left, v));
        }
        {
            PyObjectRef right = getattr<PyObjectRef>(node, "right");
            v->rhs = static_cast<ExpressionAst*>(visitExprNode(right, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_UnaryOp)) {
        UnaryOperationAst* v = new  UnaryOperationAst(parent);
        {
            PyObjectRef op = getattr<PyObjectRef>(node, "op");
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
        }
        {
            PyObjectRef operand = getattr<PyObjectRef>(node, "operand");
            v->operand = static_cast<ExpressionAst*>(visitExprNode(operand, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Lambda)) {
        LambdaAst* v = new  LambdaAst(parent);
        {
            PyObjectRef args = getattr<PyObjectRef>(node, "args");
            v->arguments = static_cast<ArgumentsAst*>(visitArgumentsNode(args, v));
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = static_cast<ExpressionAst*>(visitExprNode(body, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_IfExp)) {
        IfExpressionAst* v = new  IfExpressionAst(parent);
        {
            PyObjectRef test = getattr<PyObjectRef>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = static_cast<ExpressionAst*>(visitExprNode(body, v));
        }
        {
            PyObjectRef orelse = getattr<PyObjectRef>(node, "orelse");
            v->orelse = static_cast<ExpressionAst*>(visitExprNode(orelse, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Dict)) {
        DictAst* v = new  DictAst(parent);
        {
            PyObjectRef keys = getattr<PyObjectRef>(node, "keys");
            v->keys = visitNodeList<ExpressionAst>(keys, v);
        }
        {
            PyObjectRef values = getattr<PyObjectRef>(node, "values");
            v->values = visitNodeList<ExpressionAst>(values, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Set)) {
        SetAst* v = new  SetAst(parent);
        {
            PyObjectRef elts = getattr<PyObjectRef>(node, "elts");
            v->elements = visitNodeList<ExpressionAst>(elts, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_ListComp)) {
        ListComprehensionAst* v = new  ListComprehensionAst(parent);
        {
            PyObjectRef elt = getattr<PyObjectRef>(node, "elt");
            v->element = static_cast<ExpressionAst*>(visitExprNode(elt, v));
        }
        {
            PyObjectRef generators = getattr<PyObjectRef>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_SetComp)) {
        SetComprehensionAst* v = new  SetComprehensionAst(parent);
        {
            PyObjectRef elt = getattr<PyObjectRef>(node, "elt");
            v->element = static_cast<ExpressionAst*>(visitExprNode(elt, v));
        }
        {
            PyObjectRef generators = getattr<PyObjectRef>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_DictComp)) {
        DictionaryComprehensionAst* v = new  DictionaryComprehensionAst(parent);
        {
            PyObjectRef key = getattr<PyObjectRef>(node, "key");
            v->key = static_cast<ExpressionAst*>(visitExprNode(key, v));
        }
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        {
            PyObjectRef generators = getattr<PyObjectRef>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_GeneratorExp)) {
        GeneratorExpressionAst* v = new  GeneratorExpressionAst(parent);
        {
            PyObjectRef elt = getattr<PyObjectRef>(node, "elt");
            v->element = static_cast<ExpressionAst*>(visitExprNode(elt, v));
        }
        {
            PyObjectRef generators = getattr<PyObjectRef>(node, "generators");
            v->generators = visitNodeList<ComprehensionAst>(generators, v);

        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Yield)) {
        YieldAst* v = new  YieldAst(parent);
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Compare)) {
        CompareAst* v = new  CompareAst(parent);
        {
            PyObjectRef left = getattr<PyObjectRef>(node, "left");
            v->leftmostElement = static_cast<ExpressionAst*>(visitExprNode(left, v));
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
            PyObjectRef comparators = getattr<PyObjectRef>(node, "comparators");
            v->comparands = visitNodeList<ExpressionAst>(comparators, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Call)) {
        CallAst* v = new  CallAst(parent);
        {
            PyObjectRef func = getattr<PyObjectRef>(node, "func");
            v->function = static_cast<ExpressionAst*>(visitExprNode(func, v));
        }
        {
            PyObjectRef args = getattr<PyObjectRef>(node, "args");
            v->arguments = visitNodeList<ExpressionAst>(args, v);
        }
        {
            PyObjectRef keywords = getattr<PyObjectRef>(node, "keywords");
            v->keywords = visitNodeList<KeywordAst>(keywords, v);
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
            PyObjectRef n = getattr<PyObjectRef>(node, "n");
            v->isInt = PyLong_Check(n);
            v->value = PyLong_AsLong(n);
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
            PyObjectRef values = getattr<PyObjectRef>(node, "values");
            v->values = visitNodeList<ExpressionAst>(values, v);
        }
        result = v;
    }
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    else if (PyObject_IsInstance(node, grammar.ast_FormattedValue)) {
        FormattedValueAst* v = new  FormattedValueAst(parent);
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));

        }
        v->conversion = getattr<int>(node, "conversion");
        {
            PyObjectRef format_spec = getattr<PyObjectRef>(node, "format_spec");
            v->formatSpec = static_cast<ExpressionAst*>(visitExprNode(format_spec, v));
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
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Subscript)) {
        SubscriptAst* v = new  SubscriptAst(parent);
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        {
            PyObjectRef slice = getattr<PyObjectRef>(node, "slice");
            v->slice = static_cast<SliceAst*>(visitNode(slice, v));
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Starred)) {
        StarredAst* v = new  StarredAst(parent);
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
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
            PyObjectRef elts = getattr<PyObjectRef>(node, "elts");
            v->elements = visitNodeList<ExpressionAst>(elts, v);
        }
        v->context = getattr<ExpressionAst::Context>(node, "ctx");
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Tuple)) {
        TupleAst* v = new  TupleAst(parent);
        {
            PyObjectRef elts = getattr<PyObjectRef>(node, "elts");
            v->elements = visitNodeList<ExpressionAst>(elts, v);
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
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            if (value == Py_None)
                v->value = NameConstantAst::None;
            else if (value == Py_false)
                v->value = NameConstantAst::False;
            else
                v->value = NameConstantAst::True;
        }
        result = v;
    }
#endif
    else if (PyObject_IsInstance(node, grammar.ast_YieldFrom)) {
        YieldFromAst* v = new  YieldFromAst(parent);
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
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
            PyObjectRef target = getattr<PyObjectRef>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
        }
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        result = v;
    }
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 9, 0)
    else if (PyObject_IsInstance(node, grammar.ast_Slice)) {
        SliceAst* v = new  SliceAst(parent);
        {
            PyObjectRef lower = getattr<PyObjectRef>(node, "lower");
            v->lower = static_cast<ExpressionAst*>(visitExprNode(lower, v));
        }
        {
            PyObjectRef upper = getattr<PyObjectRef>(node, "upper");
            v->upper = static_cast<ExpressionAst*>(visitExprNode(upper, v));
        }
        {
            PyObjectRef step = getattr<PyObjectRef>(node, "step");
            v->step = static_cast<ExpressionAst*>(visitExprNode(step, v));
        }
        result = v;
    }
#endif
    else {
        qWarning() << "Unsupported _expr AST type: " << PyUnicodeObjectToQString(PyObject_Str(node));
        Q_ASSERT(false);
    }

    if ( ! result ) return nullptr;
    updateRanges(node, result, ranges_copied);
    return result;
}


Ast* AstTransformer::visitSliceNode(PyObject* node, Ast* parent)
{
    if ( ! node || node == Py_None ) return nullptr;
    // qDebug() << "visit slice: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_slice));
    Ast* result = nullptr;
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 9, 0)
    if (PyObject_IsInstance(node, grammar.ast_Slice)) {
        SliceAst* v = new  SliceAst(parent);
        {
            PyObjectRef lower = getattr<PyObjectRef>(node, "lower");
            v->lower = static_cast<ExpressionAst*>(visitExprNode(lower, v));
        }
        {
            PyObjectRef upper = getattr<PyObjectRef>(node, "upper");
            v->upper = static_cast<ExpressionAst*>(visitExprNode(upper, v));
        }
        {
            PyObjectRef step = getattr<PyObjectRef>(node, "step");
            v->step = static_cast<ExpressionAst*>(visitExprNode(step, v));
        }
        result = v;
    }
#endif
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 9, 0)
    if (PyObject_IsInstance(node, grammar.ast_ExtSlice)) {
        TupleAst* v = new  TupleAst(parent);
        {
            PyObjectRef dims = getattr<PyObjectRef>(node, "dims");
            v->elements = visitNodeList<ExpressionAst>(dims, parent);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Index)) {
        PyObjectRef value = getattr<PyObjectRef>(node, "value");
        return visitNode(value, parent);
    }
#endif
    else {
        qWarning() << "Unsupported _slice AST type: " << PyUnicodeObjectToQString(PyObject_Str(node));
        Q_ASSERT(false);
    }
    updateRanges(node, result, false);
    return result;
}

Ast* AstTransformer::visitStmtNode(PyObject* node, Ast* parent)
{
    if ( !node || node == Py_None ) return nullptr;
    // qDebug() << "visit stmt: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_stmt));
    bool ranges_copied = false;
    Ast* result = nullptr;
    if (PyObject_IsInstance(node, grammar.ast_Expr)) {
        ExpressionAst* v = new  ExpressionAst(parent);
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
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
            PyObjectRef args = getattr<PyObjectRef>(node, "args");
            v->arguments = static_cast<ArgumentsAst*>(visitArgumentsNode(args, v));
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
        }
        {
            PyObjectRef decorator_list = getattr<PyObjectRef>(node, "decorator_list");
            v->decorators = visitNodeList<ExpressionAst>(decorator_list, v);
        }
        {
            PyObjectRef returns = getattr<PyObjectRef>(node, "returns");
            v->returns = static_cast<ExpressionAst*>(visitExprNode(returns, v));
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
            PyObjectRef bases = getattr<PyObjectRef>(node, "bases");
            v->baseClasses = visitNodeList<ExpressionAst>(bases, v);
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
        }
        {
            PyObjectRef decorator_list = getattr<PyObjectRef>(node, "decorator_list");
            v->decorators = visitNodeList<ExpressionAst>(decorator_list, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Return)) {
        ReturnAst* v = new  ReturnAst(parent);
        PyObjectRef value = getattr<PyObjectRef>(node, "value");
        v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Delete)) {
        DeleteAst* v = new  DeleteAst(parent);
        PyObjectRef targets = getattr<PyObjectRef>(node, "targets");
        v->targets = visitNodeList<ExpressionAst>(targets, v);
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Assign)) {
        AssignmentAst* v = new  AssignmentAst(parent);
        {
            PyObjectRef targets = getattr<PyObjectRef>(node, "targets");
            v->targets = visitNodeList<ExpressionAst>(targets, v);
        }
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_AugAssign)) {
        AugmentedAssignmentAst* v = new  AugmentedAssignmentAst(parent);
        {
            PyObjectRef target = getattr<PyObjectRef>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
        }
        v->op = getattr<Ast::OperatorTypes>(node, "op");
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
        }
        result = v;
    }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    else if (PyObject_IsInstance(node, grammar.ast_AnnAssign)) {
        AnnotationAssignmentAst* v = new  AnnotationAssignmentAst(parent);
        {
            PyObjectRef target = getattr<PyObjectRef>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
        }
        {
            PyObjectRef annotation = getattr<PyObjectRef>(node, "annotation");
            v->annotation = static_cast<ExpressionAst*>(visitExprNode(annotation, v));
        }
        {
            PyObjectRef value = getattr<PyObjectRef>(node, "value");
            v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
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
            PyObjectRef target = getattr<PyObjectRef>(node, "target");
            v->target = static_cast<ExpressionAst*>(visitExprNode(target, v));
        }
        {
            PyObjectRef iter = getattr<PyObjectRef>(node, "iter");
            v->iterator = static_cast<ExpressionAst*>(visitExprNode(iter, v));
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
        }
        {
            PyObjectRef orelse = getattr<PyObjectRef>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
        }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        v->async = PyObject_IsInstance(node, grammar.ast_AsyncFor);
#endif
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_While)) {
        WhileAst* v = new  WhileAst(parent);
        {
            PyObjectRef test = getattr<PyObjectRef>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
        }
        {
            PyObjectRef orelse = getattr<PyObjectRef>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_If)) {
        IfAst* v = new  IfAst(parent);
        {
            PyObjectRef test = getattr<PyObjectRef>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
        }
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
        }
        {
            PyObjectRef orelse = getattr<PyObjectRef>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
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
                PyObjectRef body = getattr<PyObjectRef>(node, "body");
                v->body = visitNodeList<Ast>(body, v);
            }
            {
                PyObjectRef items = getattr<PyObjectRef>(node, "items");
                v->items = visitNodeList<WithItemAst>(items, v);
            }
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
            v->async = PyObject_IsInstance(node, grammar.ast_AsyncWith);
#endif
            result = v;
    }

    else if (PyObject_IsInstance(node, grammar.ast_Raise)) {
        RaiseAst* v = new  RaiseAst(parent);
        {
            PyObjectRef exc = getattr<PyObjectRef>(node, "exc");
            v->type = static_cast<ExpressionAst*>(visitExprNode(exc, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Try)) {
        TryAst* v = new  TryAst(parent);
        {
            PyObjectRef body = getattr<PyObjectRef>(node, "body");
            v->body = visitNodeList<Ast>(body, v);
        }
        {
            PyObjectRef handlers = getattr<PyObjectRef>(node, "handlers");
            v->handlers = visitNodeList<ExceptionHandlerAst>(handlers, v);

        }
        {
            PyObjectRef orelse = getattr<PyObjectRef>(node, "orelse");
            v->orelse = visitNodeList<Ast>(orelse, v);
        }
        {
            PyObjectRef finalbody = getattr<PyObjectRef>(node, "finalbody");
            v->finally = visitNodeList<Ast>(finalbody, v);
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Assert)) {
        AssertionAst* v = new  AssertionAst(parent);
        {
            PyObjectRef test = getattr<PyObjectRef>(node, "test");
            v->condition = static_cast<ExpressionAst*>(visitExprNode(test, v));
        }
        {
            PyObjectRef msg = getattr<PyObjectRef>(node, "msg");
            v->message = static_cast<ExpressionAst*>(visitExprNode(msg, v));
        }
        result = v;
    }
    else if (PyObject_IsInstance(node, grammar.ast_Import)) {
        ImportAst* v = new  ImportAst(parent);
        {
            PyObjectRef names = getattr<PyObjectRef>(node, "names");
            v->names = visitNodeList<AliasAst>(names, v);
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
            PyObjectRef names = getattr<PyObjectRef>(node, "names");
            v->names = visitNodeList<AliasAst>(names, v);
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
        Py_DECREF(names);

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
    updateRanges(node, result, ranges_copied);
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
        PyObjectRef value = getattr<PyObjectRef>(node, "value");
        v->value = static_cast<ExpressionAst*>(visitExprNode(value, v));
    }
    return v;
}


Ast* AstTransformer::visitWithItemNode(PyObject* node, Ast* parent)
{
    if ( !node || node == Py_None ) return nullptr;
    // qDebug() << "visit with item: " << PyUnicodeObjectToQString(PyObject_Str(node));
    Q_ASSERT(PyObject_IsInstance(node, grammar.ast_withitem));
    WithItemAst* v = new  WithItemAst(parent);
    {
        PyObjectRef context_expr = getattr<PyObjectRef>(node, "context_expr");
        v->contextExpression = static_cast<ExpressionAst*>(visitExprNode(context_expr, v));
    }
    {
        PyObjectRef optional_vars = getattr<PyObjectRef>(node, "optional_vars");
        v->optionalVars = static_cast<ExpressionAst*>(visitExprNode(optional_vars, v));
    }
    return v;
}


void AstTransformer::updateRanges(PyObject* node, Ast* result, bool ranges_copied)
{
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
}

} // end namespace Python
