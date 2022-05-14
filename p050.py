from defs import *

s, l, c = 0, [], 0
while s < 1000000:
    c += 1
    if prime(c) == True:
        l.append(s)
        s += c

for k in l:
    p = l[len(l)-1]
    p -= k
    if prime(p) == True: break
    
print(p)
