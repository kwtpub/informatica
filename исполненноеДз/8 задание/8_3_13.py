from itertools import *

k = 0
for i in product('ДЕЙКСТРА', repeat=6):
	n = ''.join(i)
	if all(n.count(x)<=1 for x in 'ДЕЙКСТРА'):
		n = n.replace('К','*').replace('С','*').replace('Т','*').replace('Р','*').replace('Д', '*')
		if n.count('Й') == 1 and 'Й*' in n:
			k += 1 
print(k)