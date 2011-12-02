// avoid compiler warnings... urgh
#undef _POSIX_C_SOURCE
#undef _XOPEN_SOURCE

#include <language/duchain/duchainlock.h>

#include "python-src/Include/pyport.h"
#include "python-src/pyconfig.h"
#include "python-src/Include/node.h"

#include "python-src/Include/Python.h"

#include "python-src/Include/Python-ast.h"
#include "python-src/Include/ast.h"

#include "python-src/Include/graminit.h"
#include "python-src/Include/grammar.h"
#include "python-src/Include/parsetok.h"

#include "python-src/Include/unicodeobject.h"

#include "python-src/Include/object.h"

// remove evil macros from headers which pollute the namespace (grr!)
#undef test
#undef decorators
#undef Attribute