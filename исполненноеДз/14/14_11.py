def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

a = tob(33,4).split()
print(a)

for x in range(0,1000):
    res = tob(33,x+4) - tob(33, 4)
    if res == 33:
        print(x)