from turtle import * 
screensize(5000,5000)
scale = 30
tracer(0)

for i in range(2): 
    fd(23*scale)
    lt(90)
    backward(27*scale)
    lt(90)
up()
backward(5*scale)
rt(90)
fd(11*scale)
lt(90)
down()
for i in range(2):
    fd(26*scale)
    rt(90)
    fd(32*scale)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*scale,y*scale)
        dot(4,'red')

print((28*24+33*27)-22*17)


update()
done()

