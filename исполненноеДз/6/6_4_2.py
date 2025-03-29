# from turtle import * 

# lt(90)
# screensize(5000,5000)
# scale = 30
# tracer(0)


# for i in range(8):
#     for j in range(4):
#         fd(7*scale)
#         rt(30)
#         fd(8*scale)
#         rt(150)

# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*scale,y*scale)
#         dot(4,'red')
    


# update()
# done()

import turtle
import math

# Функция для вычисления площади многоугольника по формуле Гаусса
def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

# Настройка окна
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

# Создаём черепаху
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость
t.penup()
t.goto(0, 0)  # Начинаем с центра координат
t.pendown()

# Начальные условия
x, y = 0, 0  # Текущие координаты
angle = 90  # Направление (вверх)
points = [(x, y)]  # Список точек

# Основной цикл (повторяем 8 раз)
for _ in range(8):
    for _ in range(4):
        # Вперёд 5
        x += 5 * math.cos(math.radians(angle))
        y += 5 * math.sin(math.radians(angle))
        points.append((x, y))
        t.goto(x, y)  # Двигаем черепаху
        
        angle -= 30  # Направо 30 градусов
        
        # Вперёд 6
        x += 6 * math.cos(math.radians(angle))
        y += 6 * math.sin(math.radians(angle))
        points.append((x, y))
        t.goto(x, y)  # Двигаем черепаху

        angle -= 150  # Направо 150 градусов
    
    angle -= 60  # Внешний поворот на 60 градусов

# Завершаем черепаху
t.hideturtle()
turtle.done()

# Вычисляем площадь фигуры
area = polygon_area(points)
print(f"Площадь фигуры: {area}")


