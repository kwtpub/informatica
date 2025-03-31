P = {x for x in range(2,20,2)}
Q = {x for x in range(5,50,5)}
A = set(range(1,1000))

def f(x):
    a = x in A
    p = x in P
    q = x in Q
    return (a <= p) and (q <= (not a))
for x in range(1000):
    if f(x)==0:
        A.remove(x)
print(len(A))