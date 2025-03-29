from turtle import * 

lt(90)
screensize(5000,5000)
scale = 30
tracer(0)


for i in range(8):
    for j in range(4):
        fd(5*scale)
        rt(30)
        fd(6*scale)
        rt(150)
    rt(60)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*scale,y*scale)
        dot(4,'red')
    


update()
done()

