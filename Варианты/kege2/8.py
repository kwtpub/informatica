from itertools import *
k = 0
for i in product('КОСУФ', repeat=5):
    n = ''.join(i)
    k += 1
    if n.count('Ф') == 0 and n.count('У') == 2:
        print(k, n)