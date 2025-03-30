def to_base(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

a = 2 * 27**7 + 3**10 - 9 

res = to_base(a,3).count(0)

print(res)