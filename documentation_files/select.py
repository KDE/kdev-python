# AUTO-GENERATED FILE -- DO NOT EDIT

""" This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows and OpenVMS, only sockets are supported; on Unix, all file descriptors. """

EPOLLERR = 8
EPOLLET = -2147483648
EPOLLHUP = 16
EPOLLIN = 1
EPOLLMSG = 1024
EPOLLONESHOT = 1073741824
EPOLLOUT = 4
EPOLLPRI = 2
EPOLLRDBAND = 128
EPOLLRDNORM = 64
EPOLLWRBAND = 512
EPOLLWRNORM = 256
PIPE_BUF = 4096
POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLMSG = 1024
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDNORM = 64
POLLWRBAND = 512
POLLWRNORM = 256
__package__ = None

class epoll(object):
  """ select.epoll([sizehint=-1])
  
  Returns an epolling object
  
  sizehint must be a positive integer or -1 for the default size. The
  sizehint is used to optimize internal data structures. It doesn't limit
  the maximum number of monitored events. """

  def close(self):
    """ close() -> None
    
    Close the epoll control file descriptor. Further operations on the epoll
    object will raise an exception. """
    return None

  closed = property(None, None, None,
                    """ True if the epoll handler is closed """
                    )


  def fileno(self):
    """ fileno() -> int
    
    Return the epoll control file descriptor. """
    return 1

  def fromfd(self, fd):
    """ fromfd(fd) -> epoll
    
    Create an epoll object from a given control fd. """
    return None

  def modify(self, fd, eventmask):
    """ modify(fd, eventmask) -> None
    
    fd is the target file descriptor of the operation
    events is a bit set composed of the various EPOLL constants """
    return None

  def poll(self, timeout=_1, maxevents=_1):
    """ poll([timeout=-1[, maxevents=-1]]) -> [(fd, events), (...)]
    
    Wait for events on the epoll file descriptor for a maximum time of timeout
    in seconds (as float). -1 makes poll wait indefinitely.
    Up to maxevents are returned to the caller. """
    return []

  def register(self, fd, eventmask=None):
    """ register(fd[, eventmask]) -> None
    
    Registers a new fd or modifies an already registered fd.
    fd is the target file descriptor of the operation.
    events is a bit set composed of the various EPOLL constants; the default
    is EPOLL_IN | EPOLL_OUT | EPOLL_PRI.
    
    The epoll interface supports all file descriptors that support poll. """
    return None

  def unregister(self, fd):
    """ unregister(fd) -> None
    
    fd is the target file descriptor of the operation. """
    return None

class error(Exception):

  pass

def poll():
  """ Returns a polling object, which supports registering and
  unregistering file descriptors, and then polling them for I/O events. """
  pass

def select(rlist, wlist, xlist, timeout=None):
  """ select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
  
  Wait until one or more file descriptors are ready for some kind of I/O.
  The first three arguments are sequences of file descriptors to be waited for:
  rlist -- wait until ready for reading
  wlist -- wait until ready for writing
  xlist -- wait for an ``exceptional condition''
  If only one kind of condition is required, pass [] for the other lists.
  A file descriptor is either a socket or file object, or a small integer
  gotten from a fileno() method call on one of those.
  
  The optional 4th argument specifies a timeout in seconds; it may be
  a floating point number to specify fractions of seconds.  If it is absent
  or None, the call will never time out.
  
  The return value is a tuple of three lists corresponding to the first three
  arguments; each contains the subset of the corresponding file descriptors
  that are ready.
  
  *** IMPORTANT NOTICE ***
  On Windows and OpenVMS, only sockets are supported; on Unix, all file
  descriptors can be used. """
  return ([], [], [])

