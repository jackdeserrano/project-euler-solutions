from defs import *

JOSH = time()
for k in range(1000000):
    if prime(k) == True:
        p = str(k)
        u = []
        for z in range(10):
            if p.count(str(z)) > 1:
                u.append(str(z))
        if u == []:
            continue
        for m in u:
            l = []
            for b in range(10):
                p = str(k)
                p = p.replace(m, str(b))
                if p[0] != '0' and prime(int(p)) == True:
                    l.append(int(p))
            if len(l) == 8:
                u = 0
                break
        if u == 0:
            break

print(l[0], time() - JOSH)
