# SPDX-FileCopyrightText: 2014 Sven Brauch <svenbrauch@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

import sys
import traceback
import pdb
import json
import signal
import kdevpdbconn

# pylint: disable=C0103, R0903


class kdevPdb(pdb.Pdb):
    ''' KDevelop python debugger (kdevpdb)
        A few points:
        * kdevPdb normally shouldn't output anything into stdout or stderr, and message()
          and error() have been overridden below to mostly reach this.
        * kdevPdb replaces a few of key methods from Pdb to implement the out-of-band
          communication, and to structure command output into JSON data.
    '''
    def __init__(self, socketpath="/tmp/"):
        self.pdbsrv = kdevpdbconn.kdevPdbConnection()
        preinit = {"seq": -1, "input": "pass\n"}
        self.pdbsrv.dataframes.append(json.dumps(preinit).encode())
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
        super().__init__(completekey=None, stdin=None, stdout=None, skip=None, nosigint=True)
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
        # temporarily disable tracing.
        sys.settrace(None)
        # Tell the client the current request was interrupted.
        self.append_response({"halt": True})
        # Ensure we will stop in the most recent inferior frame only.
        stop_frame = None
        f = sys._getframe().f_back
        f_prev = f
        while f is not None:
            if f_prev.f_code is self.trace_dispatch.__code__:
                # f is the most recent inferior frame.
                stop_frame = f
            f.f_trace = None if stop_frame is None else self.trace_dispatch
            self.botframe = f
            f_prev = f
            f = f.f_back
        self.set_next(stop_frame)
        sys.settrace(self.trace_dispatch)

    def do_return(self, arg):
        """Augmented version of pdb.do_return(...)"""
        # TODO: this needs *more* improvements.
        self.set_return(self.curframe)
        return 1
    do_r = do_return

    def append_response(self, obj):
        assert isinstance(obj, dict)
        self.responses.setdefault(self.command_seqnro, []).append(obj)

    def send_response(self):
        '''Send the current response to KDevelop'''
        resp = self.responses.pop(self.command_seqnro, [])
        fmt = {"seq": self.command_seqnro, "data": resp}
        self.pdbsrv.sendDataFrame(json.dumps(fmt).encode())

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
                    request = json.loads(self.pdbsrv.getDataFrame().decode())
                    assert "seq" in request
                    self.command_seqnro = int(request["seq"])
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
        except kdevpdbconn.Stop:
            raise
        except BaseException:
            # Hang up and die immediately. :-(
            print('Internal kdevPdb error:', file=sys.stderr)
            traceback.print_exc(None, file=sys.stderr)
            raise kdevpdbconn.Stop()

    def make_frame_entry(self, frame_lineno):
        frame, lineno = frame_lineno
        filename = self.canonic(frame.f_code.co_filename)
        entry = {"current": (frame is self.curframe), "filename": filename, "line": lineno,
                 # Separate source line contents with '\n' which should be easier to parse.
                 # After the first ')' char is the function info, and
                 # after '\n' is the source line contents)
                 "location": self.format_stack_entry(frame_lineno, '\n')}
        return entry

    def do_where(self, _):
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
