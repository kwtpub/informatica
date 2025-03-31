for N in range(0,1000):
    R = bin(N)[2:]
    if int(R, 2) % 2 == 0:
        R = '10' + R 
    elif int(R, 2) % 2 != 0:
        R = '1' + R + '01'
    R1 = int(R, 2)
    if N <= 12:
        print(R1)