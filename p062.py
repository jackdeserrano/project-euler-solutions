from defs import *

def cp(x):
    l = []
    for k in range(1, x):
        c = pow(k, 3)
        l.append(c)
    return set(l)
 
s = time()
l = cp(10000)

for k in l:
    c, w = sorted(list(str(k))), []
    for z in l:
        p = sorted(list(str(z)))
        if p == c:
            w.append(z)
    if len(w) == 5:
        print(sorted(w)[0], time()-s)
        break
    else: continue
 
