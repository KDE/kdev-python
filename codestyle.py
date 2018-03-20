#!/usr/bin/env python3

from contextlib import redirect_stdout
from io import StringIO
from sys import stdin, stdout, stderr
import sys
try:
    from pycodestyle import Checker, StyleGuide
except ImportError:
    try:
        from pep8 import Checker, StyleGuide
    except ImportError:
        Checker = None

while True:
    size = stdin.buffer.read(10)
    size = int(size)
    if not size > 0:
        continue
    buf = bytes()
    while len(buf) < size:
        buf += stdin.buffer.read(min(1024, size - len(buf)))
    lines = buf.decode("utf-8").splitlines()
    opts, text = lines[:3], [l + "\n" for l in lines[3:]]

    if Checker is not None:
        style_guide = StyleGuide()
        options = style_guide.options
        select = [x for x in opts[0].strip().split(',') if len(x) > 0]
        ignore = [x for x in opts[1].strip().split(',') if len(x) > 0]
        options.select = tuple(select)
        options.ignore = tuple(ignore)
        options.max_line_length = int(opts[2])
        stderr.flush()
        c = Checker(lines=text, options=options)
        output = StringIO()
        with redirect_stdout(output):
            # writes directly to stdout, so catch it ...
            c.check_all()
        output = output.getvalue()
        output = output[:2**15]

        stdout.write("{0:>10}".format(len(output)))
        stdout.write(output)
        stdout.flush()
    else:
        stderr.write("The `pycodestyle` (previously `pep8`) module is not installed.")
        stderr.flush()
        stdout.write("{0:>10}".format(0))
        stdout.flush()
