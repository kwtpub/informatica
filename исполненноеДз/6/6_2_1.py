from turtle import *

screensize(5000,5000)

scale = 30 
tracer(0)
lt(90)

for i in range(9):
    fd(22*scale)
    rt(90)
    fd(6*scale)
    rt(90)

up()

fd(1*scale)
rt(90)
fd(5*scale)
lt(90)

down()

for i in range(9):
    fd(53*scale)
    rt(90)
    fd(75*scale)
    rt(90)

up()

print('otvet:', 48)
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*scale,y*scale)
        dot(4,'red')

update()
done()
