from defs import *

def pdg(x):
    p = str(x)
    if len(p) == 9 and p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and p.count('7') == 1 and p.count('8') == 1 and p.count('9') == 1:
        return True
    return False

p = []
for k in range(18):
    if prime(k) == True: p.append(k)

l = []

for k in perm(1234567890):
    if len(str(k)) != 10: continue
    o = 0
    r = [j for j in str(k)]
    for z in range(len(p)):
        if int(r[z+1]+r[z+2]+r[z+3]) % p[z] != 0:
            o = 1
    if o == 0: l.append(k)

print(sum(l))
