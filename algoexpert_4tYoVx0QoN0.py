import rich
import copy

# return matrix with 1 if connected to border
def remove_islands(m):
  r=len(m) # row
  c=len(m[0]) # col
  k=[[0 for j in range(c)] for i in range(r)] # keep
  for j in range(c):
    if m[0][j] == 1:
      mark(0,j,m,k,r,c)
    if m[r-1][j] == 1:
      mark(r-1,j,m,k,r,c)
  for i in range(r):
    if m[i][0] == 1:
      mark(i,0,m,k,r,c)
    if m[i][c-1] == 1:
      mark(i,c-1,m,k,r,c)
  return k

def mark(i,j,m,k,r,c):
  m[i][j]=0
  k[i][j]=1
  for (x,y) in ns(i,j):
    if inm(x,y,r,c) and m[x][y]:
      mark(x,y,m,k,r,c) 

def ns(i,j):
  return [(i+x,j+y) for (x,y) in [(-1,0),(0,-1),(1,0),(0,1)]]

def inm(i,j,r,c):
  return (i >= 0) and (j >= 0) and (i < r) and (j < c)

rich.print(ns(1,1))
  
m1 = [
  [1,0,0,0,0,0],
  [0,1,0,1,1,1],
  [0,0,1,0,1,0],
  [1,1,0,0,1,0],
  [1,0,1,1,0,0],
  [1,0,0,0,0,1],
]
o1 = [
  [1,0,0,0,0,0],
  [0,0,0,1,1,1],
  [0,0,0,0,1,0],
  [1,1,0,0,1,0],
  [1,0,0,0,0,0],
  [1,0,0,0,0,1],
]

a1=remove_islands(copy.deepcopy(m1))
rich.print(m1)
rich.print(o1)
rich.print(a1)
