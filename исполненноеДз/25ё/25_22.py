  def f(x):
    d = set()

    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(2_000_000,3_000_000):
    b = f(i)
    for i in range(0,len(b),+2):
        print()