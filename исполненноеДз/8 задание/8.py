from itertools import *
k = 0
for i in product('КОСУФ', repeat=5):
    k += 1 
    n = ''.join(i)
    if n.count('Ф') == 0  and n.count('У') == 2:
        print(k)