/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

// avoid compiler warnings... urgh
#undef _POSIX_C_SOURCE
#undef _XOPEN_SOURCE

#define Py_BUILD_CORE

#include <stdbool.h>

// remove interfering qt macro
#undef slots

#include <sys/types.h>
#include <unistd.h>

#include "pyport.h"
#ifndef _WIN32
#include "pyconfig.h"
#endif

#include "Python.h"

#include <unicodeobject.h>

#include <object.h>

// remove evil macros from headers which pollute the namespace (grr!)
#undef test
#undef decorators
#undef Attribute
