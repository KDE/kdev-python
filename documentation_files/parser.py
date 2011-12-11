# AUTO-GENERATED FILE -- DO NOT EDIT

""" This is an interface to Python's internal parser. """

class ASTType(object):
  """ Intermediate representation of a Python parse tree. """

  pass

class ParserError(Exception):

  pass

__copyright__ = """Copyright 1995-1996 by Virginia Polytechnic Institute & State
University, Blacksburg, Virginia, USA, and Fred L. Drake, Jr., Reston,
Virginia, USA.  Portions copyright 1991-1995 by Stichting Mathematisch
Centrum, Amsterdam, The Netherlands."""
__package__ = None
__version__ = '0.5'

def _pickler():
  """ Returns the pickle magic to allow ST objects to be pickled. """
  pass

def ast2list():
  """ Creates a list-tree representation of an ST. """
  pass

def ast2tuple():
  """ Creates a tuple-tree representation of an ST. """
  pass

def compileast():
  """ Compiles an ST object into a code object. """
  pass

def compilest():
  """ Compiles an ST object into a code object. """
  pass

def expr():
  """ Creates an ST object from an expression. """
  pass

def isexpr():
  """ Determines if an ST object was created from an expression. """
  pass

def issuite():
  """ Determines if an ST object was created from a suite. """
  pass

def sequence2ast():
  """ Creates an ST object from a tree representation. """
  pass

def sequence2st():
  """ Creates an ST object from a tree representation. """
  pass

def st2list():
  """ Creates a list-tree representation of an ST. """
  pass

def st2tuple():
  """ Creates a tuple-tree representation of an ST. """
  pass

def suite():
  """ Creates an ST object from a suite. """
  pass

def tuple2ast():
  """ Creates an ST object from a tree representation. """
  pass

def tuple2st():
  """ Creates an ST object from a tree representation. """
  pass

