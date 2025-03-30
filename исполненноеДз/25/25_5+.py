def f(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k = 0 
for i in range(250200,250200+1000):
    if k == 5:
        break
    n = f(i)
    if len(n) > 1:
        a = n[0] + n[-1]
    if len(n)>1 and a % 123 == 17: 
        k += 1 
        print(i,a)

