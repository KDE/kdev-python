#!/usr/bin/env python

import importlib

modules = ["numpy", "numpy.ctypeslib",
           "numpy.lib.scimath", "numpy.fft", "numpy.linalg",
           "numpy.testing", "numpy.random"]

special_hints = {
    "array": { "returns": "ndarray()" }
}

import sys
sys.path.append("../introspection/")
import introspect
with open("../../documentation_files/numpy.py", 'w') as sys.stdout:
    sys.stdout.write("class getset_descriptor: pass\n")
    sys.stdout.write("class dictproxy: pass\n")
    sys.stdout.write("class member_descriptor: pass\n")

    for module in modules:
        dumper = introspect.ModuleDumper(importlib.import_module(module),
                                         startIndent=4*(module.count('.')),
                                         special_hints=special_hints)
        for index, component in enumerate(module.split('.')[1:]):
            sys.stdout.write((" "*index*4) + "class " + component + ":\n")
        dumper.dump()

    sys.stdout.write("fromfile = _fromfile\n")
    sys.stdout.write("frombuffer = _frombuffer\n")
    sys.stdout.write("fromstring = _fromstring\n")
