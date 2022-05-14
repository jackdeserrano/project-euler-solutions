from defs import *

def p(z):
    z = str(z)
    p = z[::-1]
    if z == p:
        return True
    return False

l = []
for k in range(1000000):
    if p(bin(k)[2:]) == True and p(k) == True:
        l.append(k)

print(sum(l))
