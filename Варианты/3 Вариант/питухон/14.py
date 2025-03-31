def to_base(n, bs): 
    a = []
    while n > 0: 
        a = [n % bs] + a 
        n = n // bs 
    return a

for x in range(1,1000):
    rs = 6**2025 + 6**25 - x
    if to_base(rs,6).count(0) == 2002:
        print(x)
