def to_base(x,bs):
    if x == 0: 
        return '0'
    a = []
    s = ''
    while x > 0: 
        a = [x%bs] + a 
        x = x // bs 
    for i in a: 
        s += str(i)
    return s
n = 0
for i in range(1,100):
    n = to_base(i,4)
    if i % 4 == 0: 
        n = n + n[-2] + n[-1]
    else: 
        n = n + to_base((i%4)*2,4)
    r = int(n,4)
    if r < 261: 
        print(r,i)

