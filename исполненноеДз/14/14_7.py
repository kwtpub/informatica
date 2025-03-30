def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

a = 3*3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024

res = tob(a,25)

print(res.count(0))