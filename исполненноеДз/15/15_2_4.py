def d(n, m): 
    if n % m == 0:
        return 1
    else:
        return 0
    
def f(x,a):
    return (d(x,a) and d(x,24) and (not d(x,16))) <= (not d(x,a))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a) #16
		break