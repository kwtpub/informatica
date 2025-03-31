k = 0
for s in open('kege/9/9_1.txt'):
    n = sorted([int(x) for x in s.split()])
    if n[0]**2 +n[1]**2 > n[2]**2:
        k += 1
print(k) #1074