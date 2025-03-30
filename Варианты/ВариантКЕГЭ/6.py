from turtle import *

screensize(1000, 1000)
tracer(0)
scale = 30

lt(90)

for i in range(9):
    fd(27 * scale)
    rt(90)

up()
fd(3 * scale)
lt(90)
fd(6 * scale)
lt(90)

for i in range(9):
    fd(77 * scale)
    rt(90)
    fd(66 * scale)
    rt(90)



for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * scale, y * scale)
        dot(3, "blue")
update()
done()