p, q, s = 1, 1, 0

for k in range(1000):
    p, q = p + 2*q, p + q
    if len(str(p)) > len(str(q)):
        s += 1
        
print(s)
