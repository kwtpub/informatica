def tobase(n,bs):
    a = []
    while n > 0:
        a = [n%bs] + a 
        n = n//bs
    return a 

expression = 3 * 16**8 - 4**5 + 3 

result = tobase(expression, 4).count(3)

print(result)