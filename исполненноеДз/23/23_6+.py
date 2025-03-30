def f(a,b): 
    if a == b:
        return 1 
    if a > b: 
        return 0 
    else: 
        return f(a+1, b) + f(a+2,b) + f(a+3,b)

print(f(1,8) * f(8,15)) 1936
