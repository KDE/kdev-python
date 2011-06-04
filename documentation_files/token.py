#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Constants representing terminal nodes of the parse tree.
"""
"""
Dictionary mapping the numeric values of the constants defined in this module
back to name strings, allowing more human-readable representation of parse trees
to be generated.


"""
tok_name = None
"""NAME
NUMBER
STRING
NEWLINE
INDENT
DEDENT
LPAR
RPAR
LSQB
RSQB
COLON
COMMA
SEMI
PLUS
MINUS
STAR
SLASH
VBAR
AMPER
LESS
GREATER
EQUAL
DOT
PERCENT
BACKQUOTE
LBRACE
RBRACE
EQEQUAL
NOTEQUAL
LESSEQUAL
GREATEREQUAL
TILDE
CIRCUMFLEX
LEFTSHIFT
RIGHTSHIFT
DOUBLESTAR
PLUSEQUAL
MINEQUAL
STAREQUAL
SLASHEQUAL
PERCENTEQUAL
AMPEREQUAL
VBAREQUAL
CIRCUMFLEXEQUAL
LEFTSHIFTEQUAL
RIGHTSHIFTEQUAL
DOUBLESTAREQUAL
DOUBLESLASH
DOUBLESLASHEQUAL
AT
OP
ERRORTOKEN
N_TOKENS
NT_OFFSET


"""
ENDMARKER = None
def ISTERMINAL(x):
	"""
	Return true for terminal token values.
	
	
	"""
	pass
	
def ISNONTERMINAL(x):
	"""
	Return true for non-terminal token values.
	
	
	"""
	pass
	
def ISEOF(x):
	"""
	Return true if *x* is the marker indicating the end of input.
	
	
	The token constants are:
	
	"""
	pass
	
