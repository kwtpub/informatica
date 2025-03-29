def f(x): 
    d = set()

    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d) 
k = 0 
for i in range(550_000,550_000+5000): 
    if k == 5:
        break
    z = []
    n = f(i)
    for j in n: 
        if str(j)[-1] == '7':
            z.append(j)
    if len(z) == 3: 
        k += 1
        print(i,sorted(z)[-1])