for i in range(200, 1000):
    n = '1' * i
    while '1111' in n:
        n = n.replace('1111', '22', 1)
        n = n.replace('222', '1', 1)
    print(i, n.count('1'))
##204