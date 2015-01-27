from turtle import *

def star():
    for n in range(4):
        left(45)
        forward(30)
        right(45)
        forward(30)
        left(90)
        forward(30)
        right(45)
        forward(30)
        left(45)

def cross():
    for n in range(4):
        left(45)
        forward(30)
        right(45)
        forward(30)
        left(90)
        forward(30)
        right(45)
        forward(30)
        right(135)


# The pattern
for k in range(3):
    for k in range(3):
        star()
        penup()
        forward(10)
        right(90)
        forward(10)
        left(90)
        pendown()
        cross()
        penup()
        forward(154)
        left(90)
        forward(10)
        right(90)
        pendown()
    penup()
    left(180)
    forward(492)
    left(90)
    forward(164)
    left(90)
    pendown()
