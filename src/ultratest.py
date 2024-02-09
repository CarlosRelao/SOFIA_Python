from model.system_motors import SystemMotors
import time
import numpy as np
import json as js
import os
# Setting the motor's position to 0

# Motors

motor1 = SystemMotors(1)  # instantiate SystemMotors class >> number of motors
motor1.loadMotors([1], "SoftGripperMotorConfig.json")  # motor's ids

motor2 = SystemMotors(1)  # instantiate SystemMotors class >> number of motors
motor2.loadMotors([2], "SoftGripperMotorConfig.json")  # motor's ids

motor3 = SystemMotors(1)  # instantiate SystemMotors class >> number of motors
motor3.loadMotors([3], "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")

motor1.startMotors()  # start m
motor2.startMotors()  # start m
motor3.startMotors()  # start m

time.sleep(2)

print("Setting up motors...")
motor1.setupPositionsMode(5, 5)  # setting velocity and acceleration values
motor2.setupPositionsMode(5, 5)  # setting velocity and acceleration values
motor3.setupPositionsMode(5, 5)  # setting velocity and acceleration values


time.sleep(1)



print("Vamos a cero")

motor1.setPositions([0])
motor2.setPositions([0])
motor3.setPositions([0])
time.sleep(3)
print("Initial motor "+str(1)+" position: "+str(round(motor1.motorsArray[0].getPosition(),2)))
print("Initial motor "+str(2)+" position: "+str(round(motor2.motorsArray[0].getPosition(),2)))
print("Initial motor "+str(3)+" position: "+str(round(motor3.motorsArray[0].getPosition(),2)))



motor3.setPositions([-0.7])
time.sleep(3)
print("Initial motor "+str(1)+" position: "+str(round(motor1.motorsArray[0].getPosition(),2)))
print("Initial motor "+str(2)+" position: "+str(round(motor2.motorsArray[0].getPosition(),2)))
print("Initial motor "+str(3)+" position: "+str(round(motor3.motorsArray[0].getPosition(),2)))


motor2.setPositions([-2])
time.sleep(3)
print("Initial motor "+str(1)+" position: "+str(round(motor1.motorsArray[0].getPosition(),2)))
print("Initial motor "+str(2)+" position: "+str(round(motor2.motorsArray[0].getPosition(),2)))
print("Initial motor "+str(3)+" position: "+str(round(motor3.motorsArray[0].getPosition(),2)))



motor1.setPositions([0])
motor2.setPositions([0])
motor3.setPositions([0])
time.sleep(3)
print("Final motor "+str(1)+" position: "+str(round(motor1.motorsArray[0].getPosition(),2)))
print("Final motor "+str(2)+" position: "+str(round(motor2.motorsArray[0].getPosition(),2)))
print("Final motor "+str(3)+" position: "+str(round(motor3.motorsArray[0].getPosition(),2)))


