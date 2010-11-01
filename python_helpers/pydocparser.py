#!/usr/bin/env python2.6

import re
import os
import sys
import subprocess

modules = ['random']
state = None

PackageScanState, ClassScanState = 'pkg', 'cls'
ClassScanState_Outline, ClassScanState_MethodResolution, ClassScanState_MethodDefinition, ClassScanState_DataDescriptors, ClassScanState_Attributes, ClassScanState_InheritedMethods = 'c_otl', 'c_res', 'c_mdf', 'c_dat', 'c_att', 'c_inh'
ClassScanState_InheritedAttributes, ClassScanState_MethodDocumentation = 'c_iat', 'c_mdc'

ClassMatchRegex = re.compile(r'    (class .*?\(.*?\).*?)')
InClassMatchRegex = re.compile(r'     \|  ')
ResolvedMethodMatchRegex = re.compile(r'     \|  ([A-Za-z_]*?\(.*?\))')
UnresolvedMethodMatchRegex = re.compile(r'     \|  (.*? = \<built\-in function.*?\>)')
CouldBeMethodDocLineRegex = re.compile(r'     \|      (.*)')

class method():
    documentation = ''
    name = ''
    parameters = []
    
    def __repr__(self):
        return '<'+self.name+'>'

for module in modules:
    doctext = subprocess.Popen(['/usr/bin/pydoc', module], stdout = subprocess.PIPE).stdout.read()
    doctext_lines = doctext.split('\n')
    methods = []
    currentMethod = None
    state = None
    classState = None
    
    for line in doctext_lines:
        print state, classState, line[:70]
        if state == None:
            if re.match(ClassMatchRegex, line): 
                state = ClassScanState
                classState = ClassScanState_Outline
            if re.match(ResolvedMethodMatchRegex, line): pass
        elif state == ClassScanState:
            if not re.match(InClassMatchRegex, line): 
                state = None
                classState = None
                continue
            if line == '     |  Method resolution order:':
                classState = ClassScanState_MethodResolution
                continue
            if line == '     |  Methods defined here:':
                classState = ClassScanState_MethodDefinition
                continue
            
            if classState == ClassScanState_MethodDocumentation:
                if re.match(CouldBeMethodDocLineRegex, line):
                    currentMethod.documentation += line
                else:
                    classState = ClassScanState_MethodDefinition
            
            if classState == ClassScanState_MethodDefinition:
                if re.match(ResolvedMethodMatchRegex, line):
                    if currentMethod is not None:
                        methods.append(currentMethod)
                    currentMethod = method()
                    currentMethod.name = line
                    classState = ClassScanState_MethodDocumentation
            
for m in methods:
    print m
