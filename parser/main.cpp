/*****************************************************************************
 * Copyright (c) 2006 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush Verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/

#include "pythondriver.h"
#include "decoder.h"

#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace python;

static void usage(char const* arg0);

int main(int argc, char *argv[])
{
  if (argc == 1)
    {
      usage(argv[0]);
      exit(EXIT_FAILURE);
    }
  while (char const *arg = *++argv)
    {
      /*if (!strncmp(arg, "--option=", 9))
        {
          char const* option = arg + 9;

          std::cerr << "--option=" << option
                    << " has been given!" << std::endl;
        }
      else */
      if (!strncmp(arg, "--", 2))
        {
          std::cerr << "Unknown option: " << arg << std::endl;
          usage(argv[0]);
          exit(EXIT_FAILURE);
        }
      else if(!PythonDriver::parse_file(arg))
        {
          exit(EXIT_FAILURE);
        }
    }
}


static void usage(char const* argv0)
{
  std::cerr << "usage: " << argv0 /*<< " [options]"*/ << " file1.py [file2.py...]"
    << std::endl; /*<< std::endl
    << "Options:" << std::endl
    << "  --option=BLA: Do BLAH while parsing." << std::endl
    << "                BLAH is one of FOO, BAR or KUNG, default is FOO."
    << std::endl;
    */
}

// kate: space-indent on; indent-width 4; tab-width: 4; replace-tabs on; auto-insert-doxygen on
