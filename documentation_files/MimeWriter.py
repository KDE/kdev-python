#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Write MIME format files.
:deprecated:

"""
class MimeWriter:


	"""
	Return a new instance of the :class:`MimeWriter` class.  The only argument
	passed, *fp*, is a file object to be used for writing. Note that a
	:class:`StringIO` object could also be used.
	
	
	.. imeWriter Objects
	------------------
	
	:class:`MimeWriter` instances have the following methods:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def addheader(self, key,value,prefix):
		"""
		Add a header line to the MIME message. The *key* is the name of the header,
		where the *value* obviously provides the value of the header. The optional
		argument *prefix* determines where the header  is inserted; ``0`` means append
		at the end, ``1`` is insert at the start. The default is to append.
		
		
		"""
		pass
		
	def flushheaders(self, ):
		"""
		Causes all headers accumulated so far to be written out (and forgotten). This is
		useful if you don't need a body part at all, e.g. for a subpart of type
		:mimetype:`message/rfc822` that's (mis)used to store some header-like
		information.
		
		
		"""
		pass
		
	def startbody(self, ctype,plist,prefix):
		"""
		Returns a file-like object which can be used to write to the body of the
		message.  The content-type is set to the provided *ctype*, and the optional
		parameter *plist* provides additional parameters for the content-type
		declaration. *prefix* functions as in :meth:`addheader` except that the default
		is to insert at the start.
		
		
		"""
		pass
		
	def startmultipartbody(self, subtype,boundary,plist,prefix):
		"""
		Returns a file-like object which can be used to write to the body of the
		message.  Additionally, this method initializes the multi-part code, where
		*subtype* provides the multipart subtype, *boundary* may provide a user-defined
		boundary specification, and *plist* provides optional parameters for the
		subtype. *prefix* functions as in :meth:`startbody`.  Subparts should be created
		using :meth:`nextpart`.
		
		
		"""
		pass
		
	def nextpart(self, ):
		"""
		Returns a new instance of :class:`MimeWriter` which represents an individual
		part in a multipart message.  This may be used to write the  part as well as
		used for creating recursively complex multipart messages. The message must first
		be initialized with :meth:`startmultipartbody` before using :meth:`nextpart`.
		
		
		"""
		pass
		
	


