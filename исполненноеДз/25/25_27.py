def f(x): 
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(460_000_001,460_000_000+100):
    d = f(i)
    m = 0 
    if len(d) > 4: m = d[-5] 
    if m > 0:
        print(m)
