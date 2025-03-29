k = 0 
for s in open('kege/9/9_2_11.txt'):
    n = sorted([int(x) for x in s.split()])
    n4 = [int(x) for x in n if n.count(x) == 4]
    n1 = [int(x) for x in n if n.count(x) == 1]
    if len(n4) == 4 and len(n1) == 3 and sum(n4)/len(n4) > sum(n1)/len(n1):
        k += 1
print(k)