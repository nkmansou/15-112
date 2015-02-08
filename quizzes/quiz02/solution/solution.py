from turtle import *

def triangle(size):
    for i in range(3):
        forward(size)
        left(120)

def nested(size,nbtri):
    for i in range(nbtri):
        triangle(size * (i+1))

def sequence(size,nb):
    for i in range(nb):
        nested(size,(i+1))
        penup()
        forward(size*(i+1)+size)
        pendown()

#triangle(50)
#triangle(120)
#nested(50,3)
#nested(20,12)
#sequence(40,4)
sequence(10,8)

exitonclick()