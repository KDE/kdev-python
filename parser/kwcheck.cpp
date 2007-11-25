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

#include "kwcheck.h"
#include "pythonparser.h"

namespace PythonParser
{

int checkForKeyword( const QChar* txt, int len )
{
    switch( len )
    {
        case 2:
            return kwcheck2(txt);
        case 3:
            return kwcheck3(txt);
        case 4:
            return kwcheck4(txt);
        case 5:
            return kwcheck5(txt);
        case 6:
            return kwcheck6(txt);
        case 7:
            return kwcheck7(txt);
        case 8:
            return kwcheck8(txt);
        default:
            return Parser::Token_IDENTIFIER;
    }
}

int kwcheck2( const QChar* s )
{
    if( s[0] == 'a' )
    {
        if( s[1] == 's' )
        {
            return Parser::Token_AS;
        }
    }else if( s[0] == 'i' )
    {
        if( s[1] == 's' )
        {
            return Parser::Token_IS;
        }else if( s[1] == 'n' )
        {
            return Parser::Token_IN;
        }else if( s[1] == 'f' )
        {
            return Parser::Token_IF;
        }
    }else if( s[0] == 'o' )
    {
        if( s[1] == 'r' )
            return Parser::Token_OR;
    }
    return Parser::Token_IDENTIFIER;
}

int kwcheck3( const QChar* s )
{
    if( s[0] == 'a' )
    {
        if( s[1]  == 'n' )
        {
            if( s[2]  == 'd' )
            {
                return Parser::Token_AND;
            }
        }
    } else if( s[0] == 'd' )
    {
        if( s[1] == 'e' )
        {
            if( s[2] == 'l' )
            {
                return Parser::Token_DEL;
            }else if( s[2] == 'f' )
            {
                return Parser::Token_DEF;
            }
        }
    } else if( s[0] == 'f' )
    {
        if( s[1] == 'o' )
        {
            if( s[2] == 'r' )
            {
                return Parser::Token_FOR;
            }
        }
    }else if( s[0] == 'n' )
    {
        if( s[1] == 'o' )
        {
            if( s[2] == 't' )
            {
                return Parser::Token_NOT;
            }
        }
    }else if( s[0] == 't' )
    {
        if( s[1] == 'r' )
        {
            if( s[2] == 'y' )
            {
                return Parser::Token_TRY;
            }
        }
    }
    return Parser::Token_IDENTIFIER;
}


int kwcheck4( const QChar* s )
{
    if( s[0] == 'e' )
    {
        if( s[1] == 'l' )
        {
            if( s[2] == 's' )
            {
                if( s[3] == 'e' )
                {
                    return Parser::Token_ELSE;
                }
            }else if( s[2] == 'i' )
            {
                if( s[3] == 'f' )
                {
                    return Parser::Token_ELIF;
                }
            }
        }else if( s[1] == 'x' )
        {
            if( s[2] == 'e' )
            {
                if( s[3] == 'c' )
                {
                    return Parser::Token_EXEC;
                }
            }
        }
    }else if( s[0] == 'f' )
    {
        if( s[1] == 'r' )
        {
            if( s[2] == 'o' )
            {
                if( s[3] == 'm' )
                {
                    return Parser::Token_FROM;
                }
            }
        }
    }else if( s[0] == 'p' )
    {
        if( s[1] == 'a' )
        {
            if( s[2] == 's' )
            {
                if( s[3] == 's' )
                {
                    return Parser::Token_PASS;
                }
            }
        }
    }
    return Parser::Token_IDENTIFIER;
}

int kwcheck5( const QChar* s )
{
    if( s[0] == 'b' )
    {
        if( s[1] == 'r' )
        {
            if( s[2] == 'e' )
            {
                if( s[3] == 'a' )
                {
                    if( s[4] == 'k' )
                    {
                        return Parser::Token_BREAK;
                    }
                }
            }
        }
    }else if( s[0] == 'c' )
    {
        if( s[1] == 'l' )
        {
            if( s[2] == 'a' )
            {
                if( s[3] == 's' )
                {
                    if( s[4] == 's' )
                    {
                        return Parser::Token_CLASS;
                    }
                }
            }
        }
    }else if( s[0] == 'p' )
    {
        if( s[1] == 'r' )
        {
            if( s[2] == 'i' )
            {
                if( s[3] == 'n' )
                {
                    if( s[4] == 't' )
                    {
                        return Parser::Token_PRINT;
                    }
                }
            }
        }
    }else if( s[0] == 'r' )
    {
        if( s[1] == 'a' )
        {
            if( s[2] == 'i' )
            {
                if( s[3] == 's' )
                {
                    if( s[4] == 'e' )
                    {
                        return Parser::Token_RAISE;
                    }
                }
            }
        }
    }else if( s[0] == 'w' )
    {
        if( s[1] == 'h' )
        {
            if( s[2] == 'i' )
            {
                if( s[3] == 'l' )
                {
                    if( s[4] == 'e' )
                    {
                        return Parser::Token_WHILE;
                    }
                }
            }
        }
    }else if( s[0] == 'y' )
    {
        if( s[1] == 'i' )
        {
            if( s[2] == 'e' )
            {
                if( s[3] == 'l' )
                {
                    if( s[4] == 'd' )
                    {
                        return Parser::Token_YIELD;
                    }
                }
            }
        }
    }
    return Parser::Token_IDENTIFIER;
}

int kwcheck6( const QChar* s )
{
    if( s[0] == 'a' )
    {
        if( s[1] == 's' )
        {
            if( s[2] == 's' )
            {
                if( s[3] == 'e' )
                {
                    if( s[4] == 'r' )
                    {
                        if( s[5] == 't' )
                        {
                            return Parser::Token_ASSERT;
                        }
                    }
                }
            }
        }
    }else if( s[0] == 'e' )
    {
        if( s[1] == 'x' )
        {
            if( s[2] == 'c' )
            {
                if( s[3] == 'e' )
                {
                    if( s[4] == 'p' )
                    {
                        if( s[5] == 't' )
                        {
                            return Parser::Token_EXCEPT;
                        }
                    }
                }
            }
        }
    }else if( s[0] == 'g' )
    {
        if( s[1] == 'l' )
        {
            if( s[2] == 'o' )
            {
                if( s[3] == 'b' )
                {
                    if( s[4] == 'a' )
                    {
                        if( s[5] == 'l' )
                        {
                            return Parser::Token_GLOBAL;
                        }
                    }
                }
            }
        }
    }else if( s[0] == 'i' )
    {
        if( s[1] == 'm' )
        {
            if( s[2] == 'p' )
            {
                if( s[3] == 'o' )
                {
                    if( s[4] == 'r' )
                    {
                        if( s[5] == 't' )
                        {
                            return Parser::Token_IMPORT;
                        }
                    }
                }
            }
        }
    }else if( s[0] == 'l' )
    {
        if( s[1] == 'a' )
        {
            if( s[2] == 'm' )
            {
                if( s[3] == 'b' )
                {
                    if( s[4] == 'd' )
                    {
                        if( s[5] == 'a' )
                        {
                            return Parser::Token_LAMBDA;
                        }
                    }
                }
            }
        }
    }else if( s[0] == 'r' )
    {
        if( s[1] == 'e' )
        {
            if( s[2] == 't' )
            {
                if( s[3] == 'u' )
                {
                    if( s[4] == 'r' )
                    {
                        if( s[5] == 'n' )
                        {
                            return Parser::Token_RETURN;
                        }
                    }
                }
            }
        }
    }
    return Parser::Token_IDENTIFIER;
}

int kwcheck7( const QChar* s )
{
    if( s[0] == 'f' )
    {
        if( s[1] == 'i' )
        {
            if( s[2] == 'n' )
            {
                if( s[3] == 'a' )
                {
                    if( s[4] == 'l' )
                    {
                        if( s[5] == 'l' )
                        {
                            if( s[6] == 'y' )
                            {
                                return Parser::Token_FINALLY;
                            }
                        }
                    }
                }
            }
        }
    }
    return Parser::Token_IDENTIFIER;
}

int kwcheck8( const QChar* s )
{
    if( s[0] == 'c' )
    {
        if( s[1] == 'o' )
        {
            if( s[2] == 'n' )
            {
                if( s[3] == 't' )
                {
                    if( s[4] == 'i' )
                    {
                        if( s[5] == 'n' )
                        {
                            if( s[6] == 'u' )
                            {
                                if( s[7] == 'e' )
                                {
                                    return Parser::Token_CONTINUE;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return Parser::Token_IDENTIFIER;
}

}

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
