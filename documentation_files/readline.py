#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: GNU readline support for Python.
"""
def parse_and_bind(string):
	"""
	Parse and execute single line of a readline init file.
	
	
	"""
	pass
	
def get_line_buffer():
	"""
	Return the current contents of the line buffer.
	
	
	"""
	pass
	
def insert_text(string):
	"""
	Insert text into the command line.
	
	
	"""
	pass
	
def read_init_file(filename):
	"""
	Parse a readline initialization file. The default filename is the last filename
	used.
	
	
	"""
	pass
	
def read_history_file(filename):
	"""
	Load a readline history file. The default filename is :file:`~/.history`.
	
	
	"""
	pass
	
def write_history_file(filename):
	"""
	Save a readline history file. The default filename is :file:`~/.history`.
	
	
	"""
	pass
	
def clear_history():
	"""
	Clear the current history.  (Note: this function is not available if the
	installed version of GNU readline doesn't support it.)
	
	"""
	pass
	
def get_history_length():
	"""
	Return the desired length of the history file.  Negative values imply unlimited
	history file size.
	
	
	"""
	pass
	
def set_history_length(length):
	"""
	Set the number of lines to save in the history file. :func:`write_history_file`
	uses this value to truncate the history file when saving.  Negative values imply
	unlimited history file size.
	
	
	"""
	pass
	
def get_current_history_length():
	"""
	Return the number of lines currently in the history.  (This is different from
	:func:`get_history_length`, which returns the maximum number of lines that will
	be written to a history file.)
	
	"""
	pass
	
def get_history_item(index):
	"""
	Return the current contents of history item at *index*.
	
	"""
	pass
	
def remove_history_item(pos):
	"""
	Remove history item specified by its position from the history.
	
	"""
	pass
	
def replace_history_item(pos,line):
	"""
	Replace history item specified by its position with the given line.
	
	"""
	pass
	
def redisplay():
	"""
	Change what's displayed on the screen to reflect the current contents of the
	line buffer.
	
	"""
	pass
	
def set_startup_hook(function):
	"""
	Set or remove the startup_hook function.  If *function* is specified, it will be
	used as the new startup_hook function; if omitted or ``None``, any hook function
	already installed is removed.  The startup_hook function is called with no
	arguments just before readline prints the first prompt.
	
	
	"""
	pass
	
def set_pre_input_hook(function):
	"""
	Set or remove the pre_input_hook function.  If *function* is specified, it will
	be used as the new pre_input_hook function; if omitted or ``None``, any hook
	function already installed is removed.  The pre_input_hook function is called
	with no arguments after the first prompt has been printed and just before
	readline starts reading input characters.
	
	
	"""
	pass
	
def set_completer(function):
	"""
	Set or remove the completer function.  If *function* is specified, it will be
	used as the new completer function; if omitted or ``None``, any completer
	function already installed is removed.  The completer function is called as
	``function(text, state)``, for *state* in ``0``, ``1``, ``2``, more, until it
	returns a non-string value.  It should return the next possible completion
	starting with *text*.
	
	
	"""
	pass
	
def get_completer():
	"""
	Get the completer function, or ``None`` if no completer function has been set.
	
	"""
	pass
	
def get_completion_type():
	"""
	Get the type of completion being attempted.
	
	"""
	pass
	
def get_begidx():
	"""
	Get the beginning index of the readline tab-completion scope.
	
	
	"""
	pass
	
def get_endidx():
	"""
	Get the ending index of the readline tab-completion scope.
	
	
	"""
	pass
	
def set_completer_delims(string):
	"""
	Set the readline word delimiters for tab-completion.
	
	
	"""
	pass
	
def get_completer_delims():
	"""
	Get the readline word delimiters for tab-completion.
	
	"""
	pass
	
def set_completion_display_matches_hook(function):
	"""
	Set or remove the completion display function.  If *function* is
	specified, it will be used as the new completion display function;
	if omitted or ``None``, any completion display function already
	installed is removed.  The completion display function is called as
	``function(substitution, [matches], longest_match_length)`` once
	each time matches need to be displayed.
	
	"""
	pass
	
def add_history(line):
	"""
	Append a line to the history buffer, as if it was the last line typed.
	
	"""
	pass
	
