from turtle import *

# problem: draw 5 nested squares

# my solution: draw one square and then draw the next square with its size twice the size as the pevious one

# this draws five circles
for nbsquare in range(5):
   # this draws one circle
   for nbside in range(4):
      forward(50*(nbsquare+1))
      left(90)

done()