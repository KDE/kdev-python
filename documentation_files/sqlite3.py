#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A DB-API 2.0 implementation using SQLite 3.x.
"""
"""
This constant is meant to be used with the *detect_types* parameter of the
:func:`connect` function.

Setting it makes the :mod:`sqlite3` module parse the declared type for each
column it returns.  It will parse out the first word of the declared type,
i. e.  for "integer primary key", it will parse out "integer", or for
"number(10)" it will parse out "number". Then for that column, it will look
into the converters dictionary and use the converter function registered for
that type there.


"""
PARSE_DECLTYPES = None
"""
This constant is meant to be used with the *detect_types* parameter of the
:func:`connect` function.

Setting this makes the SQLite interface parse the column name for each column it
returns.  It will look for a string formed [mytype] in there, and then decide
that 'mytype' is the type of the column. It will try to find an entry of
'mytype' in the converters dictionary and then use the converter function found
there to return the value. The column name found in :attr:`Cursor.description`
is only the first word of the column name, i.  e. if you use something like
``'as "x [datetime]"'`` in your SQL, then we will parse out everything until the
first blank for the column name: the column name would simply be "x".


"""
PARSE_COLNAMES = None
def connect(database,timeout,detect_types,isolation_level,check_same_thread,factory,cached_statements):
	"""
	Opens a connection to the SQLite database file *database*. You can use
	``":memory:"`` to open a database connection to a database that resides in RAM
	instead of on disk.
	
	When a database is accessed by multiple connections, and one of the processes
	modifies the database, the SQLite database is locked until that transaction is
	committed. The *timeout* parameter specifies how long the connection should wait
	for the lock to go away until raising an exception. The default for the timeout
	parameter is 5.0 (five seconds).
	
	For the *isolation_level* parameter, please see the
	:attr:`Connection.isolation_level` property of :class:`Connection` objects.
	
	SQLite natively supports only the types TEXT, INTEGER, FLOAT, BLOB and NULL. If
	you want to use other types you must add support for them yourself. The
	*detect_types* parameter and the using custom **converters** registered with the
	module-level :func:`register_converter` function allow you to easily do that.
	
	*detect_types* defaults to 0 (i. e. off, no type detection), you can set it to
	any combination of :const:`PARSE_DECLTYPES` and :const:`PARSE_COLNAMES` to turn
	type detection on.
	
	By default, the :mod:`sqlite3` module uses its :class:`Connection` class for the
	connect call.  You can, however, subclass the :class:`Connection` class and make
	:func:`connect` use your class instead by providing your class for the *factory*
	parameter.
	
	Consult the section :ref:`sqlite3-types` of this manual for details.
	
	The :mod:`sqlite3` module internally uses a statement cache to avoid SQL parsing
	overhead. If you want to explicitly set the number of statements that are cached
	for the connection, you can set the *cached_statements* parameter. The currently
	implemented default is to cache 100 statements.
	
	
	"""
	pass
	
def register_converter(typename,callable):
	"""
	Registers a callable to convert a bytestring from the database into a custom
	Python type. The callable will be invoked for all database values that are of
	the type *typename*. Confer the parameter *detect_types* of the :func:`connect`
	function for how the type detection works. Note that the case of *typename* and
	the name of the type in your query must match!
	
	
	"""
	pass
	
def register_adapter(type,callable):
	"""
	Registers a callable to convert the custom Python type *type* into one of
	SQLite's supported types. The callable *callable* accepts as single parameter
	the Python value, and must return a value of the following types: int, long,
	float, str (UTF-8 encoded), unicode or buffer.
	
	
	"""
	pass
	
def complete_statement(sql):
	"""
	Returns :const:`True` if the string *sql* contains one or more complete SQL
	statements terminated by semicolons. It does not verify that the SQL is
	syntactically correct, only that there are no unclosed string literals and the
	statement is terminated by a semicolon.
	
	This can be used to build a shell for SQLite, as in the following example:
	
	
	"""
	pass
	
def enable_callback_tracebacks(flag):
	"""
	By default you will not get any tracebacks in user-defined functions,
	aggregates, converters, authorizer callbacks etc. If you want to debug them, you
	can call this function with *flag* as True. Afterwards, you will get tracebacks
	from callbacks on ``sys.stderr``. Use :const:`False` to disable the feature
	again.
	
	
	.. onnection Objects
	------------------
	
	"""
	pass
	
class Connection:


	"""
	A SQLite database connection has the following attributes and methods:
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Cursor:


	"""
	A :class:`Cursor` instance has the following attributes and methods.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Row:


	"""
	A :class:`Row` instance serves as a highly optimized
	:attr:`~Connection.row_factory` for :class:`Connection` objects.
	It tries to mimic a tuple in most of its features.
	
	It supports mapping access by column name and index, iteration,
	representation, equality testing and :func:`len`.
	
	If two :class:`Row` objects have exactly the same columns and their
	members are equal, they compare equal.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


