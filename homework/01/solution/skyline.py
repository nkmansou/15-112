from turtle import *

# minaret
def rectangle():
    for n in range(2):
        forward(100)
        left(90)
        forward(50)
        left(90)

def trapezoid():
    forward(100)
    left(75)
    forward(52)
    left(105)
    forward(126)
    left(105)
    forward(52)
    left(75)

def palm():
    for n in range(4):
        rectangle()
        penup()
        left(90)
        forward(50)
        right(90)
        pendown()
        trapezoid()
        penup()
        left(90)
        forward(50)
        right(90)
        pendown()
    # roof
    left(90)
    forward(50)
    right(135)
    forward(71)
    left(90)
    forward(71)
    right(135)
    forward(50)


def burj():
    left(90)
    forward(300)
    circle(-60,60)
    circle(100,30)
    left(30)
    forward(50)
    left(180)
    forward(50)
    left(30)
    circle(100,30)
    circle(-60,60)
    forward(300)
    right(90)
    forward(133)

speed(0)
palm()
penup()
home()
forward(150)
pendown()
burj()
# move
penup()
home()
forward(333)
pendown()
palm()
penup()
home()
done()




