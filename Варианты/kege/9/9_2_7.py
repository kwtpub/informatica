k = 0 

for s in open('kege/9/9_2_7.txt'):
    n = sorted([int(x) for x in s.split()])
    n1 = [int(x) for x in n if n.count(x) == 1]
    n2 = [int(x) for x in n if n.count(x) == 2]
    if len(n2) == 2 and len(n1) == 4 and sum(n1)/len(n1) <= sum(n2):
        k += 1 
print(k)