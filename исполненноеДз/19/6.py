from turtle import * 

screensize(2000,2000)
tracer(0)

scale = 20 

lt(90)

for _ in range(2): 
    fd(17*scale)
    lt(90)
    fd(10*scale)
    lt(90)

up()

backward(4*scale)
rt(90)
backward(3*scale)
lt(90)

down()

for _ in range(2):
    fd(40*scale)
    rt(90)
    fd(10*scale)
    rt(90)

up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*scale,y*scale)
        dot(3,'red')

update()
done()