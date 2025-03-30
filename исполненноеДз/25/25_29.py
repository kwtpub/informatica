def f(x): 
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)
k = 0
for i in range(452022,452021+1000): 
    if k == 5:
        break
    n = f(i)
    m = 0 
    if len(n) > 0: m = min(n) + max(n)
    if m % 7 == 3: 
        k += 1
        print(i,m)
