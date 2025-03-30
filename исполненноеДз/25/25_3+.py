def f(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

for j in range(174457,174505):
    n = f(j)
    if len(n) == 2:
        print(*n)

