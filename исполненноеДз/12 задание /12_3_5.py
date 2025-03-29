b = set()

for i in range(1,1000):
    n = '5' * i
    while '555' in n or '888' in n:
        n = n.replace('555', '8', 1)
        n = n.replace('888', '55', 1)
    b.add(n)

print('i= ', i, 'n= ',n, b)
##8