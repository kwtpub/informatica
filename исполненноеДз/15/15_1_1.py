def f(x,y,a):
    return (x*y < 121) or (y > a) or (x >= a)

for a in range(1,1000):
    if all(f(x,y,a) ==1 for x in range(1,100) for y in range(1,100)):
        print(a) #11
