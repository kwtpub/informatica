for i in range(1000, 10000):
	s1 = i // 1000 + i // 100 % 10
	s2 = i // 100 % 10 + i // 10 % 10
	s3 = i // 10 % 10 + i % 10
	d = sorted([s1, s2, s3])
	r = str(d[1]) + str(d[2])
	if r == '1315':
		print(i)
		