s = ''
for k in range(1, 10000000):
    s += str(k)
    if len(s) > 1000000: break

print(int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999]))
        
