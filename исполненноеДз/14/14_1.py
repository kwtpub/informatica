def to_base(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

num = 64**30 + 2**300 - 4

result = (to_base(num, 8).count(7))

print(result)