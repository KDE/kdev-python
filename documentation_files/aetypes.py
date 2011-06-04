#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Python representation of the Apple Event Object Model.
:deprecated:
"""
class Unknown:


	"""
	The representation of OSA descriptor data for which the :mod:`aepack` and
	:mod:`aetypes` modules have no support, i.e. anything that is not represented by
	the other classes here and that is not equivalent to a simple Python value.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Enum:


	"""
	An enumeration value with the given 4-character string value.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class InsertionLoc:


	"""
	Position ``pos`` in object ``of``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Boolean:


	"""
	A boolean.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class StyledText:


	"""
	Text with style information (font, face, etc) included.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class AEText:


	"""
	Text with script system and style information included.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class IntlText:


	"""
	Text with script system and language information included.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class IntlWritingCode:


	"""
	Script system and language information.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class QDPoint:


	"""
	A quickdraw point.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class QDRectangle:


	"""
	A quickdraw rectangle.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class RGBColor:


	"""
	A color.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Type:


	"""
	An OSA type value with the given 4-character name.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Keyword:


	"""
	An OSA keyword with the given 4-character name.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Range:


	"""
	A range.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Ordinal:


	"""
	Non-numeric absolute positions, such as ``"firs"``, first, or ``"midd"``,
	middle.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Logical:


	"""
	The logical expression of applying operator ``logc`` to ``term``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Comparison:


	"""
	The comparison ``relo`` of ``obj1`` to ``obj2``.
	
	The following classes are used as base classes by the generated stub packages to
	represent AppleScript classes and properties in Python:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ComponentItem:


	"""
	Abstract baseclass for an OSA class. The subclass should set the class attribute
	``want`` to the 4-character OSA class code. Instances of subclasses of this
	class are equivalent to AppleScript Object Specifiers. Upon instantiation you
	should pass a selector in ``which``, and optionally a parent object in ``fr``.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class NProperty:


	"""
	Abstract baseclass for an OSA property. The subclass should set the class
	attributes ``want`` and ``which`` to designate which property we are talking
	about. Instances of subclasses of this class are Object Specifiers.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


