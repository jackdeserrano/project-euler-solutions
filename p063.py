from defs import *

s = 0
for k in range(1, 1000):
    for z in range(1, 100):
        if len(str(k**z)) == z:
            s += 1
print(s)
