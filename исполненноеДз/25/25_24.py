def f(x): 
    d = set()
    for i in range(1,int(x**0.5)+1): 
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)
k = 0 
for i in range(500000, 500000+5000): 
    if k == 5: 
        break
    n = f(i)
    n1 = [x for x in n if x % 10 == 8 and x != 8]
    for x in n: 
        if x % 10 == 8 and x != 8 and x != i: 
            print(i,min(n1))
            k += 1
            break
    
