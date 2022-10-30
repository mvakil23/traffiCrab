#Adapted from @ethanlipson on github
#4 leg motion

from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo1.set_angle_limits(0, 169)
    servo2.set_angle_limits(0, 140)

    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo3.set_angle_limits(0, 169)
    servo4.set_angle_limits(0, 140)

    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo5.set_angle_limits(0, 169)
    servo6.set_angle_limits(0, 140)

    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo7.set_angle_limits(0, 169)
    servo8.set_angle_limits(0, 140)

    #angle1 = servo1.get_physical_angle()

    #method to initialize angles, fix and test this part
    servo1.move(60, 60)
    servo2.move(60, 60)
    servo3.move(60, 60)
    servo4.move(60, 60)
    servo5.move(60, 60)
    servo6.move(60, 60)
    servo7.move(60, 60)
    servo8.move(60, 60)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
#set limit to loop
while t<=50:
    servo1.move(sin(3 * t) * 25 + 60)
    servo2.move(cos(3 * t) * 60 + 60)

    servo3.move(sin(3 * t) * 25 + 60)
    servo4.move(cos(3 * t) * 60 + 60)

    servo5.move(cos(3*t) * 25 + 60)
    servo6.move(sin(3*t) * 60 + 60)

    servo7.move(cos(3 * t) * 25 + 60)
    servo8.move(sin(3 * t) * 60 + 60)
    time.sleep(0.05)
    t += 0.1