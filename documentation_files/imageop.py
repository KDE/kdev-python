#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Manipulate raw image data.
:deprecated:

"""
def crop(image,psize,width,height,x0,y0,x1,y1):
	"""
	Return the selected part of *image*, which should be *width* by *height* in size
	and consist of pixels of *psize* bytes. *x0*, *y0*, *x1* and *y1* are like the
	:func:`gl.lrectread` parameters, i.e. the boundary is included in the new image.
	The new boundaries need not be inside the picture.  Pixels that fall outside the
	old image will have their value set to zero.  If *x0* is bigger than *x1* the
	new image is mirrored.  The same holds for the y coordinates.
	
	
	"""
	pass
	
def scale(image,psize,width,height,newwidth,newheight):
	"""
	Return *image* scaled to size *newwidth* by *newheight*. No interpolation is
	done, scaling is done by simple-minded pixel duplication or removal.  Therefore,
	computer-generated images or dithered images will not look nice after scaling.
	
	
	"""
	pass
	
def tovideo(image,psize,width,height):
	"""
	Run a vertical low-pass filter over an image.  It does so by computing each
	destination pixel as the average of two vertically-aligned source pixels.  The
	main use of this routine is to forestall excessive flicker if the image is
	displayed on a video device that uses interlacing, hence the name.
	
	
	"""
	pass
	
def grey2mono(image,width,height,threshold):
	"""
	Convert a 8-bit deep greyscale image to a 1-bit deep image by thresholding all
	the pixels.  The resulting image is tightly packed and is probably only useful
	as an argument to :func:`mono2grey`.
	
	
	"""
	pass
	
def dither2mono(image,width,height):
	"""
	Convert an 8-bit greyscale image to a 1-bit monochrome image using a
	(simple-minded) dithering algorithm.
	
	
	"""
	pass
	
def mono2grey(image,width,height,p0,p1):
	"""
	Convert a 1-bit monochrome image to an 8 bit greyscale or color image. All
	pixels that are zero-valued on input get value *p0* on output and all one-value
	input pixels get value *p1* on output.  To convert a monochrome black-and-white
	image to greyscale pass the values ``0`` and ``255`` respectively.
	
	
	"""
	pass
	
def grey2grey4(image,width,height):
	"""
	Convert an 8-bit greyscale image to a 4-bit greyscale image without dithering.
	
	
	"""
	pass
	
def grey2grey2(image,width,height):
	"""
	Convert an 8-bit greyscale image to a 2-bit greyscale image without dithering.
	
	
	"""
	pass
	
def dither2grey2(image,width,height):
	"""
	Convert an 8-bit greyscale image to a 2-bit greyscale image with dithering.  As
	for :func:`dither2mono`, the dithering algorithm is currently very simple.
	
	
	"""
	pass
	
def grey42grey(image,width,height):
	"""
	Convert a 4-bit greyscale image to an 8-bit greyscale image.
	
	
	"""
	pass
	
def grey22grey(image,width,height):
	"""
	Convert a 2-bit greyscale image to an 8-bit greyscale image.
	
	
	"""
	pass
	
