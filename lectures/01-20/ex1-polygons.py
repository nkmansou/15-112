from turtle import *

def polygon(length, side):
        for i in range(side):
            forward(length)
            left(360/side)

# polygon(4,50)
# polygon(6,50)
# polygon(8,50)
# polygon(10,50)
# polygon(12,50)
# polygon(20,50)

for i in range(18):
    polygon(10,(i+4))
done()