from itertools import *

ox = {x for x in range(1, 20)}
p = {x for x in range(1, 11)}
q = {2,4,8,10}

def f(x, a):
	A = x in a
	P = x in p
	Q = x in q
	return (Q <= A) and (A <= P)
	
k = 0
for ln in range(1, 20):
	for a in combinations(ox, ln):
		if all(f(x, a) for x in ox):
			k += 1
print(k)