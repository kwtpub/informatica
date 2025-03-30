def f(x):
    b = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)

k = 0
for i in range(150_001,150_000+1000):
    if k == 7:
        break
    s = sum(f(i))
    if s % 13 == 10:
        k += 1
        print(i,s)

