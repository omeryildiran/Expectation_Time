""" Omer Faruk Yildiran  function for converting time to coordinates on circle
arguments:
    time_point: asked time point for getting x and y coordinate
    total_time: full revolution of time cycle duration in miliseconds
    """

from math import pi, tan, atan2
from math import atan as arctan
import math

def time2coord(time_point, total_time=2000):
    msPerDeg=total_time/360
    timeDeg=90-(time_point/msPerDeg)
    timeRad=math.radians(timeDeg)
    total_time_8th=(total_time/8)
    if time_point>=0 and time_point<=(total_time_8th*2):    x,y=1,tan(timeRad)
    elif time_point>(total_time_8th*2) and time_point<=(total_time_8th*4):  x,y=1,tan(timeRad)
    elif time_point>(total_time_8th*4) and time_point<=(total_time_8th*6):  x,y=-1,-tan(timeRad)
    elif time_point>(total_time_8th*6) and time_point<=(total_time_8th*8):  x,y=-1,-tan(timeRad)
    else:	x,y=None,None
    return x,y

#print(tan(250/250))
#print(time2coord(1))