a = '1234567890abcdefghijklm'
for x in a: 
    result = int(f'1{x}1{x}1{x}1{x}1', 23) + int(f'20{x}24',23) + int(f'1{x}235', 23)
    if result % 22 == 0: 
        print(result//22)
