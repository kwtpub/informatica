def to_base(n,bs):
    a = []
    while n > 0: 
        a = [n%bs] + a 
        n //= bs
    return a 

for i in range(2,32):
    n = to_base(68,i)
    print(n)
