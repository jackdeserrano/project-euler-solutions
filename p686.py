from time import time
from math import log10
"""
The trick is to lose as much precision as you can afford. For 686, subscripting
to [:15] was enough. Depending on the scale this number will change.
"""

def p(L, n, h=1, c=0, r=0):
    """ L of type str """
    while r < n:
        h = str(h*2)[:15]
        c += 1
        if h[:3] == L: r += 1
        h = int(h)
    return c
w=time()
print(p('123', 678910),time()-w)

#139 s
