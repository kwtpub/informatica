from itertools import * 
k = 0
for i in product('ПУЛЯ', repeat=6):
    n = ''.join(i)
    if n.count('Л') == 2:
        k += 1 
print(k) #1215