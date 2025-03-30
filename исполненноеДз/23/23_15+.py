def f(a,b):  
    if a == b:
        return 1 
    if a > b or a == 43: 
        return 0 
    else: 
        return f(a+2,b) + f(a*2-1, b) + f(a*2+1,b)

print(f(7,63)) 116

