def to_base(n, to_base):
	s = ''
	while n > 0:
		s = str(n % to_base) + s
		n = n // to_base
	return int(s)

n = [int(x) for x in open('17/17_2402.txt')]
asl = []
for i in range(0, len(n)-2):
    if abs(to_base(n[i], 3))%10 == 2 or abs(to_base(n[i+1], 3))%10 == 2 or abs(to_base(n[i+2], 3))%10 == 2:
        asl.append(min(n[i],n[i+1],n[i+2]))
print(sum(asl))
print(len(asl))