#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: General floating point formatting functions.
:deprecated:

"""
def fix(x,digs):
	"""
	Format *x* as ``[-]ddd.ddd`` with *digs* digits after the point and at least one
	digit before. If ``digs <= 0``, the decimal point is suppressed.
	
	*x* can be either a number or a string that looks like one. *digs* is an
	integer.
	
	Return value is a string.
	
	
	"""
	pass
	
def sci(x,digs):
	"""
	Format *x* as ``[-]d.dddE[+-]ddd`` with *digs* digits after the  point and
	exactly one digit before. If ``digs <= 0``, one digit is kept and the point is
	suppressed.
	
	*x* can be either a real number, or a string that looks like one. *digs* is an
	integer.
	
	Return value is a string.
	
	
	"""
	pass
	
