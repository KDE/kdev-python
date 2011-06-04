#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A framework for network servers.

"""
class BaseServer:


	"""
	This is the superclass of all Server objects in the module.  It defines the
	interface, given below, but does not implement most of the methods, which is
	done in subclasses.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def fileno(self, ):
		"""
		Return an integer file descriptor for the socket on which the server is
		listening.  This function is most commonly passed to :func:`select.select`, to
		allow monitoring multiple servers in the same process.
		
		
		"""
		pass
		
	def handle_request(self, ):
		"""
		Process a single request.  This function calls the following methods in
		order: :meth:`get_request`, :meth:`verify_request`, and
		:meth:`process_request`.  If the user-provided :meth:`handle` method of the
		handler class raises an exception, the server's :meth:`handle_error` method
		will be called.  If no request is received within :attr:`self.timeout`
		seconds, :meth:`handle_timeout` will be called and :meth:`handle_request`
		will return.
		
		
		"""
		pass
		
	def shutdown(self, ):
		"""
		Tells the :meth:`serve_forever` loop to stop and waits until it does.
		
		"""
		pass
		
	def finish_request(self, ):
		"""
		Actually processes the request by instantiating :attr:`RequestHandlerClass` and
		calling its :meth:`handle` method.
		
		
		"""
		pass
		
	def get_request(self, ):
		"""
		Must accept a request from the socket, and return a 2-tuple containing the *new*
		socket object to be used to communicate with the client, and the client's
		address.
		
		
		"""
		pass
		
	def handle_error(self, request,client_address):
		"""
		This function is called if the :attr:`RequestHandlerClass`'s :meth:`handle`
		method raises an exception.  The default action is to print the traceback to
		standard output and continue handling further requests.
		
		
		"""
		pass
		
	def handle_timeout(self, ):
		"""
		This function is called when the :attr:`timeout` attribute has been set to a
		value other than :const:`None` and the timeout period has passed with no
		requests being received.  The default action for forking servers is
		to collect the status of any child processes that have exited, while
		in threading servers this method does nothing.
		
		
		"""
		pass
		
	def process_request(self, request,client_address):
		"""
		Calls :meth:`finish_request` to create an instance of the
		:attr:`RequestHandlerClass`.  If desired, this function can create a new process
		or thread to handle the request; the :class:`ForkingMixIn` and
		:class:`ThreadingMixIn` classes do this.
		
		
		.. ny point in documenting the following two functions?
		What would the purpose of overriding them be: initializing server
		instance variables, adding new network families?
		
		"""
		pass
		
	def server_activate(self, ):
		"""
		Called by the server's constructor to activate the server.  The default behavior
		just :meth:`listen`\ s to the server's socket. May be overridden.
		
		
		"""
		pass
		
	def server_bind(self, ):
		"""
		Called by the server's constructor to bind the socket to the desired address.
		May be overridden.
		
		
		"""
		pass
		
	def verify_request(self, request,client_address):
		"""
		Must return a Boolean value; if the value is :const:`True`, the request will be
		processed, and if it's :const:`False`, the request will be denied. This function
		can be overridden to implement access controls for a server. The default
		implementation always returns :const:`True`.
		
		
		RequestHandler Objects
		----------------------
		
		The request handler class must define a new :meth:`handle` method, and can
		override any of the following methods.  A new instance is created for each
		request.
		
		
		"""
		pass
		
	


