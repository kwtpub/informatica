d = [0] * 10000
for i in range(1, 1000):
	n = bin(i)[2:]
	n += bin(i%4)[2:]
	r = int(n, 2)
	d[r] = 1
	
sum = 0
for i in range(0, len(d)-65):
	mx = max(mx, sum(d[i:i+65]))
	
print(sum)