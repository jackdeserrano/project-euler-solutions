import time
def pdg(y, z):
    p = [k for k in str(z)+str(y)+str(y*z)]
    if len(p) != 9: return False
    elif p.count('1') == 1 and p.count('2') == 1 and p.count('3') == 1 and p.count('4') == 1 and p.count('5') == 1 and p.count('6') == 1 and p.count('7') == 1 and p.count('8') == 1 and p.count('9') == 1 and '0' not in p:
        return True
    return False
s = time.time()
l = []
for k in range(1, 1964):
    for z in range(1, 484):
        if pdg(k,z) == True:
            if k*z in l:
                continue
            else: l.append(k*z)
print(sum(l),str(time.time()-s))
