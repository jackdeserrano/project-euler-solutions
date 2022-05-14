from defs import *

def rt(z):
    if prime(z) == False: return False
    p = str(z)
    for k in range(1, len(p)):
        if prime(int(p[:len(p)-k])) == False: return False
    return True
def lt(z):
    if prime(z) == False: return False
    p = str(z)
    for k in range(1, len(p)):
        if prime(int(p[len(p)-k:])) == False: return False
    return True

l = []
for k in range(11, 1000000, 2):
    if lt(k) == True and rt(k) == True: l.append(k)


print(l, sum(l))
