for i in range(60,1000):
    n = '1' * i
    while '111' in n:
        n = n.replace('111', '2', 1)
        n = n.replace('222', '11', 1)
    if n == '221':
        print(i, n)
##63