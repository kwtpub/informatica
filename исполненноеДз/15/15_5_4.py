n = {x for x in range(1,12,2)}
p = {3,6,9,12}
a = set()

def f(x):
    N = x in n
    P = x in p
    A = x in a
    return N <= (not P) or A
for x in range(0,1000):
    if f(x) == 0:
        a.add(x)
print(a) #12