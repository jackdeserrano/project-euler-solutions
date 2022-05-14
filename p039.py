from defs import *

def p(x, y):
    if sqrt(x**2 + y**2).is_integer():
        return sqrt(x**2 + y**2) + x + y
    return False

l = []
for k in range(3, 1000):
    for z in range(3, 333):
        if p(k, z) != False and (sqrt(k**2 + z**2) + k + z) <= 1000:
            if (z,k) not in l: l.append((k,z))

for k in range(len(l)):
    l[k] = sqrt(l[k][0]**2 + l[k][1]**2) + l[k][0] + l[k][1]

print(max(set(l), key = l.count))
