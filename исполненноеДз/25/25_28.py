def f(x):
    d = set()
    for i in range(1,x+1):
        if x % i == 0: 
            if i % 2 == 0:
               d.add(i)
    return sorted(d)

for i in range(110203,110245): 
    d = f(i)
    if len(d) == 4: 
        print(d[0],d[1],d[2],d[3])

