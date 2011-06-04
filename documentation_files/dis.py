#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Disassembler for Python bytecode.


The :mod:`dis` module supports the analysis of CPython :term:`bytecode` by
disassembling it. The CPython bytecode which this module takes as an
input is defined in the file :file:`Include/opcode.h` and used by the compiler
and the interpreter.

"""
"""
Sequence of operation names, indexable using the bytecode.


"""
opname = None
"""
Dictionary mapping operation names to bytecodes.


"""
opmap = None
"""
Sequence of all compare operation names.


"""
cmp_op = None
"""
Sequence of bytecodes that have a constant parameter.


"""
hasconst = None
"""
Sequence of bytecodes that access a free variable.


"""
hasfree = None
"""
Sequence of bytecodes that access an attribute by name.


"""
hasname = None
"""
Sequence of bytecodes that have a relative jump target.


"""
hasjrel = None
"""
Sequence of bytecodes that have an absolute jump target.


"""
hasjabs = None
"""
Sequence of bytecodes that access a local variable.


"""
haslocal = None
"""
Sequence of bytecodes of Boolean operations.


.. ython Bytecode Instructions
----------------------------

The Python compiler currently generates the following bytecode instructions.


"""
hascompare = None
def dis(bytesource):
	"""
	Disassemble the *bytesource* object. *bytesource* can denote either a module, a
	class, a method, a function, or a code object.   For a module, it disassembles
	all functions.  For a class, it disassembles all methods.  For a single code
	sequence, it prints one line per bytecode instruction.  If no object is
	provided, it disassembles the last traceback.
	
	
	"""
	pass
	
def distb(tb):
	"""
	Disassembles the top-of-stack function of a traceback, using the last traceback
	if none was passed.  The instruction causing the exception is indicated.
	
	
	"""
	pass
	
def disassemble(code,lasti):
	"""
	Disassembles a code object, indicating the last instruction if *lasti* was
	provided.  The output is divided in the following columns:
	
	#. the line number, for the first instruction of each line
	#. the current instruction, indicated as ``-->``,
	#. a labelled instruction, indicated with ``>>``,
	#. the address of the instruction,
	#. the operation code name,
	#. operation parameters, and
	#. interpretation of the parameters in parentheses.
	
	The parameter interpretation recognizes local and global variable names,
	constant values, branch targets, and compare operators.
	
	
	"""
	pass
	
def disco(code,lasti):
	"""
	A synonym for :func:`disassemble`.  It is more convenient to type, and kept
	for compatibility with earlier Python releases.
	
	
	"""
	pass
	
def findlinestarts(code):
	"""
	This generator function uses the ``co_firstlineno`` and ``co_lnotab``
	attributes of the code object *code* to find the offsets which are starts of
	lines in the source code.  They are generated as ``(offset, lineno)`` pairs.
	
	
	"""
	pass
	
def findlabels(code):
	"""
	Detect all offsets in the code object *code* which are jump targets, and
	return a list of these offsets.
	
	
	"""
	pass
	
