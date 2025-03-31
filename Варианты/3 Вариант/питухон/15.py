def dels(n,m):
    return n % m == 0

def f(x,a):
    b = 200 <= x <= 300
    return dels(x,a) or (b <= (not dels(x,77)))

for a in range(1,1000): 
    if all(f(x,a) for x in range(1,1000)):
        print(a)
