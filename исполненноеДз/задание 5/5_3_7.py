d = set()
for i in range(10, 1000+1):
	n = bin(i)[2:]
	n = n[1:]
	r = i - int(n, 2)
	d.add(r)
	
print(len(d))