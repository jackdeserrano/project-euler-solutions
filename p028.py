import time
r, s, c, p = 0, [1], 1, 0
start = time.time()
while True: 
    if p % 4==0:
        r += 2
    p += 1
    c += r
    s.append(c)
    if c == 1002001:
        break
print(sum(s), time.time()-start)


