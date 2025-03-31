from turtle import * 
screensize(5000,5000)
scale = 30
tracer(0)

for i in range(2): 
    fd(13*scale)
    lt(90)
    backward(20*scale)
    lt(90)
up()
fd(8*scale)
rt(90)
backward(3*scale)
lt(90)
down()
for i in range(2):
    fd(16*scale)
    rt(90)
    fd(8*scale)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*scale,y*scale)
        dot(4,'red')

print(21*14+17*9-6*6) #411


update()
done()

