# connected components solution

def river_sizes(m):
  sn = {} # seen
  rs = [] # rivers
  h = len(m)
  w = len(m[0])
  for i, js in enumerate(m):
    for j, v in enumerate(js):
      if v == 1 and not (i,j) in sn:
        rs.append(visit(m,sn,i,j,h,w))
  return [len(r) for r in rs]

def visit(m,sn,i,j,h,w):
  sn[(i,j)] = True
  print(sn)
  r = [()]
  for (ni,nj) in ns(i,j,h,w):
    if m[ni][nj] == 1 and not (ni,nj) in sn:
      r += visit(m,sn,ni,nj,h,w)
  return r

def ns(i,j,h,w):
  ps = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
  return [p for p in ps if inside(p,h,w)]

def inside(p,h,w):
  (x,y)=p
  return 0 <= x < h and 0 <= y < w

m = [
  [0,1,1],
  [0,1,0],
  [1,1,0]
]
print(river_sizes(m))
