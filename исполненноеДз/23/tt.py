def plus_one(val):
    if val == 9: return 9
    return val + 1 

def f(x): 
    s = ''
    n = [int(i) for i in str(x)]
    result = list(map(plus_one,n))
    for i in result:
        s += str(i)
    return s

print(f(29))
