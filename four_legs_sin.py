#Adapted from @ethanlipson on github
#Modified by Manav V.
#4 leg motion
#Access via ssh


from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    print("Started Boot")
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo1.set_angle_limits(0, 100)
    servo1.set_angle_offset(-21)
    servo2.set_angle_limits(0, 142)
    servo2.set_angle_offset(0)

    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo3.set_angle_limits(0, 100)
    servo3.set_angle_offset(0)
    servo4.set_angle_limits(50, 222)
    servo4.set_angle_offset(0)

    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo5.set_angle_limits(120, 240)
    servo5.set_angle_offset(0)
    servo6.set_angle_limits(12, 180)
    servo6.set_angle_offset(0)

    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo7.set_angle_limits(120, 240)
    servo7.set_angle_offset(-30)
    servo8.set_angle_limits(0, 165)
    servo8.set_angle_offset(-30)

    # angle1 = servo1.get_physical_angle()

    # method to initialize angles, fix and test this part
    servo1.move(0, 500)
    servo2.move(100, 500)
    servo3.move(0, 500)
    servo4.move(165, 500)
    servo5.move(212, 500)
    servo6.move(60, 500)
    servo7.move(185, 500)
    servo8.move(30, 500)
    print("Initialized")
    time.sleep(3)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
#set limit to loop
while t<=50:
    speed = 2
    #servo1.move(sin(2 * t) * 31 + 31) #sin(2 * t) * 15.5 + 15.5
    servo1.move(sin(speed * t) * 15.5 + 35.5)
    servo2.move(cos(speed * t) * 71 + 71)

    servo7.move(sin(speed * t) * 35.5 + 184)
    #servo7.move(sin(3 * t) * 25 + 0)
    servo8.move(cos(speed * t) * 82.5 + 82.5)

    #servo3.move(cos(2 * t) * 36 + 36) #cos(2*t) * 22 + 22
    servo3.move(cos(speed*t) * 22 + 43) #cos(2*t) * 22 + 22
    #servo3.move(cos(3*t) * 25 + 0)
    servo4.move(sin(speed*t) * 86 + 136) #this was originally cos

    servo5.move(cos(speed * t) * 34.5 + 185)
    #servo5.move(cos(3 * t) * .5 + 0)
    servo6.move(sin(speed * t) * 84 + 96)
    time.sleep(0.05)
    t += 0.1
#add check on motor angle
try:
    print("I went through the motions, but it's time to rest!")
    time.sleep(2)

    servo1.move(0, 500)
    servo2.move(100, 500)
    servo3.move(0, 500)
    servo4.move(165, 500)
    servo5.move(212, 500)
    servo6.move(60, 500)
    servo7.move(185, 500)
    servo8.move(30, 500)
    time.sleep(2)
    print("ZZzzz")
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()