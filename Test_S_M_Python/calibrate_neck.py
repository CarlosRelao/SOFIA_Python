from SystemMotors import SystemMotors
from InverseKinematics import InverseKinematics
import math
import numpy as np

# Knowing the Inclination and Orientation of the sensor, with a prevoius motor position

# Motors
motors = SystemMotors(3)  # instantiate SystemMotors class >> number of motors
motors.loadMotors([1, 2, 3])  # motor's ids
motors.startMotors()  # start motors

pos = [0, 0, 0]  # initial position
diff = [1, 1, 1]  # difference

for i in range(1000):
    vels = [val for val in motors.getVelocities()]
    if vels < [1, 1, 1] and vels > [-1, -1, -1]:
        amps = [amp for amp in motors.getAmps()]
        diff = [(40 - amp)/10000 for amp in amps]
        pos = [pos[i] + diff[i] for i in range(len(pos))]
        motors.setupPositionsMode(10, 10)
        motors.setPositions(pos)
        print(diff)

motors.stopMotors()
motors.startMotors()


pos = [val for val in motors.getPositions()]
print(pos)
