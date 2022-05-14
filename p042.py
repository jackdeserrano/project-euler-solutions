w = open('./p042_words.txt', 'r').read()
w = w.replace('"', '').replace(',',' ').replace(' ', '\n')
lt = [ '\n', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
       'X', 'Y', 'Z' ]
tnum, s = [], 0
for k in range(1, 100):
    s+=k
    tnum.append(s)

w = w.split('\n')

l = []
for k in w:
    d = 0
    z = [j for j in k]
    for p in z:
        d += lt.index(p)
    if d in tnum: l.append(d)

print(len(l))
