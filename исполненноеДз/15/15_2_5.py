def d(n, m): 
    if n % m == 0:
        return 1
    else:
        return 0
    
def f(x,a):
    return ((not d(x,84)) or (not d(x,90)) <= (not d(x,a)))

for a in range(1,25000):
    if all(f(x,a) for x in range(1,300)):
        print(a) #5