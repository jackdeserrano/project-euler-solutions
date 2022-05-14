import time as t

def d(z):
    s = 0
    for k in range(1, z//2+1):
        if z % k == 0:
            s += k
    return s

s = t.time()
n = []
for b in range(10000):
    if b == d(d(b)) and b != d(b):
        n.append(b)
        
print(sum(n), t.time()-s)
