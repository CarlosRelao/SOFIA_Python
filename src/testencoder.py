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

UP=0 # Upper motor motor ipos 1
MID=1  # Middle motor motor ipos 2
BOT=2 # Bottom motor motor ipos 3

# Choose the motor to test
id=BOT

time.sleep(2)
print("Initial upper motor position: "+str(round(motors.motorsArray[id].getPosition(),2)))


while True :
    print("---------------------------------------")
    print("Motor  position:  "+str(motors.motorsArray[id].getPosition()))

    time.sleep(1.5)