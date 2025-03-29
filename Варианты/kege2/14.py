def f(n, base):
    s = ''
    while n >0:
        s = str(n% base) + s
        n = n // base
    return s


sum = 0
for x in range(0,2030+1):
    sum = 7**91 + 7**160 - x
    sum = f(sum,7)
    if sum.count('0') == 70:
        print(x)
