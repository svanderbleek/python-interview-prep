def multiset_permutations(ms):
  s=len(ms)
  ps=[]
  def r(p,i,cs):
    if i < s:
      for c in cs:
        if cs[c] > 0:
          p[i] = c
          cs[c] -= 1
          r(p,i+1,cs)
          cs[c] += 1
    else:
      ps.append(p.copy())
  r([None]*s,0,count(ms))
  return ps

def count(ms):
  c={}
  for m in ms:
    if m in c:
      c[m] += 1
    else:
      c[m] = 1
  return c

ms = [1,1,1,2,2]
print(count(ms))
print(multiset_permutations(ms))
