/* Python Lexer Test
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

#ifndef PARSETEST_H
#define PARSETEST_H

#include <QtCore/QObject>
#include <QtTest/QtTest>

class LexerTest : public QObject
{
        Q_OBJECT
    public:
        LexerTest( QObject* parent = 0 );
        ~LexerTest();
    private slots:
        void init();
        void cleanup();
        void lexNumberLiteral();
        void lexNumberLiteral_data();
        void lexKeywordAndIdentifier();
        void lexKeywordAndIdentifier_data();
        void lexSeparatorsAndOperators();
        void lexSeparatorsAndOperators_data();
        void lexIndentation();
        void lexIndentation_data();
        void lexStringLiteral();
        void lexStringLiteral_data();
    private:
};

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
