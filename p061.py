from math import log10 as log

origial_numbers = [
    
    [str(int(i*(i+1)/2)) for i in range(1, 200)],
    
    [str(i**2) for i in range(1, 200)],
    
    [str(int(i*(3*i-1)/2)) for i in range(1, 200)],
    
    [str(i*(2*i-1)) for i in range(1, 200)],
    
    [str(int(i*(5*i-3)/2)) for i in range(1, 200)],
    
    [str(i*(3*i-2)) for i in range(1,200)],

    [str(int(i*(i+1)/2)) for i in range(1, 200)]
    
    ]

numbers = []

for i in origial_numbers:
    
    for j in range(0, 199):
        
        if len(i[j]) != 4:
            i[j] = None

    numbers.append(list(set(i)-{None}))

q = [[]]  * 30

print(q)

counter = 0

for i in range(0, 6):
    
    for j in range(0, 6):
        
        if j == i:
            continue
        
        else:
            
            for k in numbers[i]:
                for l in numbers[j]:
                    
                    if k[2:] == l[:2]:
                        q[counter].append((k, l))

            counter += 1
                        
        
p = []

for i in range(len(q)):
    
    for j in range(len(q)):

        if i == j:
            continue

        else:
            for k in q[i]:
                for l in q[j]:
                    if k[1] == l[0]:
                        p.append([k[0], k[1], l[1]])

        

            
# incomplete and inefficient method

        

    
