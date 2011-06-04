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
	
	def cursor(self, cursorClass):
		"""
		The cursor method accepts a single optional parameter *cursorClass*. If
		supplied, this must be a custom cursor class that extends
		:class:`sqlite3.Cursor`.
		
		
		"""
		pass
		
	def commit(self, ):
		"""
		This method commits the current transaction. If you don't call this method,
		anything you did since the last call to ``commit()`` is not visible from from
		other database connections. If you wonder why you don't see the data you've
		written to the database, please check you didn't forget to call this method.
		
		"""
		pass
		
	def rollback(self, ):
		"""
		This method rolls back any changes to the database since the last call to
		:meth:`commit`.
		
		"""
		pass
		
	def close(self, ):
		"""
		This closes the database connection. Note that this does not automatically
		call :meth:`commit`. If you just close your database connection without
		calling :meth:`commit` first, your changes will be lost!
		
		"""
		pass
		
	def execute(self, sql,parameters):
		"""
		This is a nonstandard shortcut that creates an intermediate cursor object by
		calling the cursor method, then calls the cursor's :meth:`execute
		<Cursor.execute>` method with the parameters given.
		
		
		"""
		pass
		
	def executemany(self, sql,parameters):
		"""
		This is a nonstandard shortcut that creates an intermediate cursor object by
		calling the cursor method, then calls the cursor's :meth:`executemany
		<Cursor.executemany>` method with the parameters given.
		
		"""
		pass
		
	def executescript(self, sql_script):
		"""
		This is a nonstandard shortcut that creates an intermediate cursor object by
		calling the cursor method, then calls the cursor's :meth:`executescript
		<Cursor.executescript>` method with the parameters given.
		
		
		"""
		pass
		
	def create_function(self, name,num_params,func):
		"""
		Creates a user-defined function that you can later use from within SQL
		statements under the function name *name*. *num_params* is the number of
		parameters the function accepts, and *func* is a Python callable that is called
		as the SQL function.
		
		The function can return any of the types supported by SQLite: unicode, str, int,
		long, float, buffer and None.
		
		Example:
		
		"""
		pass
		
	def create_aggregate(self, name,num_params,aggregate__class):
		"""
		Creates a user-defined aggregate function.
		
		The aggregate class must implement a ``step`` method, which accepts the number
		of parameters *num_params*, and a ``finalize`` method which will return the
		final result of the aggregate.
		
		The ``finalize`` method can return any of the types supported by SQLite:
		unicode, str, int, long, float, buffer and None.
		
		Example:
		
		"""
		pass
		
	def create_collation(self, name,callable):
		"""
		Creates a collation with the specified *name* and *callable*. The callable will
		be passed two string arguments. It should return -1 if the first is ordered
		lower than the second, 0 if they are ordered equal and 1 if the first is ordered
		higher than the second.  Note that this controls sorting (ORDER BY in SQL) so
		your comparisons don't affect other SQL operations.
		
		Note that the callable will get its parameters as Python bytestrings, which will
		normally be encoded in UTF-8.
		
		The following example shows a custom collation that sorts "the wrong way":
		
		"""
		pass
		
	def interrupt(self, ):
		"""
		You can call this method from a different thread to abort any queries that might
		be executing on the connection. The query will then abort and the caller will
		get an exception.
		
		
		"""
		pass
		
	def set_authorizer(self, authorizer_callback):
		"""
		This routine registers a callback. The callback is invoked for each attempt to
		access a column of a table in the database. The callback should return
		:const:`SQLITE_OK` if access is allowed, :const:`SQLITE_DENY` if the entire SQL
		statement should be aborted with an error and :const:`SQLITE_IGNORE` if the
		column should be treated as a NULL value. These constants are available in the
		:mod:`sqlite3` module.
		
		The first argument to the callback signifies what kind of operation is to be
		authorized. The second and third argument will be arguments or :const:`None`
		depending on the first argument. The 4th argument is the name of the database
		("main", "temp", etc.) if applicable. The 5th argument is the name of the
		inner-most trigger or view that is responsible for the access attempt or
		:const:`None` if this access attempt is directly from input SQL code.
		
		Please consult the SQLite documentation about the possible values for the first
		argument and the meaning of the second and third argument depending on the first
		one. All necessary constants are available in the :mod:`sqlite3` module.
		
		
		"""
		pass
		
	def set_progress_handler(self, handler,n):
		"""
		"""
		pass
		
	def enable_load_extension(self, enabled):
		"""
		"""
		pass
		
	def load_extension(self, path):
		"""
		"""
		pass
		
	


class Cursor:


	"""
	A :class:`Cursor` instance has the following attributes and methods.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def execute(self, sql,parameters):
		"""
		Executes an SQL statement. The SQL statement may be parametrized (i. e.
		placeholders instead of SQL literals). The :mod:`sqlite3` module supports two
		kinds of placeholders: question marks (qmark style) and named placeholders
		(named style).
		
		This example shows how to use parameters with qmark style:
		
		"""
		pass
		
	def executemany(self, sql,seq_of_parameters):
		"""
		Executes an SQL command against all parameter sequences or mappings found in
		the sequence *sql*.  The :mod:`sqlite3` module also allows using an
		:term:`iterator` yielding parameters instead of a sequence.
		
		"""
		pass
		
	def executescript(self, sql_script):
		"""
		This is a nonstandard convenience method for executing multiple SQL statements
		at once. It issues a ``COMMIT`` statement first, then executes the SQL script it
		gets as a parameter.
		
		*sql_script* can be a bytestring or a Unicode string.
		
		Example:
		
		"""
		pass
		
	def fetchone(self, ):
		"""
		Fetches the next row of a query result set, returning a single sequence,
		or :const:`None` when no more data is available.
		
		
		"""
		pass
		
	def fetchall(self, ):
		"""
		Fetches all (remaining) rows of a query result, returning a list.  Note that
		the cursor's arraysize attribute can affect the performance of this operation.
		An empty list is returned when no rows are available.
		
		
		"""
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
	
	def keys(self, ():
		"""
		This method returns a tuple of column names. Immediately after a query,
		it is the first member of each tuple in :attr:`Cursor.description`.
		
		"""
		pass
		
	


