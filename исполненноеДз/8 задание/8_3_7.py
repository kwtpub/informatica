from itertools import *
k = 0
for i in product('АНДРЕЙ', repeat=6):
	n = ''.join(i)
	if n.count('А') >= 1 and n.count('Й') <= 1:
		k += 1 
print(k)