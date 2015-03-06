from turtle import *

# problem: draw the olympic sign

# my solution: I use the code from 5 circles.py
# first I draw the 3 circles on the top
# then I move the turtle
# finally I draw the 2 circles on the bottom

# this draws 3 circles on the top
for n in range(3):
   # this draws one circle
   circle(50)
   # This moves the turtle without drawing
   penup()
   forward(80)
   pendown()

# This moves the turtle without drawing
penup()
left(180)
forward(200)
left(90)
forward(50)
left(90)
pendown()

# this draws 2 circles on the bottom
for n in range(2):
   # this draws one circle
   circle(50)
   # This moves the turtle without drawing
   penup()
   forward(80)
   pendown()

done()