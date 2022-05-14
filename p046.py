from defs import *

for k in range(3, 1000000, 2):
    r = 0
    if prime(k) == True: continue
    for z in range(200):
        r = 0
        if prime(k - (2*z**2)) == True: break
        else: r = 1
    if r == 1:
        o = k
        break

print(o)






