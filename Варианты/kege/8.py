k = 0
for i in range(1,100000):
    n = oct(i)[2:]
    print(len(n))
    if len(n) == 5 and n[0] != '0' and int(n[0]) % 2 == 0 and n[-1] not in '26' and n.count('7') <= 2:
        k += 1 
print(k)