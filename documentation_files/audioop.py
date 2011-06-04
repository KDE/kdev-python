#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Manipulate raw audio data.


The :mod:`audioop` module contains some useful operations on sound fragments.
It operates on sound fragments consisting of signed integer samples 8, 16 or 32
bits wide, stored in Python strings.  This is the same format as used by the
:mod:`al` and :mod:`sunaudiodev` modules.  All scalar items are integers, unless
specified otherwise.

"""
def add(fragment1,fragment2,width):
	"""
	Return a fragment which is the addition of the two samples passed as parameters.
	*width* is the sample width in bytes, either ``1``, ``2`` or ``4``.  Both
	fragments should have the same length.
	
	
	"""
	pass
	
def adpcm2lin(adpcmfragment,width,state):
	"""
	Decode an Intel/DVI ADPCM coded fragment to a linear fragment.  See the
	description of :func:`lin2adpcm` for details on ADPCM coding. Return a tuple
	``(sample, newstate)`` where the sample has the width specified in *width*.
	
	
	"""
	pass
	
def alaw2lin(fragment,width):
	"""
	Convert sound fragments in a-LAW encoding to linearly encoded sound fragments.
	a-LAW encoding always uses 8 bits samples, so *width* refers only to the sample
	width of the output fragment here.
	
	"""
	pass
	
def avg(fragment,width):
	"""
	Return the average over all samples in the fragment.
	
	
	"""
	pass
	
def avgpp(fragment,width):
	"""
	Return the average peak-peak value over all samples in the fragment. No
	filtering is done, so the usefulness of this routine is questionable.
	
	
	"""
	pass
	
def bias(fragment,width,bias):
	"""
	Return a fragment that is the original fragment with a bias added to each
	sample.
	
	
	"""
	pass
	
def cross(fragment,width):
	"""
	Return the number of zero crossings in the fragment passed as an argument.
	
	
	"""
	pass
	
def findfactor(fragment,reference):
	"""
	Return a factor *F* such that ``rms(add(fragment, mul(reference, -F)))`` is
	minimal, i.e., return the factor with which you should multiply *reference* to
	make it match as well as possible to *fragment*.  The fragments should both
	contain 2-byte samples.
	
	The time taken by this routine is proportional to ``len(fragment)``.
	
	
	"""
	pass
	
def findfit(fragment,reference):
	"""
	Try to match *reference* as well as possible to a portion of *fragment* (which
	should be the longer fragment).  This is (conceptually) done by taking slices
	out of *fragment*, using :func:`findfactor` to compute the best match, and
	minimizing the result.  The fragments should both contain 2-byte samples.
	Return a tuple ``(offset, factor)`` where *offset* is the (integer) offset into
	*fragment* where the optimal match started and *factor* is the (floating-point)
	factor as per :func:`findfactor`.
	
	
	"""
	pass
	
def findmax(fragment,length):
	"""
	Search *fragment* for a slice of length *length* samples (not bytes!) with
	maximum energy, i.e., return *i* for which ``rms(fragment[i*2:(i+length)*2])``
	is maximal.  The fragments should both contain 2-byte samples.
	
	The routine takes time proportional to ``len(fragment)``.
	
	
	"""
	pass
	
def getsample(fragment,width,index):
	"""
	Return the value of sample *index* from the fragment.
	
	
	"""
	pass
	
def lin2adpcm(fragment,width,state):
	"""
	Convert samples to 4 bit Intel/DVI ADPCM encoding.  ADPCM coding is an adaptive
	coding scheme, whereby each 4 bit number is the difference between one sample
	and the next, divided by a (varying) step.  The Intel/DVI ADPCM algorithm has
	been selected for use by the IMA, so it may well become a standard.
	
	*state* is a tuple containing the state of the coder.  The coder returns a tuple
	``(adpcmfrag, newstate)``, and the *newstate* should be passed to the next call
	of :func:`lin2adpcm`.  In the initial call, ``None`` can be passed as the state.
	*adpcmfrag* is the ADPCM coded fragment packed 2 4-bit values per byte.
	
	
	"""
	pass
	
def lin2alaw(fragment,width):
	"""
	Convert samples in the audio fragment to a-LAW encoding and return this as a
	Python string.  a-LAW is an audio encoding format whereby you get a dynamic
	range of about 13 bits using only 8 bit samples.  It is used by the Sun audio
	hardware, among others.
	
	"""
	pass
	
def lin2lin(fragment,width,newwidth):
	"""
	Convert samples between 1-, 2- and 4-byte formats.
	
	"""
	pass
	
def lin2ulaw(fragment,width):
	"""
	Convert samples in the audio fragment to u-LAW encoding and return this as a
	Python string.  u-LAW is an audio encoding format whereby you get a dynamic
	range of about 14 bits using only 8 bit samples.  It is used by the Sun audio
	hardware, among others.
	
	
	"""
	pass
	
def minmax(fragment,width):
	"""
	Return a tuple consisting of the minimum and maximum values of all samples in
	the sound fragment.
	
	
	"""
	pass
	
def max(fragment,width):
	"""
	Return the maximum of the *absolute value* of all samples in a fragment.
	
	
	"""
	pass
	
def maxpp(fragment,width):
	"""
	Return the maximum peak-peak value in the sound fragment.
	
	
	"""
	pass
	
def mul(fragment,width,factor):
	"""
	Return a fragment that has all samples in the original fragment multiplied by
	the floating-point value *factor*.  Overflow is silently ignored.
	
	
	"""
	pass
	
def ratecv(fragment,width,nchannels,inrate,outrate,state,weightA,weightB):
	"""
	Convert the frame rate of the input fragment.
	
	*state* is a tuple containing the state of the converter.  The converter returns
	a tuple ``(newfragment, newstate)``, and *newstate* should be passed to the next
	call of :func:`ratecv`.  The initial call should pass ``None`` as the state.
	
	The *weightA* and *weightB* arguments are parameters for a simple digital filter
	and default to ``1`` and ``0`` respectively.
	
	
	"""
	pass
	
def reverse(fragment,width):
	"""
	Reverse the samples in a fragment and returns the modified fragment.
	
	
	"""
	pass
	
def rms(fragment,width):
	"""
	Return the root-mean-square of the fragment, i.e. ``sqrt(sum(S_i^2)/n)``.
	
	This is a measure of the power in an audio signal.
	
	
	"""
	pass
	
def tomono(fragment,width,lfactor,rfactor):
	"""
	Convert a stereo fragment to a mono fragment.  The left channel is multiplied by
	*lfactor* and the right channel by *rfactor* before adding the two channels to
	give a mono signal.
	
	
	"""
	pass
	
def tostereo(fragment,width,lfactor,rfactor):
	"""
	Generate a stereo fragment from a mono fragment.  Each pair of samples in the
	stereo fragment are computed from the mono sample, whereby left channel samples
	are multiplied by *lfactor* and right channel samples by *rfactor*.
	
	
	"""
	pass
	
