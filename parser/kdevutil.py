import sys
import pydoc
from pydoc import *

def get_python_path(): 
    return sys.path
    
def append_to_python_path(path):
    sys.path.append(path)

def getdoc(*args):
    '''Entry point to get the documentation.
    '''
    try:
        if not args: return ''
        for arg in args:
            if ispath(arg) and not os.path.exists(arg):
                return 'file %r does not exist' % arg
                break
            try:
                if ispath(arg) and os.path.isfile(arg):
                    arg = importfile(arg)
                if ispath(arg) and os.path.isdir(arg):
                    return writedocs(arg)
                else:
                    return writedoc(arg)
            except ErrorDuringImport as value:
                raise value

    except Exception as e:
        import traceback
        print traceback.print_exc()
        return 'Error %r: %r' % (args, e)

def writedoc(thing, forceload=0):
    '''Reimplementation of pydoc.writedoc to return the generated html
    instead of writing it to a file.
    '''
    try:
        obj, name = resolve(thing, forceload)
        page = html.page(describe(obj),
                         html.document(obj, name))
        return page
    except (ImportError, ErrorDuringImport) as value:
        raise value

def writedocs(dirs, pkgpath='', done=None):
    '''Reimplementation of pydoc.writedocs to return the generated html
    instead of writing it to a file.
    '''    
    if done is None: done = {}
    output = list()
    for importer, modname, ispkg in pkgutil.walk_packages([dirs], pkgpath):
        output.append(writedoc(modname))
    return ''.join(output)

def safeimport(path, forceload=0, cache={}):        
    ''' Reimplementation of pydoc.safeimport so that it works inside Kross
    
    -elif exc is ImportError and extract_tb(tb)[-1][2]=='safeimport':
    +elif exc is ImportError and any([item[2]=='safeimport' for item in extract_tb(tb)]):
    
    Import a module; handle errors; return None if the module isn't found.

    If the module *is* found but an exception occurs, it's wrapped in an
    ErrorDuringImport exception and reraised.  Unlike __import__, if a
    package path is specified, the module at the end of the path is returned,
    not the package at the beginning.  If the optional 'forceload' argument
    is 1, we reload the module from disk (unless it's a dynamic extension).'''
    try:
        # If forceload is 1 and the module has been previously loaded from
        # disk, we always have to reload the module.  Checking the file's
        # mtime isn't good enough (e.g. the module could contain a class
        # that inherits from another module that has changed).
        if forceload and path in sys.modules:
            if path not in sys.builtin_module_names:
                # Avoid simply calling reload() because it leaves names in
                # the currently loaded module lying around if they're not
                # defined in the new source file.  Instead, remove the
                # module from sys.modules and re-import.  Also remove any
                # submodules because they won't appear in the newly loaded
                # module's namespace if they're already in sys.modules.
                subs = [m for m in sys.modules if m.startswith(path + '.')]
                for key in [path] + subs:
                    # Prevent garbage collection.
                    cache[key] = sys.modules[key]
                    del sys.modules[key]
        module = __import__(path)
    except:
        # Did the error occur before or after the module was found?
        (exc, value, tb) = info = sys.exc_info()
        if path in sys.modules:
            # An error occurred while executing the imported module.
            raise ErrorDuringImport(sys.modules[path].__file__, info)
        elif exc is SyntaxError:
            # A SyntaxError occurred before we could execute the module.
            raise ErrorDuringImport(value.filename, info)
        elif exc is ImportError and any([item[2]=='safeimport' for item in extract_tb(tb)]):
            # The import error occurred directly in this function,
            # which means there is no such module in the path.
            return None
        else:
            # Some other error occurred during the importing process.
            raise ErrorDuringImport(path, sys.exc_info())
    for part in split(path, '.')[1:]:
        try: module = getattr(module, part)
        except AttributeError: return None
    return module

pydoc.safeimport = safeimport
pydoc.writedocs = writedocs
pydoc.writedoc = writedoc

def test():
    return sum(range(10))
    
