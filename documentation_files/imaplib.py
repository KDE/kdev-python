#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: IMAP4 protocol client (requires sockets).
"""
class IMAP4:


	"""
	This class implements the actual IMAP4 protocol.  The connection is created and
	protocol version (IMAP4 or IMAP4rev1) is determined when the instance is
	initialized. If *host* is not specified, ``''`` (the local host) is used. If
	*port* is omitted, the standard IMAP4 port (143) is used.
	
	Three exceptions are defined as attributes of the :class:`IMAP4` class:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def append(self, mailbox,flags,date_time,message):
		"""
		Append *message* to named mailbox.
		
		
		"""
		pass
		
	def authenticate(self, mechanism,authobject):
		"""
		Authenticate command --- requires response processing.
		
		*mechanism* specifies which authentication mechanism is to be used - it should
		appear in the instance variable ``capabilities`` in the form ``AUTH=mechanism``.
		
		*authobject* must be a callable object::
		
		data = authobject(response)
		
		It will be called to process server continuation responses. It should return
		``data`` that will be encoded and sent to server. It should return ``None`` if
		the client abort response ``*`` should be sent instead.
		
		
		"""
		pass
		
	def check(self, ):
		"""
		Checkpoint mailbox on server.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Close currently selected mailbox. Deleted messages are removed from writable
		mailbox. This is the recommended command before ``LOGOUT``.
		
		
		"""
		pass
		
	def copy(self, message_set,new_mailbox):
		"""
		Copy *message_set* messages onto end of *new_mailbox*.
		
		
		"""
		pass
		
	def create(self, mailbox):
		"""
		Create new mailbox named *mailbox*.
		
		
		"""
		pass
		
	def delete(self, mailbox):
		"""
		Delete old mailbox named *mailbox*.
		
		
		"""
		pass
		
	def deleteacl(self, mailbox,who):
		"""
		Delete the ACLs (remove any rights) set for who on mailbox.
		
		"""
		pass
		
	def expunge(self, ):
		"""
		Permanently remove deleted items from selected mailbox. Generates an ``EXPUNGE``
		response for each deleted message. Returned data contains a list of ``EXPUNGE``
		message numbers in order received.
		
		
		"""
		pass
		
	def fetch(self, message_set,message_parts):
		"""
		Fetch (parts of) messages.  *message_parts* should be a string of message part
		names enclosed within parentheses, eg: ``"(UID BODY[TEXT])"``.  Returned data
		are tuples of message part envelope and data.
		
		
		"""
		pass
		
	def getacl(self, mailbox):
		"""
		Get the ``ACL``\ s for *mailbox*. The method is non-standard, but is supported
		by the ``Cyrus`` server.
		
		
		"""
		pass
		
	def getannotation(self, mailbox,entry,attribute):
		"""
		Retrieve the specified ``ANNOTATION``\ s for *mailbox*. The method is
		non-standard, but is supported by the ``Cyrus`` server.
		
		"""
		pass
		
	def getquota(self, root):
		"""
		Get the ``quota`` *root*'s resource usage and limits. This method is part of the
		IMAP4 QUOTA extension defined in rfc2087.
		
		"""
		pass
		
	def getquotaroot(self, mailbox):
		"""
		Get the list of ``quota`` ``roots`` for the named *mailbox*. This method is part
		of the IMAP4 QUOTA extension defined in rfc2087.
		
		"""
		pass
		
	def list(self, directory,pattern):
		"""
		List mailbox names in *directory* matching *pattern*.  *directory* defaults to
		the top-level mail folder, and *pattern* defaults to match anything.  Returned
		data contains a list of ``LIST`` responses.
		
		
		"""
		pass
		
	def login(self, user,password):
		"""
		Identify the client using a plaintext password. The *password* will be quoted.
		
		
		"""
		pass
		
	def login_cram_md5(self, user,password):
		"""
		Force use of ``CRAM-MD5`` authentication when identifying the client to protect
		the password.  Will only work if the server ``CAPABILITY`` response includes the
		phrase ``AUTH=CRAM-MD5``.
		
		"""
		pass
		
	def logout(self, ):
		"""
		Shutdown connection to server. Returns server ``BYE`` response.
		
		
		"""
		pass
		
	def lsub(self, directory,pattern):
		"""
		List subscribed mailbox names in directory matching pattern. *directory*
		defaults to the top level directory and *pattern* defaults to match any mailbox.
		Returned data are tuples of message part envelope and data.
		
		
		"""
		pass
		
	def myrights(self, mailbox):
		"""
		Show my ACLs for a mailbox (i.e. the rights that I have on mailbox).
		
		"""
		pass
		
	def namespace(self, ):
		"""
		Returns IMAP namespaces as defined in RFC2342.
		
		"""
		pass
		
	def noop(self, ):
		"""
		Send ``NOOP`` to server.
		
		
		"""
		pass
		
	def open(self, host,port):
		"""
		Opens socket to *port* at *host*.  This method is implicitly called by
		the :class:`IMAP4` constructor.  The connection objects established by this
		method will be used in the ``read``, ``readline``, ``send``, and ``shutdown``
		methods.  You may override this method.
		
		
		"""
		pass
		
	def partial(self, message_num,message_part,start,length):
		"""
		Fetch truncated part of a message. Returned data is a tuple of message part
		envelope and data.
		
		
		"""
		pass
		
	def proxyauth(self, user):
		"""
		Assume authentication as *user*. Allows an authorised administrator to proxy
		into any user's mailbox.
		
		"""
		pass
		
	def read(self, size):
		"""
		Reads *size* bytes from the remote server. You may override this method.
		
		
		"""
		pass
		
	def readline(self, ):
		"""
		Reads one line from the remote server. You may override this method.
		
		
		"""
		pass
		
	def recent(self, ):
		"""
		Prompt server for an update. Returned data is ``None`` if no new messages, else
		value of ``RECENT`` response.
		
		
		"""
		pass
		
	def rename(self, oldmailbox,newmailbox):
		"""
		Rename mailbox named *oldmailbox* to *newmailbox*.
		
		
		"""
		pass
		
	def response(self, code):
		"""
		Return data for response *code* if received, or ``None``. Returns the given
		code, instead of the usual type.
		
		
		"""
		pass
		
	def search(self, charset,criterion,more):
		"""
		Search mailbox for matching messages.  *charset* may be ``None``, in which case
		no ``CHARSET`` will be specified in the request to the server.  The IMAP
		protocol requires that at least one criterion be specified; an exception will be
		raised when the server returns an error.
		
		Example::
		
		# M is a connected IMAP4 instance*more
		typ, msgnums = M.search(None, 'FROM', '"LDJ"')
		
		# or:
		typ, msgnums = M.search(None, '(FROM "LDJ")')
		
		
		"""
		pass
		
	def select(self, mailbox,readonly):
		"""
		Select a mailbox. Returned data is the count of messages in *mailbox*
		(``EXISTS`` response).  The default *mailbox* is ``'INBOX'``.  If the *readonly*
		flag is set, modifications to the mailbox are not allowed.
		
		
		"""
		pass
		
	def send(self, data):
		"""
		Sends ``data`` to the remote server. You may override this method.
		
		
		"""
		pass
		
	def setacl(self, mailbox,who,what):
		"""
		Set an ``ACL`` for *mailbox*. The method is non-standard, but is supported by
		the ``Cyrus`` server.
		
		
		"""
		pass
		
	def setannotation(self, mailbox,entry,attribute,more):
		"""
		Set ``ANNOTATION``\ s for *mailbox*. The method is non-standard, but is
		supported by the ``Cyrus`` server.
		
		"""
		pass
		
	def setquota(self, root,limits):
		"""
		Set the ``quota`` *root*'s resource *limits*. This method is part of the IMAP4
		QUOTA extension defined in rfc2087.
		
		"""
		pass
		
	def shutdown(self, ):
		"""
		Close connection established in ``open``.  This method is implicitly
		called by :meth:`IMAP4.logout`.  You may override this method.
		
		
		"""
		pass
		
	def socket(self, ):
		"""
		Returns socket instance used to connect to server.
		
		
		"""
		pass
		
	def sort(self, sort_criteria,charset,search_criterion,more):
		"""
		The ``sort`` command is a variant of ``search`` with sorting semantics for the
		results.  Returned data contains a space separated list of matching message
		numbers.
		
		Sort has two arguments before the *search_criterion* argument(s); a
		parenthesized list of *sort_criteria*, and the searching *charset*.  Note that
		unlike ``search``, the searching *charset* argument is mandatory.  There is also
		a ``uid sort`` command which corresponds to ``sort`` the way that ``uid search``
		corresponds to ``search``.  The ``sort`` command first searches the mailbox for
		messages that match the given searching criteria using the charset argument for
		the interpretation of strings in the searching criteria.  It then returns the
		numbers of matching messages.
		
		This is an ``IMAP4rev1`` extension command.
		
		
		"""
		pass
		
	def status(self, mailbox,names):
		"""
		Request named status conditions for *mailbox*.
		
		
		"""
		pass
		
	def store(self, message_set,command,flag_list):
		"""
		Alters flag dispositions for messages in mailbox.  *command* is specified by
		section 6.4.6 of :rfc:`2060` as being one of "FLAGS", "+FLAGS", or "-FLAGS",
		optionally with a suffix of ".SILENT".
		
		For example, to set the delete flag on all messages::
		
		typ, data = M.search(None, 'ALL')
		for num in data[0].split():
		M.store(num, '+FLAGS', '\\Deleted')
		M.expunge()
		
		
		"""
		pass
		
	def subscribe(self, mailbox):
		"""
		Subscribe to new mailbox.
		
		
		"""
		pass
		
	def thread(self, threading_algorithm,charset,search_criterion,more):
		"""
		The ``thread`` command is a variant of ``search`` with threading semantics for
		the results.  Returned data contains a space separated list of thread members.
		
		Thread members consist of zero or more messages numbers, delimited by spaces,
		indicating successive parent and child.
		
		Thread has two arguments before the *search_criterion* argument(s); a
		*threading_algorithm*, and the searching *charset*.  Note that unlike
		``search``, the searching *charset* argument is mandatory.  There is also a
		``uid thread`` command which corresponds to ``thread`` the way that ``uid
		search`` corresponds to ``search``.  The ``thread`` command first searches the
		mailbox for messages that match the given searching criteria using the charset
		argument for the interpretation of strings in the searching criteria. It then
		returns the matching messages threaded according to the specified threading
		algorithm.
		
		This is an ``IMAP4rev1`` extension command.
		
		"""
		pass
		
	def uid(self, command,arg,more):
		"""
		Execute command args with messages identified by UID, rather than message
		number.  Returns response appropriate to command.  At least one argument must be
		supplied; if none are provided, the server will return an error and an exception
		will be raised.
		
		
		"""
		pass
		
	def unsubscribe(self, mailbox):
		"""
		Unsubscribe from old mailbox.
		
		
		"""
		pass
		
	def xatom(self, name,arg,more):
		"""
		Allow simple extension commands notified by server in ``CAPABILITY`` response.
		
		Instances of :class:`IMAP4_SSL` have just one additional method:
		
		
		"""
		pass
		
	


class IMAP4_SSL:


	"""
	This is a subclass derived from :class:`IMAP4` that connects over an SSL
	encrypted socket (to use this class you need a socket module that was compiled
	with SSL support).  If *host* is not specified, ``''`` (the local host) is used.
	If *port* is omitted, the standard IMAP4-over-SSL port (993) is used.  *keyfile*
	and *certfile* are also optional - they can contain a PEM formatted private key
	and certificate chain file for the SSL connection.
	
	The second subclass allows for connections created by a child process:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def ssl(self, ):
		"""
		Returns SSLObject instance used for the secure connection with the server.
		
		The following attributes are defined on instances of :class:`IMAP4`:
		
		
		"""
		pass
		
	


class IMAP4_stream:


	"""
	This is a subclass derived from :class:`IMAP4` that connects to the
	``stdin/stdout`` file descriptors created by passing *command* to
	``os.popen2()``.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def Internaldate2tuple(self, datestr):
		"""
		Parse an IMAP4 ``INTERNALDATE`` string and return corresponding local
		time.  The return value is a :class:`time.struct_time` instance or
		None if the string has wrong format.
		
		"""
		pass
		
	def Int2AP(self, num):
		"""
		Converts an integer into a string representation using characters from the set
		"""
		pass
		
	def ParseFlags(self, flagstr):
		"""
		Converts an IMAP4 ``FLAGS`` response to a tuple of individual flags.
		
		
		"""
		pass
		
	def Time2Internaldate(self, date_time):
		"""
		Convert *date_time* to an IMAP4 ``INTERNALDATE`` representation.  The
		return value is a string in the form: ``"DD-Mmm-YYYY HH:MM:SS
		+HHMM"`` (including double-quotes).  The *date_time* argument can be a
		number (int or float) representing seconds since epoch (as returned
		by :func:`time.time`), a 9-tuple representing local time (as returned by
		:func:`time.localtime`), or a double-quoted string.  In the last case, it
		is assumed to already be in the correct format.
		
		Note that IMAP4 message numbers change as the mailbox changes; in particular,
		after an ``EXPUNGE`` command performs deletions the remaining messages are
		renumbered. So it is highly advisable to use UIDs instead, with the UID command.
		
		At the end of the module, there is a test section that contains a more extensive
		example of usage.
		
		
		"""
		pass
		
	


