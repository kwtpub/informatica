def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a
for x in range(0,2000):
    a = 125**200 - 5**x + 74 
    if tob(a,5).count(4) == 100:
        print(x)