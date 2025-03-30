def to_base(n,base): 
    a = []
    while n > 0:
        a = [n % base] + a
        n = n // base
    return a

n = 3**100
for x in range(0,2030+1):
    a= n - x
    
    if to_base(a,3).count(0) == 1:
        print(x)
