/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

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