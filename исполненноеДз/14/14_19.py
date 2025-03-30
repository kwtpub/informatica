def to_base(n,bs):
    a = []
    while n > 0: 
        a = [n%bs] + a 
        n //= bs 
    return a

k = 0
for i in range(1,1000):
    if len(to_base(i,5)) <=4 and len(to_base(i,2)) >=5 and (to_base(i,16))[-1] == 12:
        k += 1

print(k)
