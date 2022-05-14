from defs import *
from decimal import *

getcontext().prec = 105
qw = time()
l, s = [k**2 for k in range(1, 10)], []

for k in range(1, 100):
    if k in l: continue
    r = str(Decimal(k).sqrt())
    r = r.replace('.', '')[:-(4+(len(str(math.floor(math.sqrt(k))))))]
    s.append(digit_sum(int(r)))
    
print(sum(s), time()-qw)
    
# MAYBE USE
# http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
