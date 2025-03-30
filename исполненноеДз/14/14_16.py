for i in range(10,40):
    n = bin(i)[2::]
    print(i ,n[-4] + n[-3] + n[-2] + n[-1])
