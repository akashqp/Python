import turtle
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
t.pensize(3)
width = 90
t.speed(3)

def h():
    t.penup()
    t.goto(-210, 50)
    t.right(-90)
    t.pendown()
    t.forward(width)
    t.right(180)
    t.forward(width / 2)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(width / 2)
    t.right(180)
    t.forward(width)
    t.penup()

def a():
    t.left(90)
    t.forward(width / 2)
    t.pendown()
    t.left(75.96)
    t.forward(92.77)
    t.right(180-14.036*2)
    t.forward(92.77)
    t.right(180)
    t.forward(40)
    t.left(75.96)
    t.forward(25)
    t.backward(25)
    t.left(90+(90-75.96))
    t.forward(40)
    t.right(90-75.96)
    t.penup()

def p():
    t.left(90)
    t.forward(width / 2)
    t.pendown()
    t.left(90)
    t.forward(width)
    t.right(90)
    t.forward(width / 3)
    t.speed(0)
    for i in range(73):
        t.forward(1)
        t.right(2.5)
    t.forward(30)
    t.speed(3)
    t.penup()
    t.left(90)
    t.forward(46)
    t.left(93)
    t.forward(width/2)
    t.right(90)

def y():
    t.left(90)
    t.forward(width / 2)
    t.left(90)
    t.forward(90)
    t.right(90+63.43494882292201)
    t.pendown()
    t.forward(50.31)
    t.left(90+(90-53.121))
    t.forward(50.31)
    t.backward(50.31)
    t.left(180+53.121/2)
    t.forward(45)
    t.penup()
    t.left(90)
    t.forward(width/4)
    t.right(90)

def d():
    t.pendown()
    t.left(180)
    t.forward(width)
    t.right(90)
    t.speed(0)
    for i in range(90):
        t.forward(1.57)
        t.right(2)
    t.speed(3)
    t.penup()
    t.right(180)
    t.forward(width/2)
    t.right(90)

def i():
    t.left(90)
    t.forward(width / 2)
    t.pendown()
    t.left(90)
    t.forward(90)
    t.backward(90)
    t.right(180)
    t.penup()

def w():
    i()
    t.left(90)
    t.forward(20)
    t.right(90)
    i()
    t.right(90)
    t.forward(65)
    t.pendown()
    t.right(180-54.16234704572172)
    t.forward(55.51)
    t.right(180-2*35.837652954278305)
    t.forward(55.51)
    t.left(54.16234704572172)
    t.right(90)
    t.penup()

def l():
    i()
    t.left(90)
    t.pendown()
    t.forward(50)
    t.right(90)
    t.penup()

    
h()
a()
p()
p()
y()
t.goto(-225, -95)
d()
t.right(1)
i()
w()
a()
l()
i()


turtle.done()