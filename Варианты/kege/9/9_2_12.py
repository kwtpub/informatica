k = 0 
for s in open('kege/9/9_2_12.txt'):
    n = [int(x) for x in s.split()]
    n2 = [int(x) for x in n if n.count(x) == 2]
    n1 = [int(x) for x in n if n.count(x) == 1]
    if len(n2) == 4 and len(n1) == 3 and sum(n1)/len(n1) > sum(n2)/len(n2):
        k += 1 

print(k)