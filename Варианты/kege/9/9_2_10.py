k = 0
for s in open('kege/9/9_2_10.txt'):
    n = [int(x) for x in s.split()]
    n2 = [int(x) for x in n if n.count(x) > 1]
    if len(n2) != 0 and max(n) not in n2 and sum(n2) < max(n):
        k += 1 

print(k)