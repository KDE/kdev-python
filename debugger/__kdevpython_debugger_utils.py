# This file is imported from within the debugger

# SPDX-FileCopyrightText: 2014 Sven Brauch <svenbrauch@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

from kdevpdb import kdevOutputFormatter

import sys

__kdevpython_builtin_locals = locals

try:
    from numpy import ndarray
except:
    class ndarray: pass

# TODO: weakref those, but python can't in general :(
objectTable = {}

def cleanup():
    objectTable.clear()

def obj_to_string(value):
    if type(value) == ndarray:
        value = "numpy.array, shape={0}".format(value.shape)
    value = str(value).replace('\n', r'\n')
    if len(value) > 120:
        value = value[:120] + "..."
    return value

def format_locals(locals_):
    '''Print local variables in a machine-readable format'''
    cleanup()
    for key, value in locals_.items():
        if key == '__kdevpython_debugger_utils':
            continue
        value = obj_to_string(value)
        print("%s => %s" % (key, value))

def format_ptr_children(ptr):
    try:
        expr = objectTable[ptr]
    except KeyError:
        print("Address of object not in memory any more")
        return
    format_object_children(expr)

def format_object_children(expr):
    if type(expr) == set:
        expr = list(expr)

    output = []
    if type(expr) == list or type(expr) == ndarray:
        for i in range(len(expr)):
            identifier = id(expr[i])
            obj = expr[i]
            output.append('ptr:<%s> [%s] => %s' % (identifier, i, obj_to_string(obj)))
            objectTable[identifier] = obj
    elif type(expr) == dict:
        for k, v in expr.items():
            output.append('ptr:<%s> [%s] => %s' % (id(v), obj_to_string(k), obj_to_string(v)))
            objectTable[id(v)] = v
    else:
        for i in dir(expr):
            obj = getattr(expr, i)
            output.append('ptr:<%s> .%s => %s' % (id(obj), i, obj_to_string(obj)))
            objectTable[id(obj)] = obj
    print('\n'.join(output))

