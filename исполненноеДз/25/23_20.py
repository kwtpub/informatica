def f(x):
    d = set()

    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

k = 0
for i in range(6638225,6638322):
    if len(f(i)) == 0: 
        k+= 1 
        print(f'{k}: {i}')