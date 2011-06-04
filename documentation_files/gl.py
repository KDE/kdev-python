#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: Functions from the Silicon Graphics Graphics Library.
:deprecated:


"""
def varray(argument):
	"""
	Equivalent to but faster than a number of ``v3d()`` calls. The *argument* is a
	list (or tuple) of points. Each point must be a tuple of coordinates ``(x, y,
	z)`` or ``(x, y)``. The points may be 2- or 3-dimensional but must all have the
	same dimension. Float and int values may be mixed however. The points are always
	converted to 3D double precision points by assuming ``z = 0.0`` if necessary (as
	indicated in the man page), and for each point ``v3d()`` is called.
	
	.. rgument-argument added
	
	
	"""
	pass
	
def nvarray():
	"""
	Equivalent to but faster than a number of ``n3f`` and ``v3f`` calls. The
	argument is an array (list or tuple) of pairs of normals and points. Each pair
	is a tuple of a point and a normal for that point. Each point or normal must be
	a tuple of coordinates ``(x, y, z)``. Three coordinates must be given. Float and
	int values may be mixed. For each pair, ``n3f()`` is called for the normal, and
	then ``v3f()`` is called for the point.
	
	
	"""
	pass
	
def vnarray():
	"""
	Similar to  ``nvarray()`` but the pairs have the point first and the normal
	second.
	
	
	"""
	pass
	
def nurbssurface(s_k,t_k,ctl,s_ord,t_ord,type):
	"""
	Defines a nurbs surface. The dimensions of ``ctl[][]`` are computed as follows:
	``[len(s_k) - s_ord]``, ``[len(t_k) - t_ord]``.
	
	.. _k[], ctl[][]
	
	
	"""
	pass
	
def nurbscurve(knots,ctlpoints,order,type):
	"""
	Defines a nurbs curve. The length of ctlpoints is ``len(knots) - order``.
	
	
	"""
	pass
	
def pwlcurve(points,type):
	"""
	Defines a piecewise-linear curve. *points* is a list of points. *type* must be
	``N_ST``.
	
	
	"""
	pass
	
def pick(n):
	"""select(n)
	
	The only argument to these functions specifies the desired size of the pick or
	select buffer.
	
	
	"""
	pass
	
def endpick():
	"""endselect()
	
	These functions have no arguments. They return a list of integers representing
	the used part of the pick/select buffer. No method is provided to detect buffer
	overrun.
	
	Here is a tiny but complete example GL program in Python::
	
	import gl, GL, time
	
	def main():
	gl.foreground()
	gl.prefposition(500, 900, 500, 900)
	w = gl.winopen('CrissCross')
	gl.ortho2(0.0, 400.0, 0.0, 400.0)
	gl.color(GL.WHITE)
	gl.clear()
	gl.color(GL.RED)
	gl.bgnline()
	gl.v2f(0.0, 0.0)
	gl.v2f(400.0, 400.0)
	gl.endline()
	gl.bgnline()
	gl.v2f(400.0, 0.0)
	gl.v2f(0.0, 400.0)
	gl.endline()
	time.sleep(5)
	
	main()
	
	
	"""
	pass
	
