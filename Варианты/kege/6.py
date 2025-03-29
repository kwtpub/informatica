from turtle import * 

left(90)
k = 25 
tracer(0)

for i in range(4):
    forward(10*k)
    right(270)
up()


forward(3*k)
right(270)
forward(5*k)
right(90)
down()

for i in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)
up()

for x in range(-30, 30+1):
    for y in range(-30,30+1):
        goto(x*k,y*k)
        dot(4, 'blue')