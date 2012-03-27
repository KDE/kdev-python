#ifndef PYTHONDEBUGEXPORT_H
#define PYTHONDEBUGEXPORT_H

/* needed for KDE_EXPORT macros */
#include <kdemacros.h>


#ifndef KDEVPYTHONDEBUG_EXPORT
# ifdef MAKE_KDEV4PYTHONDEBUG_LIB
#  define KDEVPYTHONDEBUG_EXPORT KDE_EXPORT
# else
#  define KDEVPYTHONDEBUG_EXPORT KDE_IMPORT
# endif
#endif

#endif

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
