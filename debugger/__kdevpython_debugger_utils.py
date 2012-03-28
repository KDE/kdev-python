# This file is imported from within the debugger

from kdevpdb import kdevOutputFormatter

__kdevpython_builtin_locals = locals

# TODO: weakref those, but python can't in general :(
objectTable = {}

def cleanup():
    objectTable.clear()

def format_locals(locals_):
    '''Print local variables in a machine-readable format'''
    cleanup()
    for key, value in locals_.iteritems():
        if key == '__kdevpython_debugger_utils':
            continue
        value = str(value).replace('\n', r'\n')
        if len(value) > 120:
            value = value[:120] + "..."
        print "%s => %s" % (key, value)

def format_ptr_children(ptr):
    try:
        expr = objectTable[ptr]
    except KeyError:
        print "Address of object not in memory any more";
        return
    format_object_children(expr)

def format_object_children(expr):
    if type(expr) == set:
        expr = list(expr)
    
    output = []
    if type(expr) == list:
        for i in range(len(expr)):
            output.append('ptr:<%s> [%s] => %s' % (id(expr[i]), i, str(expr[i]).replace('\n', r'\n')))
            objectTable[id(expr[i])] = expr[i]
    elif type(expr) == dict:
        for k, v in expr.iteritems():
            output.append('ptr:<%s> [%s] => %s' % (id(v), str(k).replace('\n', r'\n'), str(v).replace('\n', r'\n')))
            objectTable[id(v)] = v
    else:
        for i in dir(expr):
            obj = getattr(expr, i)
            output.append('ptr:<%s> .%s => %s' % (id(obj), i, str(obj).replace('\n', r'\n')))
            objectTable[id(obj)] = obj
    print '\n'.join(output)

