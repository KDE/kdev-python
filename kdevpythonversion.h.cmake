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

#define PYTHON_VERSION_MAJOR_STR "@PYTHON_VERSION_MAJOR@"
#define PYTHON_VERSION QT_VERSION_CHECK(@PYTHON_VERSION_MAJOR@, @PYTHON_VERSION_MINOR@, @PYTHON_VERSION_PATCH@)
#define PYTHON_VERSION_STR "@PYTHON_VERSION_MAJOR@.@PYTHON_VERSION_MINOR@"
#define PYTHON_EXECUTABLE "@PYTHON_EXECUTABLE@"

#endif
