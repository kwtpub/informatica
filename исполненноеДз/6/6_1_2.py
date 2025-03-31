from turtle import * 

scl = 20
tracer(0)

for i in range(4):
    fd(5*scl)
    rt(90)
    fd(7*scl)
    rt(90)

up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*scl,y*scl)
        dot(5,'red')

print('otvet:', 8*6)    #48+

update()
done()
