# SPDX-FileCopyrightText: 2014 Sven Brauch <svenbrauch@gmail.com>
# SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

''' KDevelop python debugger (kdevPdb)
        A few points:
        * kdevPdb normally doesn't output anything into stdout or stderr. message()
          and error() are used to output messages, except for fatal errors like
          uncaught exceptions which are printed to stderr.
        * kdevPdb does out-of-band communication via a stream socket using
          the kdevPdbConnection helper module.
'''

import sys
import json
import getopt
import traceback
from pdb import _ModuleTarget, _ScriptTarget, _ZipTarget
from bdb import Breakpoint
import kdevpdbcore
import kdevpdbconn

# pylint: disable=C0103, R0903


class kdevPdb(kdevpdbcore.kdevDbgCore):
    def __init__(self, socketpath="/tmp/"):
        kdevpdbcore.kdevDbgCore.__init__(self)
        # Connect to a client.
        self.pdbsrv = kdevpdbconn.kdevPdbConnection()
        self.pdbsrv.dataframes.append(json.dumps({"seq": -1}).encode())
        # Connect to a client.
        self.pdbsrv.establish(socketpath)
        # The command's output is associated with it by the command sequence number.
        # The seqnro begins from the preinit response -1.
        self.command_seqnro = -1
        self.responses = {}
        # The kdevPdb responds with {"seq":-1} once the client has connected
        # and the program is successfully started.
        self.debugger_initialized = False

    def append_response(self, obj):
        assert isinstance(obj, dict)
        # TODO: Check that the data-frame size does not grow past WARN_TOO_BIG_FRAMESIZE.
        #       We should consider an mechanism to report a such event as an error to the client.
        self.responses.setdefault(self.command_seqnro, []).append(obj)

    def send_response(self):
        '''Send the current response to KDevelop'''
        resp = self.responses.pop(self.command_seqnro, [])
        fmt = {"seq": self.command_seqnro, "data": resp}
        self.pdbsrv.sendDataFrame(json.dumps(fmt).encode())

    def message(self, msg, lnend='\n'):
        '''Log an output message.
           JSON: "message" : str()
        '''
        self.append_response({"message": msg + lnend})

    def error(self, msg, lnend='\n'):
        '''Log an error message.
           JSON: "error" : str()
        '''
        self.append_response({"error": msg + lnend})

    def postloop(self):
        # About to return from enter_debugger(), thus allow the client to
        # interrupt the current operation.
        self.pdbsrv.sendCmdFrame(kdevpdbconn.Cmd.InterruptAllowed)

    def preloop(self):
        # Disallow interrupting.
        self.pdbsrv.sendCmdFrame(kdevpdbconn.Cmd.InterruptDisallowed)

        if not self.debugger_initialized:
            # Complete the preinit handshake with the client.
            _, self.debugger_initialized = self.get_next_request()
            if not self.debugger_initialized:
                return
            self.message("The program started successfully.")
            self.debugger_initialized = True

        # Send a "frames" response of the top-most inferior frame.
        # JSON: "frames" : [{}]
        self.append_response({"frames": [self.make_frame_entry(self.stack[self.topindex])]})
        # todo: report which an breakpoint was hit?

        if hasattr(self, 'restore_brks'):
            # Re-enable breakpoints that runtolocation() disabled.
            for bpnum in self.restore_brks[1:]:
                self.get_bpbynumber(bpnum).enable()
            # Ensure self.restore_brks[0] is deleted even if it wasn't hit.
            self.clear_bpbynumber(self.restore_brks[0])
            del self.restore_brks

    def get_next_request(self):
        '''Wait for a request.'''
        try:
            request = json.loads(self.pdbsrv.getDataFrame().decode())
            assert isinstance(request, dict)
            assert "seq" in request
            self.command_seqnro = int(request["seq"])
            return request, True
        except kdevpdbconn.Stop:
            self.pdbsrv.stop()
            self.set_quit()
            return {}, False

    def enter_debugger(self):
        self.preloop()
        while True:
            # Send a response.
            self.send_response()
            # Wait for a request.
            request, ok = self.get_next_request()
            if not ok:
                return
            if "input" not in request:
                # A no-op request: send back the seqnro.
                continue
            cmd_and_args = request["input"]
            assert isinstance(cmd_and_args, list)
            assert len(cmd_and_args) > 0
            method_name = cmd_and_args[0]
            try:
                # dispatch a call to 'do_' method.
                cmd_dispatch = getattr(self, 'do_' + method_name)
                method_args = tuple(cmd_and_args[1:])
                if cmd_dispatch(*method_args):
                    # The command needs to resume the inferior.
                    self.postloop()
                    return
            except (AttributeError, TypeError):
                self.error(f"Invalid command: '{cmd_and_args}'")
                raise

    def make_frame_entry(self, frameinfo):
        '''Make a JSON response from a FrameInfo.'''
        return {"current": (frameinfo.frame is self.curframe),
                "filename": str(frameinfo.filename),
                "line": int(frameinfo.lineno),
                "address": int(frameinfo.frame.f_lasti),
                "function": str(frameinfo.fn)}

    def do_where(self):
        '''where(): Report a full stack trace, with the most recent frame
           at the front of the list.
           JSON: "frames" : [{},...]
        '''
        # Dump the inferior frame info.
        framelist = reversed([self.make_frame_entry(f) for f in self.get_inferior_stack()])
        self.append_response({"frames": list(framelist)})

    def do_selectframe(self, whichframe):
        '''Select the active stack-frame.
           JSON: "activeframe" : <int>
        '''
        # KDevelop expects most recent frame to be at index zero,
        # which is reversed to what we have in self.stack.
        kdevframe = max(min(int(whichframe), len(self.get_inferior_stack()) - 1), 0)
        # todo: nothing is yet depending on the client selected stack-frame.
        # self.activeindex = len(self.stack) - 1 - int(kdevframe)
        self.append_response({"activeframe": kdevframe})

    def do_continue(self):
        '''Resume the inferior.'''
        self.set_continue()
        return 1

    def do_step(self):
        '''Step into called code.'''
        self.set_step()
        return 1

    def do_next(self):
        '''Step over to next line.'''
        self.set_next(self.curframe)
        return 1

    def do_stepout(self):
        '''Step-out of a frame.'''
        if self.topindex > self.bottomindex:
            # Stop immediately after exiting from the frame.
            self.set_return(self.curframe)
        else:
            # No outer frames left, single step.
            self.set_next(self.curframe)
        return 1

    def do_steppast(self):
        '''Step-out of a function or past a conditional block of code.'''
        self.set_stepout()
        return 1

    def do_quit(self):
        '''Quit.'''
        self.set_quit()
        return 1

    def do_jump(self, lineno):
        '''Set the next line to be executed.'''
        try:
            self.curframe.f_lineno = int(lineno)
        except ValueError:
            self.error(f"Jump to location '{self.stack[self.topindex].filename}:{lineno}' failed!")
        finally:
            self.switch_namespaces()
            self.setup_frames()
            self.switch_namespaces()
            self.append_response({"frames": [self.make_frame_entry(self.stack[self.topindex])]})

    def do_break(self, filename, lineno, disabled):
        '''Try set a breakpoint at filename:lineno location and possibly disable it by default.
           JSON: "breakpoints": [{}] (single item) breakpoint details.
        '''
        if self.is_runnable_srcline(filename, int(lineno)) < 0:
            return
        bpnum = Breakpoint.next
        notok = self.set_break(filename, int(lineno))
        if notok:
            self.error(notok)
            return
        if disabled:
            self.get_bpbynumber(bpnum).disable()
        self.append_response({"breakpoints": [{"id": bpnum, "filename": filename, "line": lineno}]})

    def do_tbreak(self, filename, lineno):
        '''Try set a temporary breakpoint at filename:lineno location.'''
        if self.is_runnable_srcline(filename, int(lineno)) < 0:
            return
        bpnum = Breakpoint.next
        notok = self.set_break(filename, int(lineno), True)
        if notok:
            self.error(notok)
        else:
            self.append_response({"breakpoints": [{"id": bpnum, "filename": filename, "line": lineno}]})

    def do_runtolocation(self, filename, lineno, disable):
        '''Try set a temporary breakpoint at filename:lineno location.
           If successful, disable all other breakpoints if disable is set and then resume the inferior.
           Later, when the (temporary) breakpoint is reached or the debugger is interrupted,
           the enabled state of the modified breakpoints is restored.
        '''
        if self.is_runnable_srcline(filename, int(lineno)) < 0:
            self.append_response({"frames": [self.make_frame_entry(self.stack[self.topindex])]})
            return 0
        bpnum = Breakpoint.next
        notok = self.set_break(filename, int(lineno), True)
        if notok:
            self.error(notok)
            self.append_response({"frames": [self.make_frame_entry(self.stack[self.topindex])]})
            return 0
        # Ok.
        self.append_response({"breakpoints": [{"id": bpnum, "filename": filename, "line": lineno}]})
        restore_brks = [bpnum]
        if disable:
            for bp in Breakpoint.bpbynumber:
                if bp and bp.enabled and bp.number != bpnum:
                    restore_brks.append(bp.number)
                    bp.disable()
        setattr(self, 'restore_brks', restore_brks)
        self.set_continue()
        return 1

    def do_enable(self, bpnum):
        '''Enable a breakpoint'''
        try:
            bp = self.get_bpbynumber(int(bpnum))
            bp.enable()
        except ValueError as e:
            self.error(str(e))

    def do_disable(self, bpnum):
        '''Disable a breakpoint'''
        try:
            bp = self.get_bpbynumber(int(bpnum))
            bp.disable()
        except ValueError as e:
            self.error(str(e))

    def do_clear(self, arg):
        '''Implement Bdb's do_clear(), required for tbreak.'''
        notok = self.clear_bpbynumber(int(arg))
        if notok:
            self.error(notok)


def main():
    """Kdevelop python debugger main."""
    # Target command line is expected after the first '--'.
    split = [i for i in range(len(sys.argv)) if sys.argv[i] == '--']
    if not split or split[0] + 1 >= len(sys.argv):
        sys.exit(2)

    split = split[0]
    opts, args = getopt.getopt(sys.argv[1:split], 's:m:')

    if len(opts) < 1 or args:
        sys.exit(2)

    socketpath = [optarg for opt, optarg in opts if opt == '-s'][0]
    args = sys.argv[split+1:]

    if any(opt in ['-m'] for opt, optarg in opts):
        cls = _ModuleTarget
    elif args[0].endswith('.pyz'):
        cls = _ZipTarget
    else:
        cls = _ScriptTarget

    target = cls(args[0])
    sys.argv[:] = args      # Hide "kdevpdb.py" and kdevpdb options from argument list.
    debugger = kdevPdb(socketpath)
    exitcode = 0
    try:
        debugger.run_target(target)
    except SystemExit as e:
        # In most cases SystemExit does not warrant a post-mortem session.
        print("The program exited via sys.exit(). Exit status:", end=' ')
        print(e)
    except SyntaxError:
        print("Syntax error:")
        traceback.print_exc()
        exitcode = 1
    except BaseException as e:
        debugger.enter(e)
        exitcode = 1
    debugger.pdbsrv.stop()
    sys.exit(exitcode)

if __name__ == '__main__':
    main()
