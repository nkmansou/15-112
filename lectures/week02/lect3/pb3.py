from robot import *

# problem: the robot can be anywhere in the room
# but at least we know that the robot if facing the wall where the door is
# the robot might be facing the door directly

# solution: move forward until the robot reaches the wall or the door
# if it is the wall, try to reach the door

# initialize the problem
problem3()
# While the robot is not in front of the wall or the door, move forward
while not(amIFrontDoor() or amIFrontWall()):
    step(1)
# Now we know that the robot has reached either the wall or the door
# while the robot is not in front of the door
while not(amIFrontDoor()):
    # turn
    left(90)
    # move forward
    step(1)
    # face the wall or the door
    right(90)
# Now, the robot is in front of the door. Is the door opened?
if isDoorOpened():
    # yes, move forward
    step(2)
else:
    # no, open it and then move forward
    openDoor()
    step(2)