from itertools import *
k = 0 
for i in product('ЗИМА', repeat=5):
    n = ''.join(i)
    if n[0] in 'МЗ' and n[4] in 'ИА':
        k += 1
print(k) #81- +256
