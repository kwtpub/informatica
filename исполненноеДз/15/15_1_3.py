def f(x,y,a):
    return (x>a) or (y>x) or (2*y + x < 110)
for a in range(1,1000):
    if all(f(x,y,a) for x in range(1,100) for y in range(1,100)):
        print(a) #36
        