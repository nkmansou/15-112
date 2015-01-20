from turtle import *

def square(length):
    for n in range(4):
       forward(length)
       left(90)

#This is a flower
def flower(l,side):
    for k in range(side):
        square(l)
        left(360/side)

# This is my final drawing
speed(0)
flower(50,36)
# flower(4,100)
# penup()
# forward(200)
# pendown()
# flower(12,50)
# penup()
# forward(200)
# pendown()
# flower(24,75)
done()