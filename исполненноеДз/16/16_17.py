k = []

def f(n):
    global k
    k.append(n*n)
    if n >1:
        k.append(2*n+1)
        f(n-2)
        f(n//3)

print(f(100), sum(k))        