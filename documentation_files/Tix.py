#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Tk Extension Widgets for Tkinter
"""
class Tix:


	"""
	Toplevel widget of Tix which represents mostly the main window of an
	application. It has an associated Tcl interpreter.
	
	Classes in the :mod:`Tix` module subclasses the classes in the :mod:`Tkinter`
	module. The former imports the latter, so to use :mod:`Tix` with Tkinter, all
	you need to do is to import one module. In general, you can just import
	:mod:`Tix`, and replace the toplevel call to :class:`Tkinter.Tk` with
	:class:`Tix.Tk`::
	
	import Tix
	from Tkconstants import *
	root = Tix.Tk()
	
	To use :mod:`Tix`, you must have the :mod:`Tix` widgets installed, usually
	alongside your installation of the Tk widgets. To test your installation, try
	the following::
	
	import Tix
	root = Tix.Tk()
	root.tk.eval('package require Tix')
	
	If this fails, you have a Tk installation problem which must be resolved before
	proceeding. Use the environment variable :envvar:`TIX_LIBRARY` to point to the
	installed :mod:`Tix` library directory, and make sure you have the dynamic
	object library (:file:`tix8183.dll` or :file:`libtix8183.so`) in  the same
	directory that contains your Tk dynamic object library (:file:`tk8183.dll` or
	:file:`libtk8183.so`). The directory with the dynamic object library should also
	have a file called :file:`pkgIndex.tcl` (case sensitive), which contains the
	line::
	
	package ifneeded Tix 8.1 [list load "[file join $dir tix8183.dll]" Tix]
	
	
	Tix Widgets
	-----------
	
	`Tix <http://tix.sourceforge.net/dist/current/man/html/TixCmd/TixIntro.htm>`_
	introduces over 40 widget classes to the :mod:`Tkinter`  repertoire.  There is a
	demo of all the :mod:`Tix` widgets in the :file:`Demo/tix` directory of the
	standard distribution.
	
	.. ample code is still being added to Python, hence commented out
	
	
	Basic Widgets
	^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, screenName,baseName,_className):
		pass
	
	


class Balloon:


	"""
	A `Balloon
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixBalloon.htm>`_ that
	pops up over a widget to provide help.  When the user moves the cursor inside a
	widget to which a Balloon widget has been bound, a small pop-up window with a
	descriptive message will be shown on the screen.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ButtonBox:


	"""
	The `ButtonBox
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixButtonBox.htm>`_
	widget creates a box of buttons, such as is commonly used for ``Ok Cancel``.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ComboBox:


	"""
	The `ComboBox
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixComboBox.htm>`_
	widget is similar to the combo box control in MS Windows. The user can select a
	choice by either typing in the entry subwdget or selecting from the listbox
	subwidget.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Control:


	"""
	The `Control
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixControl.htm>`_
	widget is also known as the :class:`SpinBox` widget. The user can adjust the
	value by pressing the two arrow buttons or by entering the value directly into
	the entry. The new value will be checked against the user-defined upper and
	lower limits.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class LabelEntry:


	"""
	The `LabelEntry
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixLabelEntry.htm>`_
	widget packages an entry widget and a label into one mega widget. It can be used
	be used to simplify the creation of "entry-form" type of interface.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class LabelFrame:


	"""
	The `LabelFrame
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixLabelFrame.htm>`_
	widget packages a frame widget and a label into one mega widget.  To create
	widgets inside a LabelFrame widget, one creates the new widgets relative to the
	:attr:`frame` subwidget and manage them inside the :attr:`frame` subwidget.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Meter:


	"""
	The `Meter
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixMeter.htm>`_ widget
	can be used to show the progress of a background job which may take a long time
	to execute.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class OptionMenu:


	"""
	The `OptionMenu
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixOptionMenu.htm>`_
	creates a menu button of options.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class PopupMenu:


	"""
	The `PopupMenu
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixPopupMenu.htm>`_
	widget can be used as a replacement of the ``tk_popup`` command. The advantage
	of the :mod:`Tix` :class:`PopupMenu` widget is it requires less application code
	to manipulate.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Select:


	"""
	The `Select
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixSelect.htm>`_ widget
	is a container of button subwidgets. It can be used to provide radio-box or
	check-box style of selection options for the user.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class StdButtonBox:


	"""
	The `StdButtonBox
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixStdButtonBox.htm>`_
	widget is a group of standard buttons for Motif-like dialog boxes.
	
	.. f:
	.. File Selectors
	^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DirList:


	"""
	The `DirList
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixDirList.htm>`_
	widget displays a list view of a directory, its previous directories and its
	sub-directories. The user can choose one of the directories displayed in the
	list or change to another directory.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DirTree:


	"""
	The `DirTree
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixDirTree.htm>`_
	widget displays a tree view of a directory, its previous directories and its
	sub-directories. The user can choose one of the directories displayed in the
	list or change to another directory.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DirSelectDialog:


	"""
	The `DirSelectDialog
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixDirSelectDialog.htm>`_
	widget presents the directories in the file system in a dialog window.  The user
	can use this dialog window to navigate through the file system to select the
	desired directory.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class DirSelectBox:


	"""
	The :class:`DirSelectBox` is similar to the standard Motif(TM)
	directory-selection box. It is generally used for the user to choose a
	directory.  DirSelectBox stores the directories mostly recently selected into
	a ComboBox widget so that they can be quickly selected again.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ExFileSelectBox:


	"""
	The `ExFileSelectBox
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixExFileSelectBox.htm>`_
	widget is usually embedded in a tixExFileSelectDialog widget. It provides an
	convenient method for the user to select files. The style of the
	:class:`ExFileSelectBox` widget is very similar to the standard file dialog on
	MS Windows 3.1.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class FileSelectBox:


	"""
	The `FileSelectBox
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixFileSelectBox.htm>`_
	is similar to the standard Motif(TM) file-selection box. It is generally used
	for the user to choose a file. FileSelectBox stores the files mostly recently
	selected into a :class:`ComboBox` widget so that they can be quickly selected
	again.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class FileEntry:


	"""
	The `FileEntry
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixFileEntry.htm>`_
	widget can be used to input a filename. The user can type in the filename
	manually. Alternatively, the user can press the button widget that sits next to
	the entry, which will bring up a file selection dialog.
	
	.. f:
	.. Hierarchical ListBox
	^^^^^^^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HList:


	"""
	The `HList
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixHList.htm>`_ widget
	can be used to display any data that have a hierarchical structure, for example,
	file system directory trees. The list entries are indented and connected by
	branch lines according to their places in the hierarchy.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class CheckList:


	"""
	The `CheckList
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixCheckList.htm>`_
	widget displays a list of items to be selected by the user. CheckList acts
	similarly to the Tk checkbutton or radiobutton widgets, except it is capable of
	handling many more items than checkbuttons or radiobuttons.
	
	.. f:
	.. . f:
	.. . f:
	.. 
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Tree:


	"""
	The `Tree
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixTree.htm>`_ widget
	can be used to display hierarchical data in a tree form. The user can adjust the
	view of the tree by opening or closing parts of the tree.
	
	.. f:
	.. ython Demo of:
	.. 
	Tabular ListBox
	^^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class TList:


	"""
	The `TList
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixTList.htm>`_ widget
	can be used to display data in a tabular format. The list entries of a
	:class:`TList` widget are similar to the entries in the Tk listbox widget.  The
	main differences are (1) the :class:`TList` widget can display the list entries
	in a two dimensional format and (2) you can use graphical images as well as
	multiple colors and fonts for the list entries.
	
	.. f:
	.. . f:
	.. . et to be added to Python
	.. . f:
	.. . f:
	.. ython Demo of:
	.. 
	Manager Widgets
	^^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class PanedWindow:


	"""
	The `PanedWindow
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixPanedWindow.htm>`_
	widget allows the user to interactively manipulate the sizes of several panes.
	The panes can be arranged either vertically or horizontally.  The user changes
	the sizes of the panes by dragging the resize handle between two panes.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class ListNoteBook:


	"""
	The `ListNoteBook
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixListNoteBook.htm>`_
	widget is very similar to the :class:`TixNoteBook` widget: it can be used to
	display many windows in a limited space using a notebook metaphor. The notebook
	is divided into a stack of pages (windows). At one time only one of these pages
	can be shown. The user can navigate through these pages by choosing the name of
	the desired page in the :attr:`hlist` subwidget.
	
	.. f:
	"""
	
	
	def __init__(self, ):
		pass
	
	


class NoteBook:


	"""
	The `NoteBook
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixNoteBook.htm>`_
	widget can be used to display many windows in a limited space using a notebook
	metaphor. The notebook is divided into a stack of pages. At one time only one of
	these pages can be shown. The user can navigate through these pages by choosing
	the visual "tabs" at the top of the NoteBook widget.
	
	.. f:
	.. . . f:
	.. ython Demo of:
	.. ython Demo of:
	.. ython Demo of:
	.. iew}{http://tix.sourceforge.net/dist/current/demos/samples/CObjView.tcl}
	
	
	Image Types
	^^^^^^^^^^^
	
	The :mod:`Tix` module adds:
	
	* `pixmap <http://tix.sourceforge.net/dist/current/man/html/TixCmd/pixmap.htm>`_
	capabilities to all :mod:`Tix` and :mod:`Tkinter` widgets to create color images
	from XPM files.
	
	.. f:
	.. n Button}{http://tix.sourceforge.net/dist/current/demos/samples/Xpm.tcl}
	.. f:
	.. n Menu}{http://tix.sourceforge.net/dist/current/demos/samples/Xpm1.tcl}
	
	* `Compound
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/compound.htm>`_ image
	types can be used to create images that consists of multiple horizontal lines;
	each line is composed of a series of items (texts, bitmaps, images or spaces)
	arranged from left to right. For example, a compound image can be used to
	display a bitmap and a text string simultaneously in a Tk :class:`Button`
	widget.
	
	.. f:
	.. n Buttons}{http://tix.sourceforge.net/dist/current/demos/samples/CmpImg.tcl}
	.. f:
	.. n NoteBook}{http://tix.sourceforge.net/dist/current/demos/samples/CmpImg2.tcl}
	.. f:
	.. otebook Color Tabs}{http://tix.sourceforge.net/dist/current/demos/samples/CmpImg4.tcl}
	.. f:
	.. cons}{http://tix.sourceforge.net/dist/current/demos/samples/CmpImg3.tcl}
	
	
	Miscellaneous Widgets
	^^^^^^^^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class InputOnly:


	"""
	The `InputOnly
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixInputOnly.htm>`_
	widgets are to accept inputs from the user, which can be done with the ``bind``
	command (Unix only).
	
	
	Form Geometry Manager
	^^^^^^^^^^^^^^^^^^^^^
	
	In addition, :mod:`Tix` augments :mod:`Tkinter` by providing:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Form:


	"""
	The `Form
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tixForm.htm>`_ geometry
	manager based on attachment rules for all Tk widgets.
	
	
	
	Tix Commands
	------------
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class tixCommand:


	"""
	The `tix commands
	<http://tix.sourceforge.net/dist/current/man/html/TixCmd/tix.htm>`_ provide
	access to miscellaneous elements of :mod:`Tix`'s internal state and the
	:mod:`Tix` application context.  Most of the information manipulated by these
	methods pertains to the application as a whole, or to a screen or display,
	rather than to a particular window.
	
	To view the current settings, the common usage is::
	
	import Tix
	root = Tix.Tk()
	print root.tix_configure()
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


