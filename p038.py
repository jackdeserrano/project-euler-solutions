from defs import *

m = 0
for k in range(9, 100000):
    p = ''
    for z in range(1, 10):
        p += str(k*z)
        if len(p)==9:
            if p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and p.count('7') == 1 and p.count('8') == 1 and p.count('9') == 1 and '0' not in p and int(p) > m:
                m = int(p)
print(m)
