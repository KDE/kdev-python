a = a and a
a = a or b

def some_class(foo, bar):
	attr1 = 3
	attr2 = 5
	attr3 = 'str'

some_instance = some_class()
some_instance.attr1
some_instance.attr2
some_instance.some_method()

#comment
"""
multiline comment
foo
bar
"""
 
import sys
import random

import PyQt4.QtCore

print sys

def simple_func(foo):
	# usage comment, bla, param:foo
	pass

def function(foo):
	""" docstring
	more
	more more
	>>> test
	>>> test
	"""
	return foo

try:
    pass
except Exception as e:
    print e

def func(foo, bar, baz, bang, foobang, foobar, foobazbar, foobazbarbang):
    return foobang
    print foo
    print foobazbarbang
    
    if foobazbar < 5:
        pass

func(sys)
simple_func()

def func_without_param():
    pass

func_without_param()

def another_function(param):
    print param

a = 5

bar = a == a
a != a
a < a
a <= a
a > a
a >= a
a is a
a is not a
a not in a
a in a

a = a + 1
a = a - 1
a = a * 1
a = a / 1
a = a % 1
a = a ^ 1
a = a & 1
a = a | 1
a = a ** 1
a = a >> 1
a = a << 1

a = not a
a = +a
a = -a
a = ~a

a = b[1:2:3][2]
extended = a[1:2, 2:3]

i += 3
i += j

print 3 if 5 < 7 else 4

from random import random

print random

random(foo=3)

a = lambda x: x**2

@staticmethod
@classmethod
def genfunc():
    yield foo

for target1, target2 in some_dict.iteritems():
    print target1, target2

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

print somelist[...]
print somelist[1:]
print somelist[:20]
print somelist[1:20]
print somelist[1:20:2]

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
