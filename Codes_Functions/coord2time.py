import numpy as np
from math import atan as arctan
def coord2time(x,y):
	if x>=0 and y>0: 		time=(250*(arctan(x/y)/arctan(1))) # Take cotangent by dividing x/y
	elif x>0 and y<=0:		time=500+(250*(abs(arctan(y/x)/arctan(1)))) # Take tangent
	elif x<=0 and y<0:		time=1000+(250*((arctan(x/y))/arctan(1))) # Take cotangent
	elif x<0 and y>=0:		time=1500+(250*(abs(arctan(y/x)/arctan(1))))# Take tangent
	else:		time=None
	return time
