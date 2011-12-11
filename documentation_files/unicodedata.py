# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module provides access to the Unicode Character Database which
defines character properties for all Unicode characters. The data in
this database is based on the UnicodeData.txt file version
5.2.0 which is publically available from ftp://ftp.unicode.org/.

The module uses the same names and symbols as defined by the
UnicodeData File Format 5.2.0 (see
http://www.unicode.org/reports/tr44/tr44-4.html). """

class UCD(object):

  def bidirectional(self, unichr):
    """ bidirectional(unichr)
    
    Returns the bidirectional category assigned to the Unicode character
    unichr as string. If no such value is defined, an empty string is
    returned. """
    pass

  def category(self, unichr):
    """ category(unichr)
    
    Returns the general category assigned to the Unicode character
    unichr as string. """
    pass

  def combining(self, unichr):
    """ combining(unichr)
    
    Returns the canonical combining class assigned to the Unicode
    character unichr as integer. Returns 0 if no combining class is
    defined. """
    pass

  def decimal(self, unichr, default=None):
    """ decimal(unichr[, default])
    
    Returns the decimal value assigned to the Unicode character unichr
    as integer. If no such value is defined, default is returned, or, if
    not given, ValueError is raised. """
    pass

  def decomposition(self, unichr):
    """ decomposition(unichr)
    
    Returns the character decomposition mapping assigned to the Unicode
    character unichr as string. An empty string is returned in case no
    such mapping is defined. """
    pass

  def digit(self, unichr, default=None):
    """ digit(unichr[, default])
    
    Returns the digit value assigned to the Unicode character unichr as
    integer. If no such value is defined, default is returned, or, if
    not given, ValueError is raised. """
    pass

  def east_asian_width(self, unichr):
    """ east_asian_width(unichr)
    
    Returns the east asian width assigned to the Unicode character
    unichr as string. """
    pass

  def lookup(self, name):
    """ lookup(name)
    
    Look up character by name.  If a character with the
    given name is found, return the corresponding Unicode
    character.  If not found, KeyError is raised. """
    pass

  def mirrored(self, unichr):
    """ mirrored(unichr)
    
    Returns the mirrored property assigned to the Unicode character
    unichr as integer. Returns 1 if the character has been identified as
    a "mirrored" character in bidirectional text, 0 otherwise. """
    pass

  def name(self, unichr, default=None):
    """ name(unichr[, default])
    Returns the name assigned to the Unicode character unichr as a
    string. If no name is defined, default is returned, or, if not
    given, ValueError is raised. """
    pass

  def normalize(self, form, unistr):
    """ normalize(form, unistr)
    
    Return the normal form 'form' for the Unicode string unistr.  Valid
    values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'. """
    pass

  def numeric(self, unichr, default=None):
    """ numeric(unichr[, default])
    
    Returns the numeric value assigned to the Unicode character unichr
    as float. If no such value is defined, default is returned, or, if
    not given, ValueError is raised. """
    pass

  unidata_version = None

__package__ = None

def bidirectional(unichr):
  """ bidirectional(unichr)
  
  Returns the bidirectional category assigned to the Unicode character
  unichr as string. If no such value is defined, an empty string is
  returned. """
  pass

def category(unichr):
  """ category(unichr)
  
  Returns the general category assigned to the Unicode character
  unichr as string. """
  pass

def combining(unichr):
  """ combining(unichr)
  
  Returns the canonical combining class assigned to the Unicode
  character unichr as integer. Returns 0 if no combining class is
  defined. """
  pass

def decimal(unichr, default=None):
  """ decimal(unichr[, default])
  
  Returns the decimal value assigned to the Unicode character unichr
  as integer. If no such value is defined, default is returned, or, if
  not given, ValueError is raised. """
  pass

def decomposition(unichr):
  """ decomposition(unichr)
  
  Returns the character decomposition mapping assigned to the Unicode
  character unichr as string. An empty string is returned in case no
  such mapping is defined. """
  pass

def digit(unichr, default=None):
  """ digit(unichr[, default])
  
  Returns the digit value assigned to the Unicode character unichr as
  integer. If no such value is defined, default is returned, or, if
  not given, ValueError is raised. """
  pass

def east_asian_width(unichr):
  """ east_asian_width(unichr)
  
  Returns the east asian width assigned to the Unicode character
  unichr as string. """
  pass

def lookup(name):
  """ lookup(name)
  
  Look up character by name.  If a character with the
  given name is found, return the corresponding Unicode
  character.  If not found, KeyError is raised. """
  pass

def mirrored(unichr):
  """ mirrored(unichr)
  
  Returns the mirrored property assigned to the Unicode character
  unichr as integer. Returns 1 if the character has been identified as
  a "mirrored" character in bidirectional text, 0 otherwise. """
  pass

def name(unichr, default=None):
  """ name(unichr[, default])
  Returns the name assigned to the Unicode character unichr as a
  string. If no name is defined, default is returned, or, if not
  given, ValueError is raised. """
  pass

def normalize(form, unistr):
  """ normalize(form, unistr)
  
  Return the normal form 'form' for the Unicode string unistr.  Valid
  values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'. """
  pass

def numeric(unichr, default=None):
  """ numeric(unichr[, default])
  
  Returns the numeric value assigned to the Unicode character unichr
  as float. If no such value is defined, default is returned, or, if
  not given, ValueError is raised. """
  pass

ucd_3_2_0 = None
ucnhash_CAPI = None
unidata_version = '5.2.0'

