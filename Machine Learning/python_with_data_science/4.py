
import numpy as np


distance=[20,23,24,26]
time=[.30,.47,.55,3.5]

np_distance=np.array(distance)
np_time=np.array(time)

speed=np_distance/np_time

print(speed)


