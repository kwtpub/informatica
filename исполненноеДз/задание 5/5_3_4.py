for i in range(128,256):
    n = bin(i)[2:]
    n = '0'*(8-len(n)) + n
    n = n.replace('1', '*').replace('0', '1').replace('*', '0')
    r = int(n, 2)
    f = i - r
    if f == 105:
        print(i)
        break