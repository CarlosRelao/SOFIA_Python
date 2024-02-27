from model.system_motors import SystemMotors
import time
import numpy as np
import json as js
import os
# Setting the motor's position to 0

# Motors
motors = SystemMotors(3)  # instantiate SystemMotors class >> number of motors
motors.loadMotors([2,1,3], "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")

motors.startMotors()  # start m

time.sleep(1)

print("Setting up motors...")
motors.setupPositionsMode(5, 5)  # setting velocity and acceleration values
#

time.sleep(2)
print("Initial upper motor position: "+str(round(motors.motorsArray[2].getPosition(),2)))

motors.setPositions([0,0,1])# RADS

time.sleep(3)

print("Final upper motor position: "+str(round(motors.motorsArray[2].getPosition(),2)))


motors.setPositions([0,0,0])

time.sleep(3)

motors.setPositions([0,0,-1])# RADS

time.sleep(3)

print("Final upper motor position: "+str(round(motors.motorsArray[2].getPosition(),2)))


motors.setPositions([0,0,0])

time.sleep(3)

# print("Initial lower motor position: "+str(round(motors.motorsArray[0].getPosition(),2)))

# motors.setPositions([2,0])# RADS

# time.sleep(3)

# print("Final lower motor position: "+str(round(motors.motorsArray[0].getPosition(),2)))


# motors.setPositions([0,0])

# time.sleep(3)

# print("Initial upper and lower motor position: "+str(round(motors.motorsArray[1].getPosition(),2))+" and "+ str(round(motors.motorsArray[0].getPosition(),2)))

# motors.setPositions([2,-2])# RADS

# time.sleep(2)

# print("Final upper and lower motor position: "+str(round(motors.motorsArray[1].getPosition(),2))+" and "+ str(round(motors.motorsArray[0].getPosition(),2)))


# motors.setPositions([0,0])

# time.sleep(3)


# while True :
#     print("---------------------------------------")
#     print("Motor arriba position:  "+str(motors.motorsArray[0].getPosition()))

#     print("Motor abajo position:  "+str(motors.motorsArray[1].getPosition()))
#     time.sleep(1.5)