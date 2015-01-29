from turtle import *

def plus():
    for i in range(4):
        forward(20)
        left(90)
        forward(50)
        right(90)
        forward(50)
        left(90)

def round():
    for i in range(4):
        plus()
        circle(-100,90)

# this is my solution
round()
penup()
forward(500)
pendown()
round()