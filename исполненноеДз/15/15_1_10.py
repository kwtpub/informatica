def f(x,y,a):
    return (x - 3*y < a) or (y > 400) or (x > 56)

for a in range(0,1000):
    if all(f(x,y,a) for x in range(0,100) for y in range(0,100)):
        print(a)
        break #57