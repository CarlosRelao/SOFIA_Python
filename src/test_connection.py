from model.system_motors import SystemMotors
import time

# Setting the motor's position to 0

# Motors
motors = SystemMotors(1)  # instantiate SystemMotors class >> number of motors
motors.loadMotors([1], "SoftGripperMotorConfig.json")  # motor's ids
print("Starting motors...")
motors.startMotors()  # start motors
print("Setting up motors...")
motors.setupPositionsMode(1, 1)  # setting velocity and acceleration values
print("Initial motor position: "+str(motors.getPositions()))

#motors.setPositions([0])

time.sleep(1)

motors.stopMotors()
print("Final motor position: "+str(motors.getPositions()))

