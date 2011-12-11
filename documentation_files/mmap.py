# AUTO-GENERATED FILE -- DO NOT EDIT


ACCESS_COPY = 3
ACCESS_READ = 1
ACCESS_WRITE = 2
ALLOCATIONGRANULARITY = 4096
MAP_ANON = 32
MAP_ANONYMOUS = 32
MAP_DENYWRITE = 2048
MAP_EXECUTABLE = 4096
MAP_PRIVATE = 2
MAP_SHARED = 1
PAGESIZE = 4096
PROT_EXEC = 4
PROT_READ = 1
PROT_WRITE = 2
__package__ = None

class error(EnvironmentError):

  pass

class mmap(object):
  """ Windows: mmap(fileno, length[, tagname[, access[, offset]]])
  
  Maps length bytes from the file specified by the file handle fileno,
  and returns a mmap object.  If length is larger than the current size
  of the file, the file is extended to contain length bytes.  If length
  is 0, the maximum length of the map is the current size of the file,
  except that if the file is empty Windows raises an exception (you cannot
  create an empty mapping on Windows).
  
  Unix: mmap(fileno, length[, flags[, prot[, access[, offset]]]])
  
  Maps length bytes from the file specified by the file descriptor fileno,
  and returns a mmap object.  If length is 0, the maximum length of the map
  will be the current size of the file when mmap is called.
  flags specifies the nature of the mapping. MAP_PRIVATE creates a
  private copy-on-write mapping, so changes to the contents of the mmap
  object will be private to this process, and MAP_SHARED creates a mapping
  that's shared with all other processes mapping the same areas of the file.
  The default value is MAP_SHARED.
  
  To map anonymous memory, pass -1 as the fileno (both versions). """

  def close(self):
    pass

  def find(self):
    pass

  def flush(self):
    pass

  def move(self):
    pass

  def read(self):
    pass

  def read_byte(self):
    pass

  def readline(self):
    pass

  def resize(self):
    pass

  def rfind(self):
    pass

  def seek(self):
    pass

  def size(self):
    pass

  def tell(self):
    pass

  def write(self):
    pass

  def write_byte(self):
    pass

