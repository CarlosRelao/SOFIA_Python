from model.system_motors import SystemMotors
import time
import numpy as np
import json as js
import os
# Setting the motor's position to 0

# Motors
motors = SystemMotors(3)  # instantiate SystemMotors class >> number of motors
motors.loadMotors([1,2,3], "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")

motors.startMotors()  # start m

time.sleep(2)

print("Setting up motors...")
motors.setupPositionsMode(5, 5)  # setting velocity and acceleration values
#


UP=0 # Upper motor motor ipos 1
MID=1  # Middle motor motor ipos 2
BOT=2 # Bottom motor motor ipos 1

# Choose the motor to test
id=BOT

if id==UP:
    position=[1,0,0]

if id==MID:
    position=[0,-1,0]

if id==BOT:
    position=[0,0,-1]

print("Vamos a cero")


motors.setPositions([0,0,0])

time.sleep(3)
print("Initial motor position: "+str(round(motors.motorsArray[id].getPosition(),2)))

motors.setPositions(position)# RADS

time.sleep(3)

print("Final motor position: "+str(round(motors.motorsArray[id].getPosition(),2)))

motors.setPositions([0,0,-0.5])# RADS

time.sleep(3)

print("Final motor position: "+str(round(motors.motorsArray[id].getPosition(),2)))

motors.setPositions([1,-1,-1])

time.sleep(3)


print("Final motor position: "+str(round(motors.motorsArray[id].getPosition(),2)))

motors.setPositions([0,0,0])

time.sleep(3)