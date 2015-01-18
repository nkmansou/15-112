from turtle import *

# problem: draw 5 nested circles
# my solution: draw one circle and then draw the next circle with its radius twice the size as the pevious one

# this draws five circles
for n in range(5):
   # this draws the circle n with its radius being (n+1)*50
   circle(50 * (n+1))

done()









