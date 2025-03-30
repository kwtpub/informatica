def f(a,b,k):
    if a % 2 == 0: 
        k += 1 
    if a == b and k == 6: 
        return 1 
    if a > b:
        return 0 
    else: 
        return f(a+1,b,k) + f(a+3,b,k) + f(a+5,b,k)

print(f(3,25,0))
