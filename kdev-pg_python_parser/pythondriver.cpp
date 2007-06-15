/* Python Parser Test
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


#include "pythondriver.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include "python_parser.h"

#include <QtCore/QByteArray>
#include <QtCore/QStack>

using namespace python;

bool PythonDriver::parse_string(const QString& content)
{
    QByteArray qba = content.toLocal8Bit();
    std::cerr << "'" << qba.data() << "'\n";
    return PythonDriver::parse_string(qba.data());
}

bool PythonDriver::parse_string(char const *content)
{
    char* contents = const_cast<char*>(content) ;
    parser::token_stream_type token_stream;
    parser::memory_pool_type memory_pool;

    std::cerr << "Parsing string\n";

    // 0) setup
    parser python_parser;
    python_parser.set_token_stream(&token_stream);
    python_parser.set_memory_pool(&memory_pool);

    // 1) tokenize
    python_parser.tokenize(contents);

    // 2) parse
    project_ast *ast = 0;
    bool matched = python_parser.parse_project(&ast);
    if (matched)
    {
        std::cerr<<"Matched";
    }
    else
    {
        python_parser.yy_expected_symbol(ast_node::Kind_project, "project"); // ### remove me
    }

    return matched;
}

bool PythonDriver::parse_file(const QString& filename)
{
    QByteArray qba = filename.toLocal8Bit();
    return PythonDriver::parse_file(qba.data());
}

bool PythonDriver::parse_file(char const *filename)
{
    std::cerr << "Parsing FILE\n";
    char *contents;
    std::ifstream filestr(filename);

    if (filestr.is_open())
    {
      std::filebuf *pbuf;
      long size;

      // get pointer to associated buffer object
      pbuf=filestr.rdbuf();

      // get file size using buffer's members
      size=pbuf->pubseekoff(0,std::ios::end,std::ios::in);
      pbuf->pubseekpos(0,std::ios::in);

      // allocate memory to contain file data
      contents=new char[size+1];

      // get file data
      pbuf->sgetn(contents, size);

      filestr.close();
    }
    else
    {
      std::cerr << filename << ": file not found" << std::endl;
      return false;
    }

    parser::token_stream_type token_stream;
    parser::memory_pool_type memory_pool;

    // 0) setup
    parser python_parser;
    python_parser.set_token_stream(&token_stream);
    python_parser.set_memory_pool(&memory_pool);

    // 1) tokenize
    python_parser.tokenize(contents);

    // 2) parse
    project_ast *ast = 0;
    bool matched = python_parser.parse_project(&ast);
    if (matched)
    {
    }
    else
    {
        python_parser.yy_expected_symbol(ast_node::Kind_project, "project"); // ### remove me
    }

    //This needs to be done, unfortunately it currently crashes the parser when it encounters an eof without newline
    //delete contents;

    return matched;
}

// kate: space-indent on; indent-width 4; tab-width: 4; replace-tabs on; auto-insert-doxygen on
