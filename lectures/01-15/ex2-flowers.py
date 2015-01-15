from turtle import *

# problem: draw 2 flowers as shown in flowers.png
# my solution:
# 1) draw a square
# 2) draw a flower using the square

# This is a square
def square():
    for n in range(4):
       forward(50)
       left(90)

#This is a flower
def flower():
    for k in range(12):
        square()
        left(30)

flower()
done()