from itertools import *

k = 0
for i in permutations('абиколун'):
	n = ''.join(i)
	n = n.replace('и','*').replace('о','*').replace('у','*').replace('а', '*')
	n = n.replace('к','i').replace('л','i').replace('н','i').replace('б', 'i')
	if '**' not in n and 'ii' not in n:
		k += 1 
print(k)