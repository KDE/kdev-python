#!/usr/bin/env python

from pycodestyle import Checker
from contextlib import redirect_stdout
from io import StringIO
from sys import stdin, stdout, stderr

while True:
    size = stdin.read(10)
    size = int(size)
    if not size > 0:
        continue
    buf = str()
    print("waiting for buf of size", size, file=stderr)
    while len(buf) < size:
        buf += stdin.read(size-len(buf))
        print("buf:", buf, file=stderr)
    lines = buf.splitlines()
    opts, text = lines[:3], [l + "\n" for l in lines[3:]]

    c = Checker(lines=text)
    output = StringIO()
    with redirect_stdout(output):
        # writes directly to stdout, so catch it ...
        c.check_all()
    output = output.getvalue()

    stdout.write("{0:>10}".format(len(output)))
    stdout.write(output)
    stdout.flush()
