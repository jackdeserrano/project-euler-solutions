from defs import *

r, s, c, p, l = 0, [1], 1, 0, []

while True: 
    if p % 4 == 0:
        r += 2
    p += 1
    c += r
    s.append(c)
    if prime(c) == True: l.append(c)
    if len(l) / len(s) < .1: break

print(math.sqrt(c))
    
