def f(x): 
    b = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)
k = 1
for i in range(194441,196500):
    n = f(i)
    if len(n) in [x for x in range(1,101,2)]:
        
        print(k,i,len(n),int(i**0.5))
        k += 1
