def tob(n,base):
    a = []
    while n > 0:
        a =  [n % base] + a
        n = n // base
    return a

a = 5*216**1156 - 4*36**1147 + 6**1153 - 875 

res = tob(a,6).count(5) - tob(a,6).count(0)
print(res)