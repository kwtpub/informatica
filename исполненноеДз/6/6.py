from turtle import * 
screensize(3000,3000)
scale = 30 
tracer(0)
lt(90)
for i in range(2):
    forward(21* scale)
    rt(90)
    forward(27 * scale)
    rt(90)

up()

forward(9 * scale)
rt(90)
fd(10 * scale)
lt(90)

down()

for i in range(2):
    forward(86* scale)
    rt(90)
    forward(47 * scale)
    rt(90)
up()

for x in range(-4,30):
    for y in range(-4,30):
        goto(x*scale,y*scale)
        dot(3,'red')
update()
done()

