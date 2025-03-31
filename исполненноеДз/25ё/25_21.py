def f(x):
    d = set()

    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

k = 0
for i in range(2422000,2422080): 
    if len(f(i)) == 0: 
        print(f'{k}: {i}')