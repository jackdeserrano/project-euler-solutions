from defs import *

def p(x):
    x = math.sqrt(24 * x + 1) % 6
    if x == 5:
        return True
    return False

s = 143

while True:
    s += 1
    o = s * (2 * s - 1)
    if p(o) == True:
        print(o)
        break
