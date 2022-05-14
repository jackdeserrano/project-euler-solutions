import math
def prime(z):
    if z == 1 or z == 0: return False
    else:
        for k in range(2, math.floor(math.sqrt(z)) + 1):
            if z % k == 0:
                return False
        return True

def totient(z):
    s, l = 0, []
    for k in range(z):
        if math.gcd(z, k) == 1:
            s += 1
            l.append(k)
    return s, l

l = []
for k in range(1000, 10, -1):
    if prime(k) == True: l.append(k)

o = 0
for k in l:
    if 10 in totient(k)[1]:
        for n in range(1, 1000):
            if (10 ** n) % k == 1 and n != totient(k)[0]: break
            elif (10 ** n) % k == 1 and n == totient(k)[0]:
                o = k
                break
    if o != 0: break
print(o)
                
    
# prints largest prime under 1000 that has 10 as a primitive root
