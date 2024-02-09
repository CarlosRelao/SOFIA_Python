from model.system_motors import SystemMotors
import time
import numpy as np
import json as js
import os
# Setting the motor's position to 0

ipos_id=4

print(ipos_id%3)


# Motors
motors = SystemMotors(1)  # instantiate SystemMotors class >> number of motors
motors.loadMotors([ipos_id], "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")

motors.startMotors()  # start m

if (ipos_id%3)==1:
    position=[0.5]
    print(position)


if (ipos_id%3)==2:
    position=[-0.5]
    print(position)

if (ipos_id%3)==0:
    position=[0]
    print(position)

time.sleep(2)

print("Setting up motors...")
motors.setupPositionsMode(5, 5)  # setting velocity and acceleration values

time.sleep(2)
print("Initial motor position: "+str(round(motors.motorsArray[0].getPosition(),2)))

motors.setPositions(position)# RADS

time.sleep(3)
print("During motor position: "+str(round(motors.motorsArray[0].getPosition(),2)))

motors.setPositions([0])# RADS
time.sleep(3)
print("Final motor position: "+str(round(motors.motorsArray[0].getPosition(),2)))
