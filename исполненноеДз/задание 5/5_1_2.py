for i in range(1,1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = n + '00'
    else: 
        n = n + '11'
    r = int(n, 2)
    if r < 134:
        print(i)