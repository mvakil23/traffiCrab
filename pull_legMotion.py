from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/cu.usbserial-110", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo1.move(cos(3*t) * 35 + 60)
    servo2.move(sin(3*t) * 60 + 60)

    time.sleep(0.05)
    t += 0.1