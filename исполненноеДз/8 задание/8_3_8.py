from itertools import *

k = 0
for i in product('НАСТЯ', repeat=6):
	n = ''.join(i)
	if n.count('А') <= 1 and n.count('Я') <= 1:
		k += 1 
print(k)