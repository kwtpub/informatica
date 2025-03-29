k = 0
for s in open('kege/9/9_2_3.txt'):
    n = sorted([int(x) for x in s.split()])
    n1 = [int(x) for x in n if n.count(x) == 1]
    nCh = [int(x) for x in n if x % 2 == 0]
    nNch = [int(x) for x in n if x % 2 != 0]
    if len(n1) == 5 and len(nNch) > len(nCh) and sum(nNch) < sum(nCh):
        k += 1 
print(k)