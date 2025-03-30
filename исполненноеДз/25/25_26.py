def f(x): 
    b = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)
k = 0 
for i in range(200000001, 200000000+5000):
    if k == 5:
        break
    d = f(i)
    m = 0
    if len(d) > 4: 
        m = d[0] * d[1] * d[2] * d[3] * d[4] 
    if m > 0 and m < i:
        k += 1
        print(m)

