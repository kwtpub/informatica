def d(n, m): 
    if n % m == 0:
        return 1
    else:
        return 0

def f(x,a):
    return d(a, 45) and (d(750,x) <= ((not d(a,x)) <= (not d(120,x))))

for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,300) for y in range(1,300)):
        print(a) #90
        break
