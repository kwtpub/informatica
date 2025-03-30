def f(x):
    b = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)

for i in range(400_000_001,400_000_000+100000):
    n = f(i)
    p = 0
    if len(n) > 4: 
        p = n[0] * n[1] * n[2] * n[3] * n[4]
    if p % 100 == 17 and p <= i:
        print(p,n[4])


