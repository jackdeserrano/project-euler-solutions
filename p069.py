from defs import *

w = time()
p, r = 2, 1

while True:
    if p > 1000000:
        print(p//r, time()-w)
        break
    r += 2
    if prime(r): p *= r
    

