from turtle import * 

scl = 50
tracer(0)

for i in range(15):
    fd(3*scl)
    rt(40)


up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*scl,y*scl)
        dot(4,'red')

print('otvet:', 35 ) 

update()
done()
