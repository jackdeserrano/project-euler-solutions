def opp(z):
    return int(str(z)[::-1])
               
def pa(z):
    z = str(z)
    p = z[::-1]
    if z == p:
        return True
    return False


s = 10000
for k in range(1, 10000 + 1):
    p = k
    for z in range(50):
        p += opp(p)
        if pa(p) == True:
            s -= 1
            break

print(s)
        
        
