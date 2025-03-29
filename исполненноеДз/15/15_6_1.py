from itertools import *
def d(a,b,k):
    #Использую алгоритм Евклида
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if k == (a + b):
        return 1
    else:
        return 0

def f(x,a):
    return d(a,420,2) or ((not d(a,x,12) <= (not d(110,x,11))))

k = 0
for a in range(1, 1000+1):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		k += 1
print(k) 