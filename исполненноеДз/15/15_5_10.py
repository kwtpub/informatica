a = set()
b = {1,2,4,8,16}
c = {3,4,9,16}

def f(x):
    A = x in a 
    B = x in b 
    C = x in c 
    return (not B) and (not C) or A

for x in range(0,1000):
    if f(x) == 0:
        a.add(x)
print(len(a)) #7