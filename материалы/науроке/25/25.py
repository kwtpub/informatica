def f(x):
    b = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)


for i in range(81_234,134_689+1):
    n = f(i)
    if len(n) == 3:
        print(*n)

