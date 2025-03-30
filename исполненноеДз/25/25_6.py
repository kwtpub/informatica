def f(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k = 0
for i in range(500_000,500_000+5000):
    if k == 5:
        break
    n = f(i)
    for j in n:
        if len(str(j))>1 and str(j)[-1] == '8':
            k += 1 
            print(i)
            break
