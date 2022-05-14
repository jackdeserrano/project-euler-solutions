from defs import *

def prime_factors_up_to(x):
    l = [0 for k in range(x)]
    for k in range(2, x):
        if l[k] == 0:
            for z in range(2*k, len(l), k):
                l[z] += 1
        if l[k] == 4 and l[k-1] == 4 and l[k-2] == 4 and l[k-3] == 4:
            return k - 3

s = time()
print(prime_factors_up_to(1000000), time()-s)
