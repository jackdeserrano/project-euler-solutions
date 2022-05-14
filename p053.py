from defs import *

s = 0
for k in range(2, 101):
    for z in range(1, k + 1):
        if sp.comb(k, z) > 1000000:
            s += 1
print(s)
