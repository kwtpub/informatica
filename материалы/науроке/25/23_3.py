def f(x):
    b = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)

k = 0 

for i in range(550_001,550_000+1000):   
    if k == 5:
        break
    n = f(i)
    f = 0 
    if len(n) > 0: 
        f = sum(n)//len(n)
    if f % 31 == 13: 
        k += 1 
        print(i,f)


