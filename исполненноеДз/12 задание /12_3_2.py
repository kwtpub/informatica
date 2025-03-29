for i in range(100,1000):
    n = '1' * i 
    while '111'in n:
        n = n.replace('111', '22', 1)
        n = n.replace('222', '11', 1)
    print(i ,n.count('1'))
##104