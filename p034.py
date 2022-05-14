from defs import *

def f(z):
    s = 0
    x = [k for k in str(z)]
    for k in x:
        s += factorial(int(k))
    if s == z: return True
    return False

l = []
for k in range(3, 100000):
    if f(k) == True: l.append(k)

print(sum(l))
