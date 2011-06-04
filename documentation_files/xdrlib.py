#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Encoders and decoders for the External Data Representation (XDR).


"""
class Packer:


	"""
	:class:`Packer` is the class for packing data into XDR representation. The
	:class:`Packer` class is instantiated with no arguments.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def get_buffer(self, ):
		"""
		Returns the current pack buffer as a string.
		
		
		"""
		pass
		
	def reset(self, ):
		"""
		Resets the pack buffer to the empty string.
		
		In general, you can pack any of the most common XDR data types by calling the
		appropriate ``pack_type()`` method.  Each method takes a single argument, the
		value to pack.  The following simple data type packing methods are supported:
		:meth:`pack_uint`, :meth:`pack_int`, :meth:`pack_enum`, :meth:`pack_bool`,
		:meth:`pack_uhyper`, and :meth:`pack_hyper`.
		
		
		"""
		pass
		
	def pack_float(self, value):
		"""
		Packs the single-precision floating point number *value*.
		
		
		"""
		pass
		
	def pack_double(self, value):
		"""
		Packs the double-precision floating point number *value*.
		
		The following methods support packing strings, bytes, and opaque data:
		
		
		"""
		pass
		
	def pack_fstring(self, n,s):
		"""
		Packs a fixed length string, *s*.  *n* is the length of the string but it is
		*not* packed into the data buffer.  The string is padded with null bytes if
		necessary to guaranteed 4 byte alignment.
		
		
		"""
		pass
		
	def pack_fopaque(self, n,data):
		"""
		Packs a fixed length opaque data stream, similarly to :meth:`pack_fstring`.
		
		
		"""
		pass
		
	def pack_string(self, s):
		"""
		Packs a variable length string, *s*.  The length of the string is first packed
		as an unsigned integer, then the string data is packed with
		:meth:`pack_fstring`.
		
		
		"""
		pass
		
	def pack_opaque(self, data):
		"""
		Packs a variable length opaque data string, similarly to :meth:`pack_string`.
		
		
		"""
		pass
		
	def pack_bytes(self, bytes):
		"""
		Packs a variable length byte stream, similarly to :meth:`pack_string`.
		
		The following methods support packing arrays and lists:
		
		
		"""
		pass
		
	def pack_list(self, list,pack_item):
		"""
		Packs a *list* of homogeneous items.  This method is useful for lists with an
		indeterminate size; i.e. the size is not available until the entire list has
		been walked.  For each item in the list, an unsigned integer ``1`` is packed
		first, followed by the data value from the list.  *pack_item* is the function
		that is called to pack the individual item.  At the end of the list, an unsigned
		integer ``0`` is packed.
		
		For example, to pack a list of integers, the code might appear like this::
		
		import xdrlib
		p = xdrlib.Packer()
		p.pack_list([1, 2, 3], p.pack_int)
		
		
		"""
		pass
		
	def pack_farray(self, n,array,pack_item):
		"""
		Packs a fixed length list (*array*) of homogeneous items.  *n* is the length of
		the list; it is *not* packed into the buffer, but a :exc:`ValueError` exception
		is raised if ``len(array)`` is not equal to *n*.  As above, *pack_item* is the
		function used to pack each element.
		
		
		"""
		pass
		
	def pack_array(self, list,pack_item):
		"""
		Packs a variable length *list* of homogeneous items.  First, the length of the
		list is packed as an unsigned integer, then each element is packed as in
		:meth:`pack_farray` above.
		
		
		.. npacker Objects
		----------------
		
		The :class:`Unpacker` class offers the following methods:
		
		
		"""
		pass
		
	


class Unpacker:


	"""
	``Unpacker`` is the complementary class which unpacks XDR data values from a
	string buffer.  The input buffer is given as *data*.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def reset(self, data):
		"""
		Resets the string buffer with the given *data*.
		
		
		"""
		pass
		
	def get_position(self, ):
		"""
		Returns the current unpack position in the data buffer.
		
		
		"""
		pass
		
	def set_position(self, position):
		"""
		Sets the data buffer unpack position to *position*.  You should be careful about
		using :meth:`get_position` and :meth:`set_position`.
		
		
		"""
		pass
		
	def get_buffer(self, ):
		"""
		Returns the current unpack data buffer as a string.
		
		
		"""
		pass
		
	def done(self, ):
		"""
		Indicates unpack completion.  Raises an :exc:`Error` exception if all of the
		data has not been unpacked.
		
		In addition, every data type that can be packed with a :class:`Packer`, can be
		unpacked with an :class:`Unpacker`.  Unpacking methods are of the form
		``unpack_type()``, and take no arguments.  They return the unpacked object.
		
		
		"""
		pass
		
	def unpack_float(self, ):
		"""
		Unpacks a single-precision floating point number.
		
		
		"""
		pass
		
	def unpack_double(self, ):
		"""
		Unpacks a double-precision floating point number, similarly to
		:meth:`unpack_float`.
		
		In addition, the following methods unpack strings, bytes, and opaque data:
		
		
		"""
		pass
		
	def unpack_fstring(self, n):
		"""
		Unpacks and returns a fixed length string.  *n* is the number of characters
		expected.  Padding with null bytes to guaranteed 4 byte alignment is assumed.
		
		
		"""
		pass
		
	def unpack_fopaque(self, n):
		"""
		Unpacks and returns a fixed length opaque data stream, similarly to
		:meth:`unpack_fstring`.
		
		
		"""
		pass
		
	def unpack_string(self, ):
		"""
		Unpacks and returns a variable length string.  The length of the string is first
		unpacked as an unsigned integer, then the string data is unpacked with
		:meth:`unpack_fstring`.
		
		
		"""
		pass
		
	def unpack_opaque(self, ):
		"""
		Unpacks and returns a variable length opaque data string, similarly to
		:meth:`unpack_string`.
		
		
		"""
		pass
		
	def unpack_bytes(self, ):
		"""
		Unpacks and returns a variable length byte stream, similarly to
		:meth:`unpack_string`.
		
		The following methods support unpacking arrays and lists:
		
		
		"""
		pass
		
	def unpack_list(self, unpack_item):
		"""
		Unpacks and returns a list of homogeneous items.  The list is unpacked one
		element at a time by first unpacking an unsigned integer flag.  If the flag is
		``1``, then the item is unpacked and appended to the list.  A flag of ``0``
		indicates the end of the list.  *unpack_item* is the function that is called to
		unpack the items.
		
		
		"""
		pass
		
	def unpack_farray(self, n,unpack_item):
		"""
		Unpacks and returns (as a list) a fixed length array of homogeneous items.  *n*
		is number of list elements to expect in the buffer. As above, *unpack_item* is
		the function used to unpack each element.
		
		
		"""
		pass
		
	def unpack_array(self, unpack_item):
		"""
		Unpacks and returns a variable length *list* of homogeneous items. First, the
		length of the list is unpacked as an unsigned integer, then each element is
		unpacked as in :meth:`unpack_farray` above.
		
		
		.. xceptions
		----------
		
		Exceptions in this module are coded as class instances:
		
		
		"""
		pass
		
	


