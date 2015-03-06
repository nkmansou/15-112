from turtle import *

# problem: draw 5 octagons that overlap each other

# my solution: I use the program from 5circles.py
# and I replaced the instruction "circle()" by the code that draws an octagon from octagon.py

# this draws five circles
for n in range(5):
   # this draws one octagone
   for n in range(8):
      forward(50)
      left(45)
   # This moves the turtle without drawing
   penup()
   forward(80)
   pendown()

done()