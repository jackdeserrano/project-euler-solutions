from defs import *

def q(a, b):
    if prime(abs(b)) == False: return 0
    c = 0
    while True:
        if prime(c**2 + a*c + b) == True:
            c += 1
        else:
            return c


y, z, m = 0, 0, 0
for a in range(-1000, 1000):
    for b in range(3, 1001, 2):
        if q(a, b) > m:
            m = q(a, b)
            y, z = a, b

print(y * z)
