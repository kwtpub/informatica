k = 0 
nmn = 1
for s in open('kege/9/9_2_8.txt'):
    n = sorted([int(x) for x in s.split()])
    if n[0] * 6 < n[1] + n[2] + n[3] and n[0]*n[3] > n[1]*n[2]:
        k += 1
print(k)