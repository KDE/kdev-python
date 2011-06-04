#!/usr/bin/env python

# Transforms a conversion definition file (.sdef) into C++ code. To be copied over manually. :)
# sdef example line:
# RULE_FOR _stmt;KIND Expr_kind;ACTIONS create|ExpressionAst set|value->ExpressionAst,value;CODE;;

contents = open('python26.sdef').read().replace("\n", "").split(';;')

func_structure = '''
    Ast* visitNode(%{RULE_FOR}* node) {
        if ( ! node ) return 0;
        bool ranges_copied = false; Q_UNUSED(ranges_copied);
        Ast* result = 0;
        switch ( node->kind ) {
%{SWITCH_LINES}
        default:
            kWarning() << "Unsupported statement AST type: " << node->kind;
            Q_ASSERT(false);
        }
%{APPENDIX}
        NameAst* r = dynamic_cast<NameAst*>(result);
        if ( r ) {
            r->startCol = r->identifier->startCol;
            r->endCol = r->identifier->endCol;
            r->startLine = r->identifier->startLine;
            r->endLine = r->identifier->endLine;
        }
        return result;
    }
'''

simple_func_structure = '''
    Ast* visitNode(%{RULE_FOR}* node) {
        bool ranges_copied = false; Q_UNUSED(ranges_copied);
        if ( ! node ) return 0; // return a nullpointer if no node is set, that's fine, everyone else will check for that.
%{SWITCH_LINES}
        return v;
    }
'''

switch_line = '''        case %{KIND}: {
%{ACTIONS}
                result = v;
                break;
            }'''

create_ast_line = '''                %{AST_TYPE}* v = new %{AST_TYPE}(parent());'''
create_identifier_line = '''                v->%{TARGET} = node->v.%{KIND_W/O_SUFFIX}.%{VALUE} ? new Python::Identifier(PyString_AsString(PyObject_Str(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}))) : 0;'''
set_attribute_line = '''                nodeStack.push(v); v->%{TARGET} = static_cast<%{AST_TYPE}*>(visitNode(node->v.%{KIND_W/O_SUFFIX}.%{VALUE})); nodeStack.pop();'''
resolve_list_line = '''                nodeStack.push(v); v->%{TARGET} = visitNodeList<%{PYTHON_AST_TYPE}, %{AST_TYPE}>(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}); nodeStack.pop();'''
create_identifier_line_any = '''            v->%{TARGET} = node->%{VALUE} ? new Python::Identifier(PyString_AsString(PyObject_Str(node->%{VALUE}))) : 0;'''
set_attribute_line_any = '''            nodeStack.push(v); v->%{TARGET} = static_cast<%{AST_TYPE}*>(visitNode(node->%{VALUE})); nodeStack.pop();'''
resolve_list_line_any = '''            nodeStack.push(v); v->%{TARGET} = visitNodeList<%{PYTHON_AST_TYPE}, %{AST_TYPE}>(node->%{VALUE}); nodeStack.pop();'''
direct_assignment_line = '''                v->%{TARGET} = node->v.%{KIND_W/O_SUFFIX}.%{VALUE};'''
direct_assignment_line_any = '''                v->%{TARGET} = node->v.%{VALUE};'''
cast_operator_line = '''                v->%{TARGET} = (ExpressionAst::%{AST_TYPE}) node->v.%{KIND_W/O_SUFFIX}.%{VALUE};'''
resolve_string = '''                v->%{TARGET} = PyString_AsString(PyObject_Str(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}));'''
assign_mindless = '''              v->%{TARGET} = node->%{VALUE};'''
resolve_oplist_block = '''
                for ( int _i = 0; _i < node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->size; _i++ ) {
                    v->%{TARGET}.append((ExpressionAst::%{AST_TYPE}) node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->elements[_i]);
                }
'''
resolve_identifier_block = '''
                for ( int _i = 0; _i < node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->size; _i++ ) {
                    Python::Identifier* id = new Python::Identifier(PyString_AsString(PyObject_Str(
                                    static_cast<PyObject*>(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->elements[_i])
                            )));
                    v->%{TARGET}.append(id);
                }
'''

copy_ident_ranges = '''
                if ( v->%{TARGET} ) {
                    v->%{TARGET}->startCol = node->col_offset; v->startCol = v->%{TARGET}->startCol;
                    v->%{TARGET}->startLine = node->lineno - 1;  v->startLine = v->%{TARGET}->startLine;
                    v->%{TARGET}->endCol = node->col_offset + v->%{TARGET}->value.length() - 1;  v->endCol = v->%{TARGET}->endCol;
                    v->%{TARGET}->endLine = node->lineno - 1;  v->endLine = v->%{TARGET}->endLine;
                    ranges_copied = true;
                }'''

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
    code = False
    if len(outline) > 3:
        code = ' '.join(outline[3].split(' ')[1:]) + ";"
    
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
            if commandType in ['~', ':', '$', '+']:
                if commandType == ':':
                    raw = direct_assignment_line if not any else direct_assignment_line_any
                if commandType == '~':
                    raw = create_identifier_line if not any else create_identifier_line_any
                    if rule_for in ['_expr', '_stmt', '_excepthandler', '_alias']:
                        raw += copy_ident_ranges
                if commandType == '$':
                    raw = resolve_string
                if commandType == '+':
                    raw = assign_mindless;
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
    
    if code:
        current_actions.append(code);
    
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
    void run(mod_ty syntaxtree, QString moduleName) {
        ast = new CodeAst();
        ast->name = new Identifier(moduleName);
        nodeStack.push(ast);
        ast->body = visitNodeList<_stmt, Ast>(syntaxtree->v.Module.body);
        nodeStack.pop();
        Q_ASSERT(nodeStack.isEmpty());
    }
private:
    QStack<Ast*> nodeStack;
    
    Ast* parent() {
        return nodeStack.top();
    }
    
    template<typename T, typename K> QList<K*> visitNodeList(asdl_seq* node) {
        QList<K*> nodelist;
        if ( ! node ) return nodelist;
        for ( int i=0; i < node->size; i++ ) {
            T* currentNode = static_cast<T*>(node->elements[i]);
            Q_ASSERT(currentNode);
            Ast* result = visitNode(currentNode);
            K* transformedNode = static_cast<K*>(result);
            nodelist.append(transformedNode);
        }
        return nodelist;
    }

'''

for index, lines in results.iteritems():
    current_switch_lines = "\n".join(lines)
    appendix = ''
    if index == '_expr' or index == '_stmt':
        appendix = '''
	if ( ! result ) return 0;
        if ( ! ranges_copied ) {
            result->startCol = node->col_offset;
            result->endCol = node->col_offset;
            result->startLine = node->lineno - 1;
            result->endLine = node->lineno - 1;
            result->hasUsefulRangeInformation = true;
        }
        else {
            result->hasUsefulRangeInformation = true;
        }
        '''
    appendix += '''
        // Walk through the tree and set proper end columns and lines, as the python parser sadly does not do this for us
        if ( result->hasUsefulRangeInformation ) {
            Ast* parent = result->parent;
            while ( parent ) {
                if ( parent->endLine < result->endLine ) {
                    parent->endLine = result->endLine;
                    parent->endCol = result->endCol;
                }
                if ( ! parent->hasUsefulRangeInformation && parent->startLine == -5 ) {
                    parent->startLine = result->startLine;
                    parent->startCol = result->startCol;
                }
                parent = parent->parent;
            }
        }
    '''
    if not does_match_any[index]:
        func = func_structure.replace('%{RULE_FOR}', index).replace('%{SWITCH_LINES}', current_switch_lines).replace('%{APPENDIX}', appendix)
    else:
        func = simple_func_structure.replace('%{RULE_FOR}', index).replace('%{SWITCH_LINES}', current_switch_lines)
    print func

print '''};

/*
 * End generated code
 */
'''
