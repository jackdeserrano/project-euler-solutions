from defs import *

def s(z):
    if z < 2: return False
    q, s = [i for i in str(z)], 0
    for k in q:
        s += int(k)**5
    if s == z: return True
    return False

l = []
for k in range (1000000):
    if s(k) == True:
        l.append(k)
        

print(sum(l), l)
