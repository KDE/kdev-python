# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module contains functions for accessing NIS maps.
 """

__package__ = None

def cat():
  """ cat(map, domain = defaultdomain)
  Returns the entire map as a dictionary. Optionally domain can be
  specified but it defaults to the system default domain.
   """
  pass

class error(Exception):

  pass

def get_default_domain():
  """ get_default_domain() -> str
  Corresponds to the C library yp_get_default_domain() call, returning
  the default NIS domain.
   """
  return ""

def maps(arg0):
  """ maps(domain = defaultdomain)
  Returns an array of all available NIS maps within a domain. If domain
  is not specified it defaults to the system default domain.
   """
  return None

def match():
  """ match(key, map, domain = defaultdomain)
  Corresponds to the C library yp_match() call, returning the value of
  key in the given map. Optionally domain can be specified but it
  defaults to the system default domain.
   """
  pass

