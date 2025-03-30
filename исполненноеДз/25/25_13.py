def f(x):
    d = set()
    
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k = 0 
for i in range(300_000,300_000+5000):
    z = []
    n = f(i)
    if k == 4:
        break
    for j in n: 
        if j % 3 == 0:
            z.append(j)
    if len(z) == 5:
        k += 1
        print(i,z[-1])
