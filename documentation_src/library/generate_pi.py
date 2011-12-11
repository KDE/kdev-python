""" generate_pi.py -- Generate Python interface by inspecting a module
                      at runtime

Copyright (c) 2001-2011, Archaeopteryx Software, Inc.  All rights reserved.

Written by John P. Ehresman and Stephan R.A. Deibel

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Simple utility to generate a python interface file from inspecting a module
at run time.  First argument is the name of the module.  Subsequent arguments
are name:expression pairs -- a class with given name will be created in the
interface file with methods & attributes matching the methods & attributes
of the object that results from the expression. The expression will be 
evaluated within the context of the module. The interface will be written
to stdout.

This contains some code specific to Python standard library code because it
parses the docstring standards used there to determine information about
return values. However, it works also with code that does not contain those
type hints in docstrings (but return value type cannot be determined).

"""

# IMPORTANT:  This code has to run under all Python versions!

import sys
import os
import string
import stat
try:
  import inspect
except:
  inspect = None
kIronPython = (sys.version_info >= (1, 6) and sys.version.find('IronPython') != -1)

try:
  ascii_letters = string.ascii_letters
except:
  ascii_letters = string.letters
  
version = ((sys.hexversion & (0xff << 24)) >> 24,
           (sys.hexversion & 0x00ff0000) >> 16)

def string_split(s, sep=' '):
  return s.split(sep)
def string_join(s, sep):
  return sep.join(s)
def string_find(s, t):
  return s.find(t)
def string_strip(s):
  return s.strip()
def string_replace(s, f, t, count=-1):
  return s.replace(f, t, count)
def string_lower(s):
  return s.lower()
def string_rfind(s, x):
  return s.rfind(x)
def has_key(o, key):
  if version >= (3, 0):
    return key in o
  else:
    return o.has_key(key)
if version >= (3, 0):
  def callable(o):
    return hasattr(o, '__call__')
  
if version[0] == 1:
  printable_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~  \t\n\r\x0b\x0c'
else:
  printable_chars = string.printable
  
kOneLevelIndent = '  '
kNoValue = []

kStringTypes = [type('')]
import types
try:
  kStringTypes = types.StringTypes
except:
  pass
kLiteralTypes = [type(1), type(1.0), type(None)]
try:
  kLiteralTypes.append(types.EllipsisType)
  kLiteralTypes.append(types.BooleanType)
except:
  pass
kStructureTypes = [type([]), type(()), type({})]
kFileTypes = [type(sys.stdout)]
if version >= (3, 0):
  kListType = type([])
  kTupleType = type(())
  kDictType = type({})
else:
  kListType = types.ListType
  kTupleType = types.TupleType
  kDictType = types.DictType
  
# Property support contributed by Nigel Rowe, Aug 10, 2007
kPropertyTypes = []
try:
  kPropertyTypes.append(type(property()))
except:
  pass
import types
try:
  # types.GetSetDescriptorType only exists in python versions >= 2.5
  # and would otherwise need to be extracted from an extension module
  kPropertyTypes.append(types.GetSetDescriptorType)
except:
  pass
if kIronPython:
  import System
  kPropertyTypes.append(type(System.Version.Major))
  del System



# Types of type, old-style class -- use C api names to be a bit clearer
PyType_Type = type(type(''))
class _OldStyleClass:
  pass
PyClass_Type = type(_OldStyleClass)
del _OldStyleClass
kClassLikeTypes = [PyType_Type, PyClass_Type]

def WriteDocString(obj, file, indent):
  """ Writes doc string for object if there is one. """
  
  quote = '"""'

  doc = getattr(obj, '__doc__', None)
  if doc == None:
    return
  
  doc = doc.replace('\r\n', '\n')
  
  if kIronPython or sys.version_info >= (3, 0):
    is_unicode = 0
  else:
    try:
      is_unicode = isinstance(doc, unicode)
    except:
      is_unicode = 0

  doc_parts = string_split(doc, '\n')
  for i in range(0, len(doc_parts)):
    line_repr = repr(doc_parts[i])
    if string_lower(line_repr[:1]) == 'u':
      line_repr = line_repr[1:]
    line_repr = line_repr[1:-1]
    line_parts = string_split(line_repr, quote)
    line_repr = string_join(line_parts, '\\' + quote)
    if i != 0:
      line_repr = indent + line_repr
    doc_parts[i] = line_repr

  doc = string_join(doc_parts, '\n')
  if is_unicode:
    file.write(indent + 'u%s %s %s\n' % (quote, doc, quote))
  else:
    file.write(indent + '%s %s %s\n' % (quote, doc, quote))
      
def NextNonBlank(doc, i):
  for j in range(i, len(doc)):
    if doc[j] not in ' \t\r\n':
      return j
  return -1
    
def FindFirstLine(doc):
  paren_count = 0
  bracket_count = 0
  brace_count = 0
  first_line = ''
  seen_chars = 0
  i = 0
  while i < len(doc):
    c = doc[i]
    if c == '(':
      paren_count = paren_count + 1
    elif c == '[':
      bracket_count = bracket_count + 1
      next_pos = NextNonBlank(doc, i+1)
      if doc[next_pos] == ',':
        first_line = first_line + ', ['
        i = next_pos + 1
        continue
    elif c == '{':
      brace_count = brace_count + 1
    elif c == ')':
      paren_count = paren_count - 1
    elif c == ']':
      bracket_count = bracket_count - 1
      next_pos = NextNonBlank(doc, i+1)
      if doc[next_pos] == '[':
        first_line = first_line + '], ['
        i = next_pos + 1
        bracket_count = bracket_count + 1
        continue
    elif c == '}':
      brace_count = brace_count - 1
    elif c in (' \t\r\n') and not seen_chars:
      i = i + 1
      continue
    elif c == '\n':
      if paren_count + bracket_count + brace_count == 0:
        return string_join(string_split(first_line), ' ')
      else:
        i = i + 1
        continue
    seen_chars = 1
    first_line = first_line + c
    i = i + 1
      
  return string_join(string_split(first_line), ' ')

def ValidArgName(n):
  if len(n) == 0:
    return 0
  if n[0] not in '_' + ascii_letters:
    return 0
  for c in n[1:]:
    if c not in ascii_letters + string.digits + '_':
      return 0
  return 1

def GetCallableSignatureIPy(val, obj, name):
  import_line = None
  return_line = 'pass'
  doc = getattr(val, '__doc__', None)  
  if doc is None:
    return '', None, 'pass'
  
  import clr
  try:
    clr_type = clr.GetClrType(obj)
  except TypeError:
    # XXXXX happens when we get namespace tracker objects
    # Annoying ????
    sys.stderr.write('@@@@@ Class %s is not a type. (Method = %s)\n' % (obj, name))
    a, b = GetCallableSignature(val)
    return a, None, b
  methods = [m for m in clr_type.GetMethods() if m.Name == name]

  # Very occasionally (e.g. Microsoft.CSharp.CSharpCodeProvider.CreateProvider)
  # We fail to find the method. Also happens for some IronPython methods
  # Like ReferenceEquals and ToObject (inherited methods?)
  if not methods:
    sys.stderr.write('Unlikely as it may sound, class %s has no method %s\n' % (obj, name))
    a, b = GetCallableSignature(val)
    return a, None, b
  
  # XXXX if len(methods) > 1 we have multiple overloads
  # what to do? Just use the first.
  method = methods[0]

  return_type = method.ReturnType
  
  if return_type is not None:
    ns = return_type.Namespace
    import_line = 'import %s' % ns
    return_line = 'return %s.%s()' % (ns, return_type.Name)
  
  parameter_info = method.GetParameters()
  params = [p.Name for p in parameter_info]
  if not method.IsStatic:
    params = ['self'] + params
    
  return string_join(params, ', '), import_line, return_line
  
  
def GetCallableSignature(obj):
  doc = getattr(obj, '__doc__', None)  
  if doc is None:
    return '', 'pass'

  if kIronPython:
    return _IronPythonGetCallableSignature(doc)
  else:
    return _GetCallableSignature(doc)

def _GetCallableSignature(doc):
  
  try:
    return __GetCallableSignature(doc)
  except:
    import traceback
    sys.stderr.write("Error parsing call signature from docstring:\n")
    sys.stderr.write(doc)
    etype, evalue, etb = sys.exc_info()
    sys.stderr.write(string_join(traceback.format_exception(etype, evalue, etb), '\n'))
    return '', 'pass'

import re
ret_val_re = re.compile(r'^(?: )?([A-Za-z][A-Za-z0-9_\-]*)(?: |\[.*\] ).*\(.*\)') # Yuck!!!
def _IronPythonGetCallableSignature(doc):
  a, b = _GetCallableSignature(doc)
  if b != 'pass':
    return a, b
  
  mat = ret_val_re.match(doc)
  if mat is None:
    return a, 'pass'
  ret_val = 'return ' + mat.groups()[0] + '()'
  sys.stderr.write('#### Generating return value of %s\n' % repr(ret_val))
  return a, ret_val


def _ParseArgs(args):
  """ Parse args string w/o opening and closing () into list of argument 
  names. """

  args = string_strip(args)
  if args == '':
    return []
  
  # Parse each argument
  arglist = string_split(args, ',')
  parsed_args = []
  arg_count = 0
  seen_defaults = 0
  for i in range(0, len(arglist)):
    arg = string_strip(arglist[i])
    if string_find(arg, '=') > 0:
      seen_defaults = 1

    # Remove and count []'s indicating optional args
    fixed_arg = ''
    for c in arg:
      if c == '[':
        seen_defaults = 1
      elif c == ']':
        pass
      else:
        fixed_arg = fixed_arg + c
    arg = string_strip(fixed_arg)
    arg = string_replace(arg, '-', '_')
    
    # Remove surrounding quote seen in some cases for no apparent reason
    if len(arg) > 2 and arg[0] in ('"', "'") and arg[-1] == arg[0]:
      arg = arg[1:-1]

    # Sometimes there's an extra comma; treat as anonymous arg
    if len(arg) == 0:
      arg = 'arg'
      
    # An optional argument of some type with default value or * or **
    if seen_defaults:

      # Rest of args
      if arg == '...':
        arg = '*args'
        
      # Verbal description:  Create appropriate generic arg
      elif string_find(arg, ' ') >= 0:
        if string_find(arg, 'optional') == 0 and i == len(arglist) - 1:
          if seen_defaults:
            arg = '**argv'
          else:
            arg = '*argv'
        else:
          arg = 'arg%i=None' % arg_count
          seen_defaults = 1
          arg_count = arg_count + 1
          
      # Actual arg name -- add default if appropriate
      elif string_find(arg, '=') == -1 and arg[0] != '*':
        arg = arg + '=None'
        seen_defaults = 1

    elif arg == '...':
      seen_defaults = 1
      arg = '*args'
      
    # Use generic arg name if specified but not parseable
    elif len(arg) > 0 and not ValidArgName(arg):
      arg = 'arg%i' % arg_count
      arg_count = arg_count + 1
      
    if len(arg) > 0:
      parsed_args.append(arg)

  return parsed_args


def __GetCallableSignature(doc):  
  
  doc = string_replace(doc, '\r\n', '\n')
  doc = string_replace(doc, '\r', '\n')

  # Find the argument and return value spec in the docstring
  first_line = FindFirstLine(doc)
  #sys.stdout.write("FIRSTLINE %s" % str(first_line))
  args = None

  # Sometimes in form "spec -- comment" but also sometimes use --> or <==> instead of ->
  first_line = string_replace(first_line, '-->', '->')
  first_line = string_replace(first_line, '<==>', '->')
  if string_find(first_line, '--') >= 0:
    if string_find(first_line, '->') > 0:
      first_line = first_line[:string_find(first_line, '--')]
    else:
      first_line = string_replace(first_line, '--', '->', 1)
    
  if string_find(first_line, '->') >= 0:
    parts = string_split(first_line, '->')
    if len(parts) == 2:
      args, ret = parts
  elif string_find(first_line, '=') > 0:
    _parts = string_split(first_line, '=')
    parts = []
    for part in _parts:
      parts.append(string_strip(part))
    if len(parts) > 0 and string_find(parts[0], ' ') == -1:
      ret = parts[0]
      args = string_join(parts[1:], '=')
      lparen = string_find(args, '(')
      rparen = string_find(args, ')')
      if len(args) > 2 and lparen >= 0 and rparen > lparen:
        args = args[lparen+1:rparen]
  elif string_find(first_line, '(') >= 0:
    args = first_line
    ret = ''
  if args is None:
    lines = string_split(doc, '\n')
    if len(lines) == 1:
      return '', 'pass'
    else:
      return _GetCallableSignature(string_join(lines[1:], '\n'))

  # Extract arg spec from parenthesis
  lparen = string_find(args, '(')
  rparen = -1
  pos = lparen + 1
  nesting_count = 0
  while pos < len(args) and rparen == -1:
    if args[pos] == ')' and nesting_count == 0:
      rparen = pos
    elif args[pos] in '({[':
      nesting_count += 1
    elif args[pos] in ']})':
      nesting_count -= 1
    pos += 1
  if lparen >= 0 and rparen > lparen:
    args = args[lparen+1:rparen]
  
  parsed_args = _ParseArgs(args)
  
  # Build return specification
  retval = BuildReturnSpec(ret)
  if retval == '':
    retval = 'pass'
  else:
    retval = 'return ' + retval

  return string_join(parsed_args, ', '), retval

def BuildReturnSpec(ret):
  
  ret = string_strip(ret)
  if len(ret) > 2 and ((ret[0] == '(' and ret[-1] == ')') or
                       (ret[0] == '[' and ret[-1] == ']') or
                       (ret[0] == '{' and ret[-1] == '}')):
    if string_find(ret, '...') >= 0:
      retval = ret[0] + ret[-1]
    else:
      ret_items = string_split(ret[1:-1], ',')
      fixed_items = []
      for item in ret_items:
        item = string_replace(string_strip(item), ' ', '_')
        item = string_replace(item, '-', '_')
        fixed_items.append(BuildReturnSpec(item))
      ret = ret[0] + string_join(fixed_items, ', ') + ret[-1]
      retval = ret
  elif string_find(ret, 'tuple') >= 0:
    retval = '()'
  elif string_find(ret, 'list') >= 0:
    retval = '[]'
  elif string_find(ret, 'dict') >= 0:
    retval = '{}'
  elif string_find(ret, 'str') >= 0:
    retval = '""'
  elif string_find(ret, 'file') >= 0:
    if version[0] == 1 or (version[0] == 2 and version[1] < 2):
      retval = '__FileObject()'
    else:
      retval = 'file(__file__)'
  elif string_find(ret, 'socket') >= 0:
    retval = 'SocketType()'
  elif string_find(ret, 'int') >= 0:
    retval = '1'
  elif string_find(ret, 'float') >= 0:
    retval = '1.0'
  elif len(ret) > 0:
    retval = 'None'
  else:
    retval = ''
    
  return retval

kOmitTopLevel = ('__doc__', '__class__', '__new__', '__file__', '__name__', '__module__',
                 '__builtins__')

def ValidName(scope, name):
  if len(name) < 5:
    return 1
  if len(scope) == 1 and name in kOmitTopLevel:
    return 0
  if name[:2] == '__' and name[-2:] == '__':
    name = name[2:-2]
    if len(scope) > 1:
      return name == 'init'
    else:
      return 1
  else:
    return 1
    
def GetValue(obj, slot, default):
  if type(obj) == type({}):
    return obj.get(slot, default)
  else:
    return getattr(obj, slot, default)
  
def HasValue(obj, slot):
  if type(obj) == type({}):
    return has_key(obj, slot)
  else:
    return hasattr(obj, slot)
  
def ValueItems(obj):
  if type(obj) == type({}):
    return obj.keys()
  elif type(obj) in kClassLikeTypes or type(obj) == types.ModuleType:
    return dir(obj)
  else:
    return ()

def IsClassLike(val):
  for base in kClassLikeTypes:
    if isinstance(val, base):
      return 1
    
  return 0

def IsFunctionOrMethod(val):
  return not IsClassLike(val) and callable(val)

def SafeDir(o):
  try:
    return dir(o)
  except:
    return []

def GenForObject(scope, overrides, overrides_file, obj, file, seen_vals, indent = '', use_inspect=0):

  # Use __all__ attrib if obj is a module
  name_list = None
  if isinstance(obj, type(sys)):
    name_list = getattr(obj, '__all__', None)
  elif type(obj) == type({}):
    name_list = obj.keys()

  if kIronPython:
    sys.stderr.write('**** generating %s\n' % repr(obj))
  if name_list == None:
    name_list = SafeDir(obj)

  last_val = kNoValue
  num_written = 0
  for name in name_list:

    if type(obj) == type({}):
      val = obj[name]
    else:
      # XXX Probably use kIronPython branch for CPython as well
      if kIronPython:
        val = obj.__dict__.get(name, None)
        if val is None:
          val = getattr(obj, name, None)
      else:
        val = getattr(obj, name, None)
    
    if kIronPython and name == 'None':
      name = 'None_'
    
    # skip nested namespaces
    if kIronPython:
      import System
      if isinstance(val, type(System)):
        continue
      
    if ValidName(scope, name) and (not hasattr(val, '__objclass__') or val.__objclass__ == obj):
      
      # Value is a class object
      if IsClassLike(val):
        # Skip overridden values if the override is not also a class object
        if HasValue(overrides, name):
          oval = GetValue(overrides, name, kNoValue)
          if oval is not kNoValue and type(oval) not in kClassLikeTypes:
            continue
        try:
          val_name = val.__name__
        except:
          val_name = None
        if val_name != name and val_name in name_list:
          if last_val is not kNoValue and not callable(last_val):
            file.write('\n')
          file.write(indent + '%s = %s\n' % (name, val_name))
        elif not has_key(seen_vals, val):
          try:
            seen_vals[val] = 1
          except TypeError:
            sys.stderr.write("Failed to register %s (may cause duplicates)\n" % str(val))
          if last_val is not kNoValue and not callable(last_val):
            file.write('\n')
          try:
            GenPClassForType(scope + [name], GetValue(overrides, name, {}), overrides_file,
                             name, val, file, seen_vals, indent, use_inspect)
          except:
            pass # XXX May want to write exception to stderr
          num_written = num_written + 1
      
      # Try to use inspect module if requested, to place source directly (used
      # to write overrides)
      elif use_inspect and inspect is not None and IsFunctionOrMethod(val):
        try:
          src = inspect.getsource(val)
        except:
          #sys.stderr.write("NO SOURCE FOR NAME=%s TYPE=%s VAL=%s\n" % (name, str(type(val)), str(val)))
          pass
        else:
          if src:
            #sys.stderr.write("FOUND SOURCE FOR NAME=%s TYPE=%s VAL=%s\n" % (name, str(type(val)), str(val)))
            file.write(src + '\n')
            num_written = num_written + 1
            last_val = val
            continue
          #else:
            #sys.stderr.write("EMPTY SOURCE FOR NAME=%s TYPE=%s VAL=%s\n" % (name, str(type(val)), str(val)))            
        
      # Skip functions, methods, or constants modified in overrides
      elif HasValue(overrides, name):
        continue

      # Value is a data-descriptor
      # Contributed by Nigel Rowe, Aug 10, 2007
      elif type(val) in kPropertyTypes:
        indent_to_paren = indent + ' ' * len(name) + ' ' * 12
        file.write(indent + '%s = property(None, None, None,\n' % (name,))
        WriteDocString(val, file, indent_to_paren)
        file.write(indent_to_paren + ')\n\n')
      # Value is a function or method
      elif callable(val):
        
        try:
          seen_vals[val] = 1
        except TypeError:
          sys.stderr.write("Failed to register %s (may cause duplicates)\n" % str(val))
        
        if last_val is not kNoValue and not callable(last_val):
          file.write('\n')
          
        import_line = None
        # Trick to get init docs from class level doc where it usually is
        if name == '__init__':
          doc1 = getattr(val, '__doc__', '')
          if doc1 is None:
            doc1 = ''
          doc2 = getattr(obj, '__doc__', '')
          if doc2 is None:
            doc2 = ''
          args, retval = _GetCallableSignature(doc2 + '\n' + doc1)
        elif kIronPython:
          args, import_line, retval = GetCallableSignatureIPy(val, obj, name)
        else:
          args, retval = GetCallableSignature(val)
          
        # Try to fall back on inspect, tho this only works if the module
        # is not an extension module or contains some methods defined in Python
        if args == '' and inspect is not None:
          try:
            fval = getattr(val, 'im_func', val)
            args = inspect.formatargspec(inspect.getargspec(fval)[0])
            args = args[1:-1]
          except:
            args = ''
        if type(obj) == PyType_Type or hasattr(val, 'im_func'):
          if len(args) > 0 and string_find(args, 'self') != 0:
            args = 'self, ' + args
          elif string_find(args, 'self') < 0:
            args = 'self'

        # Write the definition
        file.write(indent + 'def %s(%s):\n' % (name, args))
        WriteDocString(val, file, indent + '  ')
        if import_line is not None:
          file.write(indent + '  %s\n' % import_line)
        file.write(indent + '  %s\n\n' % retval)
        num_written = num_written + 1
      
      # Value is a constant
      elif type(val) in kStringTypes:
        use_triple = (string_find(val, '\n') > 0 and string_find(val, '"""') == -1)
        val = val.replace('\r\n', '\n')
        if use_triple:
          for c in val:
            if c not in printable_chars:
              use_triple = 0
              break
        if use_triple:
          val = '"""%s"""' % str(val)
        else:
          val = repr(val)
        file.write(indent + '%s = %s\n' % (name, val))
        num_written = num_written + 1
      elif type(val) in kLiteralTypes:
        
        file.write(indent + '%s = %s\n' % (name, str(val)))
        num_written = num_written + 1
      elif type(val) in kStructureTypes:
        
        if type(val) == kListType:
          s = '[]'
        elif type(val) == kTupleType:
          s = '()'
        elif type(val) == kDictType:
          s = '{}'
        file.write(indent + '%s = %s\n' % (name, s))
        num_written = num_written + 1
      elif type(val) in kFileTypes:
        file.write(indent + '%s = file(__file__)\n' % name)
        num_written = num_written + 1
      
      else:
        file.write(indent + '%s = None\n' % name)
        num_written = num_written + 1
        
      last_val = val

  # Add in appropriate overrides
  additions = {}
  for oname in ValueItems(overrides):
    if oname in kOmitTopLevel:
      continue
    oval = GetValue(overrides, oname, None)
    # Class overrides already processed as addition to existing class
    # are not shown again
    if type(oval) in (kListType, kDictType) or not has_key(seen_vals, oval):
      additions[oname] = oval
      last_val = oval
  if len(additions) > 0:
    try:
      seen_vals[overrides] = 1
    except TypeError:
      sys.stderr.write("Failed to register %s (may cause duplicates)\n" % str(overrides))
    file.write(indent + '# BEGIN MANUAL OVERRIDES FROM %s\n' % overrides_file)
    GenForObject(scope, GetValue(overrides, name, {}), overrides_file, additions, file, seen_vals, indent, use_inspect=1)
    file.write(indent + '# END MANUAL OVERRIDES\n')
  
  if last_val is not kNoValue and not callable(last_val):
    file.write('\n')
    
  return num_written

def GenPClassForType(scope, overrides, overrides_file, name, obj, file, 
                     seen_vals, indent = '', use_inspect=0):

  bases = ""
  if inspect is not None and hasattr(inspect, 'getmro'):
    try:
      baselist = inspect.getmro(obj)
    except:
      baselist = [obj]
    if baselist[0] is obj and len(baselist) > 1:
      bases = "(%s)" % baselist[1].__name__
      
  file.write(indent + 'class %s%s:\n' % (name, bases))
  WriteDocString(obj, file, indent + kOneLevelIndent)
  file.write('\n')
  num_written = GenForObject(scope, overrides, overrides_file, obj, file, seen_vals, indent + kOneLevelIndent, use_inspect)
  if num_written == 0:
    file.write(indent + '  ' + 'pass\n\n')
  

def ProcessModule(mod_name, magic_code=None, metadata={}, overrides={}, file=None):

  if string_find(mod_name, '-') >= 0:
    return

  if file is None:
    file = sys.stdout

  seen_vals = {}
  if type(overrides) == types.ModuleType:
    overrides_file = overrides.__file__
    overrides_file = string_join(string_split(overrides_file, os.sep)[-3:], os.sep)
    if overrides_file[-1] in ('o', 'c'):
      overrides_file = overrides_file[:-1]
  else:
    overrides_file = None

  namespace = {}
  if magic_code is not None:
    exec(magic_code, namespace)
    if not has_key(namespace, mod_name):
      exec('import %s' % mod_name, namespace)
  else:
    # Work-around for bug in 2.1's warning module
    if version == (2, 1) and mod_name == 'regex':
      namespace['__name__'] = mod_name
    try:
      exec('import %s' % mod_name, namespace)
    except ImportError:
      # This case sometimes succeeds when above fails but adding '.' to
      # path blindly seems like a bad idea so do it only as a fall-back
      sys.path.append('.')
      exec('import %s' % mod_name, namespace)
  
  if kIronPython:
    sys.stderr.write("Now imported %s\n" % repr(namespace.keys()))
  file.write('# AUTO-GENERATED FILE -- DO NOT EDIT\n')
  if overrides_file is not None:
    file.write('# OVERRIDES FILE: %s\n\n' % overrides_file)
  else:
    file.write('\n')
  
  components = mod_name.split('.')
  mod_name = components[0]
  components = components[1:]
  mod = namespace.get(mod_name)
  while components:
    mod = getattr(mod, components[0])
    del components[0]
  
  WriteDocString(mod, file, '')
  file.write('\n')
  GenForObject(['__toplevel__'], overrides, overrides_file, mod, file, seen_vals)

  fn = getattr(mod, '__file__', None)
  if fn is not None:
    try:
      fn = os.path.abspath(fn)
    except:
      metadata['file'] = repr(fn)
    else:
      metadata['file'] = fn
      try:
        if os.path.isfile(fn):
          s = os.stat(fn)
          metadata['modtime'] = s[stat.ST_MTIME]
      except:
        pass

def DecodeArg(a):
  """ If a starts with +, treat any subsequent + as indicator that the
  4 characters following are the hex representation of a code point which
  will replace the + and the following 4 chars.  Any / will be translated
  into os.sep.  On win32, always convert to unicode if possible. """
  
  if os.sep != '/':
    a = string_replace(a, '/', os.sep)

  if a == '' or a[0] != '+':
    if sys.platform == 'win32':
      try:
        return unicode(a)
      except:
        pass
    return a

  try:
    a = unicode(a)
  except:
    pass
  part_list = string_split(a[1:], '+')
  fragments = []
  for i, part in enumerate(part_list):
    if i == 0:
      frag = part
    else:
      try:
        frag = unichr(string.atoi(part[:4], 16))
      except:
        frag = chr(string.atoi(part[:4], 16))
      frag = frag + part[4:]
    
    if frag != '':
      fragments.append(frag)
  try:
    decoded = string_join(fragments, unicode(''))
  except:
    decoded = string_join(fragments, '')
  return decoded

def _PrintUsage():
  sys.stdout.write("Usage: %s [options] module-name output-file [python-path] [ld_library_path]\n")
  sys.stdout.write("output-file may be '-' to write to stdout.  The paths, if given, should be\n")
  sys.stdout.write("string separated by os.pathsep (':' or ';' depending on OS).  The output-file\n")
  sys.stdout.write("is treated as an encoded name if the name begins with a + and any + after\n")
  sys.stdout.write("the first is to be followed by a 4 digit hexadecimal number for the code\n")
  sys.stdout.write("point at that position in the string\n")
  sys.stdout.write("\n")
  sys.stdout.write("Valid options:\n")
  sys.stdout.write("  --meta-data    -- Write meta data file also -- the file name is output-file\n")
  sys.stdout.write("                    plus '.meta'.  This arg is ignored if output-file is '-'\n")
  sys.stdout.write("  --magic-code [code] -- Execute given code before attempting to import the \n")
  sys.stdout.write("                    extension module if importing it alone fails\n")
  sys.stdout.write("\n")
  sys.stdout.write("The meta data file, if output, contains a cPickle.dump()'ed Python dictionary\n")
  sys.stdout.write("with the following fields:\n")
  sys.stdout.write("  file           -- The module file name\n")
  sys.stdout.write("  modtime        -- The value of os.stat(file)[stat.M_TIME]\n")
  sys.stdout.write("\n")
  
##############################################################
# IronPython specifics

class CIronPythonNameSpaceFinder:
  
  def __init__(self):
    
    self.fNamespaces = {}
    self.fInspected = set()

    import System
    self.fNamespaceType = type(System)

  def Visit(self, obj, mod_name):
    
    if obj in self.fInspected:
      return
    self.fInspected.add(obj)
    self.fNamespaces[mod_name] = obj
  
    for name in SafeDir(obj):
      try:
        val = getattr(obj, name)
      except:
        continue
      
      if isinstance(val, self.fNamespaceType):
        dotted_name = '%s.%s' % (mod_name, name)
        self.fNamespaces[dotted_name] = val
        self.Visit(val, dotted_name)
        
def GenerateForIronPythonNameSpaces(namespace_list, output_dirname, clr_refs):
  
  import clr
  for name in clr_refs:
    clr.AddReference(name)
    
  ns_finder = CIronPythonNameSpaceFinder()
  for ns_name in namespace_list:
    mod = __import__(ns_name)
    ns_finder.Visit(mod, ns_name)
  sys.stderr.write('%s\n' % repr(ns_finder.fNamespaces.keys()))
  sys.stderr.write('%s\n' % repr(len(ns_finder.fNamespaces)))

  expanded_list = sorted(ns_finder.fNamespaces.keys())

  for ns_name in expanded_list:
    kPIPackagesAreBroken = True
    if not kPIPackagesAreBroken: # if Wing worked like it should
      dirname = os.path.join(output_dirname, *ns_name.split('.'))
      if not os.path.exists(dirname):
        os.makedirs(dirname)
      filename = os.path.join(dirname, '__init__.pi')
    else:
      filename = os.path.join(output_dirname, ns_name + '.pi')
      
    f = open(filename, 'w')
    ProcessModule(ns_name, file=f)
    f.close()
    
########################################################################
if __name__ == '__main__':

  if '--ironpython' in sys.argv:
    # CHANGE: Hardwire assembly names to add references and pre-do imports to
    #         make nested namespaces available as attributes on top level namespace
    ref_names = ['System', 'System.Data', 'System.Windows.Forms', 'System.Drawing', 'System.Xml'] 
    output_dir = os.path.abspath('.')
    GenerateForIronPythonNameSpaces(['System', 'Microsoft', 'clr'], output_dir, ref_names)
    sys.exit(0)

  if len(sys.argv) < 3:
    _PrintUsage()
    sys.exit(1)
 
  write_metadata = 0
  if '--meta-data' in sys.argv:
    sys.argv.remove('--meta-data')
    write_metadata = 1
  magic_code = None
  if '--magic-code' in sys.argv:
    mpos = sys.argv.index('--magic-code')
    if len(sys.argv) < mpos + 2:
      _PrintUsage()
      sys.exit(1)
    magic_code = sys.argv[sys.argv.index('--magic-code')+1]
    sys.argv.remove('--magic-code')
    sys.argv.remove(magic_code)
    
  modname = sys.argv[1]
  outfile = sys.argv[2]
  
   
  if len(sys.argv) >= 4:
    for p in string_split(sys.argv[3], os.pathsep):
      sys.path.append(os.path.abspath(p))
  
  if len(sys.argv) == 5:
    os.environ['LD_LIBRARY_PATH'] = sys.argv[4]
    cmd = '"%s" %s "%s" "%s" "%s"' % (sys.executable, sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
    sys.exit(os.system(cmd))
        
  if outfile != '-':
    outfile = DecodeArg(outfile)
    f = open(outfile, 'w')
    sys.stdout = f
  else:
    f = sys.stdout
    
  metadata = {}
  
  ProcessModule(modname, magic_code, metadata, file=f)
  
  if outfile != '-':
    sys.stdout = sys.__stdout__
    f.close()
    
    # Avoid leaving around lots of empty trash files
    if os.stat(outfile)[stat.ST_SIZE] == 0:
      try:
        sys.stdout.write("generate_pi.py:  Removing empty %s\n" % outfile)
        os.unlink(outfile)
      except:
        pass
    
  if write_metadata and outfile != '-':
    f = open(outfile + '.meta', 'wb')
    if sys.version_info < (3, 0):
      import cPickle 
      cPickle.dump(metadata, f)
    else:
      import pickle
      pickle.dump(metadata, f, 2)
    f.close()
    
