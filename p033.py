from defs import *

# many things probably unnecessary
def f(n, d):
    if n / d == 1: return False
    x = [k for k in str(n)]
    y = [k for k in str(d)]
    if x[0] not in y and x[1] not in y: return False
    if x[1] == '0' and y[1] == '0': return False
    if x[0] == y[0] or x[1] == y[1]: return False
    if x[0] in y and y[1] != '0':
        y.remove(x[0])
        x.remove(x[0])
    elif x[1] in y and y[1] != '0' :
        y.remove(x[1])
        x.remove(x[1])
    if n / d == int(x[0]) / int(y[0]): return (n, d)
    return False

s = time()
l = []
for k in range(10, 100):
    for z in range(10, 100):
        if f(k,z) != False:
            if f(z,k) not in l:
                l.append(f(k,z))

n, d = 1, 1
for k in range(4):
    n *= l[k][0]
    d *= l[k][1]

print(d/gcd(n,d), time()-s)
