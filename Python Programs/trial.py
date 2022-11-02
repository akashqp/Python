from turtle import *
t = Turtle()

width = 90
t.penup()
t.goto(-300,0)
t.right(-90)
t.pendown()
t.forward(width)
t.right(180)
t.forward(width/2)
t.left(90)
t.forward(60)
t.left(90)
t.forward(width/2)
t.right(180)
t.forward(width)
t.penup()

t.left(90)
t.forward(width/2)
t.pendown()
t.left(90)
t.forward(width)
t.right(90)
t.forward(width/3)
for i in range(90):
    t.right(2)
    t.forward(1)
