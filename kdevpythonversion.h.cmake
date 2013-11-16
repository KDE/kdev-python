/*****************************************************************************
 * This file is part of the KDE project
 * Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 *******************************************************************************/
#ifndef KDEVPYTHON_VERSION_H
#define KDEVPYTHON_VERSION_H

#include <kdeversion.h>

#define KDEVPYTHON_MAJOR_VERSION @KDEVPYTHON_VERSION_MAJOR@
#define KDEVPYTHON_MINOR_VERSION @KDEVPYTHON_VERSION_MINOR@
#define KDEVPYTHON_PATCH_VERSION @KDEVPYTHON_VERSION_PATCH@

#define KDEVPYTHON_VERSION_STR "@KDEVPYTHON_VERSION_MAJOR@.@KDEVPYTHON_VERSION_MINOR@.@KDEVPYTHON_VERSION_PATCH@"

#define KDEVPYTHON_VERSION KDE_MAKE_VERSION(@KDEVPYTHON_VERSION_MAJOR@, @KDEVPYTHON_VERSION_MINOR@, @KDEVPYTHON_VERSION_PATCH@)

#define PYTHON_EXECUTABLE "@PYTHON_EXECUTABLE@"

#endif
