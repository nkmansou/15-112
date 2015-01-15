from turtle import *

# problem: draw an octagon

# my solution: I draw one face of the octagon and then turn 45 dregree on the left.
# I repeat this operation 8 times.
# The octagon will be drawn anticlockwise

# # This is an octagon
# forward(100)
# left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
# left(45)

# This is an octagon (using a loop)
for n in range(8):
   forward(100)
   left(45)

done()
