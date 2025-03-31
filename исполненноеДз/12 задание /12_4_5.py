for i in range(3,1000):
    n = '3'+ '5' * i
    while '25' in n or '355' in n or '555' in n:
        if '25' in n:
            n = n.replace('25', '3', 1)
        if '355' in n:
            n = n.replace('355', '52', 1)
        if '555' in n:
            n = n.replace('555', '23', 1)
    if sum(map(int,str(n))) == 27:
        print(i)
##16


