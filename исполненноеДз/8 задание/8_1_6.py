from itertools import *
k = 0
for n in product('УЧЕНИК', repeat=5):
    if n[0] == 'У' and n[4] == 'К':
        k += 1
        print(n)
print(k) #216 
