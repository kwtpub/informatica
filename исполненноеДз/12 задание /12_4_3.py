for i in range(1,1000):
    for j in range(1,1000):
        if j == i:
            n = '0' + '1' * i + '2' * j + '0'
            while '00' not in n:
                n=n.replace('011','20', 1)
                n=n.replace('022','10', 1)
                n=n.replace('01','220', 1)
                n=n.replace('02','110', 1)
            print('кол-во 1: ', n.count('1'), 'кол-во 2:', n.count('2'))

#???