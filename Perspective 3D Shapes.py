#perspective turtle
from turtle import Turtle
import turtle
import time
screen = turtle.Screen()
screen.tracer(0,0)

t = Turtle()
t.hideturtle()

x1 = -100
x2 = 100
x3 = 100
x4 = -100
y1 = -100
y2 = 100

t.penup()
t.goto(x1,y1)
t.pendown()

direction = "forward"
colour = "blue"
x = 0
y = 0
while True:
    if y == 20 and colour == "blue":
        colour = "red"
    elif y == 60 and colour == "red":
        colour = "blue"
    t.color(colour)
    t.clear()
    t.penup()
    t.goto(x1,y1)
    t.begin_fill()
    t.pendown()
    t.goto(x2,y1)
    t.goto(x3,y2)
    t.goto(x4,y2)
    t.goto(x1,y1)
    t.end_fill()
    if y1 == y2 and direction == "forward" or y1 == x1 and direction == "forward" and x != 0:
        direction = "backward"
    elif y1 == y2 and direction == "backward" or y1 == x1 and direction == "backward" and x != 0:
        direction = "forward"
    if y1 == 100 and x != 0:
        x1 = -100
        x2 = 100
        x3 = 100
        x4 = -100
        y1 = -100
        y2 = 100
        direction = "forward"
    if direction == "forward":
        x1 += 1
        x2 -=1
        x3 += 1
        x4 -= 1
        y1 += 5
        y2 -= 5
    elif direction == "backward":
        x1 -= 1
        x2 +=1
        x3 -= 1
        x4 += 1
        y1 += 5
        y2 -= 5
    
    screen.update()
    time.sleep(0.05)
    x += 1
    y += 1
    if y == 80:
        y = 0
