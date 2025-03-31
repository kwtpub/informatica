def f(x,y,a):
    return (4*x + y < a) or (x < y) or (22 <= x) 

for a in range(0,1000):
    if all(f(x,y,a) == 1 for x in range(0,100) for y in range(0,100)): 
        print(a)
