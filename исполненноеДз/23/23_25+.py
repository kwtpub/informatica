def f(a,b, k):
    if a == b: 
        return 1 
    if a > b or k > 3: 
        return 0 
    else: 
        return f(a+2,b, k) + f(a*3,b, k+1) + f(a*5,b,k+1) 

print(f(2,200,0))
