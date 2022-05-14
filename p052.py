from defs import *

# cannot be bigger than 1.666 e len(p)

for k in range(1, 100000000):
    p = str(k)
    if k > 0.16666666*(10**len(p)):
        continue
    l = perm_num(k)
    if 2 * k in l and 3 * k in l and 4 * k in l and 5 * k in l and 6 * k in l:
        print(k)
        break
