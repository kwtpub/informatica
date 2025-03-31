def d(a,b,c):
    an = sorted([a,b,c])
    return an[0] + an[1] > an[2]

    
def f(x,a):
    return not ((d(x, 11, 18) == (not (max(x, 5) > 68))) and d(x, a, 5))


for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a) #64