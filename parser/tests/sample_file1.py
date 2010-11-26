#! /usr/bin/python
#-------------------------------------------------------------------------------
#-- Copyright (c) 2007 Piyush Verma  <piyush.verma@gmail.com>
#--
#-- This program is free software; you can redistribute it and/or
#-- modify it under the terms of the GNU General Public License
#-- as published by the Free Software Foundation; either version 2
#-- of the License, or (at your option) any later version.
#--
#-- This program is distributed in the hope that it will be useful,
#-- but WITHOUT ANY WARRANTY; without even the implied warranty of
#-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#-- GNU General Public License for more details.
#--
#-- You should have received a copy of the GNU General Public License
#-- along with this program; if not, write to the Free Software
#-- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
#-- 02110-1301, USA.
#-------------------------------------------------------------------------------

"""Test Runner for Parser"""
import os
import re
import commands
import unittest
import filecmp

class Error(Exception): pass

class TestResults:
    __doc__="The Class is the Engine of the test Suite"
    _re_test = re.compile('\S*(.py$)')
    _re_pass = re.compile('[\S\s]*\nMatched')
    def __init__(self):
        """Initiates the variables"""
        self.dir = "./"
        self.x = Dir_Content(self.dir).files
        self.tests = []
        self.success = self.failure = self.no =0
        self.Errors = []
    def __file_check(self):
        """Checks for the test cases in directory and calls a check for each test"""
        for i in self.x:
                        match = re.match(self._re_test, i)
                        if match:
                                self.tests.append(i)
        for i in self.tests:
                        if i <> 'test_runner.py':
                            self.no = self.no + 1
                            string = ("../build/python-parser "+i).strip()
                            x = commands.getoutput(string)
                            self.__check(x,i)
    def __check(self,x,i):
        """checks if the new token stream matches the ideal token stream"""
        log_file = self.dir+i+".result" 
        try:
            file = open(log_file, 'r')
            try:
                data = file.read()
                self.__parser_token_check(data,x,i)
            finally:
                file.close()
        except IOError:
            y = open(log_file, 'w')
            y.write( x )
            y.close()
            self.failure = self.failure + 1
            error = "File: "+log_file+" IOError: ReGenerating the Token Stram File"
            self.Errors.append(error)
    def __parser_token_check(self,data,x,i):
        parse = re.match(self._re_pass,x)
        if(parse):
            if( data == x ):
                y = "OK"
                self.success = self.success + 1
            else:
                self.failure = self.failure + 1
                y = "FAILED"
        else:
            self.failure = self.failure + 1
            y = "FAILED"
        print "Test token Stream match for "+i+"......."+y
    def __del__(self):
        """The Destructor defines actions at the end of the class process"""
        print "-------------------------------------------"
        print "Ran "+str(self.no)+ " tests"
        if ( self.failure ):
            print str(self.failure)+" Test(s) Failed"
            for i in self.Errors:
                print i
        if( self.success):
            print str(self.success)+" Test(s) Passed"
    def main(self):
        self.__file_check()

class Dir_Content:
    __doc__="This Class returns the list of files in a directory"
    def __init__(self,directory):
        self.files = []
        self.stack = [directory]
        self.index(directory)
    def index(self,directory):
        while(self.stack):
            directory = self.stack.pop()
            for file in os.listdir(directory):
                fullname = os.path.join(directory,file)
                if os.path.isdir(fullname):
                    self.stack.append(fullname)
                else:
                    self.files.append(file)
        return self.files

if __name__ == "__main__":
    TestResults().main()
