# SPDX-FileCopyrightText: 2014 Sven Brauch <svenbrauch@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later

import pdb
import json
import getopt
import kdevpdbconn


class kdevPdb(pdb.Pdb):
    ''' KDevelop python debugger (kdevpdb)
        A few points:
        * kdevPdb normally shouldn't output anything into stdout or stderr, and message()
          and error() have been overridden below to mostly reach this.
        * kdevPdb replaces a few of key methods from Pdb to implement the out-of-band
          communication, and to structure command output into JSON data.
    '''
    def __init__(self, kdevpath):
        # Pin down the required modules as member attributes:
        self.json = json
        self.kdevpdbconn = kdevpdbconn
        self.pdbsrv = kdevpdbconn.kdevPdbConnection()
        # Immediately adjust sys.path as the first "command".
        preinit = {"seq": -1, "input": f"import sys; sys.path.append({kdevpath!r})\n"}
        self.pdbsrv.dataframes.append(self.json.dumps(preinit).encode())
        # Connect to a client.
        self.pdbsrv.establish()
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
        super().__init__(None)
        self.prompt = ""

    def append_response(self, obj):
        assert isinstance(obj, dict)
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
                    # Wait for a request.
                    request = self.json.loads(self.pdbsrv.getDataFrame().decode())
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
        except self.kdevpdbconn.Stop:
            raise
        except BaseException as e:
            print(e)

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
    opts, args = getopt.getopt(sys.argv[1:split], 'd:mc:', ['command='])

    if len(opts) < 1 or args:
        sys.exit(2)

    commands = [optarg for opt, optarg in opts if opt in ['-c', '--command']]
    module_indicated = any(opt in ['-m'] for opt, optarg in opts)
    kdevpath = [optarg for opt, optarg in opts if opt == '-d'][0]

    cls = pdb._ModuleTarget if module_indicated else pdb._ScriptTarget
    args = sys.argv[split+1:]
    target = cls(args[0])
    target.check()
    sys.argv[:] = args      # Hide "pdb.py" and pdb options from argument list
    # Note on saving/restoring sys.argv: it's a good idea when sys.argv was
    # modified by the script being debugged. It's a bad idea when it was
    # changed by the user from the command line. There is a "restart" command
    # which allows explicit specification of command line arguments.
    debugger = kdevPdb(kdevpath)
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
