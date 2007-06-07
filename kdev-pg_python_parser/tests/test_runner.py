#-------------------------------------------------------------------------------
#-- Copyright (c) 2007 Piyush Verma  <piyush.verma@gmail.com>
#--
#-- Permission is hereby granted, free of charge, to any person obtaining
#-- a copy of this software and associated documentation files (the
#-- "Software"), to deal in the Software without restriction, including
#-- without limitation the rights to use, copy, modify, merge, publish,
#-- distribute, sublicense, and/or sell copies of the Software, and to
#-- permit persons to whom the Software is furnished to do so, subject to
#-- the following conditions:
#--
#-- The above copyright notice and this permission notice shall be
#-- included in all copies or substantial portions of the Software.
#--
#-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#-- EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#-- MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#-- NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#-- LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#-- OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#-- WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
