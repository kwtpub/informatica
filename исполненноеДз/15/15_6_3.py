def d(n, m): 
    return  n % m

def f(x,a):
    return (a + x > 700 - a) and (d(a,100) + d(100,x) > 50)

for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a) #351
        break