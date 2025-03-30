#25_1
print('Ответ 25_1:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
	
for i in range(174457, 174505+1):
	if len(f(i)) == 2:
		print('\t', *f(i))
	
	
#25_2
print('Ответ 25_2:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
	
for i in range(81234, 134689+1):
	if len(f(i)) == 3:
		print('\t',*f(i))
		
		
#25_3
print('Ответ 25_3:')

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
	
for i in range(154026, 154043+1):
	if len(f(i)) == 4:
		print('\t',*f(i)[2:])
		

#25_4
print('Ответ 25_4:')
def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(100812, 100923+1):
	d = f(i)
	if len(d) == 6:
		print('\t',*d)
		
		
#25_5
print('Ответ 25_5:')
def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
k = 1
for i in range(194441, 196500+1):
	d = f(i)
	if len(d)%2!=0:
		print('\t', k, i, len(d), int(i**0.5))
		k += 1
		
		
#25_5_1 
print("Ответ 25_5_1:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(174457, 174505+1):
	d = f(i)
	if len(d) == 2:
		print('\t', d[0], d[1])
		

#25_5_2
print("Ответ 25_5_2:")
def f(n):
	d = set()
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(201455, 201470+1):
	d = f(i)
	if len(d) == 4:
		print('\t', d[0],d[1],d[2],d[3])
		
			
#25_6
print('Ответ 25_6:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
k = 0
for i in range(150001, 200000):
	if sum(f(i)) % 13 == 10 and k < 7:
		k += 1
		print('\t',i, sum(f(i)))
		
		
#25_7
print('Ответ 25_7:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(250201, 250201+1000):
	d = f(i)
	if len(d) > 1 and (max(d) + min(d)) % 123 == 17:
		print('\t', i, max(d) + min(d))


#25_8
print('Ответ 25_8:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
k = 0
for i in range(550000, 600000):
	if len(f(i)) > 1 and sum(f(i))//len(f(i)) % 31 == 13 and k < 5:
		k += 1
		print('\t',i, sum(f(i))//len(f(i)))
		

#25_9
print('Ответ 25_9:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(400000001, 400000000+10000):
	d = f(i)
	if len(f(i)) >= 5:
		pn = d[0] * d[1] * d[2] * d[3] * d[4] 
		if pn % 100 == 17 and pn <= i:
			print('\t',pn, d[4])
			
			
#25_10
print('Ответ 25_10:')

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(190201, 190260+1):
	d = f(i)
	a = set()
	for i in range(0,len(d)):
		if d[i] % 2 == 0:
			a.add(d[i])
	if len(a) == 4:
		print('\t',*sorted(a)[::-1][:2])
		

#25_11
print('Ответ 25_11:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(1204300, 1204380+1):
	d = f(i)
	a = set()
	for j in range(0,len(d)):
		if d[j] % 2 == 0:
			a.add(d[j])
	if sum(a) % 10 == 0 and sum(a) != 0:
		print('\t',i, sum(a))
		

#25_12
print('Ответ 25_12:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(500000, 500000+100):
	d = f(i)
	a = []
	for j in range(0,len(d)):
		if d[j] % 10 == 8 and d[j] != 8:
			a.append(d[j])
	if len(a) != 0:
		print('\t',i,a[0])


#25_13
print('Ответ 25_13:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(300001, 300001+1000):
	d = f(i)
	a = []
	for j in range(0,len(d)):
		if d[j] % 3 == 0: 
			a.append(d[j])
	if len(a) == 5:
		print('\t',i, a[-1])


#25_14
print('Ответ 25_14:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for x in range(550001, 550001+1000):
	d = f(x)
	a = []
	for i in range(0,len(d)):
		if d[i] % 10 == 7:
			a.append(d[i])
	if len(a) == 3:
		print('\t',x,a[-1])
		
		
#25_15
print('Ответ 25_15:')
def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(321654, 654321+1):
	d = f(i)
	p = True
	for j in range(len(d)):
		if d[j]%2==0:
			p = False
	if p and len(d) > 70:
		print('\t', i, max(d))
		
	
#25_16
print('Ответ 25_16:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(6080068, 6080176+1):
	if len(f(i)) == 0:
		print('\t',i)
		

#25_17
print('Ответ 25_17:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for x in range(25317,51237+1):
	d = f(x)
	a = []
	for i in range(0,len(d)):
		if len(f(d[i])) == 0:
			a.append(d[i])
	if len(a) >= 6:
		print('\t',x,a[-1])
		

#25_18
print('Ответ 25_18:')

def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for x in range(500000,499000,-1):
	d = f(x)
	a = []
	for i in range(0,len(d)):
		if len(f(d[i])) == 0:
			a.append(d[i])
	if sum(a) % 10 == 0 and sum(a) != 0:
		print('\t',x, sum(a))
			
			
#25_19
print('Ответ 25_19:')

def f(n):
	d = set()
	for i in range(2,int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
	
for x in range(125697, 125721+1):
	d = f(x)
	for i in range(0,len(d)):
		if len(f(d[i])) == 0 and len(f(x//d[i]))==0 and d[i] != x//d[i]:
			print('\t',d[i],x//d[i])
			break

#25_20
print('Ответ 25_1:')

def prost(n):
	return n > 1 and all(n%i!=0 for i in range(2,int(i**0.5)+1))
k = 1
for i in range(6638225, 6638322+1):
	if prost(i):
		print('\t',i)
		k += 1
		

#25_21
print("Ответ 25_21:")
def prost(n):
	return n > 1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
k = 0
for i in range(2422000, 2422080+1):
	if prost(i):
		k+=1
		print('\t', k, i)
		
		
#25_22
print("Ответ 25_22:")
def f(n):
	d = set()
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			d.add(abs(i - n//i))
	return sorted(d)
for i in range(2000000, 3000000+1):
	d = f(i)
	if len(d) >= 3:
		if d[0] <= 115 and d[1] <= 115 and d[2] <= 115:
			print('\t',i)
			
			
#25_23
print("Ответ 25_23:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(600001, 600000+100):
	d = f(i)
	for j in range(len(d)):
		if d[j] != 7 and d[j]%10==7:
			print('\t', i, d[j])
			break

			
			
#25_24
print("Ответ 25_24:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(500000, 500000+100):
	d = f(i)
	for j in range(len(d)):
		if d[j] != 8 and d[j]%10==8:
			print('\t', i, d[j])
			break


#25_25
print("Ответ 25_25:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(700000, 700000+100):
	d = f(i)
	if len(d) > 1 and (min(d) + max(d))%10==8:
		print('\t',i, min(d) + max(d))
		
		
#25_26
print("Ответ 25_26:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(200000001, 200000000+100):
	d = f(i)
	m = 0
	if len(d) > 4: m = d[0] * d[1] * d[2] * d[3] * d[4] 
	if m > 0 and m < i:
		print('\t',m)
		
		
#25_27
print("Ответ 25_27:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(460000001, 460000000+100):
	d = f(i)
	m = 0
	if len(d) > 4: m = d[-5] 
	if m > 0:
		print('\t',m)
	
#25_28
print("Ответ 25_28:")
def f(n):
	d = set()
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(110203, 110245+1):
	d = f(i)
	k = []
	for j in range(len(d)):
		if d[j]%2==0:
			k.append(d[j])
	if len(k) == 4:
		print('\t',*k)

#25_29
print("Ответ 25_29:")
def f(n):
	d = set()
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			d.add(i)
			d.add(n//i)
	return sorted(d)
for i in range(452022, 452021+1000):
	d = f(i)
	if len(d) > 1 and (min(d) + max(d))%7==3:
		print('\t', i, min(d) + max(d))
		
		
#25_30
print("Ответ 25_30:")
for i in range(0,10**10, 3023):
	if fnmatch(str(i), '1?954*21'):
		print('\t', i)
		

#25_31
print("Ответ 25_31:")
for i in range(0,10**10,2023):
	if fnmatch(str(i), '1?493*41'):
		print('\t', i)
		

#25_32
print("Ответ 25_32:")
for i in range(0,10**10, 2023):
	if fnmatch(str(i), '1?2139*4'):
		print('\t', i, i//2023)
		
		
#25_33
print("Ответ 25_33:")
for i in range(0,10**9,23):
	if fnmatch(str(i), '12345?7?8'):
		print('\t', i, i//23)
		
		
#25_34
print("Ответ 25_34:")
for x in '0123456789':
	for y in '0123456789':
		d = int('12345' + x + '6' + y + '8')
		if d%17==0:
			print(d, d//17)
			
			
#25_35
print("Ответ 25_35:")
for i in range(0,10**8,141):
	if fnmatch(str(i), '1234*7'):
		print(i, i//141)
		
		
#25_36
print("Ответ 25_36:")
for i in range(0,10**9,169):
	if fnmatch(str(i), '123*567?'):
		print(i, i//169)
		
		
#25_37
print("Ответ 25_37:")
for i in range(0,10**6,51):
	if fnmatch(str(i), '12*45*'):
		print(i, i//51)


#25_38
print("Ответ 25_38:")

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(65001, 1000000):
	if fnmatch(str(i), '6*97*5?'):
		d = [x for x in f(i) if x%2==0]
		if len(d)>=4:
			print(i, sum(d))
			
			
#25_39
print("Ответ 25_39:")

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(10*6, 10**7):
	if fnmatch(str(i), '9?*55*7'):
		print(i, sum(f(i))%21)
		

#25_40
print("Ответ 25_40:")

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(0,10**7,168): # НОК(6,7,8) = 168
	if fnmatch(str(i), '?6*6*?6'):
		print(i, sum(f(i)))
		
		
#25_41
print("Ответ 25_41:")

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(0,10**7,217): 
	if fnmatch(str(i), '14?4*'):
		print(i, sum(x for x in f(i) if x%2!=0))
		
		
#25_42
print("Ответ 25_42:")

def f(n):
	d = set()
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			d.add(i)
			d.add(n//i)
	return sorted(d)

for i in range(700001,700000+1000): 
	if i%13 == 0 and not(fnmatch(str(i), '*0??3*') or fnmatch(str(i), '*4??2') or fnmatch(str(i), '*1*')) :
		print(i, sum(int(x) for x in str(i)))
		
