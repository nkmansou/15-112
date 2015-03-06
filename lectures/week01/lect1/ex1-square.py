from turtle import *

# problem: draw a square

# my solution: I draw one face of the square and then turn 90 dregree on the left.
# I repeat this operation 4 times.
# The square will be drawn anticlockwise

# # This is a square
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)

# This is a square (using a loop)
for n in range(4):
   forward(100)
   left(90)

done()
