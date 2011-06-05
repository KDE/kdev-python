#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Abstract base classes according to PEP 3119.
"""
class ABCMeta:


	"""
	Metaclass for defining Abstract Base Classes (ABCs).
	
	Use this metaclass to create an ABC.  An ABC can be subclassed directly, and
	then acts as a mix-in class.  You can also register unrelated concrete
	classes (even built-in classes) and unrelated ABCs as "virtual subclasses" --
	these and their descendants will be considered subclasses of the registering
	ABC by the built-in :func:`issubclass` function, but the registering ABC
	won't show up in their MRO (Method Resolution Order) nor will method
	implementations defined by the registering ABC be callable (not even via
	:func:`super`). [#]_
	
	Classes created with a metaclass of :class:`ABCMeta` have the following method:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def register(self, sub_class):
		"""
		Register *subclass* as a "virtual subclass" of this ABC. For
		example::
		
		from abc import ABCMeta
		
		class MyABC:
		__metaclass__ = ABCMeta
		
		MyABC.register(tuple)
		
		assert issubclass(tuple, MyABC)
		assert isinstance((), MyABC)
		
		You can also override this method in an abstract base class:
		
		"""
		pass
		
	def __sub_classhook__(self, sub_class):
		"""
		(Must be defined as a class method.)
		
		Check whether *subclass* is considered a subclass of this ABC.  This means
		that you can customize the behavior of ``issubclass`` further without the
		need to call :meth:`register` on every class you want to consider a
		subclass of the ABC.  (This class method is called from the
		:meth:`__subclasscheck__` method of the ABC.)
		
		This method should return ``True``, ``False`` or ``NotImplemented``.  If
		it returns ``True``, the *subclass* is considered a subclass of this ABC.
		If it returns ``False``, the *subclass* is not considered a subclass of
		this ABC, even if it would normally be one.  If it returns
		``NotImplemented``, the subclass check is continued with the usual
		mechanism.
		
		.. he "usual mechanism"
		
		
		For a demonstration of these concepts, look at this example ABC definition::
		
		class Foo(object):
		def __getitem__(self, index):
		more
		def __len__(self):
		more
		def get_iterator(self):
		return iter(self)
		
		class MyIterable:
		__metaclass__ = ABCMeta
		
		@abstractmethod
		def __iter__(self):
		while False:
		yield None
		
		def get_iterator(self):
		return self.__iter__()
		
		@classmethod
		def __subclasshook__(cls, C):
		if cls is MyIterable:
		if any("__iter__" in B.__dict__ for B in C.__mro__):
		return True
		return NotImplemented
		
		MyIterable.register(Foo)
		
		The ABC ``MyIterable`` defines the standard iterable method,
		:meth:`__iter__`, as an abstract method.  The implementation given here can
		still be called from subclasses.  The :meth:`get_iterator` method is also
		part of the ``MyIterable`` abstract base class, but it does not have to be
		overridden in non-abstract derived classes.
		
		The :meth:`__subclasshook__` class method defined here says that any class
		that has an :meth:`__iter__` method in its :attr:`__dict__` (or in that of
		one of its base classes, accessed via the :attr:`__mro__` list) is
		considered a ``MyIterable`` too.
		
		Finally, the last line makes ``Foo`` a virtual subclass of ``MyIterable``,
		even though it does not define an :meth:`__iter__` method (it uses the
		old-style iterable protocol, defined in terms of :meth:`__len__` and
		:meth:`__getitem__`).  Note that this will not make ``get_iterator``
		available as a method of ``Foo``, so it is provided separately.
		
		
		It also provides the following decorators:
		"""
		pass
		
	def abstractmethod(self, function):
		"""
		A decorator indicating abstract methods.
		
		Using this decorator requires that the class's metaclass is :class:`ABCMeta` or
		is derived from it.
		A class that has a metaclass derived from :class:`ABCMeta`
		cannot be instantiated unless all of its abstract methods and
		properties are overridden.
		The abstract methods can be called using any of the normal 'super' call
		mechanisms.
		
		Dynamically adding abstract methods to a class, or attempting to modify the
		abstraction status of a method or class once it is created, are not
		supported.  The :func:`abstractmethod` only affects subclasses derived using
		regular inheritance; "virtual subclasses" registered with the ABC's
		:meth:`register` method are not affected.
		
		Usage::
		
		class C:
		__metaclass__ = ABCMeta
		@abstractmethod
		def my_abstract_method(self, more):
		more
		
		"""
		pass
		
	def abstractproperty(self, fget,fset,fdel,doc):
		"""
		A subclass of the built-in :func:`property`, indicating an abstract property.
		
		Using this function requires that the class's metaclass is :class:`ABCMeta` or
		is derived from it.
		A class that has a metaclass derived from :class:`ABCMeta` cannot be
		instantiated unless all of its abstract methods and properties are overridden.
		The abstract properties can be called using any of the normal
		'super' call mechanisms.
		
		Usage::
		
		class C:
		__metaclass__ = ABCMeta
		@abstractproperty
		def my_abstract_property(self):
		more
		
		This defines a read-only property; you can also define a read-write abstract
		property using the 'long' form of property declaration::
		
		class C:
		__metaclass__ = ABCMeta
		def getx(self): more
		def setx(self, value): more
		x = abstractproperty(getx, setx)
		
		
		"""
		pass
		
	


