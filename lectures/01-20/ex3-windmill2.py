from turtle import *

# This is a triangle
def triangle(size):
    left(60)
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(size)
    left(60)

# This is a windmill
def windmill(bladeSize, bladeNumber, postHeight):
    # The sails
    for k in range(bladeNumber):
        triangle(bladeSize)
        left(360/bladeNumber)
    # The post
    right(90)
    forward(postHeight)
    right(90)
    forward(30)
    left(180)
    forward(60)

speed(0)
# This is the final draw
windmill(50,3,100)
penup()
home()
forward(200)
pendown()
windmill(100,5,300)

done()
