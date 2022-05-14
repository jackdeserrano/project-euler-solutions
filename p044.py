from defs import *

pt = []
for k in range(1, 10000):
    pt.append((3*k**2-k)/2)

D = inf
for j in range(len(pt)):
    for k in range(j):
        if pt[j] + pt[k] in pt and pt[j] - pt[k] in pt and abs(pt[j] - pt[k]) < D:
            D = abs(pt[j] - pt[k])
            print(D)
            
            

