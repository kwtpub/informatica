# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if ((not (x <= y)) or (x == z) or w) == 0:
#                     print(x,y,z,w)
print('x y z w')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((not x <= y) or (x == z) or w) == 0:
                    print(x,y,z,w)
