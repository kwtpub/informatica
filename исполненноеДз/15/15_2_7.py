def d(n, m): 
    return n % m 


def f(x,a):
    return ((d(x,4)!=3) or (d(x,6) != 1)) <= (d(x,36) != a)

for a in range(1,1000):
    if all(f(x,a)==1 for x in range(1,1000)):
        print(a) #7