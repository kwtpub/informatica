def f(x,y,a):
    return (2*x + y != 70) or (x < y) or (a<x)

for a in range(0,1000):
    if all(f(x,y,a) for x in range(0,100) for y in range(0,100)):
        print(a) #23