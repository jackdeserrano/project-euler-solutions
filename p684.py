from defs import *

##def F(x):
##    fl = [0, 1]
##    for i in range(x-1):
##        fl.append(fl[i] + fl[i+1])
##    return fl
##
##def SDS(n):
##    x = n//9
##    return (1+(n-(9*x)))*(10**x)-1
##
##def SA(k):
##    n, s = 1, 0
##    while n <= k:
##        s += SDS(n)
##        n += 1
##    return s

# Josh's fcns

MOD = 1000000007

def S(n):
    k, r = divmod(n, 9)
    return (pow(10, k, MOD) * (6 + r*(r + 3) // 2) - 6 - n)

w = time()
l, f = 0, fib(91)
for k in range(2, 91):
    l = (l + S(f[k])) % MOD
print(l,  time()-w)
