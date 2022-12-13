import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(1, 10, num = 100)
#1,2
plt.plot(t, np.sin(2 * t) * 31 + 33)
# plt.plot(t, np.cos(2 * t) * 71 + 71)
#
#7,8
plt.plot(t, np.sin(2 * t) * 35.5 + 204)
# plt.plot(t, np.cos(2 * t) * 82.5 + 82.5)
#
#3,4

plt.plot(t, np.cos(2 * t) * 36 + 38)
# plt.plot(t, np.cos(2 * t) * 86 + 136)
#
plt.plot(t, np.cos(2 * t) * 34.5 + 205)
# plt.plot(t, np.sin(2 * t) * 84 + 96)

plt.ylabel("Angle (Degrees)")
plt.xlabel("Time (s)")


# plt.legend(['Thigh 1', 'Claw 1','Thigh 2', 'Claw 2','Thigh 3', 'Claw 3',
#            'Thigh 4', 'Claw 4','Thigh 5', 'Claw 5','Thigh 6', 'Claw 6',
#            'Thigh 7', 'Claw 7','Thigh 8', 'Claw 8'], loc = 'lower right', bbox_to_anchor=(1.15, .5))

plt.legend(['1,','3','7', '5'], loc = 'lower right', bbox_to_anchor=(1.15, .5))
plt.show()