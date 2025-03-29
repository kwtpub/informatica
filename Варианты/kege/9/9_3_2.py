k = 0 
nall = []
for s in open('kege/9/9_3_2.txt'):
    nall.append([int(x) for x in s.split()])
    
for s in nall:
    n = [int(x) for x in s.split()]
    n2 = [int(x) for x in n if n.count(x) != 2]
    nR = [int(x) for x in n if nall.count(x) == 45]
print(len(n2))
    