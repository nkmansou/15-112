from turtle import *

# problem: draw an octogon

# my solution: I draw one face of the octogon and then turn 45 dregree on the left.
# I repeat this operation 8 times.
# The octogon will be drawn anticlockwise

# # This is an octogon
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)

# This is an octogon (using a loop)
for n in range(8):
   forward(100)
   left(45)

done()
