from turtle import *

# problem: draw 5 circles that overlap each other

# my solution: I draw one circle and move the turtle on the left. I repeat this operation 5 times.

# this draws five circles
for n in range(5):
   # this draws one circle
   circle(50)
   # This moves the turtle without drawing
   penup()
   forward(80)
   pendown()

done()