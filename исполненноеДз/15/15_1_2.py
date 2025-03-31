def f(x,y,a):
    return (x*y < a) or (y > x) or (x >= 8)

for a in range(1,10000):
    if all(f(x,y,a) == 1 for x in range(1,300) for y in range(1,300)):
        print(a) #50