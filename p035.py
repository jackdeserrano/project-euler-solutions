from defs import *

def rotate(z):
    if prime(z) == False: return False
    q, l = [], [k for k in str(z)]
    for k in range(len(str(z))):
        l.append(l[0])
        l.remove(l[0])
        p = ''.join(l)
        q.append(int(p))
    for j in q:
        if prime(j) == False: return False
    return True

l = [2]
for k in range(3, 1000000, 2):
    if rotate(k) == True: l.append(k)
print(len(l))
    
