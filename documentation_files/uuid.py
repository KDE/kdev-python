#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: UUID objects (universally unique identifiers) according to RFC 4122
"""
class UUID:


	"""
	Create a UUID from either a string of 32 hexadecimal digits, a string of 16
	bytes as the *bytes* argument, a string of 16 bytes in little-endian order as
	the *bytes_le* argument, a tuple of six integers (32-bit *time_low*, 16-bit
	*time_mid*, 16-bit *time_hi_version*, 8-bit *clock_seq_hi_variant*, 8-bit
	*clock_seq_low*, 48-bit *node*) as the *fields* argument, or a single 128-bit
	integer as the *int* argument.  When a string of hex digits is given, curly
	braces, hyphens, and a URN prefix are all optional.  For example, these
	expressions all yield the same UUID::
	
	UUID('{12345678-1234-5678-1234-567812345678}')
	UUID('12345678123456781234567812345678')
	UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
	UUID(bytes='\x12\x34\x56\x78'*4)
	UUID(bytes_le='\x78\x56\x34\x12\x34\x12\x78\x56' +
	'\x12\x34\x56\x78\x12\x34\x56\x78')
	UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
	UUID(int=0x12345678123456781234567812345678)
	
	Exactly one of *hex*, *bytes*, *bytes_le*, *fields*, or *int* must be given.
	The *version* argument is optional; if given, the resulting UUID will have its
	variant and version number set according to RFC 4122, overriding bits in the
	given *hex*, *bytes*, *bytes_le*, *fields*, or *int*.
	
	:class:`UUID` instances have these read-only attributes:
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def getnode(self, ):
		"""
		Get the hardware address as a 48-bit positive integer.  The first time this
		runs, it may launch a separate program, which could be quite slow.  If all
		attempts to obtain the hardware address fail, we choose a random 48-bit number
		with its eighth bit set to 1 as recommended in RFC 4122.  "Hardware address"
		means the MAC address of a network interface, and on a machine with multiple
		network interfaces the MAC address of any one of them may be returned.
		
		"""
		pass
		
	def uuid1(self, node,clock_seq):
		"""
		Generate a UUID from a host ID, sequence number, and the current time. If *node*
		is not given, :func:`getnode` is used to obtain the hardware address. If
		*clock_seq* is given, it is used as the sequence number; otherwise a random
		14-bit sequence number is chosen.
		
		"""
		pass
		
	def uuid3(self, namespace,name):
		"""
		Generate a UUID based on the MD5 hash of a namespace identifier (which is a
		UUID) and a name (which is a string).
		
		"""
		pass
		
	def uuid4(self, ):
		"""
		Generate a random UUID.
		
		"""
		pass
		
	def uuid5(self, namespace,name):
		"""
		Generate a UUID based on the SHA-1 hash of a namespace identifier (which is a
		UUID) and a name (which is a string).
		
		"""
		pass
		
	"""
	When this namespace is specified, the *name* string is a fully-qualified domain
	name.
	
	
	"""
	NAMESPACE_DNS = None
	"""
	When this namespace is specified, the *name* string is a URL.
	
	
	"""
	NAMESPACE_URL = None
	"""
	When this namespace is specified, the *name* string is an ISO OID.
	
	
	"""
	NAMESPACE_OID = None
	"""
	When this namespace is specified, the *name* string is an X.500 DN in DER or a
	text output format.
	
	The :mod:`uuid` module defines the following constants for the possible values
	of the :attr:`variant` attribute:
	
	
	"""
	NAMESPACE_X500 = None
	"""
	Reserved for NCS compatibility.
	
	
	"""
	RESERVED_NCS = None
	"""
	Specifies the UUID layout given in :rfc:`4122`.
	
	
	"""
	RFC_4122 = None
	"""
	Reserved for Microsoft compatibility.
	
	
	"""
	RESERVED_MICROSOFT = None
	"""
	Reserved for future definition.
	
	
	"""
	RESERVED_FUTURE = None
	


