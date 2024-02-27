from model.system_motors import SystemMotors
import time
import numpy as np
import json as js
import os
# Setting the motor's position to 0

id_fingers=[1,2,3,4,5,6,7,8,9]
# Motors
motors = SystemMotors(9)  # instantiate SystemMotors class >> number of motors
motors.loadMotors(id_fingers, "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")

motors.startMotors()  # start m

time.sleep(4)

print("Setting up motors...")
motors.setupPositionsMode(3, 3)  # setting velocity and acceleration values
#
time.sleep(4)

print("Lets go to zero...")

motors.setPositions([0,0,0,0,0,0,0,0,0])
time.sleep(3)
i=0
for id in id_fingers:
    print("Initial motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

print("Pose!")
motors.setPositions([0,0,-0.5,0,0,-0.5,0,0,-0.5])# RADS
time.sleep(3)
i=0
for id in id_fingers:
    print("During motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

print("Pose!")
motors.setPositions([2,0,-0.5,2,0,-0.5,2,0,-0.5])# RADS
time.sleep(3)
i=0
for id in id_fingers:
    print("During motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

print("Pose!")
motors.setPositions([0,0,-0.5,0,0,-0.5,0,0,-0.5])# RADS
time.sleep(3)
i=0
for id in id_fingers:
    print("During motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

print("Pose!")
motors.setPositions([0,0,0,0,0,0,0,0,0])
time.sleep(3)
i=0
for id in id_fingers:
    print("During motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

print("Pose!")
motors.setPositions([1,-1,0,1,-1,0,1,-1,0])# RADS
time.sleep(3)
i=0
for id in id_fingers:
    print("During motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1

input()

print("Pose!")
motors.setPositions([0,0,0,0,0,0,0,0,0])
time.sleep(3)

i=0
for id in id_fingers:
    print("Final motor "+str(id)+" position: "+str(round(motors.motorsArray[i].getPosition(),2)))
    i=i+1