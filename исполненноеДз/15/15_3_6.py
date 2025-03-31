def f(x,a):
    return (x & 57 == 0) or (x & 23 == 0) <= (not (x & a == 0))

for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a) 
        break