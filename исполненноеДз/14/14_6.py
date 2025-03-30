def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

a = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338

b = tob(a,15)



print(len(set(b)))