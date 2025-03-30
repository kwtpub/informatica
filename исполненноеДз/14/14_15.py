def f(x,bs):
    a = []
    s = ''
    while x > 0: 
        a = [x%bs] + a 
        x = x // bs
    for i in a:
        s += str(i)
    return int(s)


for i in range(20,31):
    if f(i,3) % 100 == 11: 
        print(i)
