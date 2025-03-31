print('x y z w  f1 True')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((x <= y) == (w or (not(z)))) == 1: 
                    print(x,y,z,w)
                    
print('x y z w  f2 True')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((x <= y) and ((not(w)) == z)) == 1: 
                    print(x,y,z,w)
print('x y z w  f1 False')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((x <= y) == (w or (not(z))))  == 0: 
                    print(x,y,z,w)
                    
print('x y z w  f2 False')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((x <= y) and ((not(w)) == z)) == 0: 
                    print(x,y,z,w)