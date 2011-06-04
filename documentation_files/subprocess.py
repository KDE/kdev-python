#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Subprocess management.
"""
class Popen:


	"""
	Arguments are:
	
	*args* should be a string, or a sequence of program arguments.  The program
	to execute is normally the first item in the args sequence or the string if
	a string is given, but can be explicitly set by using the *executable*
	argument.  When *executable* is given, the first item in the args sequence
	is still treated by most programs as the command name, which can then be
	different from the actual executable name.  On Unix, it becomes the display
	name for the executing program in utilities such as :program:`ps`.
	
	On Unix, with *shell=False* (default): In this case, the Popen class uses
	:meth:`os.execvp` to execute the child program. *args* should normally be a
	sequence.  If a string is specified for *args*, it will be used as the name
	or path of the program to execute; this will only work if the program is
	being given no arguments.
	
	"""
	
	
	def __init__(self, args,bufsize=0,executable=None,stdin=None,stdout=None,stderr=None,preexec_fn=None,close_fds=False,shell=False,cwd=None,env=None,universal_newlines=False,startupinfo=None,creationflags=0):
		pass
	
	def call(popenargs,kwargs):
		"""
		Run command with arguments.  Wait for command to complete, then return the
		:attr:`returncode` attribute.
		
		The arguments are the same as for the :class:`Popen` constructor.  Example::
		
		>>> retcode = subprocess.call(["ls", "-l"])
		
		"""
		pass
		
	def check_call(popenargs,kwargs):
		"""
		Run command with arguments.  Wait for command to complete. If the exit code was
		zero then return, otherwise raise :exc:`CalledProcessError`. The
		:exc:`CalledProcessError` object will have the return code in the
		:attr:`returncode` attribute.
		
		The arguments are the same as for the :class:`Popen` constructor.  Example::
		
		>>> subprocess.check_call(["ls", "-l"])
		0
		
		"""
		pass
		
	def check_output(popenargs,kwargs):
		"""
		Run command with arguments and return its output as a byte string.
		
		If the exit code was non-zero it raises a :exc:`CalledProcessError`.  The
		:exc:`CalledProcessError` object will have the return code in the
		:attr:`returncode`
		attribute and output in the :attr:`output` attribute.
		
		The arguments are the same as for the :class:`Popen` constructor.  Example::
		
		>>> subprocess.check_output(["ls", "-l", "/dev/null"])
		'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'
		
		The stdout argument is not allowed as it is used internally.
		To capture standard error in the result, use ``stderr=subprocess.STDOUT``::
		
		>>> subprocess.check_output(
		*more     ["/bin/sh", "-c", "ls non_existent_file; exit 0"],
		*more     stderr=subprocess.STDOUT)
		'ls: non_existent_file: No such file or directory\n'
		
		"""
		pass
		
	"""
	Special value that can be used as the *stdin*, *stdout* or *stderr* argument
	to :class:`Popen` and indicates that a pipe to the standard stream should be
	opened.
	
	
	"""
	PIPE = None
	"""
	Special value that can be used as the *stderr* argument to :class:`Popen` and
	indicates that standard error should go into the same handle as standard
	output.
	
	
	Convenience Functions
	^^^^^^^^^^^^^^^^^^^^^
	
	This module also defines the following shortcut functions:
	
	
	"""
	STDOUT = None
	


class STARTUPINFO:


	"""
	Partial support of the Windows
	`STARTUPINFO <http://msdn.microsoft.com/en-us/library/ms686331(v=vs.85).aspx>`__
	structure is used for :class:`Popen` creation.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	"""
	The standard input device. Initially, this is the console input buffer,
	``CONIN$``.
	
	"""
	STD_INPUT_HANDLE = None
	"""
	The standard output device. Initially, this is the active console screen
	buffer, ``CONOUT$``.
	
	"""
	STD_OUTPUT_HANDLE = None
	"""
	The standard error device. Initially, this is the active console screen
	buffer, ``CONOUT$``.
	
	"""
	STD_ERROR_HANDLE = None
	"""
	Hides the window. Another window will be activated.
	
	"""
	SW_HIDE = None
	"""
	Specifies that the :attr:`STARTUPINFO.hStdInput`,
	:attr:`STARTUPINFO.hStdOutput`, and :attr:`STARTUPINFO.hStdError` members
	contain additional information.
	
	"""
	STARTF_USESTDHANDLES = None
	"""
	Specifies that the :attr:`STARTUPINFO.wShowWindow` member contains
	additional information.
	
	"""
	STARTF_USESHOWWINDOW = None
	"""
	The new process has a new console, instead of inheriting its parent's
	console (the default).
	
	This flag is always set when :class:`Popen` is created with ``shell=True``.
	
	"""
	CREATE_NEW_CONSOLE = None
	"""
	A :class:`Popen` ``creationflags`` parameter to specify that a new process
	group will be created. This flag is necessary for using :func:`os.kill`
	on the subprocess.
	
	This flag is ignored if :data:`CREATE_NEW_CONSOLE` is specified.
	
	
	.. eplacing Older Functions with the subprocess Module
	----------------------------------------------------
	
	In this section, "a ==> b" means that b can be used as a replacement for a.
	
	"""
	CREATE_NEW_PROCESS_GROUP = None
	


