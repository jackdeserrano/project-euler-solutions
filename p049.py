from defs import *

st = time()
l = []
for k in range(1001, 10000, 2):
    c, p = 0, []
    if prime(k) == True:
        for z in perm_num(k):
            if prime(z) == True and len(str(int(z))) == 4 and z not in p:
                p.append(z)
                c += 1
            if c == 3:
                l.append(p)
                break

s = []
for k in l:
    if k[2] - k[1] == k[1] - k[0]:
        s.append(k[0])
        s.append(k[1])
        s.append(k[2])

y = ''
s.sort()
for k in s:
    y += str(k)

print(y, time()-st)
