#15_1
print('Ответ 15_1: ', end = '')

def f(x, y, a):
	return (3*x + 7*y < a) or (x >= y) or (y > 6)
	
for a in range(1,10000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)
		break


#15_1_1
print('Ответ 15_1_1: ', end = '')

def f(x, y, a):
	return (x*y < 121) or (y > a) or (x >= a)

for a in range(1,1000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)


#15_1_2
print('Ответ 15_1_2: ', end = '')

def f(x, y, a):
	return (x*y < a) or (y > x) or (x >= 8)

for a in range(1,10000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)
		break


#15_1_3
print('Ответ 15_1_3: ', end = '')

def f(x, y, a):
	return (x > a) or (y > x) or (2*y + x < 110)

for a in range(1,1000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)


#15_1_4
print('Ответ 15_1_4: ', end = '')

def f(x, y, a):
	return (2*x + y != 70) or (x < y) or (a < x)

for a in range(1,1000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)


#15_1_5
print('Ответ 15_1_5: ', end = '')

def f(x, y, a):
	return (x*y > a) and (x > y) and (x < 8)

for a in range(1,10000):
	if all(f(x, y, a)==0 for x in range(1,100) for y in range(1,100)):
		print(a)
		break
		
		
#15_1_6
print('Ответ 15_1_6: ', end = '')

def f(x, y, a):
	return (x > 39) or (y > 26) or (2*x + 4*y < a)

for a in range(1,10000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)
		break


#15_1_7
print('Ответ 15_1_7: ', end = '')

def f(x, y, a):
	return (2*x + y != 70) or (x < y) or (a < x)

for a in range(1,1000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)


#15_1_8
print('Ответ 15_1_8: ', end = '')

def f(x, y, a):
	return (x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2*a)

for a in range(1,10000):
	if all(f(x, y, a)==1 for x in range(1,100) for y in range(1,100)):
		print(a)
		break


#15_1_9
print('Ответ 15_1_9: ', end = '')
def f(x, y, a):
	return (2 * x + 3 * y > 30) or (x + y <= a)
	
for a in range(0, 1000):
	if all(f(x, y, a) == 1 for x in range(0, 200) for y in range(0, 200)):
		print(a)
		break
		
		
#15_1_10
print('Ответ 15_1_10: ', end = '')
def f(x, y, a):
	return (x - 3 * y < a) or (y > 400) or (x > 56)
	
for a in range(0, 1000):
	if all(f(x, y, a) == 1 for x in range(1, 200) for y in range(1, 200)):
		print(a)
		break
		

#15_1_11
print('Ответ 15_1_11: ', end = '')
def f(x, y, a):
	return not((x < 7) or (y >= 3 * x + a - 20) or (x >= 34) or (y < 121))
	
for a in range(0, 1000):
	if all(f(x, y, a) == 0 for x in range(0, 200) for y in range(0, 200)):
		print(a)
		
	
#15_1_12
print('Ответ 15_1_12: ', end = '')
def f(x, y, a):
	return (3 * x + y > 48) or (x > y) or (4 * x + y < a)
	
for a in range(0, 1000):
	if any(f(x, y, a) == 0 for x in range(0, 200) for y in range(0, 200)):
		print(a)	


#15_1_13
print('Ответ 15_1_13: ', end = '')
def f(x, y, a):
	return ((a < x) or (x ** 2 - 7 * x + 10 > 0)) and ((a >= y) or (y ** 2 + 7 * y + 12 > 0))
	
k = 0
for a in range(-200, 200):
	if all(f(x, y, a) == 1 for x in range(-200, 200) for y in range(-200, 200)):
		k += 1
print(k)	


#15_2
print('Ответ 15_2: ', end = '')

def f(x, a):
	return (x%a!=0) <= ((x%6==0) <= (x%4!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)


#15_2_1
print('Ответ 15_2_1: ', end = '')

def f(x, a):
	return (a < 50) and ((x%a!=0) <= ((x%10==0) <= (x%18!=0)))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)


#15_2_2
print('Ответ 15_2_2: ', end = '')

def f(x, a):
	return (120%a==0) and ((x%a!=0) <= ((x%18==0) <= (x%24!=0)))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)


#15_2_3
print('Ответ 15_2_3: ', end = '')

def f(x, a):
	return (a%45==0) and ((750%x==0) <= ((a%x!=0) <= (120%x!=0)))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_2_4
print('Ответ 15_2_4: ', end = '')

def f(x, a):
	return ((x%a==0) and (x%24==0) and (x%16!=0)) <= (x%a!=0)

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_2_5
print('Ответ 15_2_5: ', end = '')

def f(x, a):
	return ((x%84!=0) or (x%90!=0)) <= (x%a!=0)

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_2_6
print('Ответ 15_2_6: ', end = '')

def f(x, a):
	return ((x%15==0) and (x%21!=0)) <= ((x%a!=0) or (x%15!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break
		
		
#15_2_7
print('Ответ 15_2_7: ', end = '')

def f(x, a):
	return ((x%4!=3) or (x%6!=1)) <= (x%36!=a)

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_2_8
print('Ответ 15_2_8: ', end = '')

def f(x, a):
	return (a%7==0) and (240%x==0) <= ((a%x!=0) <= (780%x!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break
		
		
#15_3
print('Ответ 15_3: ', end = '')

def f(x, a):
	return (x&29!=0) <= ((x&17==0) <= (x&a!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_3_1
print('Ответ 15_3_1: ', end = '')

def f(x, a):
	return (x&29!=0) <= ((x&12==0) <= (x&a!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_3_2
print('Ответ 15_3_2: ', end = '')

def f(x, a):
	return (x&17==0) <= ((x&29!=0) <= (x&a!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_3_3
print('Ответ 15_3_3: ', end = '')

def f(x, a):
	return ((x&26!=0) or (x&13!=0)) <= ((x&29==0) <= (x&a!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_3_4
print('Ответ 15_3_4: ', end = '')

def f(x, a):
	return (((x&13!=0) or (x&a!=0)) <= (x&13!=0)) or ((x&a!=0) and (x&39==0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)


#15_3_5
print('Ответ 15_3_5: ', end = '')

def f(x, a):
	return (x&107==0) <= ((x&55!=0) <= (x&a!=0))

for a in range(1,10000):
	if all(f(x, a)==1 for x in range(1,10000)):
		print(a)
		break


#15_3_6
print('Ответ 15_3_6: ', end = '')

def f(x, a):
	return (x & 57 == 0) or ((x & 23 == 0) <= (x & a != 0))
	
for a in range(1, 1000):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)
		break
		
		
#15_4
print('Ответ 15_4: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 4 <= x <= 15
	q = 12 <= x <= 20
	a = a1 <= x <= a2
	return (p and q) <= a
	
ox = [x/4 for x in range(3 * 4, 22 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2-a1)

print(min(ans))


#15_4_1
print('Ответ 15_4_1: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 10 <= x <= 29
	q = 13 <= x <= 18
	a = a1 <= x <= a2
	return (a <= p) or q
	
ox = [x/4 for x in range(9 * 4, 31 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)
		
print(max(ans))


#15_4_2
print('Ответ 15_4_2: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 25 <= x <= 50
	q = 32 <= x <= 47
	a = a1 <= x <= a2
	return ((not a) <= p) <= (a <= q)
	
ox = [x/4 for x in range(24 * 4, 52 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(max(ans))


#15_4_3
print('Ответ 15_4_3: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 130 <= x <= 171
	q = 150 <= x <= 185
	a = a1 <= x <= a2
	return p <= ((q and (not a)) <= (not p))
	
ox = [x/4 for x in range(129 * 4, 187 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(min(ans))


#15_4_4
print('Ответ 15_4_4: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 5 <= x <= 30
	q = 14 <= x <= 23
	a = a1 <= x <= a2
	return (p == q) <= (not a)
	
ox = [x/4 for x in range(4 * 4, 32 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(max(ans))


#15_4_5
print('Ответ 15_4_5: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 10 <= x <= 40
	q = 5 <= x <= 15
	r = 35 <= x <= 50
	a = a1 <= x <= a2
	return (a or p) or (q <= r)
	
ox = [x/4 for x in range(4 * 4, 52 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(min(ans))


#15_4_6
print('Ответ 15_4_6: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 10 <= x <= 39
	q = 23 <= x <= 58
	a = a1 <= x <= a2
	return (p and q) <= (q and a)
	
ox = [x/4 for x in range(9 * 4, 60 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)
		
print(min(ans))


#15_4_7
print('Ответ 15_4_7: ', end = '')

from itertools import *

def f(x, a1, a2):
	d = 17 <= x <= 58
	c = 29 <= x <= 80
	a = a1 <= x <= a2
	return d <= (((not c) and (not a)) <= (not d))
	
ox = [x/4 for x in range(16 * 4, 82 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(min(ans))


#15_4_8
print('Ответ 15_4_8: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 17 <= x <= 54
	q = 37 <= x <= 83
	a = a1 <= x <= a2
	return p <= ((q and (not a)) <= (not p))
	
ox = [x/4 for x in range(16 * 4, 85 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(min(ans))


#15_4_9
print('Ответ 15_4_9: ', end = '')

from itertools import *

def f(x, a1, a2):
	b = 18 <= x <= 52
	c = 16 <= x <= 41
	a = a1 <= x <= a2
	return (b <= a) and ((not c) or a)
	
ox = [x/4 for x in range(15 * 4, 54 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(min(ans))


#15_4_10
print('Ответ 15_4_10: ', end = '')

from itertools import *

def f(x, a1, a2):
	p = 10 <= x <= 150
	q = 160 <= x <= 250
	r = 240 <= x <= 300
	a = a1 <= x <= a2
	return (q <= p) or ((not a) <= r)
	
ox = [x for x in range(9 * 2, 302 * 2)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(min(ans))


#15_4_11
print('Ответ 15_4_11: ', end = '')

from itertools import *

def f(x, a1, a2):
	c = 48 <= x <= 94
	j = 83 <= x <= 100
	a = a1 <= x <= a2
	return (not (c or j)) <= (not a)
	
ox = [x/4 for x in range(47 * 4, 102 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(max(ans))


#15_4_12
print('Ответ 15_4_12: ', end = '')
# Решать только аналитикой! :)
from itertools import *

def f(x, a1, a2):
	p = 257 <= x <= 1000
	q = 5 <= x <= 100
	r = 99 <= x <= 258
	a = a1 <= x <= a2
	return (a <= r) and (not (a <= p)) <= q
	
ox = [x/4 for x in range(4 * 4, 1002 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) == 1 for x in ox):
		ans.append(a2 - a1)

print(max(ans))


#15_5
print('Ответ 15_5: ', end = '')

a = set()
p = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
q = {x for x in range(3, 31, 3)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (P <= A) or ((not A) <= (not Q))
	
for x in range(1000):
	if f(x) == 0:
		a.add(x)

s = 1
for i in a:
	s *= i
print(s)


#15_5_1
print('Ответ 15_5_1: ', end = '')

a = set()
p = {x for x in range(2, 21, 2)}
q = {x for x in range(3, 31, 3)}
r = {x for x in range(12, 61, 12)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	R = x in r
	return (not A) <= ((P and Q) <= R)
	
for x in range(1000):
	if f(x) == 0:
		a.add(x)

s = 1
for i in a:
	s *= i
print(s)


#15_5_2
print('Ответ 15_5_2: ', end = '')

a = set()
p = {x for x in range(3, 13, 3)}
q = {x for x in range(1, 7)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return not ((not A) and P) or (not Q)
	
for x in range(1000):
	if f(x) == 0:
		a.add(x)

print(len(a))


#15_5_3
print('Ответ 15_5_3: ', end = '')

a = set()
p = {1, 12}
q = {x for x in range(12, 17)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (not A) <= ((not P) and (not Q))
	
for x in range(1000):
	if f(x) == 0:
		a.add(x)

print(len(a))


#15_5_4
print('Ответ 15_5_4: ', end = '')

a = set()
p = {1, 3, 5, 7, 9, 11}
q = {x for x in range(3, 13, 3)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (P <= (not Q)) or A
	
for x in range(1000):
	if f(x) == 0:
		a.add(x)

print(sum(a))


#15_5_5
print('Ответ 15_5_5: ', end = '')

a = set(range(1000))
p = {x for x in range(2, 21, 2)}
q = {x for x in range(5, 51, 5)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (A <= P) and (Q <= (not A))
	
for x in range(1000):
	if f(x) == 0:
		a.remove(x)

print(len(a))


#15_5_6
print('Ответ 15_5_6: ', end = '')

a = set(range(1000))

def f(x):
	A = x in a
	P = x in {x for x in range(2, 21, 2)}
	Q = x in {x for x in range(3, 31, 3)}
	return (A <= P) and ((not Q) <= (not A))
	
for x in range(1000):
	if f(x) == 0:
		a.remove(x)

print(len(a))


#15_5_7
print('Ответ 15_5_7: ', end = '')

a = set(range(1000))
b = {x for x in range(12, 57, 11)}
c = {23, 35, 56, 68, 89}

def f(x):
	A = x in a
	B = x in b
	C = x in c
	return B or C or (not A)
	
for x in range(1000):
	if f(x) == 0:
		a.remove(x)

print(len(a))


#15_5_8
print('Ответ 15_5_8: ', end = '')

a = set(range(1000))
p = {x for x in range(2, 21, 2)}
q = {x for x in range(5, 51, 5)}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (A <= P) and (Q <= (not A))
	
for x in range(1000):
	if f(x) == 0:
		a.remove(x)

print(len(a))


#15_5_9
print('Ответ 15_5_9: ', end = '')

from itertools import *

ox = {x for x in range(1, 20)}
p = {x for x in range(1, 11)}
q = {2, 4, 8, 10}

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


#15_5_10
print('Ответ 15_5_10: ', end = '')

a = set()
p = {1, 2, 4, 8, 16}
q = {3, 4, 9, 16}

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (not P) and (not Q) or A

for x in range(1000):
	if f(x) == 0:
		a.add(x)
		
print(len(a))
		

#15_5_11
print('Ответ 15_5_11: ', end = '')

from itertools import *

a = set()
p = {''.join(x) for x in product('01', repeat = 8) if ''.join(x)[:2] == '11'}		
q = {''.join(x) for x in product('01', repeat = 8) if ''.join(x)[-1] == '0'}		

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (not A) <= (P or (not Q))
	
for x in product('01', repeat = 8):
	n = ''.join(x)
	if f(n) == 0:
		a.add(n)
		
print(len(a))


#15_5_12
print('Ответ 15_5_12: ', end = '')

from itertools import *

a = set()
p = {''.join(x) for x in product('01', repeat = 16) if ''.join(x)[:2] == '01'}		
q = {''.join(x) for x in product('01', repeat = 16) if ''.join(x)[-1] == '1'}		

def f(x):
	A = x in a
	P = x in p
	Q = x in q
	return (not A) <= (P or (not Q))
	
for x in product('01', repeat = 16):
	n = ''.join(x)
	if f(n) == 0:
		a.add(n)
		
print(len(a))


#15_6
print('Ответ 15_6: ', end = '')

def cif(x, y):
	return x % 10 == y % 10
	
def f(x, a):
	return ((not cif(x, 5)) and cif(x, 4)) <= (x > a - 11)
	
for a in range(1, 1000):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)


#15_6_1
print('Ответ 15_6_1: ', end = '')

def nod(x, y, k):
	for i in range(max(x, y), 0, -1):
		if x % i == 0 and y % i == 0 and i != k:
			return 0
		if x % i == 0 and y % i == 0 and i == k:
			return 1
	
def f(x, a):
	return nod(a, 420, 2) or ((not nod(a, x, 12)) <= (not nod(110, x, 11)))
	
k = 0
for a in range(1, 1001):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		k += 1
print(k)


#15_6_2
print('Ответ 15_6_2: ', end = '')

def treug(n, m, k):
	d = sorted([n, m, k])
	if d[0] + d[1] > d[2]:
		return 1
	return 0
	
def f(x, a):
	return treug(a, 7, x) <= ((max(x + 5, 14) <= 27) == (not treug(36, 21, x)))
	
for a in range(1, 1001):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)
		
		
#15_6_3
print('Ответ 15_6_3: ', end = '')

def f(x, a):
	return (a + x > 700 - a) and (a % 100 + 100 % x > 50)
	
for a in range(1, 1001):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)
		break


#15_6_4
print('Ответ 15_6_4: ', end = '')

def treug(n, m, k):
	d = sorted([n, m, k])
	return d[0] + d[1] > d[2]:
	
def f(x, a):
	return not ((treug(x, 11, 18) == (not (max(x, 5) > 68))) and treug(x, a, 5))
	
for a in range(1, 1001):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)


#15_6_5
print('Ответ 15_6_5: ', end = '')

def plosh(a, b, c):
	return a * b > c
	
def f(x, y, a):
	return (not plosh(x, y, a + 13)) <= plosh(28, y, 520) or plosh(x, 25, 800)
	
for a in range(-100, 100):
	if all(f(x, y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
		print(a)


#15_6_6
print('Ответ 15_6_6: ', end = '')

def ugol(a, b, c):
	return a + b + c == 180
	
def f(x, y, a):
	return ugol(37, a, x + 45) == ugol(a, x, 90) and (not (a + 23 < 120))
	
for a in range(1000):
	if all(f(x, y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
		print(a)
		break


#15_6_7
print('Ответ 15_6_7: ', end = '')

def div(n, m):
	return n // m == 0
	
def f(x, a):
	return (div(x, 50) > 3) or (not (div(x, 13) > 3)) or (div(x, a) > 6)
	
for a in range(1, 1000):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)
		break


#15_6_8
print('Ответ 15_6_8: ', end = '')

def od(n, m):
	for i in range(2, min(n, m) + 1):
		if n % i == 0 and m % i == 0:
			return 1
	return 0
	
def f(x, a):
	return (od(x, 42) <= (not od(x, 7))) or (x + a >= 25)
	
for a in range(1, 1000):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		print(a)
		break


#15_7
print('Ответ 15_7: ', end = '')
# Решать аналитикой


#15_7_1
print('Ответ 15_7_1: ', end = '')

def f(x, y, z):
	return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > a // 8)
	
for a in range(1, 1000):
	if all(f(x, y, z) == 1 for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
		print(a)


#15_7_2
print('Ответ 15_7_2: ', end = '')

from itertools import *

def f(x, a1, a2):
	b = 10 <= x <= 40
	a = a1 <= x <= a2
	return a or (b <= (x % 6 != 0))
	
ox = [x/4 for x in range(9 * 4, 42 * 4)]
ans = []

for a1, a2 in combinations(ox, 2):
	if all(f(x, a1, a2) for x in ox):
		ans.append(a2 - a1)

print(min(ans))
	

#15_7_3
print('Ответ 15_7_3: ', end = '')

def f(x, a):
	return ((x % 115 == 0) and (x % 5 != 0)) or (((a % x == 0) <= (a % 5 != 0)) and (not (5 <= a <= 137)))
	
for a in range(1, 1000):
	if all(f(x, a) == 1 for x in range(1, 1000)) == 0 and any(f(x, a) == 1 for x in range(1, 1000)):
		print(a)
		break


#15_7_4
print('Ответ 15_7_4: ', end = '')

def f(x, a):
	b = 70 <= x <= 80
	return (x % a == 0) or (b <= (x % 18 != 0))
	
k = 0
for a in range(1, 1000):
	if all(f(x, a) == 1 for x in range(1, 1000)):
		k += 1

print(k)


#15_7_5
print('Ответ 15_7_5: ', end = '')

def f(x, a):
	return ((not (5 <= x <= 54)) and (50 <= x <= 93)) <= (x > a)
	
	
for a in range(1, 1000):
	if sum(f(x, a) == 0 for x in range(-1000, 1000)) == 20:
		print(a)
		break
