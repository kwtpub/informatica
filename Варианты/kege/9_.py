#9_1
print('Ответ 9_1:', end = " ")

k = 0
for s in open('9_1.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[2] < n[0] + n[1]:
		k += 1
print(k)


#9_1_1
print('Ответ 9_1_1:', end = " ")

k = 0
for s in open('9_1_1.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[2]**2 < n[0]**2 + n[1]**2:
		k += 1
print(k)


#9_1_2
print('Ответ 9_1_2:', end = " ")

k = 0
for s in open('9_1_2.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[2]**2 == n[0]**2 + n[1]**2:
		k += 1
print(k)


#9_1_3
print('Ответ 9_1_3:', end = " ")

k = 0
for s in open('9_1_3.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[0]*n[1] + n[0]*n[2] < n[1]*n[2]:
		k += 1
print(k)


#9_1_4
print('Ответ 9_1_4:', end = " ")

k = 0
for s in open('9_1_4.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[0] + n[1] < n[3]:
		k += 1
print(k)


#9_1_5
print('Ответ 9_1_5:', end = " ")

k = 0
for s in open('9_1_5.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[0] + n[1] > n[3]:
		k += 1
print(k)


#9_1_6
print('Ответ 9_1_6:', end = " ")

k = 0
for s in open('9_1_6.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[0]*n[1] + n[0]*n[2] > n[1]*n[2]:
		k += 1
print(k)


#9_2
print('Ответ 9_2:', end = " ")

k = 0
for s in open('9_2.txt'):
	n = sorted([int(x) for x in s.split()])
	n3 = [x for x in n if n.count(x)==3]
	n1 = [x for x in n if n.count(x)==1]
	if len(n1) == 4 and len(n3) == 3 and sum(n1)/len(n1) <= n3[0]:
		k += 1
print(k)


#9_2_1
print('Ответ 9_2_1:', end = " ")

k = 0
for s in open('9_2_1.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x)==1]
	if len(n1) == 5 and 2*(n[0]+n[4]) <= n[1]+n[2]+n[3]:
		k += 1
print(k)


#9_2_2
print('Ответ 9_2_2:', end = " ")

k = 0
for s in open('9_2_2.txt'):
	n = sorted([int(x) for x in s.split()])
	n4 = [x for x in n if n.count(x)==4]
	n1 = [x for x in n if n.count(x)==1]
	if len(n1) == 3 and len(n4) == 4 and sum(n4)/len(n4) < sum(n)/len(n):
		k += 1
print(k)


#9_2_3
print('Ответ 9_2_3:', end = " ")

k = 0
for s in open('9_2_3.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x) == 1]
	k0 = [x for x in n if x%2==0]
	k1 = [x for x in n if x%2!=0]
	if len(n1) == 5 and len(k0) < len(k1) and sum(k1) < sum(k0):
		k += 1
print(k)


#9_2_4
print('Ответ 9_2_4:', end = " ")

k = 0
for s in open('9_2_4.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x)==1]
	n2 = [x for x in n if n.count(x)==2]
	if len(n1) == 2 and len(n2) == 4 and sum(n1) > sum(set(n2)):
		k += 1
print(k)


#9_2_5
print('Ответ 9_2_5:', end = " ")

k = 0 
for s in open('9_2_5.txt'):
	n = sorted([int(x) for x in s.split()])
	np = [x for x in n if n.count(x) > 1]
	if len(np) != 0 and max(n) not in np and sum(np) > max(n):
		k += 1
print(k)


#9_2_6
print('Ответ 9_2_6:', end = " ")

k = 0 
for s in open('9_2_6.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x) == 1]
	np = [x for x in n if n.count(x) > 1]
	if len(np) != 0 and len(n1) != 0 and sum(n1)/len(n1) > sum(np)/len(np):
		k += 1
print(k)


#9_2_7
print('Ответ 9_2_7:', end = " ")

k = 0 
for s in open('9_2_7.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x) == 1]
	n2 = [x for x in n if n.count(x) == 2]
	if len(n2) == 2 and len(n1) == 4 and sum(n1)/len(n1) <= sum(n2):
		k += 1
print(k)


#9_2_8
print('Ответ 9_2_8:', end = " ")

k = 0 
for s in open('9_2_8.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[0] * 6 < n[1] + n[2] + n[3] and n[0]*n[3] > n[1]*n[2]:
		k += 1
print(k)


#9_2_9
print('Ответ 9_2_9:', end = " ")

k = 0 
for s in open('9_2_9.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x)==1]
	if len(n1) == 6 and (n[0]+n[5])/2 < (n[1]+n[2]+n[3]+n[4])/4:
		k += 1
print(k)


#9_2_10
print('Ответ 9_2_10:', end = " ")

k = 0 
for s in open('9_2_10.txt'):
	n = sorted([int(x) for x in s.split()])
	n1 = [x for x in n if n.count(x) == 1]
	np = [x for x in n if n.count(x) > 1]
	if len(np) != 0 and max(n) not in np and sum(np) < max(n):
		k += 1
print(k)


#9_2_11
print('Ответ 9_2_11:', end = " ")

k = 0 
for s in open('9_2_11.txt'):
	n = sorted([int(x) for x in s.split()])
	n4 = [x for x in n if n.count(x) == 4]
	n1 = [x for x in n if n.count(x) == 1]
	if len(n4) == 4 and len(n1) == 3 and n4[0] > sum(n1)/len(n1):
		k += 1
print(k)


#9_2_12
print('Ответ 9_2_12:', end = " ")

k = 0 
for s in open('9_2_12.txt'):
	n = sorted([int(x) for x in s.split()])
	n2 = [x for x in n if n.count(x) == 2]
	n1 = [x for x in n if n.count(x) == 1]
	if len(n2) == 4 and len(n1) == 3 and sum(n1)/len(n1) > sum(n2)/len(n2):
		k += 1
print(k)


#9_3
print('Ответ 9_3:', end = " ")

nrow = [] 
for s in open('9_3.txt'):
	nrow.append([int(x) for x in s.split()])

ncol = [[] for x in range(0, 6)]
for s in nrow:
	for i in range(0, 6):
		ncol[i].append(s[i])

k = 0 # Кол-во строк с подходящим условием	
for s in nrow:
	t = 0 # Кол-во ячеек в строке с подходящим условием
	for x in range(0, 6):
		if s.count(s[x]) == 1 and ncol[x].count(s[x]) > 150:
			t += 1
	if t >= 5:
		k += 1
print(k)


#9_3_1
print('Ответ 9_3_1:', end = " ")

n = []
for s in open('9_3_1.txt'):
	n.append([int(x) for x in s.split()])

k = 0 # Кол-во строк с подходящим условием	
for s in n:
	t = 0 # Кол-во ячеек в строке с подходящим условием
	for x in range(0, 6):
		if s.count(s[x]) == 1:
			r = 0 # Кол-во повторений s[x] во всей таблице
			for sr in n:
				r += sr.count(s[x])
			if r == 51:
				t += 1
	if t >= 1:
		k += 1
print(k)


#9_3_2
print('Ответ 9_3_2:', end = " ")

n = []
for s in open('9_3_2.txt'):
	n.append([int(x) for x in s.split()])

k = 0 # Кол-во строк с подходящим условием	
for s in n:
	t = 0 # Кол-во ячеек в строке с подходящим условием
	for x in range(0, 6):
		if s.count(s[x]) == 1:
			r = 0 # Кол-во повторений s[x] во всей таблице
			for sr in n:
				r += sr.count(s[x])
			if r == 46:
				t += 1
	if t >= 1:
		k += 1
print(k)


#9_4
print('Ответ 9_4:', end = " ")

k = 0
for s in open('9_4.txt'):
	n = sorted([int(x) for x in s.split()])
	if n[3]**2 > n[0]*n[1]*n[2] or n[3]-n[2] == n[2]-n[1] == n[1]-n[0]:
		k += 1
print(k)
