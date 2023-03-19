# adaptation of https://github.com/mkirchner/linked-list-good-taste

import dataclasses
import typing
 
@dataclasses.dataclass
class LV: # list value
  key: int
  nxt: 'LR'
  
@dataclasses.dataclass
class LR: # list reference
  val: typing.Optional['LV']

@dataclasses.dataclass
class LL:
  hed: LR

def ll_rem(ll, k): # simulate references
  cr = ll.hed
  while cr.val and cr.val.key != k:
    cr = cr.val.nxt
  if cr.val:
    cr.val = cr.val.nxt.val

l1 = LL(hed=LR(val=None))
print(l1)
ll_rem(l1,1)
print(l1)

l2 = LL(hed=LR(val=LV(key=1,nxt=LR(val=None))))
print(l2)
ll_rem(l2,1)
print(l2)

l3 = LL(hed=LR(val=LV(key=1,nxt=LR(val=LV(key=2,nxt=LR(val=LV(key=3,nxt=LR(val=None))))))))
print(l3)
ll_rem(l3,2)
print(l3)

l4 = LL(hed=LR(val=LV(key=1,nxt=LR(val=LV(key=2,nxt=LR(val=LV(key=3,nxt=LR(val=None))))))))
print(l4)
ll_rem(l4,1)
print(l4)

l5 = LL(hed=LR(val=LV(key=1,nxt=LR(val=LV(key=2,nxt=LR(val=LV(key=3,nxt=LR(val=None))))))))
print(l5)
ll_rem(l5,3)
print(l5)
