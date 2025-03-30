def to_base(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a



a = 51 * 7**12 - 7**3 - 22 

r = to_base(a,7)
print(sum(r))