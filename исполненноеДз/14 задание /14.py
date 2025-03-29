for x in range(3,50):
    t = x 
    a = []
    while x>0:
        a = [x%3] + a 
        x //= 3
    if a[-2]==2 and a[-1]==1:
        print(t)