for i in range(1,1000):
    n = bin(i)[2:]
    if sum(map(int, n)) % 2 == 0:
        n = n + '0'
        n = '10' + n[2:]
    elif sum(map(int, n)) % 2 == 1:
        n = n + '1'
        n = '11' + n[2:]
    if int(n,2) >= 50:
        print(i)