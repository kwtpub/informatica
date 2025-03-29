def f(n, base):
	s = ''
	while n > 0:
		s = str(n % base) + s
		n = n//base
	return s
	
for i in range(1, 1000):
	n = f(i, 3)
	n += str(i % 3)
	r = int(n, 3)
	if r >= 1000:
		print(r)
		break