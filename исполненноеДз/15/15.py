def ch(x,y):
    return str(x)[-1] == str(y)[-1]
def f(x,a):
    return ((not ch(x,5)) and ch(x,4)) <= (x > a - 11)

for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,1000)):
        print(a)
