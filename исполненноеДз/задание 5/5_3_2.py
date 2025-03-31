for i in range(3,1000): #?????
    n = bin(i)[2:]
    n = n[:-1] + n[1] + n[1]
    r = int(n, 2)
    if r > 92:
        print(i)
        break