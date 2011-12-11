# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module provides access to the Unix shadow password database.
It is available on various Unix versions.

Shadow password database entries are reported as 9-tuples of type struct_spwd,
containing the following items from the password database (see `<shadow.h>'):
sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max, sp_warn, sp_inact, sp_expire, sp_flag.
The sp_namp and sp_pwdp are strings, the rest are integers.
An exception is raised if the entry asked for cannot be found.
You have to be root to be able to use this module. """

__package__ = None

def getspall():
  """ getspall() -> list_of_entries
  Return a list of all available shadow password database entries, in arbitrary order.
  See spwd.__doc__ for more on shadow password database entries. """
  return []

def getspnam(name):
  """ getspnam(name) -> (sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max,
                      sp_warn, sp_inact, sp_expire, sp_flag)
  Return the shadow password database entry for the given user name.
  See spwd.__doc__ for more on shadow password database entries. """
  return (None, None, None, None, None, None, None, None, None)

class struct_spwd(object):
  """ spwd.struct_spwd: Results from getsp*() routines.
  
  This object may be accessed either as a 9-tuple of
    (sp_nam,sp_pwd,sp_lstchg,sp_min,sp_max,sp_warn,sp_inact,sp_expire,sp_flag)
  or via the object attributes as named in the above tuple. """

  n_fields = 9
  n_sequence_fields = 9
  n_unnamed_fields = 0
  sp_expire = None
  sp_flag = None
  sp_inact = None
  sp_lstchg = None
  sp_max = None
  sp_min = None
  sp_nam = None
  sp_pwd = None
  sp_warn = None

