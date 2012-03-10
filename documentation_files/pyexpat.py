# AUTO-GENERATED FILE -- DO NOT EDIT

""" Python wrapper for Expat parser. """

EXPAT_VERSION = 'expat_2.0.1'

def ErrorString(errno):
  """ ErrorString(errno) -> string
  Returns string error for given number. """
  return ""

class ExpatError(Exception):

  pass

def ParserCreate(encoding=None, namespace_separator=None):
  """ ParserCreate([encoding[, namespace_separator]]) -> parser
  Return a new XML parser object. """
  return None

class XMLParserType(object):
  """ XML parser """

  pass

XML_PARAM_ENTITY_PARSING_ALWAYS = 2
XML_PARAM_ENTITY_PARSING_NEVER = 0
XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE = 1
__package__ = None
__version__ = '2.7.2'

error = ExpatError
errors = None
expat_CAPI = None
features = []
model = None
native_encoding = 'UTF-8'
version_info = ()

