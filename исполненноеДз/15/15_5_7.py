n = {12,23,34,45,56}
p = {23,35,56,68,89}
a = set(range(1,1000))

def f(x):
    N = x in n
    P = x in p 
    A = x in a 
    return N or P or (not A)

for x in range(1000):
    if f(x)==0:
        a.remove(x)
print(len(a)) #8
