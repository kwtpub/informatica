for i in range(0,1000):
    n = bin(i)[2::]
    if sum(map(int,n)) % 2 == 0: 
        n = '0' + n
        n = n[::-1]
        n = n[2::]
        n = n[::-1]
        n = n + '10'
    else: 
        n = '1' + n 
        n = n[::-1]
        n = n[2::]
        n = n[::-1]
        n = n + '11'
    r = int(n,2)
    if r > 19:
        print(i) 8
    