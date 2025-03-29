k = 0 
for s in open('kege/9/9_2_1.txt'):
    n = sorted(int(x) for x in s.split())
    n1 = [x for x in n if n.count(x) == 1]
    if len(n1) == 5 and 2*(min(n) + max(n)) <= sum(n) - (min(n) + max(n)):
        k += 1
print(k) 