# AUTO-GENERATED FILE -- DO NOT EDIT


RLIMIT_AS = 9
RLIMIT_CORE = 4
RLIMIT_CPU = 0
RLIMIT_DATA = 2
RLIMIT_FSIZE = 1
RLIMIT_MEMLOCK = 8
RLIMIT_NOFILE = 7
RLIMIT_NPROC = 6
RLIMIT_OFILE = 7
RLIMIT_RSS = 5
RLIMIT_STACK = 3
RLIM_INFINITY = -1
RUSAGE_CHILDREN = -1
RUSAGE_SELF = 0
__package__ = None

class error(Exception):

  pass

def getpagesize():
  pass

def getrlimit():
  pass

def getrusage():
  pass

def setrlimit():
  pass

class struct_rusage(object):
  """ struct_rusage: Result from getrusage.
  
  This object may be accessed either as a tuple of
      (utime,stime,maxrss,ixrss,idrss,isrss,minflt,majflt,
      nswap,inblock,oublock,msgsnd,msgrcv,nsignals,nvcsw,nivcsw)
  or via the attributes ru_utime, ru_stime, ru_maxrss, and so on. """

  n_fields = 16
  n_sequence_fields = 16
  n_unnamed_fields = 0
  ru_idrss = None
  ru_inblock = None
  ru_isrss = None
  ru_ixrss = None
  ru_majflt = None
  ru_maxrss = None
  ru_minflt = None
  ru_msgrcv = None
  ru_msgsnd = None
  ru_nivcsw = None
  ru_nsignals = None
  ru_nswap = None
  ru_nvcsw = None
  ru_oublock = None
  ru_stime = None
  ru_utime = None

