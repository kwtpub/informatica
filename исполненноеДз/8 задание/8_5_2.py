k = 0
for i in permutations('ИГРОК'):
	n = ''.join(i)
	if n[0] != 'К' and 'РОК' not in n:
		k += 1 
print(k)