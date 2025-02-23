# SPDX-FileCopyrightText: 2025 Jarmo Tiitto <jarmo.tiitto@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

import bdb
import linecache
import signal
import sys
import traceback
from collections import namedtuple
# Only needed to implement our run_target()
from pdb import _ExecutableTarget
import asmskip

# pylint: disable=R0902

__all__ = ["kdevDbgCore", "FrameInfo"]

# Decomposed frame object.
FrameInfo = namedtuple('FrameInfo', ['frame', 'filename', 'lineno', 'fn', 'f_code', 'f_globals', 'f_locals'])


class kdevDbgCore(bdb.Bdb):
    '''Debugger core class on top of Bdb.
       kdevDbgCore handles low-level tracing functions, isolation
       of the inferior's __main__ namespace from the debugger and
       provides the stack frame list.
    '''

    def __init__(self, skip=None):
        bdb.Bdb.__init__(self, skip=skip)
        # Override Bdb's trace_dispatch()
        self.__trace_dispatch, self.trace_dispatch = self.trace_dispatch, self._trace_dispatch
        # Avoid triggering __getattr__ auditing events when  .__code__ is accessed.
        self.topcode = (self._sigint_handler.__code__, self.trace_dispatch.__code__)
        self.bottomcode = self.run_target.__code__
        # setup_frames() expects inferior_ns_active to be True for efficiency reasons,
        # and setup_frames_from_exc() also requires this. Therefore, FrameInfo, sys
        # and traceback are pinned as instance attributes.
        # to guarantee access to these.
        self._frameinfo = FrameInfo
        self._sys = sys
        self._traceback = traceback
        # switch_namespaces()
        self.saved_namespace = None
        self.saved_main = None
        self.inferior_ns_active = False
        # The stack
        self.stack = []
        self.curframe = None
        self.topindex = -1
        self.bottomindex = -1
        # Caught values.
        self.exc_info = None
        self.ret_value = None
        self.call_args = None
        # Zero: inferior is running and can be interrupted.
        # One: inferior is in progress of being interrupted.
        # Two: debugger cannot be interrupted, inferior is not running.
        self.running = 0
        self.mainpyfile = None
        signal.signal(signal.SIGINT, self._sigint_handler)

    def run_target(self, target: _ExecutableTarget):
        '''Debug a target executed via the exec() function.'''
        self.mainpyfile = self.canonic(target.filename)
        # The target has to run in __main__ namespace (or imports from __main__ will break).
        # Clear __main__ and replace with the target namespace.
        # Since want to keep the debugger  __main__ namespace intact, the __main__.__dict__
        # contents is stashed into self.saved_namespace, while the inferior is running.
        # pylint: disable=C0415, W0122
        import __main__
        self.saved_main = __main__
        self.saved_namespace = {}
        self.saved_namespace.update(__main__.__dict__)
        self.inferior_ns_active = True
        _bdb_Quit = bdb.BdbQuit
        __main__.__dict__.clear()
        __main__.__dict__.update(target.namespace)
        _globals = __main__.__dict__
        _locals = _globals
        self.reset()
        _code = target.code
        assert isinstance(_code, str)
        cmd = compile(_code, "<string>", "exec")
        self._sys.settrace(self.trace_dispatch)
        try:
            exec(cmd, _globals, _locals)
        except _bdb_Quit:
            pass
        finally:
            self.set_quit()
            # Restore debugger __main__.
            self.switch_namespaces()

    def switch_namespaces(self):
        '''Swap between the inferior and the debugger __main__ namespace.'''
        ns_swap = {}
        ns_swap.update(self.saved_main.__dict__)
        self.saved_main.__dict__.clear()
        self.saved_main.__dict__.update(self.saved_namespace)
        self.saved_namespace = ns_swap
        self.inferior_ns_active = not self.inferior_ns_active

    def _sigint_handler(self, signum, frame):
        '''Regain debugger control and suspend the inferior.'''
        # NOTE: this runs with the inferior __main__!
        if self.running >= 1:
            return
        self.running += 1
        # need up-to-date self.curframe
        assert self.inferior_ns_active
        self.setup_frames()
        self.set_trace(self.curframe)

    def _trace_dispatch(self, frame, event, arg):
        '''The trace dispatch trampoline method.'''
        # NOTE: All methods that Bdb invokes run with
        #       the inferior's __main__ namespace, until self.enter() does the switch.
        return self.__trace_dispatch(frame, event, arg)

    def user_call(self, frame, argument_list):
        '''This method is called when there is the remote possibility
           that we ever need to stop in this function.'''
        if self.stop_here(frame):
            # fixme: argument_list provides no useful information.
            self.call_args = (argument_list,)
            self.enter()

    def user_line(self, frame):
        '''This function is called when we stop or break at this line.'''
        self.enter()

    def user_return(self, frame, return_value):
        if self.ret_value is not None:
            # enter_debugger() has not consumed the previous
            # return value yet so stop here.
            self.enter()
        self.ret_value = (return_value,)

    def user_exception(self, frame, exc_info):
        '''This function is called if an exception occurs,
           but only if we are to stop at or just below this level.'''
        self.exc_info = (exc_info,)

    def forget_frames(self):
        '''Clear stack state.'''
        self.stack = []
        self.curframe = None
        self.topindex = -1
        self.bottomindex = -1

    def forget_caught_values(self):
        '''Drop all captured values.'''
        self.exc_info = None
        self.ret_value = None
        self.call_args = None

    def update_tracing(self):
        '''Ensure only the inferior's frames are being traced.'''
        for i, f in enumerate(self.stack):
            if self.topindex >= i >= self.bottomindex:
                f.frame.f_trace = self.trace_dispatch
            else:
                f.frame.f_trace = None

    def make_frameinfo(self, f, lineno):
        '''Construct a FrameInfo from a Frame object.'''
        # NOTE: f.f_code triggers an auditing event, so it is retrieved once
        #       here and stored as part of the FrameInfo.
        f_code = f.f_code
        filename = self.canonic(f_code.co_filename)
        fn = "<lambda>" if not f_code.co_name else f_code.co_name
        # capture the f_globals and f_locals dictionaries.
        f_globals = {}
        f_globals.update(f.f_globals)
        f_locals = {}
        f_locals.update(f.f_locals)
        return self._frameinfo(f, filename, lineno, fn, f_code, f_globals, f_locals)

    def setup_frames(self):
        '''Update the debugger stack state and Bdb.botframe.'''
        # pylint: disable=W0212,W0201
        assert self.inferior_ns_active
        self.forget_frames()
        f = self._sys._getframe().f_back
        # Ignore frames until self.trace_dispatch or self._sigint_handler
        while f is not None:
            if f.f_code in self.topcode:
                break
            f = f.f_back
        while f is not None:
            self.stack.append(self.make_frameinfo(f, f.f_lineno))
            self.botframe = f
            f = f.f_back
        # Reverse, to make indexes into the list stable when frames are added/removed.
        self.stack.reverse()
        self.update_stack_state()
        self.update_tracing()

    def update_stack_state(self):
        '''Update self.bottomindex, self.topindex and self.curframe.'''
        # The inferior's frames are wedged between a frame after run_target() call,
        # and either before a _sigint_handler() or  a _trace_dispatch() frame.
        for i, f in enumerate(self.stack):
            if f.f_code in self.topcode:
                self.topindex = i - 1
                break
            if f.f_code is self.bottomcode:
                self.bottomindex = i + 1
        if self.topindex == -1:
            self.topindex = len(self.stack) - 1
        # Don't trace the exec() frame (which filename is "<string>")
        # after an actual inferior frame becomes available.
        self.bottomindex = min(self.bottomindex + 1, self.topindex)
        self.curframe = self.stack[self.topindex].frame

    def setup_frames_from_exc(self, exc):
        '''Update the debugger stack state from exception's traceback object.'''
        assert self.inferior_ns_active
        if not isinstance(exc, BaseException):
            self.error("No traceback available!")
            return

        print("Uncaught exception:", file=self._sys.stderr)
        self._traceback.print_exception(type(exc), exc, exc.__traceback__, file=self._sys.stderr)
        print("Entering post mortem debugging - continuing will terminate the inferior.", file=self._sys.stderr)

        # Decompose frames from the traceback.
        self.forget_frames()
        t = exc.__traceback__
        while t is not None:
            f = t.tb_frame
            self.stack.append(self.make_frameinfo(f, t.tb_lineno))
            t = t.tb_next
        self.update_stack_state()

    def get_inferior_stack(self):
        '''Get all inferior stack frames. (a subset of self.stack[])'''
        return [f for i, f in enumerate(self.stack) if self.topindex >= i >= self.bottomindex]

    def message(self, msg, lnend='\n'):
        '''Output an informal message.'''
        print(msg, end=lnend, file=self._sys.stdout)

    def error(self, msg, lnend='\n'):
        '''Ouput an error message.'''
        print(msg, end=lnend, file=self._sys.stderr)

    def __enter__(self):
        '''Prepare calling debugger methods.'''
        assert self.inferior_ns_active
        # Restore debugger __main__.
        self.switch_namespaces()

    def __exit__(self, exc_type, exc, tb):
        '''Prepare resuming the inferior.'''
        if exc is not None:
            print("Internal kdevPdb error:", file=self._sys.stderr)
            self._traceback.print_exception(exc_type, exc, tb, file=self._sys.stderr)
            # clear the possible stop condition and terminate instead.
            self.reset()
            self.set_quit()
        # Restore inferior __main__.
        self.switch_namespaces()

        self.forget_frames()
        self.running = 0
        return True  # Eat the exception, if any.

    def enter(self, exc=None):
        '''This function is called when the inferior is suspended.'''
        if self.running == 1:
            # The signal handler has enabled a stop condition:
            # A _sigint_handler() frame exists at this point due to the self.set_trace(),
            # and we *must* get rid of it by resuming execution.
            self.running = 2
            return
        self.running = 2
        # Update stack state.
        self.reset()
        if exc:
            # Setting up post-mortem debugging.
            # run_target() has switched back to the debugger __main__ due to the escaped exc.
            # setup_frames_from_exc() needs the inferior __main__, so do the switch now.
            self.switch_namespaces()
            self.setup_frames_from_exc(exc)
        else:
            self.setup_frames()
        # All code within this block has debugger top-level __main__ imports and types available.
        with self:
            if getattr(self, 'mainpyfile', False):
                # Resume until mainpyfile appears in the inferior stack.
                stack = self.get_inferior_stack()
                if self.mainpyfile not in [x.filename for x in stack]:
                    return
                if stack[-1].lineno < 0:
                    # There is no actual inferior frame at this point,
                    # so step over to get to the first actual source line.
                    self.set_next(self.curframe)
                    return
                # start up done.
                del self.mainpyfile
            if self.curframe.f_code is self.bottomcode:
                # no actual inferior frames?
                # (Inferior has likely raised an unhandled exception)
                return
            self.enter_debugger()

    def enter_debugger(self):
        '''By returning from this method the inferior resumes its execution,
           or the debugger quits if post mortem debugging is ongoing.
           If self.quitting is set, this causes Bdb to throw BdbQuit terminating the inferior.
        '''
        raise NotImplementedError("subclass of kdevDbgCore must implement enter_debugger()")

    def set_stepout(self):
        """Step-out of a function or past a conditional block of code."""
        lineno = asmskip.stepout_lineno(self.curframe.f_code, self.curframe.f_lineno)
        if lineno >= self.curframe.f_lineno:
            # Can step out of this block of code.
            self.set_until(self.curframe, lineno)
        elif self.topindex > self.bottomindex:
            # Stop immediately after exiting from the frame.
            self.set_return(self.curframe)
        else:
            # No outer frames left, single step.
            self.set_next(self.curframe)
        return 1

    def is_runnable_srcline(self, filename, lineno):
        '''Check if source line contains executable code.'''
        line = linecache.getline(filename, lineno, self.curframe.f_globals)
        if not line:
            self.error(f"Invalid location {filename}:{lineno} (end-of-file)")
            return -1
        line = line.strip()
        if not line:
            self.error(f"Invalid location {filename}:{lineno} (blank)")
            return -2
        if line[0] == '#':
            self.error(f"Invalid location {filename}:{lineno} (comment)")
            return -3
        if line[:3] in ('"""', "'''"):
            self.error(f"Invalid location {filename}:{lineno} (doc-string)")
            return -4
        return lineno
