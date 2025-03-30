# def f(a,b):
#     if a == b: return 1 
#     elif a > b: return 0
#     else: return f(a+1,b) + f(a*2,b) + f(a**2,b)

# print(f(5,154)) 


# def f(a,b): 
#     if a == b: return 1
#     if a > b: return 0 
#     else: return f(a+1, b) + f(a+2, b)  + f(a+3, b)

# print(f(1,8) * f(8,15))

# def f(a,b): 
#     if a == b: return 1
#     if a > b or a == 6: return 0 
#     else: return f(a+2, b) + f(a*3, b)

# print(f(1,25) * f(25,63))

# def f(a,b): 
#     if a == b: return 1
#     if a > b: return 0 
#     else: return f(a+1, b) + f(a*2, b)  + f(2*a+1, b) + f(a*10, b)


# print(f(1,15)) 


# def f(a,b): 
#     if a == b: return 1
#     if a > b: return 0 
#     else: return f(a + 2, b) + f(a + 4, b)  + f(a + 5, b)

# for b in range(31,1000):
#     if f(31,b) == 1001:
#         print(b)

# def f(a,b, k): 
#     if a == b and k == 0: return 1
#     if a > b or k < 0: return 0 
#     else: return f(a + 31, b, k-10) + f(a * 4, b, k-10)  + f(a * 5, b, k-10)

# print(f(1,4400,700))


def f(a,b, k): 
    if a % 2 != 0: k += 1 
    if a == b and k == 1: return 1
    if a > b or k > 1: return 0 
    else: return f(a + 1, b, k) + f(a +2, b, k)  + f(a * 2, b, k)

print(f(2,40, 0))