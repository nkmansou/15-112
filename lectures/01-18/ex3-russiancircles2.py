from turtle import *

# problem: draw 5 aligned circles that overlap each other. Each circle is twice bigger than the previous one.

# my solution: draw a circle and move down to align the center of the next one

# Uncomment if you want to draw this backwards
penup()
backward(500)
pendown()
for n in range(5):
   # this draws one circle
   circle(50 * (n+1))
   # This moves the turtle without drawing
   penup()
   forward(50 * (n+2))
   right(90)
   forward(50)
   left(90)
   pendown()

done()