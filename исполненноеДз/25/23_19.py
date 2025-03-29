def f(x):
    d = set()

    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(125697,125721+1):
    n = f(i)
    for j in range(0,len(n)):
        if len(f(n[j])) == 0 and len(f(i//n[j])) == 0 and n[j] != i//n[j]:
            print(n[j],i//n[j])
            break