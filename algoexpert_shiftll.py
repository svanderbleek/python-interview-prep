import dataclasses
import typing

@dataclasses.dataclass
class LV:
  v: int
  n: typing.Optional['LV']

def shift_ll(h,k):
  if h.n == None:
    return h
    
  if k < 0:
    for _ in range(abs(k)):
      h = shift_bw(h)
  else:
    for _ in range(abs(k)):
      h = shift_fw(h)
  return h

def shift_fw(h):
  p = c = h
  while(c.n):
    p = c
    c = c.n
  p.n = None
  c.n = h
  return c

def shift_bw(h):
  t = h.n
  h.n = None
  c = t
  while(c.n):
    c = c.n
  c.n = h
  return t

print(shift_ll(LV(v=1,n=LV(v=2,n=LV(v=3,n=None))),6))
