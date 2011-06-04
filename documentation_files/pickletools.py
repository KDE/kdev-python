#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Contains extensive comments about the pickle protocols and pickle-machine
opcodes, as well as some useful functions.


"""
def dis(pickle,out=None,memo=None,indentlevel=4):
	"""
	Outputs a symbolic disassembly of the pickle to the file-like object *out*,
	defaulting to ``sys.stdout``.  *pickle* can be a string or a file-like object.
	*memo* can be a Python dictionary that will be used as the pickle's memo; it can
	be used to perform disassemblies across multiple pickles created by the same
	pickler. Successive levels, indicated by ``MARK`` opcodes in the stream, are
	indented by *indentlevel* spaces.
	
	
	"""
	pass
	
def genops(pickle):
	"""
	Provides an :term:`iterator` over all of the opcodes in a pickle, returning a
	sequence of ``(opcode, arg, pos)`` triples.  *opcode* is an instance of an
	:class:`OpcodeInfo` class; *arg* is the decoded value, as a Python object, of
	the opcode's argument; *pos* is the position at which this opcode is located.
	*pickle* can be a string or a file-like object.
	
	"""
	pass
	
def optimize(picklestring):
	"""
	Returns a new equivalent pickle string after eliminating unused ``PUT``
	opcodes. The optimized pickle is shorter, takes less transmission time,
	requires less storage space, and unpickles more efficiently.
	
	"""
	pass
	
