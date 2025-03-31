from turtle import * 

screensize(5000,5000)
tracer(0)
scale = 30 

lt(90)

for _ in range(8):
    fd(16*scale)
    rt(90)
    fd(22*scale)
    rt(90)
up()

fd(5*scale)
rt(90)
fd(5*scale)
left(90)

down()

for _ in range(8):
    fd(52*scale)
    rt(90)
    fd(77*scale)
    rt(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*scale, y*scale)
        dot(5,'green')


update()
done() #187

