#Adapted from @ethanlipson on github
#push motion for rear legs
from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo5.set_angle_limits(0, 169)
    servo6.set_angle_limits(0, 140)
    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo7.set_angle_limits(0, 169)
    servo8.set_angle_limits(0, 140)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo5.move(sin(3*t) * 25 + 60)
    servo6.move(cos(3*t) * 60 + 60)
    servo7.move(sin(3 * t) * 25 + 60)
    servo8.move(cos(3 * t) * 60 + 60)
    time.sleep(0.05)
    t += 0.1