for i in '1234567890abcdefg':
    a = int(f'9759{i}', 17) + int(f'3{i}108', 17)
    if a % 11 == 0:
        print(i,a//11)
