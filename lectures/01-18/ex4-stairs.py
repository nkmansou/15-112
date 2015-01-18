from turtle import *

# problem: draw stairs by pilling up circle. The next step should be one circle higher than the previous one

# solution:
# 1) be able to draw n circles piled on top of each other
# 2) be able to draw different piles by incrementing the number of circles at each iteration.

# number of piles
for nbstep in range(5):
    # number of circles per pile
    for nbcircles in range(nbstep):
        circle(50)
        # move up
        penup()
        left(90)
        forward(100)
        right(90)
        pendown()
    # move to the next pile
    penup()
    home()
    forward(nbstep*100)
    pendown()

done()

