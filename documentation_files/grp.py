# AUTO-GENERATED FILE -- DO NOT EDIT

""" Access to the Unix group database.

Group entries are reported as 4-tuples containing the following fields
from the group database, in order:

  name   - name of the group
  passwd - group password (encrypted); often empty
  gid    - numeric ID of the group
  mem    - list of members

The gid is an integer, name and password are strings.  (Note that most
users are not explicitly listed as members of the groups they are in
according to the password database.  Check both databases to get
complete membership information.) """

__package__ = None

def getgrall():
  """ getgrall() -> list of tuples
  Return a list of all available group entries, in arbitrary order.
  An entry whose name starts with '+' or '-' represents an instruction
  to use YP/NIS and may not be accessible via getgrnam or getgrgid. """
  return ()

def getgrgid(id):
  """ getgrgid(id) -> tuple
  Return the group database entry for the given numeric group ID.  If
  id is not valid, raise KeyError. """
  return ()

def getgrnam(name):
  """ getgrnam(name) -> tuple
  Return the group database entry for the given group name.  If
  name is not valid, raise KeyError. """
  return ()

class struct_group(object):
  """ grp.struct_group: Results from getgr*() routines.
  
  This object may be accessed either as a tuple of
    (gr_name,gr_passwd,gr_gid,gr_mem)
  or via the object attributes as named in the above tuple.
   """

  gr_gid = None
  gr_mem = None
  gr_name = None
  gr_passwd = None
  n_fields = 4
  n_sequence_fields = 4
  n_unnamed_fields = 0

