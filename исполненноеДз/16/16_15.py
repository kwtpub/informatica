def f(n): 
    if n == 0:
        return 0
    elif n %2==0:
        return f(n/2)
    elif n%2!= 0:
        return 1 + f(n-1)
k = 0
for i in range(1,500+1):
    if f(i) == 8:
        k +=1 
print(k)