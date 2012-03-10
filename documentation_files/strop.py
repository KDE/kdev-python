# AUTO-GENERATED FILE -- DO NOT EDIT

""" Common string manipulations, optimized for speed.

Always use "import string" rather than referencing
this module directly. """

__package__ = None

def atof(s):
  """ atof(s) -> float
  
  Return the floating point number represented by the string s. """
  return 1.0

def atoi(s, base=None):
  """ atoi(s [,base]) -> int
  
  Return the integer represented by the string s in the given
  base, which defaults to 10.  The string s must consist of one
  or more digits, possibly preceded by a sign.  If base is 0, it
  is chosen from the leading characters of s, 0 for octal, 0x or
  0X for hexadecimal.  If base is 16, a preceding 0x or 0X is
  accepted. """
  return 1

def atol(s, base=None):
  """ atol(s [,base]) -> long
  
  Return the long integer represented by the string s in the
  given base, which defaults to 10.  The string s must consist
  of one or more digits, possibly preceded by a sign.  If base
  is 0, it is chosen from the leading characters of s, 0 for
  octal, 0x or 0X for hexadecimal.  If base is 16, a preceding
  0x or 0X is accepted.  A trailing L or l is not accepted,
  unless base is 0. """
  return None

def capitalize(s):
  """ capitalize(s) -> string
  
  Return a copy of the string s with only its first character
  capitalized. """
  return ""

def count(s, sub, start=None, end=None):
  """ count(s, sub[, start[, end]]) -> int
  
  Return the number of occurrences of substring sub in string
  s[start:end].  Optional arguments start and end are
  interpreted as in slice notation. """
  return 1

def expandtabs(string, tabsize=None):
  """ expandtabs(string, [tabsize]) -> string
  
  Expand tabs in a string, i.e. replace them by one or more spaces,
  depending on the current column and the given tab size (default 8).
  The column number is reset to zero after each newline occurring in the
  string.  This doesn't understand other non-printing characters. """
  return ""

def find(s, sub, start=None, end=None):
  """ find(s, sub [,start [,end]]) -> in
  
  Return the lowest index in s where substring sub is found,
  such that sub is contained within s[start,end].  Optional
  arguments start and end are interpreted as in slice notation.
  
  Return -1 on failure. """
  return None

def join(list, sep=None):
  """ join(list [,sep]) -> string
  joinfields(list [,sep]) -> string
  
  Return a string composed of the words in list, with
  intervening occurrences of sep.  Sep defaults to a single
  space.
  
  (join and joinfields are synonymous) """
  return ""

def joinfields(list, sep=None):
  """ join(list [,sep]) -> string
  joinfields(list [,sep]) -> string
  
  Return a string composed of the words in list, with
  intervening occurrences of sep.  Sep defaults to a single
  space.
  
  (join and joinfields are synonymous) """
  return ""

def lower(s):
  """ lower(s) -> string
  
  Return a copy of the string s converted to lowercase. """
  return ""

lowercase = 'abcdefghijklmnopqrstuvwxyz'

def lstrip(s):
  """ lstrip(s) -> string
  
  Return a copy of the string s with leading whitespace removed. """
  return ""

def maketrans(frm, to):
  """ maketrans(frm, to) -> string
  
  Return a translation table (a string of 256 bytes long)
  suitable for use in string.translate.  The strings frm and to
  must be of the same length. """
  return ""

def replace(str, old, new, maxsplit=None):
  """ replace (str, old, new[, maxsplit]) -> string
  
  Return a copy of string str with all occurrences of substring
  old replaced by new. If the optional argument maxsplit is
  given, only the first maxsplit occurrences are replaced. """
  return ""

def rfind(s, sub, start=None, end=None):
  """ rfind(s, sub [,start [,end]]) -> int
  
  Return the highest index in s where substring sub is found,
  such that sub is contained within s[start,end].  Optional
  arguments start and end are interpreted as in slice notation.
  
  Return -1 on failure. """
  return 1

def rstrip(s):
  """ rstrip(s) -> string
  
  Return a copy of the string s with trailing whitespace removed. """
  return ""

def split(s, sep=None, maxsplit=None):
  """ split(s [,sep [,maxsplit]]) -> list of strings
  splitfields(s [,sep [,maxsplit]]) -> list of strings
  
  Return a list of the words in the string s, using sep as the
  delimiter string.  If maxsplit is nonzero, splits into at most
  maxsplit words.  If sep is not specified, any whitespace string
  is a separator.  Maxsplit defaults to 0.
  
  (split and splitfields are synonymous) """
  return []

def splitfields(s, sep=None, maxsplit=None):
  """ split(s [,sep [,maxsplit]]) -> list of strings
  splitfields(s [,sep [,maxsplit]]) -> list of strings
  
  Return a list of the words in the string s, using sep as the
  delimiter string.  If maxsplit is nonzero, splits into at most
  maxsplit words.  If sep is not specified, any whitespace string
  is a separator.  Maxsplit defaults to 0.
  
  (split and splitfields are synonymous) """
  return []

def strip(s):
  """ strip(s) -> string
  
  Return a copy of the string s with leading and trailing
  whitespace removed. """
  return ""

def swapcase(s):
  """ swapcase(s) -> string
  
  Return a copy of the string s with upper case characters
  converted to lowercase and vice versa. """
  return ""

def translate(s, table, deletechars=None):
  """ translate(s,table [,deletechars]) -> string
  
  Return a copy of the string s, where all characters occurring
  in the optional argument deletechars are removed, and the
  remaining characters have been mapped through the given
  translation table, which must be a string of length 256. """
  return ""

def upper(s):
  """ upper(s) -> string
  
  Return a copy of the string s converted to uppercase. """
  return ""

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
whitespace = """	
 """

