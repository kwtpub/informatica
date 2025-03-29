k = 0 
for s in open('kege/9/9_2_4.txt'):
    n = sorted([int(x) for x in s.split()])
    n1 = sorted([int(x) for x in n if n.count(x) == 1])
    n2 = sorted([int(x) for x in n if n.count(x) == 2])
    if len(n1) == 2 and len(n2) == 4 and sum(set(n2)) < sum(n1):
        k += 1
print(k)