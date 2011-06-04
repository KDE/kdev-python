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
	
	def abstractmethod(function):
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
		def my_abstract_method(self, *more):
		*more
		
		"""
		pass
		
	def abstractproperty(fget,fset,fdel,doc):
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
		*more
		
		This defines a read-only property; you can also define a read-write abstract
		property using the 'long' form of property declaration::
		
		class C:
		__metaclass__ = ABCMeta
		def getx(self): *more
		def setx(self, value): *more
		x = abstractproperty(getx, setx)
		
		
		"""
		pass
		
	


