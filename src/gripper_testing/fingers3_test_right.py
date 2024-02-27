from model.system_motors import SystemMotors
import time
import numpy as np
import json as js
import os
# Setting the motor's position to 0

id_fingers=[1,2,4,5,7,8]
# Motors
motors = SystemMotors(6)  # instantiate SystemMotors class >> number of motors
motors.loadMotors(id_fingers, "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")

motors.startMotors()  # start m

time.sleep(2)

print("Setting up motors...")
motors.setupPositionsMode(5, 5)  # setting velocity and acceleration values
#

motors.setPositions([0,0,0,0,0,0])

time.sleep(3)

i=0
for id in id_fingers:
    print("Initial motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

motors.setPositions([0,-2,0,-2,0,-2])# RADS

time.sleep(3)

i=0
for id in id_fingers:
    print("During motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1



motors.setPositions([0,0,0,0,0,0])

time.sleep(3)

i=0
for id in id_fingers:
    print("Final motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

