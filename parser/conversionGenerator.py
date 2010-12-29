#!/usr/bin/env python

# Transforms a conversion definition file (.sdef) into C++ code. To be copied over manually. :)
# sdef example line:
# RULE_FOR _stmt;KIND Expr_kind;ACTIONS create|ExpressionAst set|value->ExpressionAst,value;CODE;;

contents = open('python26.sdef').read().replace("\n", "").split(';;')

func_structure = '''
    Ast* visitNode(%{RULE_FOR}* node) {
        switch ( node->kind ) {
%{SWITCH_LINES}
        default:
            kWarning() << "Unsupported statement AST type: " << node->kind;
            Q_ASSERT(false);
        }
        return 0; // this will never be reached, but avoids gcc warnings
    }
'''

simple_func_structure = '''
    Ast* visitNode(%{RULE_FOR}* node) {
%{SWITCH_LINES}
        return 0; // this will never be reached, but avoids gcc warnings
    }
'''

switch_line = '''        case %{KIND}: {
%{ACTIONS}
                return v;
            }'''

create_ast_line = '''                %{AST_TYPE}* v = new %{AST_TYPE}(parent());'''
create_identifier_line = '''                v->%{TARGET} = new Python::Identifier(PyString_AsString(PyObject_Str(node->v.%{KIND_W/O_SUFFIX}.%{VALUE})));'''
set_attribute_line = '''                v->%{TARGET} = dynamic_cast<%{AST_TYPE}*>(visitNode(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}));'''
resolve_list_line = '''                v->%{TARGET} = visitNodeList<%{PYTHON_AST_TYPE}, %{AST_TYPE}>(node->v.%{KIND_W/O_SUFFIX}.%{VALUE});'''
create_identifier_line_any = '''            v->%{TARGET} = new Python::Identifier(PyString_AsString(PyObject_Str(node->%{VALUE})));'''
set_attribute_line_any = '''            v->%{TARGET} = dynamic_cast<%{AST_TYPE}*>(visitNode(node->%{VALUE}));'''
resolve_list_line_any = '''            v->%{TARGET} = visitNodeList<%{PYTHON_AST_TYPE}, %{AST_TYPE}>(node->%{VALUE});'''
direct_assignment_line = '''                v->%{TARGET} = node->v.%{KIND_W/O_SUFFIX}.%{VALUE};'''
direct_assignment_line_any = '''                v->%{TARGET} = node->v.%{VALUE};'''
cast_operator_line = '''                v->%{TARGET} = (ExpressionAst::%{AST_TYPE}) node->v.%{KIND_W/O_SUFFIX}.%{VALUE};'''
resolve_oplist_block = '''
                for ( int _i = 0; _i < node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->size; _i++ ) {
                    v->%{TARGET}.append((ExpressionAst::%{AST_TYPE}) node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->elements[_i]);
                }
'''
resolve_identifier_block = '''
                for ( int _i = 0; _i < node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->size; _i++ ) {
                    Python::Identifier* id = new Python::Identifier(PyString_AsString(PyObject_Str(
                                    reinterpret_cast<PyObject*>(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->elements[_i])
                            )));
                    v->%{TARGET}.append(id);
                }
'''

results = dict()
does_match_any = dict()

def pluginAstToPythonAstType(plugintypestr):
    if plugintypestr == 'ExpressionAst': return '_expr'
    if plugintypestr == 'StatementAst' : return '_stmt'
    if plugintypestr == 'NameAst': return '_expr'
    if plugintypestr == 'ExceptionHandlerAst': return '_excepthandler'
    if plugintypestr == 'ComprehensionAst': return '_comprehension'
    if plugintypestr == 'KeywordAst': return '_keyword'
    if plugintypestr == 'ArgumentsAst': return '_arguments'
    if plugintypestr == 'AliasAst': return '_alias'
    if plugintypestr == 'SliceAst': return '_slice'
    if plugintypestr == 'Ast': return '_stmt' # not sure about this
    else: return '<ERROR>'

for rule in contents:
    outline = rule.split(';')
    command = outline[0]
    if command[:7] == 'COMMENT' or command == '':
        continue
    elif command[:7] != 'RULE_FO':
        raise SyntaxError('Invalid syntax in sdef file, line: ' + rule)
    
    rule_for = outline[0].split(' ')[1]
    kind = outline[1].split(' ')[1]
    kind_wo_suffix = kind.replace('_kind', '')
    actions = outline[2].split(' ')[1:]
    
    if not results.has_key(rule_for):
        results[rule_for] = list()
    
    current_actions = list()
    for action in actions:
        command = action.split('|')[0]
        try:
            arguments = action.split('|')[1]
        except IndexError:
            continue
        action = '<ERROR>'
        if command == 'set':
            s = arguments.split('>')
            commandType = s[0][-1] # -, ~, =, : , *, #
            target = s[0][:-1]
            s = s[1].split(',')
            raw = False
            
            if kind == 'any': any = True
            else: any = False
            
            
            # commands with one argument
            if commandType == '~' or commandType == ':':
                if commandType == ':':
                    raw = direct_assignment_line if not any else direct_assignment_line_any
                if commandType == '~':
                    raw = create_identifier_line if not any else create_identifier_line_any
                value = s[0]
            # commands with two arguments
            else:
                astType = s[0]
                try:
                    value = s[1]
                except IndexError:
                    raise SyntaxError('Missing argument for operator ' + commandType + ' in rule: ' + rule)
                if commandType == '=':
                    if astType == 'Identifier':
                        raw = resolve_identifier_block
                    else:
                        raw = resolve_list_line if not any else resolve_list_line_any
                if commandType == '-':
                    raw = set_attribute_line if not any else set_attribute_line_any
                if commandType == '*':
                    raw = cast_operator_line
                if commandType == '#':
                    raw = resolve_oplist_block
            
            if raw:
                command = raw.replace('%{AST_TYPE}', astType).replace('%{TARGET}', target) \
                             .replace('%{PYTHON_AST_TYPE}', pluginAstToPythonAstType(astType)) \
                             .replace('%{KIND_W/O_SUFFIX}', kind_wo_suffix).replace('%{VALUE}', value)
            else: command = '<MISSING RAW>'
            
            current_actions.append(command)
            
        elif command == 'create':
            astType = arguments
            current_actions.append(create_ast_line.replace('%{AST_TYPE}', astType))
    
    current_actions = "\n".join(current_actions)
    if kind == 'any':
        current_stmt = current_actions
    else:
        current_stmt = switch_line.replace('%{KIND}', kind).replace('%{ACTIONS}', current_actions)
    results[rule_for].append(current_stmt)
    does_match_any[rule_for] = any

print '''/* This code is generated by conversiongenerator.py.
 * I do not recommend editing it.
 */
    
class PythonAstTransformer {
public:
    CodeAst* ast;
    void run(mod_ty syntaxtree) {
        ast = new CodeAst();
        nodeStack.push(ast);
        ast->body = visitNodeList<_expr, Ast>(syntaxtree->v.Module.body);
    }
private:
    QStack<Ast*> nodeStack;
    
    Ast* parent() {
        return nodeStack.top();
    }
    
    template<typename T, typename K> QList<K*> visitNodeList(asdl_seq* node) {
        QList<K*> nodelist;
        for ( int i=0; i < node->size; i++ ) {
            T* currentNode = reinterpret_cast<T*>(node->elements[i]);
            Q_ASSERT(currentNode);
            K* transformedNode = dynamic_cast<K*>(visitNode(currentNode));
            Q_ASSERT(transformedNode);
            nodelist.append(transformedNode);
        }
        return nodelist;
    }

'''

for index, lines in results.iteritems():
    current_switch_lines = "\n".join(lines)
    if not does_match_any[index]:
        func = func_structure.replace('%{RULE_FOR}', index).replace('%{SWITCH_LINES}', current_switch_lines)
    else:
        func = simple_func_structure.replace('%{RULE_FOR}', index).replace('%{SWITCH_LINES}', current_switch_lines)
    print func

print '''};

/*
 * End generated code
 */
'''
