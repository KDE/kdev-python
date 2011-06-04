#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Names for built-in types.


This module defines names for some object types that are used by the standard
Python interpreter, but not for the types defined by various extension modules.
Also, it does not include some of the types that arise during processing such as
the ``listiterator`` type. It is safe to use ``from types import *`` --- the
module does not export any names besides the ones listed here. New names
exported by future versions of this module will all end in ``Type``.

Typical use is for functions that do different things depending on their
argument types, like the following::

from types import *
def delete(mylist, item):
if type(item) is IntType:
del mylist[item]
else:
mylist.remove(item)

Starting in Python 2.2, built-in factory functions such as :func:`int` and
:func:`str` are also names for the corresponding types.  This is now the
preferred way to access the type instead of using the :mod:`types` module.
Accordingly, the example above should be written as follows::

def delete(mylist, item):
if isinstance(item, int):
del mylist[item]
else:
mylist.remove(item)

The module defines the following names:


"""
"""
The type of ``None``.


"""
NoneType = None
"""
"""
TypeType = None
"""
The type of the :class:`bool` values ``True`` and ``False``; alias of the
built-in :class:`bool`.

"""
BooleanType = None
"""
The type of integers (e.g. ``1``); alias of the built-in :class:`int`.


"""
IntType = None
"""
The type of long integers (e.g. ``1L``); alias of the built-in :class:`long`.


"""
LongType = None
"""
The type of floating point numbers (e.g. ``1.0``); alias of the built-in
:class:`float`.


"""
FloatType = None
"""
The type of complex numbers (e.g. ``1.0j``).  This is not defined if Python was
built without complex number support.


"""
ComplexType = None
"""
The type of character strings (e.g. ``'Spam'``); alias of the built-in
:class:`str`.


"""
StringType = None
"""
The type of Unicode character strings (e.g. ``u'Spam'``).  This is not defined
if Python was built without Unicode support.  It's an alias of the built-in
:class:`unicode`.


"""
UnicodeType = None
"""
The type of tuples (e.g. ``(1, 2, 3, 'Spam')``); alias of the built-in
:class:`tuple`.


"""
TupleType = None
"""
The type of lists (e.g. ``[0, 1, 2, 3]``); alias of the built-in
:class:`list`.


"""
ListType = None
"""
The type of dictionaries (e.g. ``{'Bacon': 1, 'Ham': 0}``); alias of the
built-in :class:`dict`.


"""
DictType = None
"""
An alternate name for ``DictType``.


"""
DictionaryType = None
"""LambdaType

The type of user-defined functions and functions created by :keyword:`lambda`
expressions.


"""
FunctionType = None
"""
The type of :term:`generator`-iterator objects, produced by calling a
generator function.

"""
GeneratorType = None
"""
"""
CodeType = None
"""
The type of user-defined old-style classes.


"""
ClassType = None
"""
The type of instances of user-defined classes.


"""
InstanceType = None
"""
The type of methods of user-defined class instances.


"""
MethodType = None
"""
An alternate name for ``MethodType``.


"""
UnboundMethodType = None
"""BuiltinMethodType

The type of built-in functions like :func:`len` or :func:`sys.exit`, and
methods of built-in classes.  (Here, the term "built-in" means "written in
C".)


"""
BuiltinFunctionType = None
"""
The type of modules.


"""
ModuleType = None
"""
The type of open file objects such as ``sys.stdout``; alias of the built-in
:class:`file`.


"""
FileType = None
"""
"""
XRangeType = None
"""
"""
SliceType = None
"""
The type of ``Ellipsis``.


"""
EllipsisType = None
"""
The type of traceback objects such as found in ``sys.exc_traceback``.


"""
TracebackType = None
"""
The type of frame objects such as found in ``tb.tb_frame`` if ``tb`` is a
traceback object.


"""
FrameType = None
"""
"""
BufferType = None
"""
The type of dict proxies, such as ``TypeType.__dict__``.


"""
DictProxyType = None
"""
The type of ``NotImplemented``


"""
NotImplementedType = None
"""
The type of objects defined in extension modules with ``PyGetSetDef``, such
as ``FrameType.f_locals`` or ``array.array.typecode``.  This type is used as
descriptor for object attributes; it has the same purpose as the
:class:`property` type, but for classes defined in extension modules.

"""
GetSetDescriptorType = None
"""
The type of objects defined in extension modules with ``PyMemberDef``, such
as ``datetime.timedelta.days``.  This type is used as descriptor for simple C
data members which use standard conversion functions; it has the same purpose
as the :class:`property` type, but for classes defined in extension modules.

"""
MemberDescriptorType = None
"""
A sequence containing ``StringType`` and ``UnicodeType`` used to facilitate
easier checking for any string object.  Using this is more portable than using a
sequence of the two string types constructed elsewhere since it only contains
``UnicodeType`` if it has been built in the running version of Python.  For
example: ``isinstance(s, types.StringTypes)``.

"""
StringTypes = None
