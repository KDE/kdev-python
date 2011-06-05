#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Low-level networking interface.


This module provides access to the BSD *socket* interface. It is available on
all modern Unix systems, Windows, Mac OS X, BeOS, OS/2, and probably additional
platforms.

"""
"""AF_INET
AF_INET6

These constants represent the address (and protocol) families, used for the
first argument to :func:`socket`.  If the :const:`AF_UNIX` constant is not
defined then this protocol is unsupported.


"""
AF_UNIX = None
"""SOCK_DGRAM
SOCK_RAW
SOCK_RDM
SOCK_SEQPACKET

These constants represent the socket types, used for the second argument to
:func:`socket`. (Only :const:`SOCK_STREAM` and :const:`SOCK_DGRAM` appear to be
generally useful.)


"""
SOCK_STREAM = None
"""SOMAXCONN
MSG_*
SOL_*
IPPROTO_*
IPPORT_*
INADDR_*
IP_*
IPV6_*
EAI_*
AI_*
NI_*
TCP_*

Many constants of these forms, documented in the Unix documentation on sockets
and/or the IP protocol, are also defined in the socket module. They are
generally used in arguments to the :meth:`setsockopt` and :meth:`getsockopt`
methods of socket objects.  In most cases, only those symbols that are defined
in the Unix header files are defined; for a few symbols, default values are
provided.

"""
SO_ = None
"""RCVALL_*

Constants for Windows' WSAIoctl(). The constants are used as arguments to the
:meth:`ioctl` method of socket objects.

"""
SIO_ = None
"""
TIPC related constants, matching the ones exported by the C socket API. See
the TIPC documentation for more information.

"""
TIPC_ = None
"""
This constant contains a boolean value which indicates if IPv6 is supported on
this platform.

"""
has_ipv6 = None
"""
This is a Python type object that represents the socket object type. It is the
same as ``type(socket(more))``.


"""
SocketType = None
def create_connection(address,timeout,source_address):
	"""
	Convenience function.  Connect to *address* (a 2-tuple ``(host, port)``),
	and return the socket object.  Passing the optional *timeout* parameter will
	set the timeout on the socket instance before attempting to connect.  If no
	*timeout* is supplied, the global default timeout setting returned by
	:func:`getdefaulttimeout` is used.
	
	If supplied, *source_address* must be a 2-tuple ``(host, port)`` for the
	socket to bind to as its source address before connecting.  If host or port
	are '' or 0 respectively the OS default behavior will be used.
	
	"""
	pass
	
def getaddrinfo(host,port,family=0,socktype=0,proto=0,flags=0):
	"""
	Translate the *host*/*port* argument into a sequence of 5-tuples that contain
	all the necessary arguments for creating a socket connected to that service.
	*host* is a domain name, a string representation of an IPv4/v6 address
	or ``None``. *port* is a string service name such as ``'http'``, a numeric
	port number or ``None``.  By passing ``None`` as the value of *host*
	and *port*, you can pass ``NULL`` to the underlying C API.
	
	The *family*, *socktype* and *proto* arguments can be optionally specified
	in order to narrow the list of addresses returned.  Passing zero as a
	value for each of these arguments selects the full range of results.
	The *flags* argument can be one or several of the ``AI_*`` constants,
	and will influence how results are computed and returned.
	For example, :const:`AI_NUMERICHOST` will disable domain name resolution
	and will raise an error if *host* is a domain name.
	
	The function returns a list of 5-tuples with the following structure:
	
	``(family, socktype, proto, canonname, sockaddr)``
	
	In these tuples, *family*, *socktype*, *proto* are all integers and are
	meant to be passed to the :func:`socket` function.  *canonname* will be
	a string representing the canonical name of the *host* if
	:const:`AI_CANONNAME` is part of the *flags* argument; else *canonname*
	will be empty.  *sockaddr* is a tuple describing a socket address, whose
	format depends on the returned *family* (a ``(address, port)`` 2-tuple for
	:const:`AF_INET`, a ``(address, port, flow info, scope id)`` 4-tuple for
	:const:`AF_INET6`), and is meant to be passed to the :meth:`socket.connect`
	method.
	
	The following example fetches address information for a hypothetical TCP
	connection to ``www.python.org`` on port 80 (results may differ on your
	system if IPv6 isn't enabled)::
	
	>>> socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)
	[(2, 1, 6, '', ('82.94.164.162', 80)),
	(10, 1, 6, '', ('2001:888:2000:d::a2', 80, 0, 0))]
	
	"""
	pass
	
def getfqdn(name):
	"""
	Return a fully qualified domain name for *name*. If *name* is omitted or empty,
	it is interpreted as the local host.  To find the fully qualified name, the
	hostname returned by :func:`gethostbyaddr` is checked, followed by aliases for the
	host, if available.  The first name which includes a period is selected.  In
	case no fully qualified domain name is available, the hostname as returned by
	:func:`gethostname` is returned.
	
	"""
	pass
	
def gethostbyname(hostname):
	"""
	Translate a host name to IPv4 address format.  The IPv4 address is returned as a
	string, such as  ``'100.50.200.5'``.  If the host name is an IPv4 address itself
	it is returned unchanged.  See :func:`gethostbyname_ex` for a more complete
	interface. :func:`gethostbyname` does not support IPv6 name resolution, and
	:func:`getaddrinfo` should be used instead for IPv4/v6 dual stack support.
	
	
	"""
	pass
	
def gethostbyname_ex(hostname):
	"""
	Translate a host name to IPv4 address format, extended interface. Return a
	triple ``(hostname, aliaslist, ipaddrlist)`` where *hostname* is the primary
	host name responding to the given *ip_address*, *aliaslist* is a (possibly
	empty) list of alternative host names for the same address, and *ipaddrlist* is
	a list of IPv4 addresses for the same interface on the same host (often but not
	always a single address). :func:`gethostbyname_ex` does not support IPv6 name
	resolution, and :func:`getaddrinfo` should be used instead for IPv4/v6 dual
	stack support.
	
	
	"""
	pass
	
def gethostname():
	"""
	Return a string containing the hostname of the machine where  the Python
	interpreter is currently executing.
	
	If you want to know the current machine's IP address, you may want to use
	``gethostbyname(gethostname())``. This operation assumes that there is a
	valid address-to-host mapping for the host, and the assumption does not
	always hold.
	
	Note: :func:`gethostname` doesn't always return the fully qualified domain
	name; use ``getfqdn()`` (see above).
	
	
	"""
	pass
	
def gethostbyaddr(ip_address):
	"""
	Return a triple ``(hostname, aliaslist, ipaddrlist)`` where *hostname* is the
	primary host name responding to the given *ip_address*, *aliaslist* is a
	(possibly empty) list of alternative host names for the same address, and
	*ipaddrlist* is a list of IPv4/v6 addresses for the same interface on the same
	host (most likely containing only a single address). To find the fully qualified
	domain name, use the function :func:`getfqdn`. :func:`gethostbyaddr` supports
	both IPv4 and IPv6.
	
	
	"""
	pass
	
def getnameinfo(sockaddr,flags):
	"""
	Translate a socket address *sockaddr* into a 2-tuple ``(host, port)``. Depending
	on the settings of *flags*, the result can contain a fully-qualified domain name
	or numeric address representation in *host*.  Similarly, *port* can contain a
	string port name or a numeric port number.
	
	"""
	pass
	
def getprotobyname(protocolname):
	"""
	Translate an Internet protocol name (for example, ``'icmp'``) to a constant
	suitable for passing as the (optional) third argument to the :func:`socket`
	function.  This is usually only needed for sockets opened in "raw" mode
	(:const:`SOCK_RAW`); for the normal socket modes, the correct protocol is chosen
	automatically if the protocol is omitted or zero.
	
	
	"""
	pass
	
def getservbyname(servicename,protocolname):
	"""
	Translate an Internet service name and protocol name to a port number for that
	service.  The optional protocol name, if given, should be ``'tcp'`` or
	``'udp'``, otherwise any protocol will match.
	
	
	"""
	pass
	
def getservbyport(port,protocolname):
	"""
	Translate an Internet port number and protocol name to a service name for that
	service.  The optional protocol name, if given, should be ``'tcp'`` or
	``'udp'``, otherwise any protocol will match.
	
	
	"""
	pass
	
def socket(family,type,proto):
	"""
	Create a new socket using the given address family, socket type and protocol
	number.  The address family should be :const:`AF_INET` (the default),
	:const:`AF_INET6` or :const:`AF_UNIX`.  The socket type should be
	:const:`SOCK_STREAM` (the default), :const:`SOCK_DGRAM` or perhaps one of the
	other ``SOCK_`` constants.  The protocol number is usually zero and may be
	omitted in that case.
	
	
	"""
	pass
	
def socketpair(family,type,proto):
	"""
	Build a pair of connected socket objects using the given address family, socket
	type, and protocol number.  Address family, socket type, and protocol number are
	as for the :func:`socket` function above. The default family is :const:`AF_UNIX`
	if defined on the platform; otherwise, the default is :const:`AF_INET`.
	Availability: Unix.
	
	"""
	pass
	
def _fromfd(fd,family,type,proto):
	"""
	Duplicate the file descriptor *fd* (an integer as returned by a file object's
	:meth:`fileno` method) and build a socket object from the result.  Address
	family, socket type and protocol number are as for the :func:`socket` function
	above. The file descriptor should refer to a socket, but this is not checked ---
	subsequent operations on the object may fail if the file descriptor is invalid.
	This function is rarely needed, but can be used to get or set socket options on
	a socket passed to a program as standard input or output (such as a server
	started by the Unix inet daemon).  The socket is assumed to be in blocking mode.
	Availability: Unix.
	
	
	"""
	pass
	
def ntohl(x):
	"""
	Convert 32-bit positive integers from network to host byte order.  On machines
	where the host byte order is the same as network byte order, this is a no-op;
	otherwise, it performs a 4-byte swap operation.
	
	
	"""
	pass
	
def ntohs(x):
	"""
	Convert 16-bit positive integers from network to host byte order.  On machines
	where the host byte order is the same as network byte order, this is a no-op;
	otherwise, it performs a 2-byte swap operation.
	
	
	"""
	pass
	
def htonl(x):
	"""
	Convert 32-bit positive integers from host to network byte order.  On machines
	where the host byte order is the same as network byte order, this is a no-op;
	otherwise, it performs a 4-byte swap operation.
	
	
	"""
	pass
	
def htons(x):
	"""
	Convert 16-bit positive integers from host to network byte order.  On machines
	where the host byte order is the same as network byte order, this is a no-op;
	otherwise, it performs a 2-byte swap operation.
	
	
	"""
	pass
	
def inet_aton(ip_string):
	"""
	Convert an IPv4 address from dotted-quad string format (for example,
	'123.45.67.89') to 32-bit packed binary format, as a string four characters in
	length.  This is useful when conversing with a program that uses the standard C
	library and needs objects of type :ctype:`struct in_addr`, which is the C type
	for the 32-bit packed binary this function returns.
	
	:func:`inet_aton` also accepts strings with less than three dots; see the
	Unix manual page :manpage:`inet(3)` for details.
	
	If the IPv4 address string passed to this function is invalid,
	:exc:`socket.error` will be raised. Note that exactly what is valid depends on
	the underlying C implementation of :cfunc:`inet_aton`.
	
	:func:`inet_aton` does not support IPv6, and :func:`inet_pton` should be used
	instead for IPv4/v6 dual stack support.
	
	
	"""
	pass
	
def inet_ntoa(packed_ip):
	"""
	Convert a 32-bit packed IPv4 address (a string four characters in length) to its
	standard dotted-quad string representation (for example, '123.45.67.89').  This
	is useful when conversing with a program that uses the standard C library and
	needs objects of type :ctype:`struct in_addr`, which is the C type for the
	32-bit packed binary data this function takes as an argument.
	
	If the string passed to this function is not exactly 4 bytes in length,
	:exc:`socket.error` will be raised. :func:`inet_ntoa` does not support IPv6, and
	:func:`inet_ntop` should be used instead for IPv4/v6 dual stack support.
	
	
	"""
	pass
	
def inet_pton(address_family,ip_string):
	"""
	Convert an IP address from its family-specific string format to a packed, binary
	format. :func:`inet_pton` is useful when a library or network protocol calls for
	an object of type :ctype:`struct in_addr` (similar to :func:`inet_aton`) or
	:ctype:`struct in6_addr`.
	
	Supported values for *address_family* are currently :const:`AF_INET` and
	:const:`AF_INET6`. If the IP address string *ip_string* is invalid,
	:exc:`socket.error` will be raised. Note that exactly what is valid depends on
	both the value of *address_family* and the underlying implementation of
	:cfunc:`inet_pton`.
	
	Availability: Unix (maybe not all platforms).
	
	"""
	pass
	
def inet_ntop(address_family,packed_ip):
	"""
	Convert a packed IP address (a string of some number of characters) to its
	standard, family-specific string representation (for example, ``'7.10.0.5'`` or
	``'5aef:2b::8'``) :func:`inet_ntop` is useful when a library or network protocol
	returns an object of type :ctype:`struct in_addr` (similar to :func:`inet_ntoa`)
	or :ctype:`struct in6_addr`.
	
	Supported values for *address_family* are currently :const:`AF_INET` and
	:const:`AF_INET6`. If the string *packed_ip* is not the correct length for the
	specified address family, :exc:`ValueError` will be raised.  A
	:exc:`socket.error` is raised for errors from the call to :func:`inet_ntop`.
	
	Availability: Unix (maybe not all platforms).
	
	"""
	pass
	
def getdefaulttimeout():
	"""
	Return the default timeout in floating seconds for new socket objects. A value
	of ``None`` indicates that new socket objects have no timeout. When the socket
	module is first imported, the default is ``None``.
	
	"""
	pass
	
def setdefaulttimeout(timeout):
	"""
	Set the default timeout in floating seconds for new socket objects. A value of
	``None`` indicates that new socket objects have no timeout. When the socket
	module is first imported, the default is ``None``.
	
	"""
	pass
	
