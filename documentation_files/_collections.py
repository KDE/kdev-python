"""This file contains auto-generated documentation extracted
from python run-time information. It is analyzed by KDevelop
to offer features such as code-completion and syntax highlighting.
If you discover errors in KDevelop's support for this module,
you can edit this file to correct the errors, e.g. you can add
additional return statements to functions to control the return
type to be used for that function by the analyzer.
Make sure to keep a copy of your changes so you don't accidentally
overwrite them by re-generating the file.
If you do significant improvements, consider sharing the file
with others through the Settings -> Configure KDevelop -> Python Documentation data
module!"""

class defaultdict:
    __doc__ = str()
    __hash__ = None
    def clear(self, _):
        """D.clear() -> None.  Remove all items from D."""
        return None
    def copy(self, _):
        """D.copy() -> a shallow copy of D."""
        return None
    default_factory = member_descriptor()
    def _fromkeys(self, _):
        """Returns a new dict with keys from iterable and values equal to value."""
        return None
    def get(self, k, d=None):
        """D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""
        return None
    def items(self, _):
        """D.items() -> a set-like object providing a view on D's items"""
        return None
    def keys(self, _):
        """D.keys() -> a set-like object providing a view on D's keys"""
        return None
    def pop(self, k, d=None):
        """D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised"""
        return None
    def popitem(self, _):
        """D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty."""
        return None
    def setdefault(self, k, d=None):
        """D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D"""
        return None
    def update(self, E=None, F=None):
        """D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]"""
        return None
    def values(self, _):
        """D.values() -> an object providing a view on D's values"""
        return None

class deque:
    """ ! TypeContainer ! """
    __doc__ = str()
    __hash__ = None
    def __init__(self):
        """! returnContentEqualsContentOf ! 0"""
        return deque()
    def append(self, _):
        """Add an element to the right side of the deque.
        ! addsTypeOfArg ! 0"""
        return None
    def appendleft(self, _):
        """
        ! addsTypeOfArg ! 0
        Add an element to the left side of the deque."""
        return None
    def clear(self, _):
        """Remove all elements from the deque."""
        return None
    def copy(self, _):
        """Return a shallow copy of a deque."""
        return deque()
    def count(self, value):
        """D.count(value) -> integer -- return number of occurrences of value"""
        return 0
    def extend(self, _):
        """! addsTypeOfArgContent ! 0
        Extend the right side of the deque with elements from the iterable"""
        return None
    def extendleft(self, _):
        """! addsTypeOfArgContent ! 0
        Extend the left side of the deque with elements from the iterable"""
        return None
    def index(self, value, start=None, stop=None):
        """D.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present."""
        return 0
    def insert(self, index, object):
        """! addsTypeOfArg ! 1
        D.insert(index, object) -- insert object before index"""
        return None
    maxlen = 1
    def pop(self, _):
        """Remove and return the rightmost element."""
        return None
    def popleft(self, _):
        """Remove and return the leftmost element."""
        return None
    def remove(self, value):
        """D.remove(value) -- remove first occurrence of value."""
        return None
    def reverse(self, _):
        """D.reverse() -- reverse *IN PLACE*"""
        return None
    def rotate(self, defaultn=1):
        """Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left."""
        return None
