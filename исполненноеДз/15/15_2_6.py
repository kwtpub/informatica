def d(n, m): 
    return  n % m
        

    
def f(x,a):
    return(d(x,15) and (not d(x,21))) <= ((not d(x,a)or d(x,15)))

for a in range(1,10000):
    if all(f(x,a) for x in range(1,10000)):
        print(a)
        break