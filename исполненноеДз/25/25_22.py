def f(x): 
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i - x//i)
    return sorted(d)

for i in range(2000000, 3000000+1):
    n = f(i)
    if 
