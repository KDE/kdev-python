#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import subprocess

import StringIO

from PyQt4.QtCore import QProcess

import re

def colorize(s, colnum):
    return "\033[9" + str(colnum) + "m" + str(s) + "\033[0m"

def green(s):
    return colorize(s, 2)

def red(s):
    return colorize(s, 1)

def yellow(s):
    return colorize(s, 3)

def blue(s):
    return colorize(s, 4)

def pink(s):
    return colorize(s, 5)

def cyan(s):
    return colorize(s, 6)

def white(s):
    return colorize(s, 7)

def indent(s, level = 1):
    return '\n'.join(["    "*level + line for line in s.splitlines()])
        
class FailedTest():
    def __init__(self, name, reason):
        self.filename = '<none>'
        self.lineno = '<none>'
        self.name = name
        self.reason = reason
        self.failExpected = False
        
    def __str__(self):
        return "%s:%s %s" % (self.filename, self.lineno, self.name)

class TestRunner():
    def __init__(self, testfile):
        self.testfile = testfile
        self.data = ""
        self.passed_tests = []
        self.failed_tests = []
    
    def writeStdout(self):
        data = self.process.readAllStandardOutput()
        if "debug" in sys.argv:
            sys.stdout.write(data)
        else:
            for line in data.split('\n'):
                if line[:4] == "PASS" or line[:5] == "FAIL!" or line[:5] == "XFAIL":
                    sys.stdout.write(".")
                    sys.stdout.flush()
        self.data += data
    
    def writeStderr(self):
        data = self.process.readAllStandardError()
        if "debug" in sys.argv:
            sys.stdout.write(data)
        self.data += data
    
    def doTestrun(self):
        data = self.fetchOutputForJob()
        last_failed = False
        for line in data.splitlines():
            success = re.match(r"PASS\s*:\s*(.*)", line)
            if success:
                function = success.groups()[0]
                self.passed_tests.append(function)
                last_failed = False
            
            if last_failed:
                getLocation = re.match(r"\s*Loc:\s*\[(.*)\((\d*)\)]", line)
                if getLocation:
                    filename = ".../" + '/'.join(getLocation.groups()[0].split('/')[-2:])
                    lineno = getLocation.groups()[1]
                    self.failed_tests[-1].filename = filename
                    self.failed_tests[-1].lineno = lineno
                    last_failed = False
            
            fail = re.match(r"FAIL!\s*:\s*(.*)\((.*)\)\s+(.*)", line)
            if fail:
                function = fail.groups()[0]
                args = fail.groups()[1]
                function = function + "(" + args + ")"
                reason = fail.groups()[2]
                self.failed_tests.append(FailedTest(function, reason))
                last_failed = True
            xfail = re.match(r"XFAIL\s*:\s*(.*)\((.*)\)\s+(.*)", line)
            if xfail:
                function = xfail.groups()[0]
                args = xfail.groups()[1]
                function = function + "(" + args + ")"
                reason = xfail.groups()[2]
                self.failed_tests.append(FailedTest(function, reason))
                self.failed_tests[-1].failExpected = True
                last_failed = True
            
            fatal_fail = re.match(r"(QFATAL|ASSERT)\s*", line)
            if fatal_fail:
                print self.data
                print red("Fatal error occured, aborting")
                return
        
        passed, failed = len(self.passed_tests), len(self.failed_tests)
        try:
            percent = round((float(passed) / (failed+passed)) * 100)
        except ZeroDivisionError:
            percent = "?"
        percent = green(percent) if percent == 100 else yellow(percent) if percent > 80 else red(percent)
        total = white(passed+failed)
        passed, failed = green(passed), red(failed)
        print "\n Done. Summary: %s tests reported total, %s passed, %s failed (%s%% passed)." % (total, passed, failed, percent)
        print " Detailed information:\n"
        print white("  ==="), green("Passed tests:"), white("===")
        namespaceFunctionArgs = r"(.*)::(.*)\((.*)\)"
        
        if len(self.passed_tests):
            for test in self.passed_tests:
                test = re.match(namespaceFunctionArgs, test)
                test = test.groups()
                test = "[%s] " % test[0] + green(test[1]) + "(" + white(test[2]) + ")"
                print  indent(green("✔ ") + test)
        
        if len(self.failed_tests):
            print "\n" + white("  ==="), red("Failed tests:"), white("===")
            for test in self.failed_tests:
                namespace, function, args = re.match(namespaceFunctionArgs, test.name).groups()
                filename = test.filename.split('/')[-1]
                path = '/'.join(test.filename.split('/')[:-1]) + "/"
                print indent((yellow("✘ ") if test.failExpected else red("✘ ")) + white(filename) + ":" + blue(test.lineno) +
                      " "*(5-len(str(lineno))) + red(function) + "(" + yellow(args) + ")")
                if 'noreason' not in sys.argv:
                    print indent("Reason of failure:" + blue(" ❮") + white(test.reason) + blue("❯ ") 
                                 + ( "(Failure expected)" if test.failExpected else "" ), 2)
                #print "[in %s]" % namespace
    
    def fetchOutputForJob(self):
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.writeStdout)
        self.process.readyReadStandardError.connect(self.writeStderr)
        print " Please wait, running tests",
        sys.stdout.flush()
        self.process.start(self.testfile, ["-maxwarnings", "0"])
        self.process.waitForFinished(-1)
        return str(self.data)
    
if __name__ == '__main__':
    runner = TestRunner(sys.argv[1])
    runner.doTestrun()
