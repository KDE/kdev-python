# AUTO-GENERATED FILE -- DO NOT EDIT

""" Conversion between binary data and ASCII """

class Error(Exception):

  pass

class Incomplete(Exception):

  pass

__package__ = None

def a2b_base64(ascii):
  """ (ascii) -> bin. Decode a line of base64 data """
  return None

def a2b_hex(hexstr):
  """ a2b_hex(hexstr) -> s; Binary data of hexadecimal representation.
  
  hexstr must contain an even number of hex digits (upper or lower case).
  This function is also available as "unhexlify()" """
  return None

def a2b_hqx(ascii):
  """ ascii -> bin, done. Decode .hqx coding """
  return None

def a2b_qp():
  """ Decode a string of qp-encoded data """
  pass

def a2b_uu(ascii):
  """ (ascii) -> bin. Decode a line of uuencoded data """
  return None

def b2a_base64(bin):
  """ (bin) -> ascii. Base64-code line of data """
  return None

def b2a_hex(data):
  """ b2a_hex(data) -> s; Hexadecimal representation of binary data.
  
  This function is also available as "hexlify()". """
  return None

def b2a_hqx():
  """ Encode .hqx data """
  pass

def b2a_qp(data, quotetabs=0, istext=1, header=0):
  """ b2a_qp(data, quotetabs=0, istext=1, header=0) -> s; 
   Encode a string using quoted-printable encoding. 
  
  On encoding, when istext is set, newlines are not encoded, and white 
  space at end of lines is.  When istext is not set, \\r and \\n (CR/LF) are 
  both encoded.  When quotetabs is set, space and tabs are encoded. """
  return None

def b2a_uu(bin):
  """ (bin) -> ascii. Uuencode line of data """
  return None

def crc32(data, arg0=None):
  """ (data, oldcrc = 0) -> newcrc. Compute CRC-32 incrementally """
  return None

def crc_hqx(data, oldcrc):
  """ (data, oldcrc) -> newcrc. Compute hqx CRC incrementally """
  return None

def hexlify(data):
  """ b2a_hex(data) -> s; Hexadecimal representation of binary data.
  
  This function is also available as "hexlify()". """
  return None

def rlecode_hqx():
  """ Binhex RLE-code binary data """
  pass

def rledecode_hqx():
  """ Decode hexbin RLE-coded string """
  pass

def unhexlify(hexstr):
  """ a2b_hex(hexstr) -> s; Binary data of hexadecimal representation.
  
  hexstr must contain an even number of hex digits (upper or lower case).
  This function is also available as "unhexlify()" """
  return None

