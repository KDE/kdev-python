#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":platform: IRIX
:synopsis: Support for SGI imglib files.
:deprecated:

"""
def getsizes(file):
	"""
	This function returns a tuple ``(x, y, z)`` where *x* and *y* are the size of
	the image in pixels and *z* is the number of bytes per pixel. Only 3 byte RGB
	pixels and 1 byte greyscale pixels are currently supported.
	
	
	"""
	pass
	
def read(file):
	"""
	This function reads and decodes the image on the specified file, and returns it
	as a Python string. The string has either 1 byte greyscale pixels or 4 byte RGBA
	pixels. The bottom left pixel is the first in the string. This format is
	suitable to pass to :func:`gl.lrectwrite`, for instance.
	
	
	"""
	pass
	
def readscaled(file,x,y,filter,blur):
	"""
	This function is identical to read but it returns an image that is scaled to the
	given *x* and *y* sizes. If the *filter* and *blur* parameters are omitted
	scaling is done by simply dropping or duplicating pixels, so the result will be
	less than perfect, especially for computer-generated images.
	
	Alternatively, you can specify a filter to use to smooth the image after
	scaling. The filter forms supported are ``'impulse'``, ``'box'``,
	``'triangle'``, ``'quadratic'`` and ``'gaussian'``. If a filter is specified
	*blur* is an optional parameter specifying the blurriness of the filter. It
	defaults to ``1.0``.
	
	:func:`readscaled` makes no attempt to keep the aspect ratio correct, so that is
	the users' responsibility.
	
	
	"""
	pass
	
def ttob(flag):
	"""
	This function sets a global flag which defines whether the scan lines of the
	image are read or written from bottom to top (flag is zero, compatible with SGI
	GL) or from top to bottom(flag is one, compatible with X).  The default is zero.
	
	
	"""
	pass
	
