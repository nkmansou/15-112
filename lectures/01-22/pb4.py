from robot import *

# problem: the robot can be anywhere in the room

# solution: move towards the first wall
# try to find a door on this wall
# if another wall is reached, try to reach the door on this wall
# eventually the robot will find the door

# initialize the problem
problem4()
# While the robot is not in front of the wall or the door, move forward
while not(amIFrontDoor() or amIFrontWall()):
    step(1)
# Now we know that the robot has reached either the wall or the door
# while the robot is not in front of the door
while not(amIFrontDoor()):
    # turn
    left(90)
    # the robot might be in front of wall
    if not(amIFrontWall()):
           # if not move forward and find the door
           step(1)
           right(90)
# Now, the robot is in front of the door. Is the door opened?
if isDoorOpened():
    # yes, move forward
    step(2)
else:
    # no, open it and then move forward
    openDoor()
    step(2)