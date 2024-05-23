#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
  i = 0
  n = 0

  while i < len(data):
    b = data[i] & 255
    
    if n == 0:
      if b & 128 == 0: 
        i += 1
        continue
      elif b & 192 == 192:  
        n = 1  
      elif b & 224 == 224:    
        n = 2
      elif b & 240 == 240:    
        n = 3
      else:
        return False
      
    else:      
      if b & 192 != 128:
        return False
      n -= 1
      
    i += 1

  return n == 0
