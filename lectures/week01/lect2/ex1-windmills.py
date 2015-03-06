from turtle import *

# problem: draw 2 flowers as shown in flowers.png
# my solution:
# 1) draw a triangle
# 2) draw the sails using 3 triangles
# 3) draw the post
# 4) draw a windmill using the sails and the post

# This is a triangle
def triangle():
    for n in range(3):
        forward(100)
        right(120)

# This is a windmill
def windmill():
    # The sails
    for k in range(3):
        triangle()
        left(120)
    # The post
    right(90)
    forward(200)
    right(90)
    forward(30)
    left(180)
    forward(60)
    penup()
    left(90)
    forward(200)
    left(90)
    forward(30)
    left(180)
    pendown()

windmill()
done()








