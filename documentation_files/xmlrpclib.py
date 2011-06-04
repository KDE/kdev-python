#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: XML-RPC client access.
"""
class ServerProxy:


	"""
	A :class:`ServerProxy` instance is an object that manages communication with a
	remote XML-RPC server.  The required first argument is a URI (Uniform Resource
	Indicator), and will normally be the URL of the server.  The optional second
	argument is a transport factory instance; by default it is an internal
	:class:`SafeTransport` instance for https: URLs and an internal HTTP
	:class:`Transport` instance otherwise.  The optional third argument is an
	encoding, by default UTF-8. The optional fourth argument is a debugging flag.
	If *allow_none* is true,  the Python constant ``None`` will be translated into
	XML; the default behaviour is for ``None`` to raise a :exc:`TypeError`. This is
	a commonly-used extension to the XML-RPC specification, but isn't supported by
	all clients and servers; see http://ontosys.com/xml-rpc/extensions.php for a
	description.  The *use_datetime* flag can be used to cause date/time values to
	be presented as :class:`datetime.datetime` objects; this is false by default.
	:class:`datetime.datetime` objects may be passed to calls.
	
	Both the HTTP and HTTPS transports support the URL syntax extension for HTTP
	Basic Authentication: ``http://user:pass@host:port/path``.  The  ``user:pass``
	portion will be base64-encoded as an HTTP 'Authorization' header, and sent to
	the remote server as part of the connection process when invoking an XML-RPC
	method.  You only need to use this if the remote server requires a Basic
	Authentication user and password.
	
	The returned instance is a proxy object with methods that can be used to invoke
	corresponding RPC calls on the remote server.  If the remote server supports the
	introspection API, the proxy can also be used to query the remote server for the
	methods it supports (service discovery) and fetch other server-associated
	metadata.
	
	:class:`ServerProxy` instance methods take Python basic types and objects as
	arguments and return Python basic types and classes.  Types that are conformable
	(e.g. that can be marshalled through XML), include the following (and except
	where noted, they are unmarshalled as the same Python type):
	
	+---------------------------------+---------------------------------------------+
	| Name                            | Meaning                                     |
	+=================================+=============================================+
	| :const:`boolean`                | The :const:`True` and :const:`False`        |
	|                                 | constants                                   |
	+---------------------------------+---------------------------------------------+
	| :const:`integers`               | Pass in directly                            |
	+---------------------------------+---------------------------------------------+
	| :const:`floating-point numbers` | Pass in directly                            |
	+---------------------------------+---------------------------------------------+
	| :const:`strings`                | Pass in directly                            |
	+---------------------------------+---------------------------------------------+
	| :const:`arrays`                 | Any Python sequence type containing         |
	|                                 | conformable elements. Arrays are returned   |
	|                                 | as lists                                    |
	+---------------------------------+---------------------------------------------+
	| :const:`structures`             | A Python dictionary. Keys must be strings,  |
	|                                 | values may be any conformable type. Objects |
	|                                 | of user-defined classes can be passed in;   |
	|                                 | only their *__dict__* attribute is          |
	|                                 | transmitted.                                |
	+---------------------------------+---------------------------------------------+
	| :const:`dates`                  | in seconds since the epoch (pass in an      |
	|                                 | instance of the :class:`DateTime` class) or |
	|                                 | a :class:`datetime.datetime` instance.      |
	+---------------------------------+---------------------------------------------+
	| :const:`binary data`            | pass in an instance of the :class:`Binary`  |
	|                                 | wrapper class                               |
	+---------------------------------+---------------------------------------------+
	
	This is the full set of data types supported by XML-RPC.  Method calls may also
	raise a special :exc:`Fault` instance, used to signal XML-RPC server errors, or
	:exc:`ProtocolError` used to signal an error in the HTTP/HTTPS transport layer.
	Both :exc:`Fault` and :exc:`ProtocolError` derive from a base class called
	:exc:`Error`.  Note that even though starting with Python 2.2 you can subclass
	built-in types, the xmlrpclib module currently does not marshal instances of such
	subclasses.
	
	When passing strings, characters special to XML such as ``<``, ``>``, and ``&``
	will be automatically escaped.  However, it's the caller's responsibility to
	ensure that the string is free of characters that aren't allowed in XML, such as
	the control characters with ASCII values between 0 and 31 (except, of course,
	tab, newline and carriage return); failing to do this will result in an XML-RPC
	request that isn't well-formed XML.  If you have to pass arbitrary strings via
	XML-RPC, use the :class:`Binary` wrapper class described below.
	
	:class:`Server` is retained as an alias for :class:`ServerProxy` for backwards
	compatibility.  New code should use :class:`ServerProxy`.
	
	"""
	
	
	def __init__(self, uri,transport,encoding,verbose,allow_none,use_datetime):
		pass
	
	


class MultiCall:


	"""
	Create an object used to boxcar method calls. *server* is the eventual target of
	the call. Calls can be made to the result object, but they will immediately
	return ``None``, and only store the call name and parameters in the
	:class:`MultiCall` object. Calling the object itself causes all stored calls to
	be transmitted as a single ``system.multicall`` request. The result of this call
	is a :term:`generator`; iterating over this generator yields the individual
	results.
	
	A usage example of this class follows.  The server code ::
	
	from SimpleXMLRPCServer import SimpleXMLRPCServer
	
	def add(x,y):
	return x+y
	
	def subtract(x, y):
	return x-y
	
	def multiply(x, y):
	return x*y
	
	def divide(x, y):
	return x/y
	
	# A simple server with simple arithmetic functions
	server = SimpleXMLRPCServer(("localhost", 8000))
	print "Listening on port 8000*more"
	server.register_multicall_functions()
	server.register_function(add, 'add')
	server.register_function(subtract, 'subtract')
	server.register_function(multiply, 'multiply')
	server.register_function(divide, 'divide')
	server.serve_forever()
	
	The client code for the preceding server::
	
	import xmlrpclib
	
	proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
	multicall = xmlrpclib.MultiCall(proxy)
	multicall.add(7,3)
	multicall.subtract(7,3)
	multicall.multiply(7,3)
	multicall.divide(7,3)
	result = multicall()
	
	print "7+3=%d, 7-3=%d, 7*3=%d, 7/3=%d" % tuple(result)
	
	
	Convenience Functions
	---------------------
	
	
	"""
	
	
	def __init__(self, server):
		pass
	
	def boolean(value):
		"""
		Convert any Python value to one of the XML-RPC Boolean constants, ``True`` or
		``False``.
		
		
		"""
		pass
		
	def dumps(params,methodname,methodresponse,encoding,allow_none):
		"""
		Convert *params* into an XML-RPC request. or into a response if *methodresponse*
		is true. *params* can be either a tuple of arguments or an instance of the
		:exc:`Fault` exception class.  If *methodresponse* is true, only a single value
		can be returned, meaning that *params* must be of length 1. *encoding*, if
		supplied, is the encoding to use in the generated XML; the default is UTF-8.
		Python's :const:`None` value cannot be used in standard XML-RPC; to allow using
		it via an extension,  provide a true value for *allow_none*.
		
		
		"""
		pass
		
	def loads(data,use_datetime):
		"""
		Convert an XML-RPC request or response into Python objects, a ``(params,
		methodname)``.  *params* is a tuple of argument; *methodname* is a string, or
		``None`` if no method name is present in the packet. If the XML-RPC packet
		represents a fault condition, this function will raise a :exc:`Fault` exception.
		The *use_datetime* flag can be used to cause date/time values to be presented as
		:class:`datetime.datetime` objects; this is false by default.
		
		"""
		pass
		
	


