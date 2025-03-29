def f(n, base):
	s = ''
	while n > 0:
		s = str(n % base) + s
		n = n//base
	return s
	
for i in range(1, 1000):
	n = f(i, 3)
	if i%3==0:
		n += n[-2:]
	else:
		n += f(i%3*5, 3)
	r = int(n, 3)
	if r < 173:
		print(r)