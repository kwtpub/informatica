from itertools import * 
k = 0 
for n in product('ГОД', repeat=6):
    i = ''.join(n)
    if i[5] in 'ГД' and i[0] in 'ГД':
        k += 1
print(k)