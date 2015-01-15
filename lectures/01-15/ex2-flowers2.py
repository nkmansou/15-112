from turtle import *

# problem: draw 2 flowers as shown in flowers.png
# my solution:
# 1) draw a square
# 2) draw a flower using the square

# This is a square
def square(length):
    for n in range(4):
       forward(length)
       left(90)

#This is a flower
def flower(nbpetals,petalsize):
    for k in range(nbpetals):
        square(petalsize)
        left(360/nbpetals)

flower(25,60)
