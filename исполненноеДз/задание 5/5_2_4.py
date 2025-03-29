for i in range(1,1000):
    n = bin(i)
    n = n + str(n.count('1') % 2) 
    n = n + str(n.count('1') % 2) 
    r = int(n, 2)
    if r > 93:
        print(r)
        break