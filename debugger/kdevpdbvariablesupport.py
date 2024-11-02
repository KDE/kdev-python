# SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

import sys
import types
import math
import copy

# pylint: disable=C0103, R0903, C0115, R1710
# This module implements the kdevPdb's variable machinery and other helpers.


class enumeratorBase():
    '''Enumerate a list of things.
       Sub classes must compute the sequence length for super().__init__(...).
    '''
    def __init__(self, ref, size):
        self.objectref = ref
        self.size = size

    def __len__(self):
        return self.size

    def next(self):
        '''Sub classes must override this method,
           and set self.objectref = None once completed.'''
        self.objectref = None


class namespaceEnumerator(enumeratorBase):
    '''Enumerate a namespace object.'''
    def __init__(self, obj):
        # filter out some uninteresting python internals.
        filtter = ('__builtins__', '__file__', '__name__', '__spec__')
        obj = [(x, y) for x, y in obj if x not in filtter]
        super().__init__(obj, len(obj))

    def next(self):
        for x, y in self.objectref:
            assert isinstance(x, str)
            yield (x, y)
        self.objectref = None


class UnknownType():
    '''Helper type to differentiate getattr() returning NoneType'''


class attributeEnumerator(enumeratorBase):
    '''Enumerate an object attributes with dir() builtin.'''
    def __init__(self, obj):
        # Sort, although KDevelop will sort the generated set differently.
        # The ordering however does help the user to obtain the attributes in
        # a much nicer order if all of the attributes aren't immediately enumerated.
        g = [[], [], [], [], [], []]
        for x in dir(obj):
            try:
                attr = getattr(obj, x, UnknownType)
                if attr is UnknownType:
                    continue
            except Exception:
                continue
            # order callable attributes after non-callable.
            iscallable = callable(attr)
            if len(x) >= 2 and x[:2] == '__':
                g[4 + iscallable].append(x)
            elif x[0] == '_':
                g[2 + iscallable].append(x)
            else:
                g[0 + iscallable].append(x)
        self.attribs = [x for l in g for x in l]
        hint = len(g[0]) + len(g[1])
        self.expandhint = min(10, len(self.attribs)) if hint == 0 else hint
        super().__init__(obj, len(self.attribs))

    def next(self):
        for x in self.attribs:
            yield (x, getattr(self.objectref, x))
        self.objectref = None


class listEnumerator(enumeratorBase):
    '''Enumerate an list() like sequence with enumerate().'''
    def __init__(self, obj):
        super().__init__(obj, len(obj))

    def next(self):
        for i, x in enumerate(self.objectref):
            yield (f'[{i}]', x)
        self.objectref = None


class dictEnumerator(enumeratorBase):
    '''Enumerate an dict() like object.'''
    def __init__(self, obj):
        super().__init__(obj, len(obj) * 2)

    def next(self):
        try:
            for i, x in enumerate(self.objectref.items()):
                yield (f'[{i}].key', x[0])
                yield (f'[{i}].value', x[1])
        except Exception:
            pass
        self.objectref = None


class chunkEnumerator(enumeratorBase):
    '''Enumerate a string like object in MAX_LEN length chunks'''
    MAX_LEN = 100

    def __init__(self, obj):
        super().__init__(obj, math.ceil(len(obj) / chunkEnumerator.MAX_LEN))

    def next(self):
        for i in range(0, len(self.objectref), chunkEnumerator.MAX_LEN):
            chunk = self.objectref[i:i + chunkEnumerator.MAX_LEN]
            yield (f'[{i}..{i + len(chunk) - 1}]', chunk)
        self.objectref = None


class ExceptionInfo():
    '''Hold user viewable exception info'''
    def __init__(self, _exc, _traceback):
        self.exc = _exc
        self.traceback = _traceback


class ExceptionNode():
    def __init__(self, _exc, _traceback):
        self.exc_type = _exc.__class__.__qualname__
        self.exc_value = ExceptionInfo(_exc, _traceback)


class Exceptions():
    '''Hold a list of ExceptionNodes'''
    def __init__(self, _data):
        self.data = _data


class excInfoEnumerator(enumeratorBase):
    def __init__(self, exc):
        super().__init__(exc, 2)

    def next(self):
        yield 'args', self.objectref.exc.args
        yield 'from', self.objectref.traceback
        self.objectref = None


class excNodeEnumerator(enumeratorBase):
    def __init__(self, nodes):
        super().__init__(nodes, len(nodes))

    def next(self):
        for x in self.objectref:
            yield (x.exc_type, x.exc_value)
        self.objectref = None


class Namespace():
    def __init__(self):
        self.label = ""    # namespace's label inserted in handles
        self.names = {}    # mapping of handles into their longnames in self.handles[]
        self.handles = {}  # mapping of longname into the current and old handle
        self.inited = set()  # set of enumerated longnames.


# Reduced set of immutable types. (see copy._copy_immutable())
_skip_shallowcopy = {types.NoneType, int, float, bool, complex, str,
                     type, range, slice, property,
                     types.BuiltinFunctionType, types.EllipsisType,
                     types.NotImplementedType, types.FunctionType, types.CodeType}


def _shallowcopy(value):
    '''Return a shallow copy of a value if possible or identity'''
    cls = type(value)
    if cls in _skip_shallowcopy:
        return value
    # pylint: disable=W0718
    # Note: copy.copy() can raise arbitrary exceptions when it fails.
    try:
        return copy.copy(value)
    except Exception:
        # Not copy-able: add the type to the ignored set of types,
        # to skip handling the exception again.
        _skip_shallowcopy.add(cls)
        return value


def compareValues(a, b):
    '''General non-equal comparison of two values'''
    try:
        changed = a != b
        if isinstance(changed, bool):
            return changed
    except Exception:
        pass


try:
    import numpy
    numpy.set_printoptions(threshold=numpy.inf)

    class ndarrayEnumerator(enumeratorBase):
        '''Decompose numpy.ndarray into a list of sub dimensions'''
        def __init__(self, obj):
            assert isinstance(obj, numpy.ndarray)
            data = [obj[i] for i in range(obj.shape[0])]
            super().__init__(data, len(data))

        def next(self):
            for i, x in enumerate(self.objectref):
                yield (f'[{i}]', x)
            self.objectref = None

    def inspectNumpyArray(obj, gens, handle):
        '''Inspect numpy.ndarray.'''
        if not isinstance(obj, numpy.ndarray):
            return None
        if len(obj.shape) == 1:
            return {'count': 0, 'data': f"{obj}"}
        if len(obj.shape) > 1:
            # peel dimensions off:
            g = ndarrayEnumerator(obj)
            gens[handle] = g.next()
            return {'count': len(g), 'data': f"shape={obj.shape}", 'expandhint': len(g)}
        return {'count': 0, 'data': '<invalid>'}

    def compareNumpyArrays(a, b):
        '''Compare ndarrays'''
        try:
            return not numpy.array_equal(a, b)
        except Exception:
            pass
except ImportError:
    pass


def inspectSimpleValue(obj, *_):
    '''Inspect a simple value with no children'''
    if isinstance(obj, (types.NoneType, int, bool, float)):
        return {'count': 0, 'data': str(obj)}


def inspectMethodOrFunction(obj, *_):
    '''Inspect a method or function type.'''
    try:
        code = obj.__func__.__code__
        if code:
            # Instance method
            return {'count': 0, 'data': f'{obj.__qualname__}'}
    except Exception:
        pass
    try:
        code = obj.__code__
        if code:
            # Function
            return {'count': 0, 'data': f'{obj.__qualname__}'}
    except Exception:
        pass


def inspectExceptions(obj, gens, handle):
    '''Inspect getreturninfo() exception list.'''
    if not isinstance(obj, Exceptions):
        return None
    # This is synthesized by getreturninfo()
    g = excNodeEnumerator(obj.data)
    gens[handle] = g.next()
    return {'count': len(g), 'type': ''}


def inspectExceptionInfo(obj, gens, handle):
    '''Inspect getreturninfo() exception node.'''
    if not isinstance(obj, ExceptionInfo):
        return None
    g = excInfoEnumerator(obj)
    gens[handle] = g.next()
    return {'count': len(g), 'type': '', 'expandhint': 2}


def inspectClass(obj, gens, handle):
    '''Inspect a class type.'''
    try:
        if obj.__class__ is type:
            report = inspectAttributes(obj, gens, handle)
            report['data'] = f'class {obj.__qualname__}'
            return report
    except AttributeError:
        pass


def inspectCallable(obj, *_):
    '''Inspect a callable type.'''
    if callable(obj):
        return {'count': 0, 'data': '<callable>'}


def inspectModuleType(obj, gens, handle):
    '''Inspect a module.'''
    if not isinstance(obj, types.ModuleType):
        return None
    report = inspectAttributes(obj, gens, handle)
    report['data'] = f"module '{obj.__name__}'"
    return report


def inspectDataString(obj, gens, handle):
    '''Inspect a string like data.'''
    if not isinstance(obj, (str, bytes, bytearray, memoryview)):
        return None
    # For shorter than chunkEnumerator.MAX_LEN chars, report a direct value with 'len'.
    # Otherwise, report in chunks as the sequence may be *very* long.
    # (megabytes perhaps even..)
    try:
        report = {'len': len(obj)}
    except TypeError:
        report = {'len': 0}
    if report['len'] > chunkEnumerator.MAX_LEN:
        g = chunkEnumerator(obj)
        gens[handle] = g.next()
        report['count'] = len(g)
        return report
    report['count'] = 0
    if isinstance(obj, (memoryview, bytearray)):
        # repr() doesn't work well for these types.
        report['data'] = repr(bytes(obj))
        return report
    report['data'] = repr(obj)
    return report


def inspectSequence(obj, gens, handle):
    '''Inspect a sequence.'''
    if not isinstance(obj, (list, tuple, set, frozenset)):
        return None
    g = listEnumerator(obj)
    gens[handle] = g.next()
    return {'count': len(g), 'len': len(obj), 'expandhint': 3}


def inspectDict(obj, gens, handle):
    '''Inspect a dictionary.'''
    if not isinstance(obj, dict):
        return None
    g = dictEnumerator(obj)
    gens[handle] = g.next()
    return {'count': len(g), 'len': len(obj), 'expandhint': 2}


def inspectAttributes(obj, gens, handle):
    '''Inspect attributes of obj.'''
    # This works on all nearly object types, if we have no better way to represent the value.
    g = attributeEnumerator(obj)
    gens[handle] = g.next()
    return {'count': len(g), 'expandhint': g.expandhint}


class kdevExprValueMapper():
    def __init__(self):
        self.handleCounter = 0
        # Mapping of handles into the pinned values.
        self.objectsByHandle = {}
        # Mapping of handles into generators.
        self.objectEnumerators = {}
        # All namespace objects.
        self.objectsByNamespace = {}
        self.droppedNamespaces = set()
        self.variableNsids = -3
        # List of inspect() functions.
        # The order is critical, the first that doesn't return None wins.
        self.detectors = [
            inspectSimpleValue,
            inspectMethodOrFunction,
            inspectExceptions,
            inspectExceptionInfo,
            inspectClass,
            inspectCallable,
            inspectModuleType,
            inspectDataString,
            inspectSequence,
            inspectDict,
            inspectAttributes]
        # List of compare() functions.
        self.comparators = [compareValues]

        # Numpy support is optional.
        if getattr(sys.modules[__name__], 'inspectNumpyArray', None):
            self.detectors.insert(1, inspectNumpyArray)
            self.comparators.append(compareNumpyArrays)

    def makeHandle(self):
        '''Make a variable handle.'''
        self.handleCounter += 1
        return self.handleCounter

    def error(self, msg, lnend='\n'):
        raise NotImplementedError("subclass must implement this method.")

    def get_topindex(self):
        raise NotImplementedError("subclass must implement this method.")

    def dropNamespace(self, ns_id):
        '''Cleanup a namespace id'''
        self.droppedNamespaces.add(ns_id)

    def cleanupobjects(self):
        '''Cleanup invalidated state after pausing'''
        self.objectEnumerators.clear()
        # Purge unavailable namespaces.
        for ns_id in self.objectsByNamespace:
            if ns_id > self.get_topindex():
                self.dropNamespace(ns_id)
        # Coarse purge handles (and longnames) that are now unreachable
        # from the possible namespaces.
        reachable = set()
        unreachable = set()
        for ns_id, ns in list(self.objectsByNamespace.items()):
            if ns_id in self.droppedNamespaces:
                unreachable.update(ns.names)
                # Drop the entire namespace object.
                del self.objectsByNamespace[ns_id]
            else:
                reachable.update(ns.names)
        self.droppedNamespaces.clear()
        # Drop handles which are not in reachable.
        unreachable -= reachable
        num_purged = len(unreachable)
        for ptr in unreachable:
            del self.objectsByHandle[ptr]
        # Purge all longnames which have not been initialized/used.
        pinned = len(self.objectsByHandle)
        for ns in self.objectsByNamespace.values():
            for longname, handles in list(ns.handles.items()):
                if longname in ns.inited:
                    continue
                ns.handles.pop(longname, None)
                ns.names.pop(handles[0], None)
                ns.names.pop(handles[1], None)
                self.objectsByHandle.pop(handles[0], None)
                self.objectsByHandle.pop(handles[1], None)
            ns.inited.clear()
        num_purged += pinned - len(self.objectsByHandle)
        return {'purged': num_purged, 'pinned': len(self.objectsByHandle)}

    def updateNamespace(self, items, ns_id, ns_label):
        '''Create a new namespace handle from a list of tuples'''
        ns = self.objectsByNamespace.setdefault(ns_id, Namespace())
        if ns_label in ns.handles:
            handle = ns.handles[ns_label][0]
        else:
            handle = self.makeHandle()
            # Link the handle inside its own namespace.
            ns.handles[ns_label] = [handle, 0]
        ns.label = ns_label
        ns.names[handle] = ns_label
        ns.inited.add(ns_label)
        self.objectsByHandle[handle] = (ns_id, True)
        g = namespaceEnumerator(items)
        self.objectEnumerators[handle] = g.next()
        return len(g), handle

    def enumerateHandle(self, handle, ns_id, do_copy=True):
        '''Enumerate next variable of a handle.'''
        try:
            # try generate the next item.
            objname, value = next(self.objectEnumerators[handle])
        except StopIteration:
            # the generator was exhausted, remove it.
            self.objectEnumerators.pop(handle, None)
            return None
        except KeyError:
            # No generator was set up.
            # (the client likely made an mistake)
            return None

        parent = self.objectsByHandle[handle]
        if len(parent) == 2:
            # The handle refers to a namespace.
            ns = self.objectsByNamespace[parent[0]]
            longname = objname
        else:
            # Build the current longname for value
            assert ns_id in self.objectsByNamespace
            ns = self.objectsByNamespace[ns_id]
            # '/' is used to join child name to the parent name rather than '.' because
            # this makes it possible later to split the longname into its components.
            longname = ns.names[handle] + '/' + objname

        if longname in ns.inited:
            # Already initialized this longname.
            return {'expression': objname, 'ptr': ns.handles[longname][0]}

        handles = ns.handles.get(longname)
        if handles is None:
            # Make a new pair handles.
            # Initially, the other handle will have no pinned value in objectsByHandle.
            handles = [self.makeHandle(), self.makeHandle()]
            ns.handles[longname] = handles
        # Swap the current and previous handles.
        handles[0], handles[1] = handles[1], handles[0]
        # Update the handles[0]'s pinned value with a shallow copy of the value
        # when possible or reference the value as-is.
        newvalue = _shallowcopy(value) if do_copy else value
        self.objectsByHandle[handles[0]] = (newvalue,)
        # Associate the handle[0] with a longname.
        # Although ns.names[handles[1]] is technically able to refer to a different
        # longname than ns.names[handles[0]], I have never observed this happening.
        # Hence the assert:
        assert handles[1] not in ns.names or ns.names[handles[1]] == longname
        ns.names[handles[0]] = longname
        # Mark the longname as initialized.
        ns.inited.add(longname)
        return {'expression': objname, 'ptr': handles[0]}

    def inspectvalue(self, handle, ns_id):
        ''' Determine the variable's value and other details:
            - The 'count' number of children items, if any, and 'type'.
              These fields must exist.
            Optional fields (can be omitted from the response):
            - 'data' provides the displayed value of the variable.
            - 'len' is displayed in place of 'data' as "len=...",
               or as prefix "len=..., " if both are provided.
            - 'expandhint' is how many children, at minimum, the client should enumerate.
               If not reported, this is min(1,count)
            return: {'count': int(), 'type': str(), 'data': str(),
                     'len': int(), 'expandhint': int()}
        '''
        try:
            obj = self.objectsByHandle[handle][0]
        except KeyError:
            # Not found in the table. Respond with "None" to tell the given handle no longer exists.
            return None

        # Compute the changed state.
        changed = False
        if ns_id is not None:
            ns = self.objectsByNamespace[ns_id]
            handles = ns.handles[ns.names[handle]]
            changed = True
            if handles[1] in self.objectsByHandle:
                for cmp in self.comparators:
                    changed = cmp(obj, self.objectsByHandle[handles[1]][0])
                    if changed is not None:
                        break

        for proc in self.detectors:
            ret = proc(obj, self.objectEnumerators, handle)
            if ret is not None:
                ret.setdefault('changed', changed)
                ret.setdefault('type', obj.__class__.__qualname__)
                return ret
        return None

    def evalexpression(self, expr, frame):
        '''Attempts to evaluate an expression in the context of a stack-frame.'''
        # confine the frame.f_globals.__builtins__ a bit.
        fglobals = {}
        fglobals.update(frame.f_globals)
        fbuiltins = {}
        fbuiltins.update(fglobals['__builtins__'])
        del fbuiltins['print']
        del fbuiltins['__import__']
        del fbuiltins['eval']
        del fbuiltins['exec']
        del fbuiltins['compile']
        fglobals['__builtins__'] = fbuiltins
        try:
            evaluate_result = frame.evaluate(expr, fglobals, frame.f_locals)
            return {'value': evaluate_result, 'error': False}
        except Exception as e:
            # Log the error.
            self.error(f"{e}")
        return {'error': True}
