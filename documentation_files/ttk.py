#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Tk themed widget set
"""
class Widget:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	def identify(self, x,y):
		"""
		Returns the name of the element at position *x* *y*, or the empty string
		if the point does not lie within any element.
		
		*x* and *y* are pixel coordinates relative to the widget.
		
		
		"""
		pass
		
	def instate(self, statespec,callback=None,args,kw):
		"""
		Test the widget's state. If a callback is not specified, returns True
		if the widget state matches *statespec* and False otherwise. If callback
		is specified then it is called with *args* if widget state matches
		*statespec*.
		
		
		"""
		pass
		
	def state(self, statespec=None):
		"""
		Modify or read widget state. If *statespec* is specified, sets the
		widget state accordingly and returns a new *statespec* indicating
		which flags were changed. If *statespec* is not specified, returns
		the currently-enabled state flags.
		
		*statespec* will usually be a list or a tuple.
		
		
		Combobox
		"""
		pass
		
	


class Combobox:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	def current(self, newindex=None):
		"""
		If *newindex* is specified, sets the combobox value to the element
		position *newindex*. Otherwise, returns the index of the current value or
		-1 if the current value is not in the values list.
		
		
		"""
		pass
		
	def get(self, ):
		"""
		Returns the current value of the combobox.
		
		
		"""
		pass
		
	def set(self, value):
		"""
		Sets the value of the combobox to *value*.
		
		
		Notebook
		"""
		pass
		
	


class Notebook:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	def add(self, child,kw):
		"""
		Adds a new tab to the notebook.
		
		If window is currently managed by the notebook but hidden, it is
		restored to its previous position.
		
		See `Tab Options`_ for the list of available options.
		
		
		"""
		pass
		
	def forget(self, tab_id):
		"""
		Removes the tab specified by *tab_id*, unmaps and unmanages the
		associated window.
		
		
		"""
		pass
		
	def hide(self, tab_id):
		"""
		Hides the tab specified by *tab_id*.
		
		The tab will not be displayed, but the associated window remains
		managed by the notebook and its configuration remembered. Hidden tabs
		may be restored with the :meth:`add` command.
		
		
		"""
		pass
		
	def identify(self, x,y):
		"""
		Returns the name of the tab element at position *x*, *y*, or the empty
		string if none.
		
		
		"""
		pass
		
	def index(self, tab_id):
		"""
		Returns the numeric index of the tab specified by *tab_id*, or the total
		number of tabs if *tab_id* is the string "end".
		
		
		"""
		pass
		
	def insert(self, pos,child,kw):
		"""
		Inserts a pane at the specified position.
		
		*pos* is either the string "end", an integer index, or the name of a
		managed child. If *child* is already managed by the notebook, moves it to
		the specified position.
		
		See `Tab Options`_ for the list of available options.
		
		
		"""
		pass
		
	def select(self, tab_id):
		"""
		Selects the specified *tab_id*.
		
		The associated child window will be displayed, and the
		previously-selected window (if different) is unmapped. If *tab_id* is
		omitted, returns the widget name of the currently selected pane.
		
		
		"""
		pass
		
	def tab(self, tab_id,option=None,kw):
		"""
		Query or modify the options of the specific *tab_id*.
		
		If *kw* is not given, returns a dictionary of the tab option values. If
		*option* is specified, returns the value of that *option*. Otherwise,
		sets the options to the corresponding values.
		
		
		"""
		pass
		
	def tabs(self, ):
		"""
		Returns a list of windows managed by the notebook.
		
		
		"""
		pass
		
	def enable_traversal(self, ):
		"""
		Enable keyboard traversal for a toplevel window containing this notebook.
		
		This will extend the bindings for the toplevel window containing the
		notebook as follows:
		
		* Control-Tab: selects the tab following the currently selected one.
		* Shift-Control-Tab: selects the tab preceding the currently selected one.
		* Alt-K: where K is the mnemonic (underlined) character of any tab, will
		select that tab.
		
		Multiple notebooks in a single toplevel may be enabled for traversal,
		including nested notebooks. However, notebook traversal only works
		properly if all panes have the notebook they are in as master.
		
		
		Progressbar
		"""
		pass
		
	


class Progressbar:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	def start(self, interval):
		"""
		Begin autoincrement mode: schedules a recurring timer event that calls
		:meth:`Progressbar.step` every *interval* milliseconds. If omitted,
		*interval* defaults to 50 milliseconds.
		
		
		"""
		pass
		
	def step(self, amount):
		"""
		Increments the progress bar's value by *amount*.
		
		*amount* defaults to 1.0 if omitted.
		
		
		"""
		pass
		
	def stop(self, ):
		"""
		Stop autoincrement mode: cancels any recurring timer event initiated by
		:meth:`Progressbar.start` for this progress bar.
		
		
		Separator
		"""
		pass
		
	


class Treeview:


	"""
	"""
	
	
	def __init__(self, ):
		pass
	
	def bbox(self, item,column=None):
		"""
		Returns the bounding box (relative to the treeview widget's window) of
		the specified *item* in the form (x, y, width, height).
		
		If *column* is specified, returns the bounding box of that cell. If the
		*item* is not visible (i.e., if it is a descendant of a closed item or is
		scrolled offscreen), returns an empty string.
		
		
		"""
		pass
		
	def get_children(self, item):
		"""
		Returns the list of children belonging to *item*.
		
		If *item* is not specified, returns root children.
		
		
		"""
		pass
		
	def set_children(self, item,newchildren):
		"""
		Replaces *item*'s child with *newchildren*.
		
		Children present in *item* that are not present in *newchildren* are
		detached from the tree. No items in *newchildren* may be an ancestor of
		*item*. Note that not specifying *newchildren* results in detaching
		*item*'s children.
		
		
		"""
		pass
		
	def column(self, column,option=None,kw):
		"""
		Query or modify the options for the specified *column*.
		
		If *kw* is not given, returns a dict of the column option values. If
		*option* is specified then the value for that *option* is returned.
		Otherwise, sets the options to the corresponding values.
		
		The valid options/values are:
		
		* id
		Returns the column name. This is a read-only option.
		* anchor: One of the standard Tk anchor values.
		Specifies how the text in this column should be aligned with respect
		to the cell.
		* minwidth: width
		The minimum width of the column in pixels. The treeview widget will
		not make the column any smaller than specified by this option when
		the widget is resized or the user drags a column.
		* stretch: True/False
		Specifies whether the column's width should be adjusted when
		the widget is resized.
		* width: width
		The width of the column in pixels.
		
		To configure the tree column, call this with column = "#0"
		
		"""
		pass
		
	def delete(self, items):
		"""
		Delete all specified *items* and all their descendants.
		
		The root item may not be deleted.
		
		
		"""
		pass
		
	def detach(self, items):
		"""
		Unlinks all of the specified *items* from the tree.
		
		The items and all of their descendants are still present, and may be
		reinserted at another point in the tree, but will not be displayed.
		
		The root item may not be detached.
		
		
		"""
		pass
		
	def exists(self, item):
		"""
		Returns True if the specified *item* is present in the tree.
		
		
		"""
		pass
		
	def focus(self, item=None):
		"""
		If *item* is specified, sets the focus item to *item*. Otherwise, returns
		the current focus item, or '' if there is none.
		
		
		"""
		pass
		
	def heading(self, column,option=None,kw):
		"""
		Query or modify the heading options for the specified *column*.
		
		If *kw* is not given, returns a dict of the heading option values. If
		*option* is specified then the value for that *option* is returned.
		Otherwise, sets the options to the corresponding values.
		
		The valid options/values are:
		
		* text: text
		The text to display in the column heading.
		* image: imageName
		Specifies an image to display to the right of the column heading.
		* anchor: anchor
		Specifies how the heading text should be aligned. One of the standard
		Tk anchor values.
		* command: callback
		A callback to be invoked when the heading label is pressed.
		
		To configure the tree column heading, call this with column = "#0".
		
		
		"""
		pass
		
	def identify(self, component,x,y):
		"""
		Returns a description of the specified *component* under the point given
		by *x* and *y*, or the empty string if no such *component* is present at
		that position.
		
		
		"""
		pass
		
	def identify_row(self, y):
		"""
		Returns the item ID of the item at position *y*.
		
		
		"""
		pass
		
	def identify_column(self, x):
		"""
		Returns the data column identifier of the cell at position *x*.
		
		The tree column has ID #0.
		
		
		"""
		pass
		
	def identify_region(self, x,y):
		"""
		Returns one of:
		
		+-----------+--------------------------------------+
		| region    | meaning                              |
		+===========+======================================+
		| heading   | Tree heading area.                   |
		+-----------+--------------------------------------+
		| separator | Space between two columns headings.  |
		+-----------+--------------------------------------+
		| tree      | The tree area.                       |
		+-----------+--------------------------------------+
		| cell      | A data cell.                         |
		+-----------+--------------------------------------+
		
		Availability: Tk 8.6.
		
		
		"""
		pass
		
	def identify_element(self, x,y):
		"""
		Returns the element at position *x*, *y*.
		
		Availability: Tk 8.6.
		
		
		"""
		pass
		
	def index(self, item):
		"""
		Returns the integer index of *item* within its parent's list of children.
		
		
		"""
		pass
		
	def insert(self, parent,index,iid=None,kw):
		"""
		Creates a new item and returns the item identifier of the newly created
		item.
		
		*parent* is the item ID of the parent item, or the empty string to create
		a new top-level item. *index* is an integer, or the value "end",
		specifying where in the list of parent's children to insert the new item.
		If *index* is less than or equal to zero, the new node is inserted at
		the beginning; if *index* is greater than or equal to the current number
		of children, it is inserted at the end. If *iid* is specified, it is used
		as the item identifier; *iid* must not already exist in the tree.
		Otherwise, a new unique identifier is generated.
		
		See `Item Options`_ for the list of available points.
		
		
		"""
		pass
		
	def item(self, item,option,kw):
		"""
		Query or modify the options for the specified *item*.
		
		If no options are given, a dict with options/values for the item is
		returned.
		If *option* is specified then the value for that option is returned.
		Otherwise, sets the options to the corresponding values as given by *kw*.
		
		
		"""
		pass
		
	def move(self, item,parent,index):
		"""
		Moves *item* to position *index* in *parent*'s list of children.
		
		It is illegal to move an item under one of its descendants. If *index* is
		less than or equal to zero, *item* is moved to the beginning; if greater
		than or equal to the number of children, it is moved to the end. If *item*
		was detached it is reattached.
		
		
		"""
		pass
		
	def next(self, item):
		"""
		Returns the identifier of *item*'s next sibling, or '' if *item* is the
		last child of its parent.
		
		
		"""
		pass
		
	def parent(self, item):
		"""
		Returns the ID of the parent of *item*, or '' if *item* is at the top
		level of the hierarchy.
		
		
		"""
		pass
		
	def prev(self, item):
		"""
		Returns the identifier of *item*'s previous sibling, or '' if *item* is
		the first child of its parent.
		
		
		"""
		pass
		
	def reattach(self, item,parent,index):
		"""
		An alias for :meth:`Treeview.move`.
		
		
		"""
		pass
		
	def see(self, item):
		"""
		Ensure that *item* is visible.
		
		Sets all of *item*'s ancestors open option to True, and scrolls the
		widget if necessary so that *item* is within the visible portion of
		the tree.
		
		
		"""
		pass
		
	def selection(self, selop=None,items=None):
		"""
		If *selop* is not specified, returns selected items. Otherwise, it will
		act according to the following selection methods.
		
		
		"""
		pass
		
	def selection_set(self, items):
		"""
		*items* becomes the new selection.
		
		
		"""
		pass
		
	def selection_add(self, items):
		"""
		Add *items* to the selection.
		
		
		"""
		pass
		
	def selection_remove(self, items):
		"""
		Remove *items* from the selection.
		
		
		"""
		pass
		
	def selection_toggle(self, items):
		"""
		Toggle the selection state of each item in *items*.
		
		
		"""
		pass
		
	def set(self, item,column=None,value=None):
		"""
		With one argument, returns a dictionary of column/value pairs for the
		specified *item*. With two arguments, returns the current value of the
		specified *column*. With three arguments, sets the value of given
		*column* in given *item* to the specified *value*.
		
		
		"""
		pass
		
	def tag_bind(self, tagname,sequence=None,callback=None):
		"""
		Bind a callback for the given event *sequence* to the tag *tagname*.
		When an event is delivered to an item, the callbacks for each of the
		item's tags option are called.
		
		
		"""
		pass
		
	def tag_configure(self, tagname,option=None,kw):
		"""
		Query or modify the options for the specified *tagname*.
		
		If *kw* is not given, returns a dict of the option settings for
		*tagname*. If *option* is specified, returns the value for that *option*
		for the specified *tagname*. Otherwise, sets the options to the
		corresponding values for the given *tagname*.
		
		
		"""
		pass
		
	def tag_has(self, tagname,item):
		"""
		If *item* is specified, returns 1 or 0 depending on whether the specified
		*item* has the given *tagname*. Otherwise, returns a list of all items
		that have the specified tag.
		
		Availability: Tk 8.6
		
		
		"""
		pass
		
	def xview(self, args):
		"""
		Query or modify horizontal position of the treeview.
		
		
		"""
		pass
		
	def yview(self, args):
		"""
		Query or modify vertical position of the treeview.
		
		
		.. tk Styling
		"""
		pass
		
	


class Style:


	"""
	This class is used to manipulate the style database.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def configure(self, style,query_opt=None,kw):
		"""
		Query or set the default value of the specified option(s) in *style*.
		
		Each key in *kw* is an option and each value is a string identifying
		the value for that option.
		
		For example, to change every default button to be a flat button with some
		padding and a different background color do::
		
		import ttk
		import Tkinter
		
		root = Tkinter.Tk()
		
		ttk.Style().configure("TButton", padding=6, relief="flat",
		background="#ccc")
		
		btn = ttk.Button(text="Sample")
		btn.pack()
		
		root.mainloop()
		
		
		"""
		pass
		
	def map(self, style,query_opt=None,kw):
		"""
		Query or sets dynamic values of the specified option(s) in *style*.
		
		Each key in *kw* is an option and each value should be a list or a
		tuple (usually) containing statespecs grouped in tuples, lists, or
		something else of your preference. A statespec is a compound of one
		or more states and then a value.
		
		An example::
		
		import Tkinter
		import ttk
		
		root = Tkinter.Tk()
		
		style = ttk.Style()
		style.map("C.TButton",
		foreground=[('pressed', 'red'), ('active', 'blue')],
		background=[('pressed', '!disabled', 'black'), ('active', 'white')]
		)
		
		colored_btn = ttk.Button(text="Test", style="C.TButton").pack()
		
		root.mainloop()
		
		
		Note that the order of the (states, value) sequences for an
		option matters.  In the previous example, if you change the
		order to ``[('active', 'blue'), ('pressed', 'red')]`` in the
		foreground option, for example, you would get a blue foreground
		when the widget is in the active or pressed states.
		
		"""
		pass
		
	def lookup(self, style,option,state=None,default=None):
		"""
		Returns the value specified for *option* in *style*.
		
		If *state* is specified, it is expected to be a sequence of one or more
		states. If the *default* argument is set, it is used as a fallback value
		in case no specification for option is found.
		
		To check what font a Button uses by default, do::
		
		import ttk
		
		print ttk.Style().lookup("TButton", "font")
		
		
		"""
		pass
		
	def layout(self, style,layoutspec=None):
		"""
		Define the widget layout for given *style*. If *layoutspec* is omitted,
		return the layout specification for given style.
		
		*layoutspec*, if specified, is expected to be a list or some other
		sequence type (excluding strings), where each item should be a tuple and
		the first item is the layout name and the second item should have the
		format described described in `Layouts`_.
		
		To understand the format, see the following example (it is not
		intended to do anything useful)::
		
		import ttk
		import Tkinter
		
		root = Tkinter.Tk()
		
		style = ttk.Style()
		style.layout("TMenubutton", [
		("Menubutton.background", None),
		("Menubutton.button", {"children":
		[("Menubutton.focus", {"children":
		[("Menubutton.padding", {"children":
		[("Menubutton.label", {"side": "left", "expand": 1})]
		})]
		})]
		}),
		])
		
		mbtn = ttk.Menubutton(text='Text')
		mbtn.pack()
		root.mainloop()
		
		
		"""
		pass
		
	def element_create(self, elementname,etype,args,kw):
		"""
		Create a new element in the current theme, of the given *etype* which is
		expected to be either "image", "from" or "vsapi". The latter is only
		available in Tk 8.6a for Windows XP and Vista and is not described here.
		
		If "image" is used, *args* should contain the default image name followed
		by statespec/value pairs (this is the imagespec), and *kw* may have the
		following options:
		
		* border=padding
		padding is a list of up to four integers, specifying the left, top,
		right, and bottom borders, respectively.
		
		* height=height
		Specifies a minimum height for the element. If less than zero, the
		base image's height is used as a default.
		
		* padding=padding
		Specifies the element's interior padding. Defaults to border's value
		if not specified.
		
		* sticky=spec
		Specifies how the image is placed within the final parcel. spec
		contains zero or more characters “n”, “s”, “w”, or “e”.
		
		* width=width
		Specifies a minimum width for the element. If less than zero, the
		base image's width is used as a default.
		
		If "from" is used as the value of *etype*,
		:meth:`element_create` will clone an existing
		element. *args* is expected to contain a themename, from which
		the element will be cloned, and optionally an element to clone from.
		If this element to clone from is not specified, an empty element will
		be used. *kw* is discarded.
		
		
		"""
		pass
		
	def element_names(self, ):
		"""
		Returns the list of elements defined in the current theme.
		
		
		"""
		pass
		
	def element_options(self, elementname):
		"""
		Returns the list of *elementname*'s options.
		
		
		"""
		pass
		
	def theme_create(self, themename,parent=None,settings=None):
		"""
		Create a new theme.
		
		It is an error if *themename* already exists. If *parent* is specified,
		the new theme will inherit styles, elements and layouts from the parent
		theme. If *settings* are present they are expected to have the same
		syntax used for :meth:`theme_settings`.
		
		
		"""
		pass
		
	def theme_settings(self, themename,settings):
		"""
		Temporarily sets the current theme to *themename*, apply specified
		*settings* and then restore the previous theme.
		
		Each key in *settings* is a style and each value may contain the keys
		'configure', 'map', 'layout' and 'element create' and they are expected
		to have the same format as specified by the methods
		:meth:`Style.configure`, :meth:`Style.map`, :meth:`Style.layout` and
		:meth:`Style.element_create` respectively.
		
		As an example, let's change the Combobox for the default theme a bit::
		
		import ttk
		import Tkinter
		
		root = Tkinter.Tk()
		
		style = ttk.Style()
		style.theme_settings("default", {
		"TCombobox": {
		"configure": {"padding": 5},
		"map": {
		"background": [("active", "green2"),
		("!disabled", "green4")],
		"fieldbackground": [("!disabled", "green3")],
		"foreground": [("focus", "OliveDrab1"),
		("!disabled", "OliveDrab2")]
		}
		}
		})
		
		combo = ttk.Combobox().pack()
		
		root.mainloop()
		
		
		"""
		pass
		
	def theme_names(self, ):
		"""
		Returns a list of all known themes.
		
		
		"""
		pass
		
	def theme_use(self, themename):
		"""
		If *themename* is not given, returns the theme in use.  Otherwise, sets
		the current theme to *themename*, refreshes all widgets and emits a
		<<ThemeChanged>> event.
		
		
		Layouts
		"""
		pass
		
	


