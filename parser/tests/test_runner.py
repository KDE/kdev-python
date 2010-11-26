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
from optparse import OptionParser
import os
import re
import commands
import unittest
import filecmp

class Error(Exception): pass

class TestResults:
    __doc__="The Class is the Engine of the test Suite"
    _re_test = re.compile('\S*(.py$)')
    _re_fail = re.compile('.*fail.py')
    def __init__(self,parserexec,sourcedir):
        """Initiates the variables"""
	self.sourcedir = sourcedir
	self.parserexec = parserexec
        self.tests = []
        self.success = self.failure = self.no =0
        self.Errors = []
    def __file_check(self):
        """Checks for the test cases in directory and calls a check for each test"""
        for i in Dir_Content(self.sourcedir).files:
                        match = re.match(self._re_test, i)
                        if match:
                                self.tests.append(i)
        for i in self.tests:
                        if i <> 'test_runner.py':
                            self.no = self.no + 1
                            string = (self.parserexec+" "+self.sourcedir+"/"+i).strip()
                            (status,out) = commands.getstatusoutput(string)
                            self.__check(status,i)
    def __check(self,parse,i):
        """checks if the new token stream matches the ideal token stream"""
        if(parse == 0):
            y = "OK"
            self.success = self.success + 1
        elif(re.match(self._re_fail,i)):
	    self.success = self.success + 1
	    y = "FAILED - Fail expected"
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
    parser = OptionParser()
    parser.add_option("-p","--parser", dest="parserexec")
    parser.add_option("-s","--source", dest="sourcedir")
    (options,args) = parser.parse_args()
    TestResults(options.parserexec,options.sourcedir).main()
