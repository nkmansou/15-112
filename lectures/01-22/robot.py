from turtle import *
from random import randint
from sys import exit

door = randint(0,1)

def getPosition():
    x,y = position()
    h = heading()
    return (int(round(x,1)),int(round(y,1)),int(round(h/10))*10)

def isDoorOpened():
    return door

def drawRoom():
    forward(300)
    left(90)
    forward(200)
    right(90)
    forward(10)
    left(90)
    if isDoorOpened():
        penup()
        forward(20)
        pendown()
    else:
        forward(20)
    left(90)
    forward(10)
    right(90)
    forward(80)
    left(90)
    forward(300)
    left(90)
    forward(300)
    left(90)
    
def crash(s):
    write("crash: " + s) 
    exitonclick()
    exit(0)
    
def victory():
    write("victory")
    exitonclick()
    exit(0)
    
def amIFrontDoor():
    x,y,h = getPosition()
    return (x == 300) and (y == 210) and (h == 0)
    
def openDoor():
    global door
    if not(amIFrontDoor()):
       crash("you are not in front of the door")
    if isDoorOpened():
        crash("the door is already open!")
    pencolor("white")
    forward(10)
    left(90)
    forward(10)
    left(180)
    forward(20)
    left(180)
    forward(10)
    left(90)
    forward(10)
    left(180)
    pencolor("black")
    door = True
    
def amIFrontWall():
    x,y,h = getPosition()
    case1 = (x == 300) and (h == 0)
    case2 = (y == 300) and (h == 90)
    case3 = (x == 0) and (h == 180)
    case4 = (y == 0) and (h == 270)
    return not(amIFrontDoor) or case1 or case2 or case3 or case4 
    
def step(n):
    forward(n*10)
    x,y,h = getPosition()
    if  (x > 300) and (y == 210) and (h == 0) and isDoorOpened():
        victory()
    else:
        if (x < 0) or (y < 0) or ( x > 300) or (y > 300):
            crash("you went through a wall")

def problem1():
  drawRoom()
  penup()
  setposition(300,210)
  pendown()

def problem2():
   drawRoom()
   penup()
   setposition(randint(0,30)*10,210)
   pendown()
    
def problem3():
  drawRoom()
  penup()
  setposition(randint(0,30)*10,randint(0,21)*10)
  pendown()

def problem4():
    drawRoom()
    penup()
    setposition(randint(0,30)*10,randint(0,30)*10)
    setheading(randint(0,3)*90)
    pendown()
    
    