def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

a = 6 * 144**26 + 11 * 12**75 - 48 

res = tob(a,12).count(11)

print(res)