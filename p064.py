from defs import *

def c(n):
    m = p = 0
    s = math.sqrt(n)
    a = int(s)
    d = 1
    if a == s: return False
    s = a
    while s != 2 * a:
        m = d * s - m
        d = (n - m**2) / d
        s = int((a + m) / d)
        p += 1
    return p % 2 == 1

w = time()
r = 0
for k in range(10000):
    if c(k): r += 1
    
print(r, time()-w)
