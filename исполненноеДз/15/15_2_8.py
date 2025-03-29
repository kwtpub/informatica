def d(n, m): 
    if n % m == 0:
        return 1
    else:
        return 0

def f(x,a):
    return d(a,7) and (d(240,x) <= ((not d(a,x)) <= (not d(780,x))))

for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a)
        break #420