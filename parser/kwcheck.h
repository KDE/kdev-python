/* KDevelop Python Support
 *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 */

#ifndef KWCHECK_H
#define KWCHECK_H

class QChar;

namespace Python
{

int kwcheck2( const QChar* s );
int kwcheck3( const QChar* s );
int kwcheck4( const QChar* s );
int kwcheck5( const QChar* s );
int kwcheck6( const QChar* s );
int kwcheck7( const QChar* s );
int kwcheck8( const QChar* s );
int checkForKeyword( const QChar* txt, int len );

}

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
