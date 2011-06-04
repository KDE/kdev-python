#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Build line-oriented command interpreters.
"""
class Cmd:


	"""
	A :class:`Cmd` instance or subclass instance is a line-oriented interpreter
	framework.  There is no good reason to instantiate :class:`Cmd` itself; rather,
	it's useful as a superclass of an interpreter class you define yourself in order
	to inherit :class:`Cmd`'s methods and encapsulate action methods.
	
	The optional argument *completekey* is the :mod:`readline` name of a completion
	key; it defaults to :kbd:`Tab`. If *completekey* is not :const:`None` and
	:mod:`readline` is available, command completion is done automatically.
	
	The optional arguments *stdin* and *stdout* specify the  input and output file
	objects that the Cmd instance or subclass  instance will use for input and
	output. If not specified, they will default to :data:`sys.stdin` and
	:data:`sys.stdout`.
	
	If you want a given *stdin* to be used, make sure to set the instance's
	:attr:`use_rawinput` attribute to ``False``, otherwise *stdin* will be
	ignored.
	
	"""
	
	
	def __init__(self, completekey,stdin,stdout):
		pass
	
	


