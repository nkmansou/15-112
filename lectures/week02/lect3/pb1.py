from robot import *

# problem: the robot is in front of the door but we do not know if the door is open or closed. 
# The robot will crash if it tries to go through an closed door 
# or if it tries to open an opened door

# solution: test if the door is open or closed.

# initialize the problem 
problem1()
# is the door opened? 
if isDoorOpened():
    # yes, move forward
    step(2)
else: 
    # no, open it and then move forward
    openDoor()
    step(2)



