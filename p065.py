from defs import *

p, q = 1, 2

for k in range(2, 101):
    if k % 3: p, q = q, p + q
    else: p, q = q, p + q * (k//3 * 2)
    
print(digit_sum(q))
