def to_base(n,bs):
    a = []
    while n > 0: 
       
        a = [n%bs] + a 
       
        n = n // bs

    return a 
b = set()
def f(a,k): 
    if k == 15: 
        b.add(a)
    else: 
        f(a*2,k+1) 
        f(a*2+1,k+1)

f(1,0)

print(len(b))
