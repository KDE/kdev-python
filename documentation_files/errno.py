#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Standard errno system symbols.


This module makes available standard ``errno`` system symbols. The value of each
symbol is the corresponding integer value. The names and descriptions are
borrowed from :file:`linux/include/errno.h`, which should be pretty
all-inclusive.


"""
"""
Dictionary providing a mapping from the errno value to the string name in the
underlying system.  For instance, ``errno.errorcode[errno.EPERM]`` maps to
``'EPERM'``.

To translate a numeric error code to an error message, use :func:`os.strerror`.

Of the following list, symbols that are not used on the current platform are not
defined by the module.  The specific list of defined symbols is available as
``errno.errorcode.keys()``.  Symbols available can include:


"""
errorcode = None
"""
Operation not permitted


"""
EPERM = None
"""
No such file or directory


"""
ENOENT = None
"""
No such process


"""
ESRCH = None
"""
Interrupted system call


"""
EINTR = None
"""
I/O error


"""
EIO = None
"""
No such device or address


"""
ENXIO = None
"""
Arg list too long


"""
E2BIG = None
"""
Exec format error


"""
ENOEXEC = None
"""
Bad file number


"""
EBADF = None
"""
No child processes


"""
ECHILD = None
"""
Try again


"""
EAGAIN = None
"""
Out of memory


"""
ENOMEM = None
"""
Permission denied


"""
EACCES = None
"""
Bad address


"""
EFAULT = None
"""
Block device required


"""
ENOTBLK = None
"""
Device or resource busy


"""
EBUSY = None
"""
File exists


"""
EEXIST = None
"""
Cross-device link


"""
EXDEV = None
"""
No such device


"""
ENODEV = None
"""
Not a directory


"""
ENOTDIR = None
"""
Is a directory


"""
EISDIR = None
"""
Invalid argument


"""
EINVAL = None
"""
File table overflow


"""
ENFILE = None
"""
Too many open files


"""
EMFILE = None
"""
Not a typewriter


"""
ENOTTY = None
"""
Text file busy


"""
ETXTBSY = None
"""
File too large


"""
EFBIG = None
"""
No space left on device


"""
ENOSPC = None
"""
Illegal seek


"""
ESPIPE = None
"""
Read-only file system


"""
EROFS = None
"""
Too many links


"""
EMLINK = None
"""
Broken pipe


"""
EPIPE = None
"""
Math argument out of domain of func


"""
EDOM = None
"""
Math result not representable


"""
ERANGE = None
"""
Resource deadlock would occur


"""
EDEADLK = None
"""
File name too long


"""
ENAMETOOLONG = None
"""
No record locks available


"""
ENOLCK = None
"""
Function not implemented


"""
ENOSYS = None
"""
Directory not empty


"""
ENOTEMPTY = None
"""
Too many symbolic links encountered


"""
ELOOP = None
"""
Operation would block


"""
EWOULDBLOCK = None
"""
No message of desired type


"""
ENOMSG = None
"""
Identifier removed


"""
EIDRM = None
"""
Channel number out of range


"""
ECHRNG = None
"""
Level 2 not synchronized


"""
EL2NSYNC = None
"""
Level 3 halted


"""
EL3HLT = None
"""
Level 3 reset


"""
EL3RST = None
"""
Link number out of range


"""
ELNRNG = None
"""
Protocol driver not attached


"""
EUNATCH = None
"""
No CSI structure available


"""
ENOCSI = None
"""
Level 2 halted


"""
EL2HLT = None
"""
Invalid exchange


"""
EBADE = None
"""
Invalid request descriptor


"""
EBADR = None
"""
Exchange full


"""
EXFULL = None
"""
No anode


"""
ENOANO = None
"""
Invalid request code


"""
EBADRQC = None
"""
Invalid slot


"""
EBADSLT = None
"""
File locking deadlock error


"""
EDEADLOCK = None
"""
Bad font file format


"""
EBFONT = None
"""
Device not a stream


"""
ENOSTR = None
"""
No data available


"""
ENODATA = None
"""
Timer expired


"""
ETIME = None
"""
Out of streams resources


"""
ENOSR = None
"""
Machine is not on the network


"""
ENONET = None
"""
Package not installed


"""
ENOPKG = None
"""
Object is remote


"""
EREMOTE = None
"""
Link has been severed


"""
ENOLINK = None
"""
Advertise error


"""
EADV = None
"""
Srmount error


"""
ESRMNT = None
"""
Communication error on send


"""
ECOMM = None
"""
Protocol error


"""
EPROTO = None
"""
Multihop attempted


"""
EMULTIHOP = None
"""
RFS specific error


"""
EDOTDOT = None
"""
Not a data message


"""
EBADMSG = None
"""
Value too large for defined data type


"""
EOVERFLOW = None
"""
Name not unique on network


"""
ENOTUNIQ = None
"""
File descriptor in bad state


"""
EBADFD = None
"""
Remote address changed


"""
EREMCHG = None
"""
Can not access a needed shared library


"""
ELIBACC = None
"""
Accessing a corrupted shared library


"""
ELIBBAD = None
"""
.lib section in a.out corrupted


"""
ELIBSCN = None
"""
Attempting to link in too many shared libraries


"""
ELIBMAX = None
"""
Cannot exec a shared library directly


"""
ELIBEXEC = None
"""
Illegal byte sequence


"""
EILSEQ = None
"""
Interrupted system call should be restarted


"""
ERESTART = None
"""
Streams pipe error


"""
ESTRPIPE = None
"""
Too many users


"""
EUSERS = None
"""
Socket operation on non-socket


"""
ENOTSOCK = None
"""
Destination address required


"""
EDESTADDRREQ = None
"""
Message too long


"""
EMSGSIZE = None
"""
Protocol wrong type for socket


"""
EPROTOTYPE = None
"""
Protocol not available


"""
ENOPROTOOPT = None
"""
Protocol not supported


"""
EPROTONOSUPPORT = None
"""
Socket type not supported


"""
ESOCKTNOSUPPORT = None
"""
Operation not supported on transport endpoint


"""
EOPNOTSUPP = None
"""
Protocol family not supported


"""
EPFNOSUPPORT = None
"""
Address family not supported by protocol


"""
EAFNOSUPPORT = None
"""
Address already in use


"""
EADDRINUSE = None
"""
Cannot assign requested address


"""
EADDRNOTAVAIL = None
"""
Network is down


"""
ENETDOWN = None
"""
Network is unreachable


"""
ENETUNREACH = None
"""
Network dropped connection because of reset


"""
ENETRESET = None
"""
Software caused connection abort


"""
ECONNABORTED = None
"""
Connection reset by peer


"""
ECONNRESET = None
"""
No buffer space available


"""
ENOBUFS = None
"""
Transport endpoint is already connected


"""
EISCONN = None
"""
Transport endpoint is not connected


"""
ENOTCONN = None
"""
Cannot send after transport endpoint shutdown


"""
ESHUTDOWN = None
"""
Too many references: cannot splice


"""
ETOOMANYREFS = None
"""
Connection timed out


"""
ETIMEDOUT = None
"""
Connection refused


"""
ECONNREFUSED = None
"""
Host is down


"""
EHOSTDOWN = None
"""
No route to host


"""
EHOSTUNREACH = None
"""
Operation already in progress


"""
EALREADY = None
"""
Operation now in progress


"""
EINPROGRESS = None
"""
Stale NFS file handle


"""
ESTALE = None
"""
Structure needs cleaning


"""
EUCLEAN = None
"""
Not a XENIX named type file


"""
ENOTNAM = None
"""
No XENIX semaphores available


"""
ENAVAIL = None
"""
Is a named type file


"""
EISNAM = None
"""
Remote I/O error


"""
EREMOTEIO = None
