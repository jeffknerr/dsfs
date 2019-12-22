"""
simple matrix ops
"""

def main():
  A = [[1,2,3],
      [4,5,6]]
  B = [[1,2],
      [3,4],
      [5,6]]
  C = []
  assert(shape(A)==(2,3))
  assert(shape(B)==(3,2))
  assert(shape(C)==(0,0))
  assert(get_row(A,0)==[1,2,3])
  assert(get_row(A,1)==[4,5,6])
  assert(get_col(A,0)==[1,4])
  assert(get_col(A,1)==[2,5])
  assert(get_col(A,2)==[3,6])
  N = 8
  NEW = make_matrix(N,N,is_diagonal)
  for r in range(N):
    for c in range(N):
      if r == c:
        assert(NEW[r][c] == 1)
      else:
        assert(NEW[r][c] == 0)

def shape(M):
  """return rows,cols of matrix"""
  rows = len(M)
  if len(M) > 0:
    cols = len(M[0]) 
  else:
    cols = 0
  return rows,cols

def get_row(M,i):
  """get ith row"""
  return M[i]

def get_col(M,j):
  """get jth col"""
  return [row[j] for row in M]

def is_diagonal(r,c):
  """return 1s on the diag, 0s elsewhere"""
  return 1 if r==c else 0

def make_matrix(nrow,ncol,func):
  """make/return nr x nc matrix, using given func(r,c)"""
  return [[func(r,c) for c in range(ncol)] for r in range(nrow)]

main()
