from robot import *

# problem: the robot is facing the door but not directly in front of it. 
# We do not know how far is the robot from the door

# solution: move forward until the robot reaches the door

# initialize the problem 
problem2()
# While the robot is not in front of the door, move forward
while not(amIFrontDoor()):
    step(1)
# Now, the robot is in front of the door. Is the door opened? 
if isDoorOpened():
    # yes, move forward
    step(2)
else: 
    # no, open it and then move forward
    openDoor()
    step(2)