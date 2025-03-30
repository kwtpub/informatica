def plus_one(val):
    if val == 9: return 9
    return val + 1 
def g(a): 
    s = ''
    n = [int(i) for i in str(a)]
    result = list(map(plus_one,n))
    for i in result:
        s += str(i)
    return int(s)

               
def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0 
    else: 
        return f(a+1,b) + f(g(a),b)

print(f(25,51))
