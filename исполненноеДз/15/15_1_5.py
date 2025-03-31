def f(x,y,a):
    return (x * y > a) and (x > y) and (x < 8)

for a in range(0,1000):
    if all(f(x,y,a)==0 for x in range(0,1000) for y in range(0,1000)):
        print(a) #42
