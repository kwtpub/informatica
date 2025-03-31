from fnmatch import * 

for i in range(0,10**10,31007):
    if i % 31007 == 0 and fnmatch(str(i), '1*34?5?9'): 
        print(i, i//31007)
