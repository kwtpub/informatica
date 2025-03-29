def d(n,m):
    if n % m == 0:
        return 1
    else:
        return 0
    
def f(x,y,a):
    return d(120,a) or (not d(x,a) <= (d(x,18) <= d(x,24)))

for a in range(1,1000):
    if all(f(x,y,a) for x in range(1,100) for y in range(1,100) ):
        print(a) #120