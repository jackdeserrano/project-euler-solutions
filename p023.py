def a(z):
    if z == 2: return False
    s = 0
    for k in range(1, z//2+1):
        if z % k == 0:
            s += k
    if s > z: return True
    return False

l = []
for k in range(1, 28123):
    if a(k) == True: l.append(k)
p = []
for k in range(24, 28123):
    for z in l:
        if z > k: break
        if k - z in l:
             p.append(k)
             break
c = []
for k in range(28123):
    if k not in p: c.append(k)
    
print(sum(c))
print(c) 
