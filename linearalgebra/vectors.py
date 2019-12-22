"""
from scratch vector ops -- after these, learn to use numpy
"""

from math import sqrt

def main():
  v = [1,2,3]
  w = [4,5,6]
  q = [4,5,6,7,8]
  x = vector_add(v,w)
  assert(x[0]==5)
  assert(x[1]==7)
  assert(x[2]==9)
  x = vector_add(v,q)
  assert(x==None)
  #
  x = vector_subtract(v,w)
  assert(x[0]==-3)
  assert(x[1]==-3)
  assert(x[2]==-3)
  #
  vectors = [v,v,v,v]
  x = vector_sum(vectors)
  for i in range(len(x)):
    assert(x[i]==4*v[i])
  #
  s = 6
  x = scalar_multiply(s,v)
  for i in range(len(x)):
    assert(x[i]==s*v[i])
  #
  vectors = [v,v,v,v,v,v]
  x = vector_mean(vectors)
  for i in range(len(x)):
    assert(x[i]==v[i])
  #
  x = dot(v,w)
  assert(x==(4+10+18))
  #
  x = sum_of_squares(v)
  assert(x==(1+4+9))
  #
  assert(magnitude(v)==sqrt(14))
  assert(magnitude(w)==sqrt(16+25+36))
  #
  v = [3,0]
  w = [3,3]
  assert(distance(v,w)==3)
  assert(distance(w,v)==3)
  v = [3,0]
  w = [0,3]
  assert(distance(v,w)==sqrt(18))
  assert(distance(w,v)==sqrt(18))

def vector_add(v,w):
  """add the corresponding elements"""
  # check to make sure allowed???
  if len(v) == len(w):
    return [vi+wi for vi,wi in zip(v,w)]
  else:
    return None

def vector_subtract(v,w):
  """subtract the corresponding elements"""
  # check to make sure allowed???
  if len(v) == len(w):
    return [vi-wi for vi,wi in zip(v,w)]
  else:
    return None

def vector_sum(vectors):
  """add the corresponding elements of all vectors in list"""
  result = vectors[0]
  for i in range(1,len(vectors)):
    result = vector_add(result, vectors[i])
  return result
  # or reduce(vector_add, vectors) ??

def scalar_multiply(s, v):
  """s is a scalar multiply number, v is a vector"""
  return [s*item for item in v]

def vector_mean(vectors):
  """
  compute the vector whose ith element is the mean of
  the ith elements of the input vectors???
  """
  n = len(vectors)
  return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
  """return dot product of two vectors"""
  return sum(vi*wi for vi,wi in zip(v,w))

def sum_of_squares(v):
  """sum of vector's components all squared"""
  return dot(v,v)

def magnitude(v):
  """return magnitude of vector"""
  return sqrt(sum_of_squares(v))

def distance(v,w):
  """distance between two vectors"""
  return magnitude(vector_subtract(v,w))

main()
