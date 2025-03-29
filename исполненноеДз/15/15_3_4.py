def f(x,a):
    return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & 13))

for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a) #13