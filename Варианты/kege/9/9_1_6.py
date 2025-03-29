k = 0 
for s in open('kege/9/9_1_6.txt'):
    n = sorted([int(x) for x in s.split()])
    if n[0]*n[1] + n[0]*n[2] > n[1]*n[2]:
        k += 1 
print(k)