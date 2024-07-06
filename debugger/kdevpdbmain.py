# SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later
import getopt


def main():
    """Kdevelop python debugger main, based on pdb.main()"""
    # pylint: disable=C0415
    # Import things we need after debugger._run()
    import sys
    import kdevpdb
    from kdevpdbconn import Stop
    from pdb import traceback, Restart, _ModuleTarget, _ScriptTarget

    # Target command line is expected after the first '--'.
    split = [i for i in range(len(sys.argv)) if sys.argv[i] == '--']
    if not split or split[0] + 1 >= len(sys.argv):
        sys.exit(2)

    split = split[0]
    opts, args = getopt.getopt(sys.argv[1:split], 's:mc:', ['command='])

    if len(opts) < 1 or args:
        sys.exit(2)

    commands = [optarg for opt, optarg in opts if opt in ['-c', '--command']]
    module_indicated = any(opt in ['-m'] for opt, optarg in opts)
    socketpath = [optarg for opt, optarg in opts if opt == '-s'][0]

    cls = _ModuleTarget if module_indicated else _ScriptTarget
    args = sys.argv[split+1:]
    target = cls(args[0])
    target.check()
    sys.argv[:] = args      # Hide "pdb.py" and pdb options from argument list
    # Note on saving/restoring sys.argv: it's a good idea when sys.argv was
    # modified by the script being debugged. It's a bad idea when it was
    # changed by the user from the command line. There is a "restart" command
    # which allows explicit specification of command line arguments.
    debugger = kdevpdb.kdevPdb(socketpath)
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
    except Stop:
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
