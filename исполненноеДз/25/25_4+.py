def f(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(201455,201470):
    n = f(i)
    if len(n) == 4:
        print(n)
