def d(a, b, c):
	return a * b > c

def f(x,y,a):
	return (not d(x, y, a + 13)) <= d(28, y, 520) or d(x, 25, 800)

for a in range(-100,1000):
	if all(f(x,y,a) for x in range(0,1000) for y in range(0,1000)):
		print(a) #-13
