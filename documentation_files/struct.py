#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Interpret strings as packed binary data.

"""
def pack(fmt,v1,v2,more):
	"""
	Return a string containing the values ``v1, v2, *more`` packed according to the
	given format.  The arguments must match the values required by the format
	exactly.
	
	
	"""
	pass
	
def pack_into(fmt,buffer,offset,v1,v2,more):
	"""
	Pack the values ``v1, v2, *more`` according to the given format, write the
	packed bytes into the writable *buffer* starting at *offset*. Note that the
	offset is a required argument.
	
	"""
	pass
	
def unpack(fmt,string):
	"""
	Unpack the string (presumably packed by ``pack(fmt, *more)``) according to the
	given format.  The result is a tuple even if it contains exactly one item.
	The string must contain exactly the amount of data required by the format
	(``len(string)`` must equal ``calcsize(fmt)``).
	
	
	"""
	pass
	
def unpack__from(fmt,buffer,offset=0):
	"""
	Unpack the *buffer* according to the given format. The result is a tuple even
	if it contains exactly one item. The *buffer* must contain at least the
	amount of data required by the format (``len(buffer[offset:])`` must be at
	least ``calcsize(fmt)``).
	
	"""
	pass
	
def calcsize(fmt):
	"""
	Return the size of the struct (and hence of the string) corresponding to the
	given format.
	
	.. ormat Strings
	--------------
	
	Format strings are the mechanism used to specify the expected layout when
	packing and unpacking data.  They are built up from :ref:`format-characters`,
	which specify the type of data being packed/unpacked.  In addition, there are
	special characters for controlling the :ref:`struct-alignment`.
	
	
	.. yte Order, Size, and Alignment
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	
	By default, C types are represented in the machine's native format and byte
	order, and properly aligned by skipping pad bytes if necessary (according to the
	rules used by the C compiler).
	
	Alternatively, the first character of the format string can be used to indicate
	the byte order, size and alignment of the packed data, according to the
	following table:
	
	+-----------+------------------------+----------+-----------+
	| Character | Byte order             | Size     | Alignment |
	+===========+========================+==========+===========+
	| ``@``     | native                 | native   | native    |
	+-----------+------------------------+----------+-----------+
	| ``=``     | native                 | standard | none      |
	+-----------+------------------------+----------+-----------+
	| ``<``     | little-endian          | standard | none      |
	+-----------+------------------------+----------+-----------+
	| ``>``     | big-endian             | standard | none      |
	+-----------+------------------------+----------+-----------+
	| ``!``     | network (= big-endian) | standard | none      |
	+-----------+------------------------+----------+-----------+
	
	If the first character is not one of these, ``'@'`` is assumed.
	
	Native byte order is big-endian or little-endian, depending on the host
	system. For example, Intel x86 and AMD64 (x86-64) are little-endian;
	Motorola 68000 and PowerPC G5 are big-endian; ARM and Intel Itanium feature
	switchable endianness (bi-endian). Use ``sys.byteorder`` to check the
	endianness of your system.
	
	Native size and alignment are determined using the C compiler's
	``sizeof`` expression.  This is always combined with native byte order.
	
	Standard size depends only on the format character;  see the table in
	the :ref:`format-characters` section.
	
	Note the difference between ``'@'`` and ``'='``: both use native byte order, but
	the size and alignment of the latter is standardized.
	
	The form ``'!'`` is available for those poor souls who claim they can't remember
	whether network byte order is big-endian or little-endian.
	
	There is no way to indicate non-native byte order (force byte-swapping); use the
	appropriate choice of ``'<'`` or ``'>'``.
	
	Notes:
	
	(1) Padding is only automatically added between successive structure members.
	No padding is added at the beginning or the end of the encoded struct.
	
	(2) No padding is added when using non-native size and alignment, e.g.
	with '<', '>', '=', and '!'.
	
	(3) To align the end of a structure to the alignment requirement of a
	particular type, end the format with the code for that type with a repeat
	count of zero.  See :ref:`struct-examples`.
	
	
	.. ormat Characters
	^^^^^^^^^^^^^^^^^
	
	Format characters have the following meaning; the conversion between C and
	Python values should be obvious given their types.  The 'Standard size' column
	refers to the size of the packed value in bytes when using standard size; that
	is, when the format string starts with one of ``'<'``, ``'>'``, ``'!'`` or
	``'='``.  When using native size, the size of the packed value is
	platform-dependent.
	
	+--------+-------------------------+--------------------+----------------+------------+
	| Format | C Type                  | Python type        | Standard size  | Notes      |
	+========+=========================+====================+================+============+
	| ``x``  | pad byte                | no value           |                |            |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``c``  | :ctype:`char`           | string of length 1 | 1              |            |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``b``  | :ctype:`signed char`    | integer            | 1              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``B``  | :ctype:`unsigned char`  | integer            | 1              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``?``  | :ctype:`_Bool`          | bool               | 1              | \(1)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``h``  | :ctype:`short`          | integer            | 2              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``H``  | :ctype:`unsigned short` | integer            | 2              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``i``  | :ctype:`int`            | integer            | 4              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``I``  | :ctype:`unsigned int`   | integer            | 4              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``l``  | :ctype:`long`           | integer            | 4              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``L``  | :ctype:`unsigned long`  | integer            | 4              | \(3)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``q``  | :ctype:`long long`      | integer            | 8              | \(2), \(3) |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``Q``  | :ctype:`unsigned long   | integer            | 8              | \(2), \(3) |
	|        | long`                   |                    |                |            |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``f``  | :ctype:`float`          | float              | 4              | \(4)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``d``  | :ctype:`double`         | float              | 8              | \(4)       |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``s``  | :ctype:`char[]`         | string             |                |            |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``p``  | :ctype:`char[]`         | string             |                |            |
	+--------+-------------------------+--------------------+----------------+------------+
	| ``P``  | :ctype:`void \*`        | integer            |                | \(5), \(3) |
	+--------+-------------------------+--------------------+----------------+------------+
	
	Notes:
	
	(1)
	The ``'?'`` conversion code corresponds to the :ctype:`_Bool` type defined by
	C99. If this type is not available, it is simulated using a :ctype:`char`. In
	standard mode, it is always represented by one byte.
	
	"""
	pass
	
class Struct:


	"""
	Return a new Struct object which writes and reads binary data according to
	the format string *format*.  Creating a Struct object once and calling its
	methods is more efficient than calling the :mod:`struct` functions with the
	same format since the format string only needs to be compiled once.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def pack(self, v1,v2,more):
		"""
		Identical to the :func:`pack` function, using the compiled format.
		(``len(result)`` will equal :attr:`self.size`.)
		
		
		"""
		pass
		
	def pack_into(self, buffer,offset,v1,v2,more):
		"""
		Identical to the :func:`pack_into` function, using the compiled format.
		
		
		"""
		pass
		
	def unpack(self, string):
		"""
		Identical to the :func:`unpack` function, using the compiled format.
		(``len(string)`` must equal :attr:`self.size`).
		
		
		"""
		pass
		
	def unpack__from(self, buffer,offset=0):
		"""
		Identical to the :func:`unpack_from` function, using the compiled format.
		(``len(buffer[offset:])`` must be at least :attr:`self.size`).
		
		
		"""
		pass
		
	


