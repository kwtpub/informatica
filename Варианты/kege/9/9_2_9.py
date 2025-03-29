k = 0 
for s in open('kege/9/9_2_9.txt'):
    n = sorted([int(x) for x in s.split()])
    n2 = [int(x) for x in n if n.count(x) > 1]
    if len(n2) == 0 and (n[0] + n[5])/2 < (n[1] + n[2] + n[3] + n[4])/4:
        k += 1

print(k)