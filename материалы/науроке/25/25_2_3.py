from fnmatch import * 

def f(x):
    b = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            b.add(i)
            b.add(x//i)
    return sorted(b)

k = 0 
for i in range(65000,65000+1000000):
    if k == 7: 
        break
    if fnmatch(str(i), '6*97*5?'):
        d = f(i)
        a = [x for x in d if x % 2 == 0]
        if len(a) >= 4:
            print(i, sum(a))
            k += 1 
