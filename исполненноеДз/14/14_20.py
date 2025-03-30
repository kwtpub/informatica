for x in '0123456789abcde':
    n = x 
    a = int(f'123{n}5', 15) + int(f'1{n}233',15)
    if a % 14 == 0:
        print(x,a//14)

