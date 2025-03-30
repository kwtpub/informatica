def to_base(n,bs):
    a = []
    while n > 0: 
        a = [n%bs] + a 
        n //= bs 
    return a

a = [6,5,11]
for j in range(0,100):
    if len(to_base(j,6)) == 2 and len(to_base(j,5)) == 3 and (to_base(j,11))[-1] == 1:
        print(j)

