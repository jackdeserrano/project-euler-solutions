from time import time
def z(x):
    s = 0
    while x > 0:
        s += (x % 10)**2
        x //= 10
    return s

def m(x):
    while x != 1:
        x = z(x)
        if x == 89: return True
    return None

def n(x):
    s = 0
    for k in range(1, 10**x):
        if m(k): s = s + 1
    return s
        
print(n(7))
