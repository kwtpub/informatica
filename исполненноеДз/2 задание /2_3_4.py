print('x y z w  True')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if (( (y <= w) == ( z <= (not(z)) ) ) and (x or w)) == 1: 
                    print(x,y,z,w)
                    
print('x y z w  False')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if (((y <= w) == (z <= (not(z)))) and (x or w)) == 0: 
                    print(x,y,z,w)
                