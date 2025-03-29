from turtle import * 

screensize(3000,3000)
tracer(0)
scale = 30 

lt(90)

for _ in range(5):
    fd(10*scale)
    rt(90)
    fd(16*scale)
    rt(90)

for _ in range(6):
    lt(45)
    fd(5*(2**0.5)*scale)
    rt(135)


for _ in range(3):
    fd(14*scale)
    lt(120)

up()
for x in range(-10,100):
    for y in range(-10,100):
        goto(x*scale, y*scale)
        dot(5,'green')

update()
done()