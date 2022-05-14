from defs import *

def pdg(x):
    p = str(x)
    if len(p) == 9 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and p.count('7') == 1 and p.count('8') == 1 and p.count('9') == 1 and prime(x) == True:
        return True
    elif len(p) == 8 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and p.count('7') == 1 and p.count('8') == 1 and prime(x) == True:
        return True
    elif len(p) == 7 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and p.count('7') == 1 and prime(x) == True:
        return True
    elif len(p) == 6 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and prime(x) == True:
        return True
    elif len(p) == 5 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and prime(x) == True:
        return True
    elif len(p) == 4 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and prime(x) == True:
        return True
    return False

m = 0
for k in range(1001, 10000000, 2):
    if pdg(k) == True and k > m: m = k

print(m)
