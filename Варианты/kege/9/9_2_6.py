k = 0 
for s in open('kege/9/9_2_6.txt'):
    n = sorted([int(x) for x in s.split()])
    n1 = [int(x) for x in n if n.count(x) == 1]
    n2 = [int(x) for x in n if n.count(x) > 1]
    if len(n1) != 0 and len(n2) != 0 and sum(n1)/len(n1) > sum(n2)/len(n2):
        k += 1 
print(k)