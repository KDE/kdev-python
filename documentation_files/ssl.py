#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: TLS/SSL wrapper for socket objects

"""
"""
Value to pass to the ``cert_reqs`` parameter to :func:`sslobject` when no
certificates will be required or validated from the other side of the socket
connection.

"""
CERT_NONE = None
"""
Value to pass to the ``cert_reqs`` parameter to :func:`sslobject` when no
certificates will be required from the other side of the socket connection,
but if they are provided, will be validated.  Note that use of this setting
requires a valid certificate validation file also be passed as a value of the
``ca_certs`` parameter.

"""
CERT_OPTIONAL = None
"""
Value to pass to the ``cert_reqs`` parameter to :func:`sslobject` when
certificates will be required from the other side of the socket connection.
Note that use of this setting requires a valid certificate validation file
also be passed as a value of the ``ca_certs`` parameter.

"""
CERT_REQUIRED = None
"""
Selects SSL version 2 as the channel encryption protocol.

This protocol is not available if OpenSSL is compiled with OPENSSL_NO_SSL2
flag.

"""
PROTOCOL_SSLv2 = None
"""
Selects SSL version 2 or 3 as the channel encryption protocol.  This is a
setting to use with servers for maximum compatibility with the other end of
an SSL connection, but it may cause the specific ciphers chosen for the
encryption to be of fairly low quality.

"""
PROTOCOL_SSLv23 = None
"""
Selects SSL version 3 as the channel encryption protocol.  For clients, this
is the maximally compatible SSL variant.

"""
PROTOCOL_SSLv3 = None
"""
Selects TLS version 1 as the channel encryption protocol.  This is the most
modern version, and probably the best choice for maximum protection, if both
sides can speak it.

"""
PROTOCOL_TLSv1 = None
"""
The version string of the OpenSSL library loaded by the interpreter::

>>> ssl.OPENSSL_VERSION
'OpenSSL 0.9.8k 25 Mar 2009'

"""
OPENSSL_VERSION = None
"""
A tuple of five integers representing version information about the
OpenSSL library::

>>> ssl.OPENSSL_VERSION_INFO
(0, 9, 8, 11, 15)

"""
OPENSSL_VERSION_INFO = None
"""
The raw version number of the OpenSSL library, as a single integer::

>>> ssl.OPENSSL_VERSION_NUMBER
9470143L
>>> hex(ssl.OPENSSL_VERSION_NUMBER)
'0x9080bfL'

"""
OPENSSL_VERSION_NUMBER = None
def wrap_socket(sock,keyfile=None,certfile=None,server_side=False,cert_reqs=CERT_NONE,ssl_version=None,ca_certs=None,do_handshake_on_connect=True,suppress_ragged_eofs=True,ciphers=None):
	"""
	Takes an instance ``sock`` of :class:`socket.socket`, and returns an instance
	of :class:`ssl.SSLSocket`, a subtype of :class:`socket.socket`, which wraps
	the underlying socket in an SSL context.  For client-side sockets, the
	context construction is lazy; if the underlying socket isn't connected yet,
	the context construction will be performed after :meth:`connect` is called on
	the socket.  For server-side sockets, if the socket has no remote peer, it is
	assumed to be a listening socket, and the server-side SSL wrapping is
	automatically performed on client connections accepted via the :meth:`accept`
	method.  :func:`wrap_socket` may raise :exc:`SSLError`.
	
	The ``keyfile`` and ``certfile`` parameters specify optional files which
	contain a certificate to be used to identify the local side of the
	connection.  See the discussion of :ref:`ssl-certificates` for more
	information on how the certificate is stored in the ``certfile``.
	
	Often the private key is stored in the same file as the certificate; in this
	case, only the ``certfile`` parameter need be passed.  If the private key is
	stored in a separate file, both parameters must be used.  If the private key
	is stored in the ``certfile``, it should come before the first certificate in
	the certificate chain::
	
	-----BEGIN RSA PRIVATE KEY-----
	more (private key in base64 encoding) more
	-----END RSA PRIVATE KEY-----
	-----BEGIN CERTIFICATE-----
	more (certificate in base64 PEM encoding) more
	-----END CERTIFICATE-----
	
	The parameter ``server_side`` is a boolean which identifies whether
	server-side or client-side behavior is desired from this socket.
	
	The parameter ``cert_reqs`` specifies whether a certificate is required from
	the other side of the connection, and whether it will be validated if
	provided.  It must be one of the three values :const:`CERT_NONE`
	(certificates ignored), :const:`CERT_OPTIONAL` (not required, but validated
	if provided), or :const:`CERT_REQUIRED` (required and validated).  If the
	value of this parameter is not :const:`CERT_NONE`, then the ``ca_certs``
	parameter must point to a file of CA certificates.
	
	The ``ca_certs`` file contains a set of concatenated "certification
	authority" certificates, which are used to validate certificates passed from
	the other end of the connection.  See the discussion of
	:ref:`ssl-certificates` for more information about how to arrange the
	certificates in this file.
	
	The parameter ``ssl_version`` specifies which version of the SSL protocol to
	use.  Typically, the server chooses a particular protocol version, and the
	client must adapt to the server's choice.  Most of the versions are not
	interoperable with the other versions.  If not specified, for client-side
	operation, the default SSL version is SSLv3; for server-side operation,
	SSLv23.  These version selections provide the most compatibility with other
	versions.
	
	Here's a table showing which versions in a client (down the side) can connect
	to which versions in a server (along the top):
	
	"""
	pass
	
def RAND_status():
	"""
	Returns True if the SSL pseudo-random number generator has been seeded with
	'enough' randomness, and False otherwise.  You can use :func:`ssl.RAND_egd`
	and :func:`ssl.RAND_add` to increase the randomness of the pseudo-random
	number generator.
	
	"""
	pass
	
def RAND_egd(path):
	"""
	If you are running an entropy-gathering daemon (EGD) somewhere, and ``path``
	is the pathname of a socket connection open to it, this will read 256 bytes
	of randomness from the socket, and add it to the SSL pseudo-random number
	generator to increase the security of generated secret keys.  This is
	typically only necessary on systems without better sources of randomness.
	
	See http://egd.sourceforge.net/ or http://prngd.sourceforge.net/ for sources
	of entropy-gathering daemons.
	
	"""
	pass
	
def RAND_add(bytes,entropy):
	"""
	Mixes the given ``bytes`` into the SSL pseudo-random number generator.  The
	parameter ``entropy`` (a float) is a lower bound on the entropy contained in
	string (so you can always use :const:`0.0`).  See :rfc:`1750` for more
	information on sources of entropy.
	
	"""
	pass
	
def cert_time_to_seconds(timestring):
	"""
	Returns a floating-point value containing a normal seconds-after-the-epoch
	time value, given the time-string representing the "notBefore" or "notAfter"
	date from a certificate.
	
	Here's an example::
	
	>>> import ssl
	>>> ssl.cert_time_to_seconds("May  9 00:00:00 2007 GMT")
	1178694000.0
	>>> import time
	>>> time.ctime(ssl.cert_time_to_seconds("May  9 00:00:00 2007 GMT"))
	'Wed May  9 00:00:00 2007'
	>>>
	
	"""
	pass
	
def get_server_certificate(addr,ssl_version=PROTOCOL_SSLv3,ca_certs=None):
	"""
	Given the address ``addr`` of an SSL-protected server, as a (*hostname*,
	*port-number*) pair, fetches the server's certificate, and returns it as a
	PEM-encoded string.  If ``ssl_version`` is specified, uses that version of
	the SSL protocol to attempt to connect to the server.  If ``ca_certs`` is
	specified, it should be a file containing a list of root certificates, the
	same format as used for the same parameter in :func:`wrap_socket`.  The call
	will attempt to validate the server certificate against that set of root
	certificates, and will fail if the validation attempt fails.
	
	"""
	pass
	
def DER_cert_to_PEM_cert(DER_cert_bytes):
	"""
	Given a certificate as a DER-encoded blob of bytes, returns a PEM-encoded
	string version of the same certificate.
	
	"""
	pass
	
def PEM_cert_to_DER_cert(PEM_cert_string):
	"""
	Given a certificate as an ASCII PEM string, returns a DER-encoded sequence of
	bytes for that same certificate.
	
	"""
	pass
	
