from turtle import *

def petal(radius1, radius2, angle):
    penup()
    forward(radius1)
    pendown()
    forward(radius2-radius1)
    left(90)
    circle(radius2,angle)
    left(90)
    forward(radius2-radius1)
    left(90)
    circle(-radius1,angle)
    right(90)
    penup()
    forward(radius1)
    left(180)
    pendown()
   
def flower(middle_radius, petal_radius, nbpetals):
    for i in range(nbpetals):
        petal(middle_radius, petal_radius, 360 / (nbpetals * 2))
        left(360 / nbpetals)
        
def growing(middle_radius, petal_radius, nbpetals):
    for i in range(nbpetals):
        petal(middle_radius, petal_radius*(i+1), 360 / (nbpetals * 2))
        left(360 / nbpetals)
    
def nuclear(radius):
    circle(radius)
    penup()
    left(90)
    forward(radius)
    right(90)
    pendown()
    flower(radius * 2, radius * 4, 3)
    
def pyramid(nbflower,middle_radius, petal_radius, nbpetals):
    for k in range(nbflower):
        for n in range(nbflower - k):
            flower(middle_radius, petal_radius, nbpetals)
            penup()
            forward(petal_radius*3)
            pendown()
        penup()
        home()
        left(90)
        forward(petal_radius*3*(k+1))
        right(90)
        forward((petal_radius + petal_radius /2) * (k+1))
        pendown()
    
def rose(middle_radius,nbpetals,nblayers):
    circle(middle_radius)
    penup()
    left(90)
    forward(middle_radius)
    pendown()
    for n in range(nblayers):
         flower((2*n+2)*middle_radius, (2*n+3)*middle_radius, nbpetals)
         left(180/nbpetals)


    