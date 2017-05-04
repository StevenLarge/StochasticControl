#This module runs teh submodules that calcualte the average work
#
#Steven Large
#November 17th 2016

from DriverConstantVelocity import *

ProtocolTime = 500
Distance = 5

CPVelocity = float(Distance)/float(ProtocolTime)

AvgWork,WorkVariance = CalculateWork(CPVelocity,ProtocolTime)

print('\n\nThe Average Work is --> %lf\n\nWork Variance is --> %lf\n\n' % (AvgWork,WorkVariance))
