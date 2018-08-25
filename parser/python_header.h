/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

// avoid compiler warnings... urgh
#undef _POSIX_C_SOURCE
#undef _XOPEN_SOURCE

// remove interfering qt macro
#undef slots

#include <language/duchain/duchainlock.h>

#include "pyport.h"
#ifndef _WIN32
#include "pyconfig.h"
#endif
#include "node.h"

#include "Python.h"

#include "Python-ast.h"
#include "ast.h"

#include "graminit.h"
#include "grammar.h"
#include "parsetok.h"

#include "unicodeobject.h"

#include "object.h"

// remove evil macros from headers which pollute the namespace (grr!)
#undef test
#undef decorators
#undef Attribute
