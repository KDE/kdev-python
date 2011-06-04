#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: Unix
:synopsis: The most common POSIX system calls (normally used via module os).


This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly disguised Unix
interface).

"""
"""
A dictionary representing the string environment at the time the interpreter
was started.  For example, ``environ['HOME']`` is the pathname of your home
directory, equivalent to ``getenv("HOME")`` in C.

Modifying this dictionary does not affect the string environment passed on by
:func:`execv`, :func:`popen` or :func:`system`; if you need to change the
environment, pass ``environ`` to :func:`execve` or add variable assignments and
export statements to the command string for :func:`system` or :func:`popen`.

"""
environ = None
