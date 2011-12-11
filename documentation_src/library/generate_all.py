#!/usr/bin/env python2.7

import subprocess

# Generate doc files for these modules.
modules = [
    'random',
    'subprocess',
    'array',
    'audioop',
    'binascii',
    'bz2',
    'cmath',
    'cPickle',
    'crypt',
    'cStringIO',
    'datetime',
    'dbm',
    'fcntl',
    'gdbm',
    'grp',
    'itertools',
    'linuxaudiodev',
    'math',
    'mmap',
    'nis',
    'operator',
    'ossaudiodev',
    'parser',
    'pyexpat',
    'readline',
    'resource',
    'select',
    'spwd',
    'strop',
    'syslog',
    'termios',
    'time',
    'unicodedata',
    'zlib'
]

target_path = '../../documentation_files/'

def generate_all():
    import os
    for module in modules:
        target_file = target_path + module.replace('.', '/') + ".py"
        print "Processing", module, "->", target_file, "...",
        result = subprocess.call(["/usr/bin/env", "python", "generate_pi.py", module, target_file])
        print "ok" if not result else "fail!"
    

if __name__ == '__main__':
    generate_all()