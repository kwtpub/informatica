
p = {x for x in range(3,13,3)}
q = {x for x in range(1,7)}

a = set()

def f(x):
	P = x in p
	Q= x in q
	A =x in a
	return not ((not A) and P) or (not Q)
	
for x in range(1000):
	if f(x)==0:
		a.add(x)

print(len(a))
