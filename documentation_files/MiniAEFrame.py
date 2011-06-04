#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Support to act as an Open Scripting Architecture (OSA) server ("Apple Events").


"""
class AEServer:


	"""
	A class that handles AppleEvent dispatch. Your application should subclass this
	class together with either :class:`MiniApplication` or
	:class:`FrameWork.Application`. Your :meth:`__init__` method should call the
	:meth:`__init__` method for both classes.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class MiniApplication:


	"""
	A class that is more or less compatible with :class:`FrameWork.Application` but
	with less functionality. Its event loop supports the apple menu, command-dot and
	AppleEvents; other events are passed on to the Python interpreter and/or Sioux.
	Useful if your application wants to use :class:`AEServer` but does not provide
	its own windows, etc.
	
	
	.. EServer Objects
	----------------
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


