#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Generate byte-code files from Python source files.
"""
def compile(file,cfile,dfile,doraise):
	"""
	Compile a source file to byte-code and write out the byte-code cache  file.  The
	source code is loaded from the file name *file*.  The  byte-code is written to
	*cfile*, which defaults to *file* ``+`` ``'c'`` (``'o'`` if optimization is
	enabled in the current interpreter).  If *dfile* is specified, it is used as the
	name of the source file in error messages instead of *file*.  If *doraise* is
	true, a :exc:`PyCompileError` is raised when an error is encountered while
	compiling *file*. If *doraise* is false (the default), an error string is
	written to ``sys.stderr``, but no exception is raised.
	
	
	"""
	pass
	
def main(args):
	"""
	Compile several source files.  The files named in *args* (or on the command
	line, if *args* is not specified) are compiled and the resulting bytecode is
	cached in the normal manner.  This function does not search a directory
	structure to locate source files; it only compiles files named explicitly.
	If ``'-'`` is the only parameter in args, the list of files is taken from
	standard input.
	
	"""
	pass
	
