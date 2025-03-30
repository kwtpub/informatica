from fnmatch import * 
k = 0 
for i in range(700000,700000+10000): 
    if k == 5: 
        break
    if (not fnmatch(str(i), '*0??3*')) and(not fnmatch(str(i), '*4??2')) and (not fnmatch(str(i), '*1*')) and i % 13 == 0: 
        k += 1 
        print(i, sum(map(int,str(i))))
         
