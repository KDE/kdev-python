def func(foo, bar, *args, **kwargs):
    pass

    
mydict = dict()
mylist = list(mydict)

class c():
    attr = 5

another_comprehended_list = [item.attr for item in [c(), c(), c()]]
    
comprehended_list = [x for x in [1, 2, 3] if x in ('a')]
print(x)
    
def func(**kwargs):
    for item in kwargs.iterkeys():
        print(item)
    return kwargs

def yieldTest():
    yield "foo"
    
def my_func():
    my_var_04 = 5
    my_var_01 = 1
    my_var_07 = 12
    my_var_07 = 12
    my_var_07 = 12
    more_vars = 2
    my_var_02 = 2
    my_var_03 = 3

class cls():
    def myfunc(self):
        some_var = my_func
    
    def another(self):
        print(self)

new_threads = cls()

try:
    known_threads = {line.strip() for line  in ["foo"] if line.strip()}
except IOError:
    pass
    known_threads = set()

# Remove threads already in the cache so we can write the new ones only.
new_threads = new_threads - known_threads
        
import os

def ASDF(arg, arg2):
    arg = arg2
    print(arg2)
print(ASDF())

a = a and a
a = a or b

class some_class(foo, bar):
    def __init__(self):
        pass
    
    attr1 = 3
    attr2 = 5
    attr3 = 'str'

argarg = 2

some_instance = some_class()
some_instance.attr1
some_instance.attr2
some_instance.some_method().foobar
some_instance.some_method(some_arg, some_arg2).second_attribute
some_instance \
		.   attr1 \
		.funcfunc(argarg, arg2arg) \
		.foo

#comment
"""
multiline comment
foo
bar
"""
 
import sys
import random

import PyQt4.QtCore

import bisect
bisect.bisect_right()

def returns_int(param):
    return 5

def returns_str(param):
    return 'str'

def returns_list(param): return [];

foo = returns_list()

bar = 'test'
foo = returns_int()
s = returns_str()
l = returns_list()

def simple_func(foo):
	""" usage comment, bla, param:foo"""
	pass

copied = simple_func

def function(foo):
	""" docstring
	more
	more more
	>>> test
	>>> test
	"""
	return foo

async def fonc(x, y, z):
    a = await z

try:
    pass
except Exception as e:
    print(e)

def func(foo, bar, baz, bang, foobang, foobar, foobazbar, foobazbarbang):
    return foobang
    
    import asynchat
    obj = asynchat.async_chat()
    obj.collect_incoming_data()
    import _winreg
    _winreg.CreateKey()
    import binhex
    binhex.hexbin()
    
    if foobazbar < 5:
        pass

func(sys)
simple_func()

def func_without_param():
    pass
    return [(lambda foo: foo) for fdlksh in [1, 2, 3]]

func_without_param()

def another_function(param):
    return [3 for x in param]

a = 5

bar = a == a
a != a
a < a
a <= a
a > a
a < a < a
a >= a
a is a
a is not a
a not in a
a in a

a = a + 1
a = a - 1
a = a * 1
a = a / 1
a = a // 1
a = a % 1
a = a ^ 1
a = a & 1
a = a | 1
a = a ** 1
a = a >> 1
a = a << 1
a = a @ 1

a = not a
a = +a
a = -a
a = ~a

a = b[1:2:3][2]
extended = a[1:2, 2:3]

i += 3
i += j

3 if 5 < 7 else 4

from random import random

random(foo=3)

a = lambda x: x**2

@staticmethod
@classmethod
def genfunc():
    yield foo

for target1, target2 in some_dict.iteritems():
    print(target1, target2)

pi = 3.1415

foo = 1, 2
bar = (1, 2)

with open('f') as foo:
    pass

global IMAGLOBALVARIABLE
IMAGLOBALVARIABLE = 0
try:
    a = 3 / 0
except ZeroDivisionError as err:
    raise ValueError
else:
    do_something()
finally:
    BAM

if 3 and 5:
    pass

for i in xrange(20):
    pass

while True:
    break
    continue

del foo

import random
random.random(3, 5)

somelist = [1, 2, 3, 4, 5]
somedict = { 'key1' : 'value1', key2: value2 }

somelist[...]
somelist[1:]
somelist[:20]
somelist[1:20]
somelist[1:20:2]

class bar(parent):
    pass

if foo in bar and 3 < 5:
    pass

a = [x*2 for x in xrange(20)]

variable.variable2.variable3 = 15
def function(param1, param2, param3, *paramstar, **paramdstar):
    pass
    return param1 * param2

assert False
if not 3:
    pass

if 3 * 5 == 7:
    pass
