def f(a,b): 
    if a == b: 
        return 1 
    if a > b: 
        return 0 
    else: 
        return f(a+1,b) + f(a*2,b) + f(a**2,b)

print(f(5,154)) 896return n


