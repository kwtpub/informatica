from turtle import * 

tracer(0)
scale = 30 
lt(90)
rt(90)

for i in range(3): 
    rt(45)
    fd(10*scale)
    rt(45)
rt(315)
fd(10*scale)
for i in range(2):
    rt(90)
    fd(10*scale)
print('otvet:', 120)
up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*scale,y*scale)
        dot(2,'red')

update()#??
done()
