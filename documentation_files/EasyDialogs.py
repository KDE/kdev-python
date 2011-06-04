#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Mac
:synopsis: Basic Macintosh dialogs.
:deprecated:


The :mod:`EasyDialogs` module contains some simple dialogs for the Macintosh.
The dialogs get launched in a separate application which appears in the dock and
must be clicked on for the dialogs be displayed.  All routines take an optional
resource ID parameter *id* with which one can override the :const:`DLOG`
resource used for the dialog, provided that the dialog items correspond (both
type and item number) to those in the default :const:`DLOG` resource. See source
code for details.

"""
def Message(str,id,ok):
	"""
	Displays a modal dialog with the message text *str*, which should be at most 255
	characters long. The button text defaults to "OK", but is set to the string
	argument *ok* if the latter is supplied. Control is returned when the user
	clicks the "OK" button.
	
	
	"""
	pass
	
def AskString(prompt,default,id,ok,cancel):
	"""
	Asks the user to input a string value via a modal dialog. *prompt* is the prompt
	message, and the optional *default* supplies the initial value for the string
	(otherwise ``""`` is used). The text of the "OK" and "Cancel" buttons can be
	changed with the *ok* and *cancel* arguments. All strings can be at most 255
	bytes long. :func:`AskString` returns the string entered or :const:`None` in
	case the user cancelled.
	
	
	"""
	pass
	
def AskPassword(prompt,default,id,ok,cancel):
	"""
	Asks the user to input a string value via a modal dialog. Like
	:func:`AskString`, but with the text shown as bullets. The arguments have the
	same meaning as for :func:`AskString`.
	
	
	"""
	pass
	
def AskYesNoCancel(question,default,yes,no,cancel,id):
	"""
	Presents a dialog with prompt *question* and three buttons labelled "Yes", "No",
	and "Cancel". Returns ``1`` for "Yes", ``0`` for "No" and ``-1`` for "Cancel".
	The value of *default* (or ``0`` if *default* is not supplied) is returned when
	the :kbd:`RETURN` key is pressed. The text of the buttons can be changed with
	the *yes*, *no*, and *cancel* arguments; to prevent a button from appearing,
	supply ``""`` for the corresponding argument.
	
	
	"""
	pass
	
def ProgressBar(title,maxval,label,id):
	"""
	Displays a modeless progress-bar dialog. This is the constructor for the
	:class:`ProgressBar` class described below. *title* is the text string displayed
	(default "Working*more"), *maxval* is the value at which progress is complete
	(default ``0``, indicating that an indeterminate amount of work remains to be
	done), and *label* is the text that is displayed above the progress bar itself.
	
	
	"""
	pass
	
def GetArgv(optionlistcommandlist,addoldfile,addnewfile,addfolder,id):
	"""
	Displays a dialog which aids the user in constructing a command-line argument
	list.  Returns the list in ``sys.argv`` format, suitable for passing as an
	argument to :func:`getopt.getopt`.  *addoldfile*, *addnewfile*, and *addfolder*
	are boolean arguments.  When nonzero, they enable the user to insert into the
	command line paths to an existing file, a (possibly) not-yet-existent file, and
	a folder, respectively.  (Note: Option arguments must appear in the command line
	before file and folder arguments in order to be recognized by
	:func:`getopt.getopt`.)  Arguments containing spaces can be specified by
	enclosing them within single or double quotes.  A :exc:`SystemExit` exception is
	raised if the user presses the "Cancel" button.
	
	*optionlist* is a list that determines a popup menu from which the allowed
	options are selected.  Its items can take one of two forms: *optstr* or
	``(optstr, descr)``.  When present, *descr* is a short descriptive string that
	is displayed in the dialog while this option is selected in the popup menu.  The
	correspondence between *optstr*\s and command-line arguments is:
	
	+----------------------+------------------------------------------+
	| *optstr* format      | Command-line format                      |
	+======================+==========================================+
	| ``x``                | :option:`-x` (short option)              |
	+----------------------+------------------------------------------+
	| ``x:`` or ``x=``     | :option:`-x` (short option with value)   |
	+----------------------+------------------------------------------+
	| ``xyz``              | :option:`--xyz` (long option)            |
	+----------------------+------------------------------------------+
	| ``xyz:`` or ``xyz=`` | :option:`--xyz` (long option with value) |
	+----------------------+------------------------------------------+
	
	*commandlist* is a list of items of the form *cmdstr* or ``(cmdstr, descr)``,
	where *descr* is as above.  The *cmdstr*\ s will appear in a popup menu.  When
	chosen, the text of *cmdstr* will be appended to the command line as is, except
	that a trailing ``':'`` or ``'='`` (if present) will be trimmed off.
	
	"""
	pass
	
def AskFileForOpen(message,typeList,defaultLocation,defaultOptionFlags,location,clientName,windowTitle,actionButtonLabel,cancelButtonLabel,preferenceKey,popupExtension,eventProc,previewProc,filterProc,wanted):
	"""
	Post a dialog asking the user for a file to open, and return the file selected
	or :const:`None` if the user cancelled. *message* is a text message to display,
	*typeList* is a list of 4-char filetypes allowable, *defaultLocation* is the
	pathname, :class:`FSSpec` or :class:`FSRef` of the folder to show initially,
	*location* is the ``(x, y)`` position on the screen where the dialog is shown,
	*actionButtonLabel* is a string to show instead of "Open" in the OK button,
	*cancelButtonLabel* is a string to show instead of "Cancel" in the cancel
	button, *wanted* is the type of value wanted as a return: :class:`str`,
	:class:`unicode`, :class:`FSSpec`, :class:`FSRef` and subtypes thereof are
	acceptable.
	
	"""
	pass
	
def AskFileForSave(message,savedFileName,defaultLocation,defaultOptionFlags,location,clientName,windowTitle,actionButtonLabel,cancelButtonLabel,preferenceKey,popupExtension,fileType,fileCreator,eventProc,wanted):
	"""
	Post a dialog asking the user for a file to save to, and return the file
	selected or :const:`None` if the user cancelled. *savedFileName* is the default
	for the file name to save to (the return value). See :func:`AskFileForOpen` for
	a description of the other arguments.
	
	
	"""
	pass
	
def AskFolder(message,defaultLocation,defaultOptionFlags,location,clientName,windowTitle,actionButtonLabel,cancelButtonLabel,preferenceKey,popupExtension,eventProc,filterProc,wanted):
	"""
	Post a dialog asking the user to select a folder, and return the folder selected
	or :const:`None` if the user cancelled. See :func:`AskFileForOpen` for a
	description of the arguments.
	
	
	"""
	pass
	
