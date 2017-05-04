#This module runs teh submodules that calcualte the average work
#
#Steven Large
#November 17th 2016

from DriverConstantVelocity2 import *

TimeDifference = 10
ProtocolTime = 1000
Distance = 15

CPVelocity = float(Distance)/float(ProtocolTime)

AvgWork,WorkVariance = CalculateWork1(CPVelocity,ProtocolTime,TimeDifference)

print('\n\nThe Average Work is --> %lf\n\nWork Variance is --> %lf\n\n' % (AvgWork,WorkVariance))
