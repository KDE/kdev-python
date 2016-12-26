#!/usr/bin/env python

from contextlib import redirect_stdout
from io import StringIO
from sys import stdin, stdout, stderr
import sys
try:
    from pycodestyle import Checker, StyleGuide
except ImportError:
    Checker = None

while True:
    size = stdin.read(10)
    size = int(size)
    if not size > 0:
        continue
    buf = str()
    while len(buf) < size:
        buf += stdin.read(size-len(buf))
    lines = buf.splitlines()
    opts, text = lines[:3], [l + "\n" for l in lines[3:]]

    if Checker is not None:
        style_guide = StyleGuide()
        options = style_guide.options
        options.select = tuple(opts[0].strip().split(','))
        options.ignore = tuple(opts[1].strip().split(','))
        options.max_line_length = int(opts[2])
        c = Checker(lines=text, options=options)
        output = StringIO()
        with redirect_stdout(output):
            # writes directly to stdout, so catch it ...
            c.check_all()
        output = output.getvalue()

        stdout.write("{0:>10}".format(len(output)))
        stdout.write(output)
        stdout.flush()
    else:
        stderr.write("The `pycodestyle` module is not installed.")
        stderr.flush()
