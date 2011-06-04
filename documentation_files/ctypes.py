#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: A foreign function library for Python.
"""
""":module: ctypes.util
:noindex:

Try to find a library and return a pathname.  *name* is the library name without
any prefix like *lib*, suffix like ``.so``, ``.dylib`` or version number (this
is the form used for the posix linker option :option:`-l`).  If no library can
be found, returns ``None``.

The exact functionality is system dependent.

On Linux, :func:`find_library` tries to run external programs
(``/sbin/ldconfig``, ``gcc``, and ``objdump``) to find the library file.  It
returns the filename of the library file.  Here are some examples::

>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
>>>

On OS X, :func:`find_library` tries several predefined naming schemes and paths
to locate the library, and returns a full pathname if successful::

>>> from ctypes.util import find_library
>>> find_library("c")
'/usr/lib/libc.dylib'
>>> find_library("m")
'/usr/lib/libm.dylib'
>>> find_library("bz2")
'/usr/lib/libbz2.dylib'
>>> find_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
>>>

On Windows, :func:`find_library` searches along the system search path, and
returns the full pathname, but since there is no predefined naming scheme a call
like ``find_library("c")`` will fail and return ``None``.

If wrapping a shared library with :mod:`ctypes`, it *may* be better to determine
the shared library name at development type, and hardcode that into the wrapper
module instead of using :func:`find_library` to locate the library at runtime.


.. oading shared libraries
^^^^^^^^^^^^^^^^^^^^^^^^

There are several ways to loaded shared libraries into the Python process.  One
way is to instantiate one of the following classes:


"""
find_libraryname = None
class CDLL:


	"""
	Instances of this class represent loaded shared libraries. Functions in these
	libraries use the standard C calling convention, and are assumed to return
	:ctype:`int`.
	
	
	"""
	
	
	def __init__(self, name,mode=DEFAULT_MODE,handle=None,use_errno=False,use_last_error=False):
		pass
	
	


class OleDLL:


	"""
	Windows only: Instances of this class represent loaded shared libraries,
	functions in these libraries use the ``stdcall`` calling convention, and are
	assumed to return the windows specific :class:`HRESULT` code.  :class:`HRESULT`
	values contain information specifying whether the function call failed or
	succeeded, together with additional error code.  If the return value signals a
	failure, an :class:`WindowsError` is automatically raised.
	
	
	"""
	
	
	def __init__(self, name,mode=DEFAULT_MODE,handle=None,use_errno=False,use_last_error=False):
		pass
	
	


class WinDLL:


	"""
	Windows only: Instances of this class represent loaded shared libraries,
	functions in these libraries use the ``stdcall`` calling convention, and are
	assumed to return :ctype:`int` by default.
	
	On Windows CE only the standard calling convention is used, for convenience the
	:class:`WinDLL` and :class:`OleDLL` use the standard calling convention on this
	platform.
	
	The Python :term:`global interpreter lock` is released before calling any
	function exported by these libraries, and reacquired afterwards.
	
	
	"""
	
	
	def __init__(self, name,mode=DEFAULT_MODE,handle=None,use_errno=False,use_last_error=False):
		pass
	
	


class PyDLL:


	"""
	Instances of this class behave like :class:`CDLL` instances, except that the
	Python GIL is *not* released during the function call, and after the function
	execution the Python error flag is checked. If the error flag is set, a Python
	exception is raised.
	
	Thus, this is only useful to call Python C api functions directly.
	
	All these classes can be instantiated by calling them with at least one
	argument, the pathname of the shared library.  If you have an existing handle to
	an already loaded shared library, it can be passed as the ``handle`` named
	parameter, otherwise the underlying platforms ``dlopen`` or ``LoadLibrary``
	function is used to load the library into the process, and to get a handle to
	it.
	
	The *mode* parameter can be used to specify how the library is loaded.  For
	details, consult the :manpage:`dlopen(3)` manpage, on Windows, *mode* is
	ignored.
	
	The *use_errno* parameter, when set to True, enables a ctypes mechanism that
	allows to access the system :data:`errno` error number in a safe way.
	:mod:`ctypes` maintains a thread-local copy of the systems :data:`errno`
	variable; if you call foreign functions created with ``use_errno=True`` then the
	:data:`errno` value before the function call is swapped with the ctypes private
	copy, the same happens immediately after the function call.
	
	The function :func:`ctypes.get_errno` returns the value of the ctypes private
	copy, and the function :func:`ctypes.set_errno` changes the ctypes private copy
	to a new value and returns the former value.
	
	The *use_last_error* parameter, when set to True, enables the same mechanism for
	the Windows error code which is managed by the :func:`GetLastError` and
	:func:`SetLastError` Windows API functions; :func:`ctypes.get_last_error` and
	:func:`ctypes.set_last_error` are used to request and change the ctypes private
	copy of the windows error code.
	
	"""
	
	
	def __init__(self, name,mode=DEFAULT_MODE,handle=None):
		pass
	
	""":noindex:
	
	Flag to use as *mode* parameter.  On platforms where this flag is not available,
	it is defined as the integer zero.
	
	
	"""
	RTLD_GLOBAL = None
	""":noindex:
	
	Flag to use as *mode* parameter.  On platforms where this is not available, it
	is the same as *RTLD_GLOBAL*.
	
	
	"""
	RTLD_LOCAL = None
	""":noindex:
	
	The default mode which is used to load shared libraries.  On OSX 10.3, this is
	*RTLD_GLOBAL*, otherwise it is the same as *RTLD_LOCAL*.
	
	Instances of these classes have no public methods, however :meth:`__getattr__`
	and :meth:`__getitem__` have special behavior: functions exported by the shared
	library can be accessed as attributes of by index.  Please note that both
	:meth:`__getattr__` and :meth:`__getitem__` cache their result, so calling them
	repeatedly returns the same object each time.
	
	The following public attributes are available, their name starts with an
	underscore to not clash with exported function names:
	
	
	"""
	DEFAULT_MODE = None
	


class LibraryLoader:


	"""
	Class which loads shared libraries.  *dlltype* should be one of the
	:class:`CDLL`, :class:`PyDLL`, :class:`WinDLL`, or :class:`OleDLL` types.
	
	:meth:`__getattr__` has special behavior: It allows to load a shared library by
	accessing it as attribute of a library loader instance.  The result is cached,
	so repeated attribute accesses return the same library each time.
	
	
	"""
	
	
	def __init__(self, dlltype):
		pass
	
	""":noindex:
	
	Creates :class:`CDLL` instances.
	
	
	"""
	cdll = None
	""":noindex:
	
	Windows only: Creates :class:`WinDLL` instances.
	
	
	"""
	windll = None
	""":noindex:
	
	Windows only: Creates :class:`OleDLL` instances.
	
	
	"""
	oledll = None
	""":noindex:
	
	Creates :class:`PyDLL` instances.
	
	For accessing the C Python api directly, a ready-to-use Python shared library
	object is available:
	
	
	"""
	pydll = None
	""":noindex:
	
	An instance of :class:`PyDLL` that exposes Python C API functions as
	attributes.  Note that all these functions are assumed to return C
	:ctype:`int`, which is of course not always the truth, so you have to assign
	the correct :attr:`restype` attribute to use these functions.
	
	
	.. oreign functions
	^^^^^^^^^^^^^^^^^
	
	As explained in the previous section, foreign functions can be accessed as
	attributes of loaded shared libraries.  The function objects created in this way
	by default accept any number of arguments, accept any ctypes data instances as
	arguments, and return the default result type specified by the library loader.
	They are instances of a private class:
	
	
	"""
	pythonapi = None
	


class _FuncPtr:


	"""
	Base class for C callable foreign functions.
	
	Instances of foreign functions are also C compatible data types; they
	represent C function pointers.
	
	This behavior can be customized by assigning to special attributes of the
	foreign function object.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	def callable(result,func,arguments):
		""":noindex:
		
		*result* is what the foreign function returns, as specified by the
		:attr:`restype` attribute.
		
		*func* is the foreign function object itself, this allows to reuse the
		same callable object to check or post process the results of several
		functions.
		
		*arguments* is a tuple containing the parameters originally passed to
		the function call, this allows to specialize the behavior on the
		arguments used.
		
		The object that this function returns will be returned from the
		foreign function call, but it can also check the result value
		and raise an exception if the foreign function call failed.
		
		
		"""
		pass
		
	def CFUNCTYPE(restype,argtypes,use_errno=False,use_last_error=False):
		"""
		The returned function prototype creates functions that use the standard C
		calling convention.  The function will release the GIL during the call.  If
		*use_errno* is set to True, the ctypes private copy of the system
		:data:`errno` variable is exchanged with the real :data:`errno` value before
		and after the call; *use_last_error* does the same for the Windows error
		code.
		
		"""
		pass
		
	def WINFUNCTYPE(restype,argtypes,use_errno=False,use_last_error=False):
		"""
		Windows only: The returned function prototype creates functions that use the
		``stdcall`` calling convention, except on Windows CE where
		:func:`WINFUNCTYPE` is the same as :func:`CFUNCTYPE`.  The function will
		release the GIL during the call.  *use_errno* and *use_last_error* have the
		same meaning as above.
		
		
		"""
		pass
		
	def PYFUNCTYPE(restype,argtypes):
		"""
		The returned function prototype creates functions that use the Python calling
		convention.  The function will *not* release the GIL during the call.
		
		Function prototypes created by these factory functions can be instantiated in
		different ways, depending on the type and number of the parameters in the call:
		
		
		"""
		pass
		
	def prototype(address):
		""":noindex:
		:module:
		
		Returns a foreign function at the specified address which must be an integer.
		
		
		"""
		pass
		
	def prototype(callable):
		""":noindex:
		:module:
		
		Create a C callable function (a callback function) from a Python *callable*.
		
		
		"""
		pass
		
	def prototype(func_spec,paramflags):
		""":noindex:
		:module:
		
		Returns a foreign function exported by a shared library. *func_spec* must be a
		2-tuple ``(name_or_ordinal, library)``. The first item is the name of the
		exported function as string, or the ordinal of the exported function as small
		integer.  The second item is the shared library instance.
		
		
		"""
		pass
		
	def prototype(vtbl_index,name,paramflags,iid):
		""":noindex:
		:module:
		
		Returns a foreign function that will call a COM method. *vtbl_index* is the
		index into the virtual function table, a small non-negative integer. *name* is
		name of the COM method. *iid* is an optional pointer to the interface identifier
		which is used in extended error reporting.
		
		COM methods use a special calling convention: They require a pointer to the COM
		interface as first argument, in addition to those parameters that are specified
		in the :attr:`argtypes` tuple.
		
		The optional *paramflags* parameter creates foreign function wrappers with much
		more functionality than the features described above.
		
		*paramflags* must be a tuple of the same length as :attr:`argtypes`.
		
		Each item in this tuple contains further information about a parameter, it must
		be a tuple containing one, two, or three items.
		
		The first item is an integer containing a combination of direction
		flags for the parameter:
		
		1
		Specifies an input parameter to the function.
		
		2
		Output parameter.  The foreign function fills in a value.
		
		4
		Input parameter which defaults to the integer zero.
		
		The optional second item is the parameter name as string.  If this is specified,
		the foreign function can be called with named parameters.
		
		The optional third item is the default value for this parameter.
		
		This example demonstrates how to wrap the Windows ``MessageBoxA`` function so
		"""
		pass
		
	def addressof(obj):
		"""
		Returns the address of the memory buffer as integer.  *obj* must be an
		instance of a ctypes type.
		
		
		"""
		pass
		
	def alignment(obj_or_type):
		"""
		Returns the alignment requirements of a ctypes type. *obj_or_type* must be a
		ctypes type or instance.
		
		
		"""
		pass
		
	def byref(obj,offset):
		"""
		Returns a light-weight pointer to *obj*, which must be an instance of a
		ctypes type.  *offset* defaults to zero, and must be an integer that will be
		added to the internal pointer value.
		
		``byref(obj, offset)`` corresponds to this C code::
		
		(((char *)&obj) + offset)
		
		The returned object can only be used as a foreign function call
		parameter.  It behaves similar to ``pointer(obj)``, but the
		construction is a lot faster.
		
		"""
		pass
		
	def cast(obj,type):
		"""
		This function is similar to the cast operator in C.  It returns a new
		instance of *type* which points to the same memory block as *obj*.  *type*
		must be a pointer type, and *obj* must be an object that can be interpreted
		as a pointer.
		
		
		"""
		pass
		
	def create_string_buffer(init_or_size,size):
		"""
		This function creates a mutable character buffer. The returned object is a
		ctypes array of :class:`c_char`.
		
		*init_or_size* must be an integer which specifies the size of the array, or a
		string which will be used to initialize the array items.
		
		If a string is specified as first argument, the buffer is made one item larger
		than the length of the string so that the last element in the array is a NUL
		termination character. An integer can be passed as second argument which allows
		to specify the size of the array if the length of the string should not be used.
		
		If the first parameter is a unicode string, it is converted into an 8-bit string
		according to ctypes conversion rules.
		
		
		"""
		pass
		
	def create_unicode_buffer(init_or_size,size):
		"""
		This function creates a mutable unicode character buffer. The returned object is
		a ctypes array of :class:`c_wchar`.
		
		*init_or_size* must be an integer which specifies the size of the array, or a
		unicode string which will be used to initialize the array items.
		
		If a unicode string is specified as first argument, the buffer is made one item
		larger than the length of the string so that the last element in the array is a
		NUL termination character. An integer can be passed as second argument which
		allows to specify the size of the array if the length of the string should not
		be used.
		
		If the first parameter is a 8-bit string, it is converted into an unicode string
		according to ctypes conversion rules.
		
		
		"""
		pass
		
	def DllCanUnloadNow():
		"""
		Windows only: This function is a hook which allows to implement in-process
		COM servers with ctypes.  It is called from the DllCanUnloadNow function that
		the _ctypes extension dll exports.
		
		
		"""
		pass
		
	def DllGetClassObject():
		"""
		Windows only: This function is a hook which allows to implement in-process
		COM servers with ctypes.  It is called from the DllGetClassObject function
		that the ``_ctypes`` extension dll exports.
		
		
		"""
		pass
		
	def find_library(name):
		""":module: ctypes.util
		
		Try to find a library and return a pathname.  *name* is the library name
		without any prefix like ``lib``, suffix like ``.so``, ``.dylib`` or version
		number (this is the form used for the posix linker option :option:`-l`).  If
		no library can be found, returns ``None``.
		
		The exact functionality is system dependent.
		
		"""
		pass
		
	def find_msvcrt():
		""":module: ctypes.util
		
		Windows only: return the filename of the VC runtype library used by Python,
		and by the extension modules.  If the name of the library cannot be
		determined, ``None`` is returned.
		
		If you need to free memory, for example, allocated by an extension module
		with a call to the ``free(void *)``, it is important that you use the
		function in the same library that allocated the memory.
		
		"""
		pass
		
	def FormatError(code):
		"""
		Windows only: Returns a textual description of the error code *code*.  If no
		error code is specified, the last error code is used by calling the Windows
		api function GetLastError.
		
		
		"""
		pass
		
	def GetLastError():
		"""
		Windows only: Returns the last error code set by Windows in the calling thread.
		This function calls the Windows `GetLastError()` function directly,
		it does not return the ctypes-private copy of the error code.
		
		"""
		pass
		
	def get_errno():
		"""
		Returns the current value of the ctypes-private copy of the system
		:data:`errno` variable in the calling thread.
		
		"""
		pass
		
	def get_last_error():
		"""
		Windows only: returns the current value of the ctypes-private copy of the system
		:data:`LastError` variable in the calling thread.
		
		"""
		pass
		
	def memmove(dst,src,count):
		"""
		Same as the standard C memmove library function: copies *count* bytes from
		*src* to *dst*. *dst* and *src* must be integers or ctypes instances that can
		be converted to pointers.
		
		
		"""
		pass
		
	def memset(dst,c,count):
		"""
		Same as the standard C memset library function: fills the memory block at
		address *dst* with *count* bytes of value *c*. *dst* must be an integer
		specifying an address, or a ctypes instance.
		
		
		"""
		pass
		
	def POINTER(type):
		"""
		This factory function creates and returns a new ctypes pointer type. Pointer
		types are cached an reused internally, so calling this function repeatedly is
		cheap. *type* must be a ctypes type.
		
		
		"""
		pass
		
	def pointer(obj):
		"""
		This function creates a new pointer instance, pointing to *obj*. The returned
		object is of the type ``POINTER(type(obj))``.
		
		Note: If you just want to pass a pointer to an object to a foreign function
		call, you should use ``byref(obj)`` which is much faster.
		
		
		"""
		pass
		
	def resize(obj,size):
		"""
		This function resizes the internal memory buffer of *obj*, which must be an
		instance of a ctypes type.  It is not possible to make the buffer smaller
		than the native size of the objects type, as given by ``sizeof(type(obj))``,
		but it is possible to enlarge the buffer.
		
		
		"""
		pass
		
	def set_conversion_mode(encoding,errors):
		"""
		This function sets the rules that ctypes objects use when converting between
		8-bit strings and unicode strings.  *encoding* must be a string specifying an
		encoding, like ``'utf-8'`` or ``'mbcs'``, *errors* must be a string
		specifying the error handling on encoding/decoding errors.  Examples of
		possible values are ``"strict"``, ``"replace"``, or ``"ignore"``.
		
		:func:`set_conversion_mode` returns a 2-tuple containing the previous
		conversion rules.  On windows, the initial conversion rules are ``('mbcs',
		'ignore')``, on other systems ``('ascii', 'strict')``.
		
		
		"""
		pass
		
	def set_errno(value):
		"""
		Set the current value of the ctypes-private copy of the system :data:`errno`
		variable in the calling thread to *value* and return the previous value.
		
		"""
		pass
		
	def set_last_error(value):
		"""
		Windows only: set the current value of the ctypes-private copy of the system
		:data:`LastError` variable in the calling thread to *value* and return the
		previous value.
		
		"""
		pass
		
	def sizeof(obj_or_type):
		"""
		Returns the size in bytes of a ctypes type or instance memory buffer. Does the
		same as the C ``sizeof()`` function.
		
		
		"""
		pass
		
	def string_at(address,size):
		"""
		This function returns the string starting at memory address address. If size
		is specified, it is used as size, otherwise the string is assumed to be
		zero-terminated.
		
		
		"""
		pass
		
	def WinError(code=None,descr=None):
		"""
		Windows only: this function is probably the worst-named thing in ctypes.  It
		creates an instance of WindowsError.  If *code* is not specified,
		``GetLastError`` is called to determine the error code.  If ``descr`` is not
		specified, :func:`FormatError` is called to get a textual description of the
		error.
		
		
		"""
		pass
		
	def wstring_at(address,size):
		"""
		This function returns the wide character string starting at memory address
		*address* as unicode string.  If *size* is specified, it is used as the
		number of characters of the string, otherwise the string is assumed to be
		zero-terminated.
		
		
		.. ata types
		^^^^^^^^^^
		
		
		"""
		pass
		
	


class _CData:


	"""
	This non-public class is the common base class of all ctypes data types.
	Among other things, all ctypes type instances contain a memory block that
	hold C compatible data; the address of the memory block is returned by the
	:func:`addressof` helper function.  Another instance variable is exposed as
	:attr:`_objects`; this contains other Python objects that need to be kept
	alive in case the memory block contains pointers.
	
	Common methods of ctypes data types, these are all class methods (to be
	exact, they are methods of the :term:`metaclass`):
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class _SimpleCData:


	"""
	This non-public class is the base class of all fundamental ctypes data
	types. It is mentioned here because it contains the common attributes of the
	fundamental ctypes data types.  :class:`_SimpleCData` is a subclass of
	:class:`_CData`, so it inherits their methods and attributes.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_byte:


	"""
	Represents the C :ctype:`signed char` datatype, and interprets the value as
	small integer.  The constructor accepts an optional integer initializer; no
	overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_char:


	"""
	Represents the C :ctype:`char` datatype, and interprets the value as a single
	character.  The constructor accepts an optional string initializer, the
	length of the string must be exactly one character.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_char_p:


	"""
	Represents the C :ctype:`char *` datatype when it points to a zero-terminated
	string.  For a general character pointer that may also point to binary data,
	``POINTER(c_char)`` must be used.  The constructor accepts an integer
	address, or a string.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_double:


	"""
	Represents the C :ctype:`double` datatype.  The constructor accepts an
	optional float initializer.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_longdouble:


	"""
	Represents the C :ctype:`long double` datatype.  The constructor accepts an
	optional float initializer.  On platforms where ``sizeof(long double) ==
	sizeof(double)`` it is an alias to :class:`c_double`.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_float:


	"""
	Represents the C :ctype:`float` datatype.  The constructor accepts an
	optional float initializer.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_int:


	"""
	Represents the C :ctype:`signed int` datatype.  The constructor accepts an
	optional integer initializer; no overflow checking is done.  On platforms
	where ``sizeof(int) == sizeof(long)`` it is an alias to :class:`c_long`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_int8:


	"""
	Represents the C 8-bit :ctype:`signed int` datatype.  Usually an alias for
	:class:`c_byte`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_int16:


	"""
	Represents the C 16-bit :ctype:`signed int` datatype.  Usually an alias for
	:class:`c_short`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_int32:


	"""
	Represents the C 32-bit :ctype:`signed int` datatype.  Usually an alias for
	:class:`c_int`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_int64:


	"""
	Represents the C 64-bit :ctype:`signed int` datatype.  Usually an alias for
	:class:`c_longlong`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_long:


	"""
	Represents the C :ctype:`signed long` datatype.  The constructor accepts an
	optional integer initializer; no overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_longlong:


	"""
	Represents the C :ctype:`signed long long` datatype.  The constructor accepts
	an optional integer initializer; no overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_short:


	"""
	Represents the C :ctype:`signed short` datatype.  The constructor accepts an
	optional integer initializer; no overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_size_t:


	"""
	Represents the C :ctype:`size_t` datatype.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_ssize_t:


	"""
	Represents the C :ctype:`ssize_t` datatype.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_ubyte:


	"""
	Represents the C :ctype:`unsigned char` datatype, it interprets the value as
	small integer.  The constructor accepts an optional integer initializer; no
	overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_uint:


	"""
	Represents the C :ctype:`unsigned int` datatype.  The constructor accepts an
	optional integer initializer; no overflow checking is done.  On platforms
	where ``sizeof(int) == sizeof(long)`` it is an alias for :class:`c_ulong`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_uint8:


	"""
	Represents the C 8-bit :ctype:`unsigned int` datatype.  Usually an alias for
	:class:`c_ubyte`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_uint16:


	"""
	Represents the C 16-bit :ctype:`unsigned int` datatype.  Usually an alias for
	:class:`c_ushort`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_uint32:


	"""
	Represents the C 32-bit :ctype:`unsigned int` datatype.  Usually an alias for
	:class:`c_uint`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_uint64:


	"""
	Represents the C 64-bit :ctype:`unsigned int` datatype.  Usually an alias for
	:class:`c_ulonglong`.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_ulong:


	"""
	Represents the C :ctype:`unsigned long` datatype.  The constructor accepts an
	optional integer initializer; no overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_ulonglong:


	"""
	Represents the C :ctype:`unsigned long long` datatype.  The constructor
	accepts an optional integer initializer; no overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_ushort:


	"""
	Represents the C :ctype:`unsigned short` datatype.  The constructor accepts
	an optional integer initializer; no overflow checking is done.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_void_p:


	"""
	Represents the C :ctype:`void *` type.  The value is represented as integer.
	The constructor accepts an optional integer initializer.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_wchar:


	"""
	Represents the C :ctype:`wchar_t` datatype, and interprets the value as a
	single character unicode string.  The constructor accepts an optional string
	initializer, the length of the string must be exactly one character.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_wchar_p:


	"""
	Represents the C :ctype:`wchar_t *` datatype, which must be a pointer to a
	zero-terminated wide character string.  The constructor accepts an integer
	address, or a string.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class c_bool:


	"""
	Represent the C :ctype:`bool` datatype (more accurately, :ctype:`_Bool` from
	C99).  Its value can be True or False, and the constructor accepts any object
	that has a truth value.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class HRESULT:


	"""
	Windows only: Represents a :ctype:`HRESULT` value, which contains success or
	error information for a function or method call.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class py_object:


	"""
	Represents the C :ctype:`PyObject *` datatype.  Calling this without an
	argument creates a ``NULL`` :ctype:`PyObject *` pointer.
	
	The :mod:`ctypes.wintypes` module provides quite some other Windows specific
	data types, for example :ctype:`HWND`, :ctype:`WPARAM`, or :ctype:`DWORD`.  Some
	useful structures like :ctype:`MSG` or :ctype:`RECT` are also defined.
	
	
	.. tructured data types
	^^^^^^^^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Union:


	"""
	Abstract base class for unions in native byte order.
	
	
	"""
	
	
	def __init__(self, args,kw):
		pass
	
	


class BigEndianStructure:


	"""
	Abstract base class for structures in *big endian* byte order.
	
	
	"""
	
	
	def __init__(self, args,kw):
		pass
	
	


class LittleEndianStructure:


	"""
	Abstract base class for structures in *little endian* byte order.
	
	Structures with non-native byte order cannot contain pointer type fields, or any
	other data types containing pointer type fields.
	
	
	"""
	
	
	def __init__(self, args,kw):
		pass
	
	


class Structure:


	"""
	Abstract base class for structures in *native* byte order.
	
	Concrete structure and union types must be created by subclassing one of these
	types, and at least define a :attr:`_fields_` class variable. :mod:`ctypes` will
	create :term:`descriptor`\s which allow reading and writing the fields by direct
	attribute accesses.  These are the
	
	
	"""
	
	
	def __init__(self, args,kw):
		pass
	
	


