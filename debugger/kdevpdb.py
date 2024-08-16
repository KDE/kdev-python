# SPDX-FileCopyrightText: 2014 Sven Brauch <svenbrauch@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

import sys
import pdb
import json
import getopt
import signal
import kdevpdbconn


class kdevPdb(pdb.Pdb):
    ''' KDevelop python debugger (kdevpdb)
        A few points:
        * kdevPdb normally shouldn't output anything into stdout or stderr, and message()
          and error() have been overridden below to mostly reach this.
        * kdevPdb replaces a few of key methods from Pdb to implement the out-of-band
          communication, and to structure command output into JSON data.
    '''
    def __init__(self, kdevpath, socketpath="/tmp/"):
        # Pin down the required modules as member attributes:
        self.json = json
        self.kdevpdbconn = kdevpdbconn
        self.pdbsrv = kdevpdbconn.kdevPdbConnection()
        # Immediately adjust sys.path as the first "command".
        preinit = {"seq": -1, "input": f"import sys; sys.path.append({kdevpath!r})\n"}
        self.pdbsrv.dataframes.append(self.json.dumps(preinit).encode())
        # Connect to a client.
        self.pdbsrv.establish(socketpath)
        # The command's output is associated with it by the command sequence number. The
        # seqnro begins from -1, because of the above preinit request.
        # * cmdloop() receives the command sequence number "seq" (seqnro) from the client. The
        #   command output is then appended into that response entry.
        # * cmdloop() then transfers the response JSON data to the client
        #   (KDevelop) with the specified seqnro just before acquiring the next command from
        #   kdevPdbConnection. This allows the client to reliably tell what the executed
        #   command's response was.
        self.command_seqnro = -1
        self.responses = {}
        # Pdb appends an operation into self.cmdqueue on start up to display the stack-frame.
        # The response of this is reported with seqnro -1 only after preinit has been processed.
        self.debugger_initialized = False
        # Init the super class:
        # - Disable tab complete
        # - Use sys.stdin and sys.stdout
        # - nosigint=True, we install our own SIGINT handler.
        # - readrc=False, don't read the user's Pdb configuration since this can interfere
        #   with the initialization of kdevPdb.
        super().__init__(completekey=None, stdin=None, stdout=None, skip=None, nosigint=True, readrc=False)
        self.prompt = ""
        self.sigint_triggered = False
        signal.signal(signal.SIGINT, self.sigint_handler)

    def sigint_handler(self, signum, frame):
        '''Augmented version of pdb.sigint_handler(...)
           JSON: "halt" : True
        '''
        if self.sigint_triggered:
            return
        self.sigint_triggered = True
        # temporarily disable tracing...
        sys.settrace(None)
        # Tell the client the current request was interrupted.
        self.append_response({"halt": True})
        # Ensure we will stop in the most recent inferior frame only.
        stop_frame = None
        f = sys._getframe().f_back
        while f is not None:
            filename = self.canonic(f.f_code.co_filename)
            if stop_frame is None and not filename.endswith(('bdb.py', 'pdb.py')):
                stop_frame = f
            f.f_trace = None if stop_frame is None else self.trace_dispatch
            self.botframe = f
            f = f.f_back
        self.set_next(stop_frame)
        sys.settrace(self.trace_dispatch)

    def do_return(self, arg):
        """kdevPdb implementation of stepOut()"""
        # Look ahead in the current frame's code and try find a line of code
        # after the current line, which has an smaller indent level.
        # This enables a fine grain stepping out of loops etc. before stepping out of the frame.
        curr = None
        lineno = None
        try:
            itr = enumerate(self.curframe.f_code.co_positions())
            while True:
                i, pyi = next(itr)
                if None in pyi or i < self.curframe.f_lasti // 2:
                    continue
                if curr is None or pyi[0] == curr[0] and pyi[2] < curr[2]:
                    # Compute a minimum indent level of this line before comparing.
                    curr = pyi
                    lineno = None
                elif pyi[2] < curr[2]:
                    # indent level decreased after lineno changed.
                    lineno = pyi[0]
                    break
        except StopIteration:
            curr = None
        if None not in (lineno, curr) and lineno > self.curframe.f_lineno:
            # Can step out of this block of code.
            self.set_until(self.curframe, lineno)
        elif self.curindex > 2:
            # Stop immediately after returning from  self.curframe.
            self.set_return(self.curframe)
        else:
            # No outer frames left, single step.
            self.set_next(self.curframe)
        return 1
    do_r = do_return

    def user_return(self, frame, return_value):
        """Augmented version of Pdb.user_exception()."""
        # By not calling self.interaction() here and in kdevPdb.user_exception()
        # kdevPdb overrides the PDB's "stop just before returning" behavior.
        if self._wait_for_mainpyfile:
            return

    def user_exception(self, frame, exc_info):
        '''Augmented version of Pdb.user_exception()'''
        # By not calling self.interaction() here and in kdevPdb.user_return()
        # kdevPdb overrides the PDB's "stop just before returning" behavior.
        if self._wait_for_mainpyfile:
            return

    def append_response(self, obj):
        assert isinstance(obj, dict)
        # TODO: Check that the data-frame size does not grow past WARN_TOO_BIG_FRAMESIZE.
        #       We should consider an mechanism to report a such event as an error to the client.
        self.responses.setdefault(self.command_seqnro, []).append(obj)

    def send_response(self):
        '''Send the current response to KDevelop'''
        resp = self.responses.pop(self.command_seqnro, [])
        fmt = {"seq": self.command_seqnro, "data": resp}
        self.pdbsrv.sendDataFrame(self.json.dumps(fmt).encode())

    def message(self, msg):
        '''Buffer a command output message.
           JSON: "message" : str()
        '''
        self.append_response({"message": msg})

    def error(self, msg):
        '''Buffer a command error message.
           JSON: "error" : str()
        '''
        self.append_response({"error": msg})

    def postcmd(self, stop, line):
        return stop

    def preloop(self):
        pass

    def cmdloop(self, intro=None):
        """Process the kdevPdbConnection received commands.
           This method replaces the cmd.Cmd.cmdloop() implementation.
           TODO: Adapting the code of Pdb.precmd(), cmd.Cmd.onecmd() and cmd.Cmd.parseline() for
                Kdevelop's purposes:
                In Pdb.precmd(), kdevPdb does not need recognize any command aliases. We should
                never have multiple commands per a request either.
                cmd.Cmd.onecmd() and cmd.Cmd.parseline() would allow to go away with the line
                based commands, removing the need for '\n', and having the command's arguments
                fed in as JSON "args" : [] list.
                Overall, such changes could simplify the overall code needed for processing.
        """
        self.preloop()
        try:
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0)
                else:
                    if self.debugger_initialized:
                        self.send_response()
                    self.sigint_triggered = False
                    # Wait for a request.
                    request = self.json.loads(self.pdbsrv.getDataFrame().decode())
                    assert "seq" in request
                    self.command_seqnro = int(request["seq"])
                    if "input" not in request:
                        # A no-op request.
                        continue
                    line = request["input"]
                    assert line.endswith('\n')
                    if not line:
                        line = 'EOF'
                    else:
                        line = line.rstrip('\r\n')
                    if self.command_seqnro == -1:
                        # reached the last (and only) preinit command.
                        self.debugger_initialized = True
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)
            self.postloop()
        except self.kdevpdbconn.Stop:
            raise
        except BaseException:
            # Hang up and die immediately. :-(
            import traceback
            import sys
            print('Internal kdevPdb error:', file=sys.stderr)
            traceback.print_exc(None, file=sys.stderr)
            raise self.kdevpdbconn.Stop()

    def make_frame_entry(self, frame_lineno):
        frame, lineno = frame_lineno
        filename = self.canonic(frame.f_code.co_filename)
        entry = {"current": (frame is self.curframe), "filename": filename, "line": lineno,
                 # Separate source line contents with '\n' which should be easier to parse.
                 # After the first ')' char is the function info, and
                 # after '\n' is the source line contents)
                 "location": self.format_stack_entry(frame_lineno, '\n')}
        return entry

    def do_where(self, arg):
        '''w(here)
           Report a stack trace, with the most recent frame at the front of the list.
           Augmented version from Pdb.do_where() to better match what Kdevelop wants.
           JSON: "frames" : [{},...]
        '''
        # Dump the frame info.
        framelist = [self.make_frame_entry(i) for i in self.stack]
        # NOTE: Some entries likely refer into bdb.py, which the kdevelop should filter out.
        self.append_response({"frames": list(reversed(framelist))})
    do_w = do_where
    do_bt = do_where

    def print_stack_entry(self, frame_lineno, prompt_prefix=""):
        '''Augmented version of pdb.print_stack_entry() to report in JSON.
           JSON: "frames": [{}]
        '''
        # dump using same scheme as with do_where(): the list just has a single entry.
        entry = self.make_frame_entry(frame_lineno)
        self.append_response({"frames": [entry]})

    def do_selectframe(self, arg):
        '''Select the active stack-frame.
           JSON: "activeframe" : <int>
        '''
        # KDevelop expects most recent frame to be at index zero,
        # which is reversed to what we have in self.stack.
        kdevframe = max(min(int(arg), len(self.stack) - 1), 0)
        nro = len(self.stack) - 1 - int(kdevframe)
        self._select_frame(nro)
        self.responses.setdefault(self.command_seqnro, []).append({"activeframe": kdevframe})


def main():
    """Kdevelop python debugger main, based on pdb.main()"""
    # Pin down pdb.Restart pdb.traceback from pdb, and import sys
    import sys
    traceback = pdb.traceback
    Restart = pdb.Restart

    # Target command line is expected after the first '--'.
    split = [i for i in range(len(sys.argv)) if sys.argv[i] == '--']
    if not split or split[0] + 1 >= len(sys.argv):
        sys.exit(2)

    split = split[0]
    opts, args = getopt.getopt(sys.argv[1:split], 'd:s:mc:', ['command='])

    if len(opts) < 2 or args:
        sys.exit(2)

    commands = [optarg for opt, optarg in opts if opt in ['-c', '--command']]
    module_indicated = any(opt in ['-m'] for opt, optarg in opts)
    kdevpath = [optarg for opt, optarg in opts if opt == '-d'][0]
    socketpath = [optarg for opt, optarg in opts if opt == '-s'][0]

    cls = pdb._ModuleTarget if module_indicated else pdb._ScriptTarget
    args = sys.argv[split+1:]
    target = cls(args[0])
    target.check()
    sys.argv[:] = args      # Hide "pdb.py" and pdb options from argument list
    # Note on saving/restoring sys.argv: it's a good idea when sys.argv was
    # modified by the script being debugged. It's a bad idea when it was
    # changed by the user from the command line. There is a "restart" command
    # which allows explicit specification of command line arguments.
    debugger = kdevPdb(kdevpath, socketpath)
    debugger.rcLines.extend(commands)

    exitcode = 0
    try:
        # NOTE: _run() *replaces* the __main__ namespace with the target's __main__. This
        #       means that any objects that we haven't pinned as local names in this routine
        #       will now cease to exist, since all references to other objects can be dropped.
        debugger._run(target)
    except Restart:
        # kdevpdb does not allow restarting.
        pass
    except debugger.kdevpdbconn.Stop:
        # Client exited
        pass
    except SystemExit as e:
        # In most cases SystemExit does not warrant a post-mortem session.
        print("The program exited via sys.exit(). Exit status:", end=' ')
        print(e)
    except SyntaxError:
        traceback.print_exc()
        exitcode = 1
    except BaseException as e:
        traceback.print_exc()
        print("Uncaught exception. Entering post mortem debugging")
        t = e.__traceback__
        debugger.interaction(None, t)
        exitcode = 1
    debugger.pdbsrv.stop()
    sys.exit(exitcode)

if __name__ == '__main__':
    main()
