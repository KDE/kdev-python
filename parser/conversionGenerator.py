#!/usr/bin/env python

# Copyright 2014 by Sven Brauch
# License: GPL v2+

# Transforms a conversion definition file (.sdef) into C++ code. To be copied over manually. :)
# sdef example line:
# RULE_FOR _stmt;KIND Expr_kind;ACTIONS create|ExpressionAst set|value->ExpressionAst,value;CODE;;

import sys

contents = open('python39.sdef').read().replace("\n", "").split(';;')

func_structure = '''
    Ast* visitNode(%{RULE_FOR}* node) {
        if ( ! node ) return nullptr;
        bool ranges_copied = false; Q_UNUSED(ranges_copied);
        Ast* result = nullptr;
        switch ( node->kind ) {
%{SWITCH_LINES}
        default:
            qWarning() << "Unsupported %{RULE_FOR} AST type: " << node->kind;
            Q_ASSERT(false);
        }
%{APPENDIX}
        if ( result && result->astType == Ast::NameAstType ) {
            NameAst* r = static_cast<NameAst*>(result);
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
        if ( ! node ) return nullptr;
%{SWITCH_LINES}
        return v;
    }
'''

switch_line = '''        case %{KIND}: {
%{ACTIONS}
                break;
            }'''

create_ast_line = '''                %{AST_TYPE}* v = new  %{AST_TYPE}(parent());'''
create_identifier_line = '''                v->%{TARGET} = node->v.%{KIND_W/O_SUFFIX}.%{VALUE} ? new Python::Identifier(PyUnicodeObjectToQString(node->v.%{KIND_W/O_SUFFIX}.%{VALUE})) : nullptr;'''
set_attribute_line = '''                nodeStack.push(v); v->%{TARGET} = static_cast<%{AST_TYPE}*>(visitNode(node->v.%{KIND_W/O_SUFFIX}.%{VALUE})); nodeStack.pop();'''
resolve_list_line = '''                nodeStack.push(v); v->%{TARGET} = visitNodeList<%{PYTHON_AST_TYPE}, %{AST_TYPE}>(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}); nodeStack.pop();'''
create_identifier_line_any = '''            v->%{TARGET} = node->%{VALUE} ? new Python::Identifier(PyUnicodeObjectToQString(node->%{VALUE})) : nullptr;'''
set_attribute_line_any = '''            nodeStack.push(v); v->%{TARGET} = static_cast<%{AST_TYPE}*>(visitNode(node->%{VALUE})); nodeStack.pop();'''
resolve_list_line_any = '''            nodeStack.push(v); v->%{TARGET} = visitNodeList<%{PYTHON_AST_TYPE}, %{AST_TYPE}>(node->%{VALUE}); nodeStack.pop();'''
direct_assignment_line = '''                v->%{TARGET} = node->v.%{KIND_W/O_SUFFIX}.%{VALUE};'''
direct_assignment_line_any = '''                v->%{TARGET} = node->v.%{VALUE};'''
cast_operator_line = '''                v->%{TARGET} = (ExpressionAst::%{AST_TYPE}) node->v.%{KIND_W/O_SUFFIX}.%{VALUE};'''
resolve_string = '''                v->%{TARGET} = PyUnicodeObjectToQString(node->v.%{KIND_W/O_SUFFIX}.%{VALUE});'''
assign_mindless = '''              v->%{TARGET} = node->%{VALUE};'''
assign_linetransform = '''              v->%{TARGET} = tline(node->%{VALUE} - 1);'''
singleton_convert_line = '''                v->%{TARGET} = node->v.NameConstant.value == Py_None ? NameConstantAst::None : node->v.NameConstant.value == Py_False ? NameConstantAst::False : NameConstantAst::True;'''
resolve_oplist_block = '''
                for ( int _i = 0; _i < node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->size; _i++ ) {
                    v->%{TARGET}.append((ExpressionAst::%{AST_TYPE}) node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->elements[_i]);
                }
'''
resolve_identifier_block = '''
                for ( int _i = 0; _i < node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->size; _i++ ) {
                    Python::Identifier* id = new Python::Identifier(PyUnicodeObjectToQString(
                                    static_cast<PyObject*>(node->v.%{KIND_W/O_SUFFIX}.%{VALUE}->elements[_i])
                            ));
                    v->%{TARGET}.append(id);
                }
'''

copy_ident_ranges = '''
                if ( v->%{TARGET} ) {
                    v->%{TARGET}->startCol = node->col_offset; v->startCol = v->%{TARGET}->startCol;
                    v->%{TARGET}->startLine = tline(node->lineno - 1);  v->startLine = v->%{TARGET}->startLine;
                    v->%{TARGET}->endCol = node->col_offset + v->%{TARGET}->value.length() - 1;  v->endCol = v->%{TARGET}->endCol;
                    v->%{TARGET}->endLine = tline(node->lineno - 1);  v->endLine = v->%{TARGET}->endLine;
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
    if plugintypestr == 'GeneratorExpressionAst': return '_expr'
    if plugintypestr == 'ArgAst': return '_arg'
    if plugintypestr == 'WithItemAst': return '_withitem'
    else:
        sys.stderr.write("W: Could not decode name %s\n" % plugintypestr)
        return '<ERROR>'

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
    code = None
    since_version = None
    before_version = None
    if len(outline) > 3:
        if outline[3].startswith('BEFORE'):
            before_version = [int(n) for n in outline[3][7:].split('.')]
        elif outline[3].startswith('SINCE'):
            since_version = [int(n) for n in outline[3][6:].split('.')]
        elif outline[3].startswith('CODE'):
            code = ' '.join(';'.join(outline[3:]).split('CODE')[1:]) + ";"
        else:
            raise SyntaxError('Invalid syntax in sdef file, line: ' + rule)
    if len(outline) > 4 and outline[4].startswith('CODE'):
        code = ' '.join(';'.join(outline[4:]).split('CODE')[1:]) + ";"
    
    if rule_for not in results:
        results[rule_for] = list()
    
    current_actions = list()
    created_v = False
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
            if commandType in ['~', ':', '$', '+', 'l', '_']:
                if commandType == '_':
                    raw = singleton_convert_line
                if commandType == ':':
                    raw = direct_assignment_line if not any else direct_assignment_line_any
                if commandType == '~':
                    raw = create_identifier_line if not any else create_identifier_line_any
                    if rule_for in ['_expr', '_stmt', '_excepthandler', '_arg']:
                        raw += copy_ident_ranges
                if commandType == '$':
                    raw = resolve_string
                if commandType == '+':
                    raw = assign_mindless;
                if commandType == 'l':
                    raw = assign_linetransform;
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
            created_v = True

    if code:
        current_actions.append(code);

    current_actions = "\n".join(current_actions)
    if kind == 'any':
        current_stmt = current_actions
    else:
        if created_v:
            current_actions += "\n                result = v;"
        current_stmt = switch_line.replace('%{KIND}', kind).replace('%{ACTIONS}', current_actions)
    if before_version:
        version_cpp_if = ("#if PYTHON_VERSION < QT_VERSION_CHECK(%d, %d, 0)\n"
                           %(before_version[0], before_version[1]))
        current_stmt = version_cpp_if + current_stmt + "\n#endif"
    if since_version:
        version_cpp_if = ("#if PYTHON_VERSION >= QT_VERSION_CHECK(%d, %d, 0)\n"
                           %(since_version[0], since_version[1]))
        current_stmt = version_cpp_if + current_stmt + "\n#endif"
    results[rule_for].append(current_stmt)
    does_match_any[rule_for] = any

print('''/* This code is generated by conversiongenerator.py.
 * I do not recommend editing it.
 * To update, run: python2 conversionGenerator.py > generated.h
 */

#include <QStack>
#include "kdevpythonversion.h"

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
    // Shift lines by some fixed amount
    inline int tline(int line) {
        if ( line == -99999 ) {
            // don't touch the marker
            return -99999;
        }
        return line;
    };
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
            Ast* result = visitNode(currentNode);
            K* transformedNode = static_cast<K*>(result);
            nodelist.append(transformedNode);
        }
        return nodelist;
    }

''')

for index, lines in sorted(results.items()):
    current_switch_lines = "\n".join(lines)
    appendix = ''
    if index == '_expr' or index == '_stmt':
        appendix = '''
	if ( ! result ) return nullptr;
        if ( ! ranges_copied ) {
            result->startCol = node->col_offset;
            result->endCol = node->col_offset;
            result->startLine = tline(node->lineno - 1);
            result->endLine = tline(node->lineno - 1);
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
                if ( ! parent->hasUsefulRangeInformation && parent->startLine == -99999 ) {
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
    if index == '_slice':
        func = "#if PYTHON_VERSION < QT_VERSION_CHECK(3, 9, 0)\n" + func + "\n#endif\n"
    print(func)

print('''};

/*
 * End generated code
 */
''')
