from itertools import *

k = 0
for i in product('ВИШНЯ', repeat=6):
	n = ''.join(i)
	if n[0] != 'Ш' and n.count('В') <= 1 and n[5] != 'И' and n[5] != 'Я':
		k += 1 
print(k)