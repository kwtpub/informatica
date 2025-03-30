def f(x):
    b = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)
    


for i in range(100812,100923+1):
    n = f(i)
    if len(n) == 6:
        print(*n)
