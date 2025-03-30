def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

for x in range(0,1000):
    a = 36**17 - 6**x + 71 
    res = sum(map(int, tob(a,6)))
    if res == 61:
        print(x)

