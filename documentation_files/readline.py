# AUTO-GENERATED FILE -- DO NOT EDIT

""" Importing this module enables command line editing using GNU readline. """

__package__ = None

def add_history(string):
  """ add_history(string) -> None
  add a line to the history buffer """
  return None

def clear_history():
  """ clear_history() -> None
  Clear the current readline history. """
  return None

def get_begidx():
  """ get_begidx() -> int
  get the beginning index of the readline tab-completion scope """
  return 1

def get_completer():
  """ get_completer() -> function
  
  Returns current completer function. """
  return None

def get_completer_delims():
  """ get_completer_delims() -> string
  get the readline word delimiters for tab-completion """
  return ""

def get_completion_type():
  """ get_completion_type() -> int
  Get the type of completion being attempted. """
  return 1

def get_current_history_length():
  """ get_current_history_length() -> integer
  return the current (not the maximum) length of history. """
  return 1

def get_endidx():
  """ get_endidx() -> int
  get the ending index of the readline tab-completion scope """
  return 1

def get_history_item():
  """ get_history_item() -> string
  return the current contents of history item at index. """
  return ""

def get_history_length():
  """ get_history_length() -> int
  return the maximum number of items that will be written to
  the history file. """
  return 1

def get_line_buffer():
  """ get_line_buffer() -> string
  return the current contents of the line buffer. """
  return ""

def insert_text(string):
  """ insert_text(string) -> None
  Insert text into the command line. """
  return None

def parse_and_bind(string):
  """ parse_and_bind(string) -> None
  Parse and execute single line of a readline init file. """
  return None

def read_history_file(filename=None):
  """ read_history_file([filename]) -> None
  Load a readline history file.
  The default filename is ~/.history. """
  return None

def read_init_file(filename=None):
  """ read_init_file([filename]) -> None
  Parse a readline initialization file.
  The default filename is the last filename used. """
  return None

def redisplay():
  """ redisplay() -> None
  Change what's displayed on the screen to reflect the current
  contents of the line buffer. """
  return None

def remove_history_item(pos):
  """ remove_history_item(pos) -> None
  remove history item given by its position """
  return None

def replace_history_item(pos, line):
  """ replace_history_item(pos, line) -> None
  replaces history item given by its position with contents of line """
  return None

def set_completer(function=None):
  """ set_completer([function]) -> None
  Set or remove the completer function.
  The function is called as function(text, state),
  for state in 0, 1, 2, ..., until it returns a non-string.
  It should return the next possible completion starting with 'text'. """
  return None

def set_completer_delims(string):
  """ set_completer_delims(string) -> None
  set the readline word delimiters for tab-completion """
  return None

def set_completion_display_matches_hook(function=None):
  """ set_completion_display_matches_hook([function]) -> None
  Set or remove the completion display function.
  The function is called as
    function(substitution, [matches], longest_match_length)
  once each time matches need to be displayed. """
  return None

def set_history_length(length):
  """ set_history_length(length) -> None
  set the maximal number of items which will be written to
  the history file. A negative length is used to inhibit
  history truncation. """
  return None

def set_pre_input_hook(function=None):
  """ set_pre_input_hook([function]) -> None
  Set or remove the pre_input_hook function.
  The function is called with no arguments after the first prompt
  has been printed and just before readline starts reading input
  characters. """
  return None

def set_startup_hook(function=None):
  """ set_startup_hook([function]) -> None
  Set or remove the startup_hook function.
  The function is called with no arguments just
  before readline prints the first prompt. """
  return None

def write_history_file(filename=None):
  """ write_history_file([filename]) -> None
  Save a readline history file.
  The default filename is ~/.history. """
  return None

