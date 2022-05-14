from defs import *

l = []

for k in range(2, 101):
    for z in range(2, 101):
        if k**z not in l:
            l.append(k**z)

print(len(l))
