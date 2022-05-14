thing = open("p067_triangle.txt", "r")
thing = thing.read().split()
rows = []
number_rows = 100

for i in range(number_rows):
    current_row = []
    for j in range(i+1):
        current_row.append(thing[int(j + ((i * (i+1)) / 2))])
    rows.append(current_row)
        

for i in range(number_rows-1, 0 ,-1):
    for j in range(len(rows[i-1])):
        rows[i-1][j] = int(rows[i-1][j]) + max(int(rows[i][j]),
                                               int(rows[i][j+1]))

    
print(rows[0][0])        
    
