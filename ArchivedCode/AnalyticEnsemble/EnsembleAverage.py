#This module calculates the average work from a distribution of protocols which each have a constant velocity with a constant velocity variance
#
#Steven Large
#November 17th 2016

from math import *
import numpy

SystemFriction = 1			 			#These are viscous friction values for the underlying system
Variance = [1,2,4,8]
Distance = 75							#Distance travelled
kTrap = 1

Realizations = 20000
TimeRange = 1000

for index1 in range(len(Variance)):

	WorkAvg = []
	TauTrack = []

	for index2 in range(TimeRange):

		ProtocolTime = 1 + index2*0.2
		AvgVel = float(Distance)/float(ProtocolTime)
		WorkTracker = []

		WorkAvg.append(0.0)
		TauTrack.append(ProtocolTime)

		for index3 in range(Realizations):

			Velocity = numpy.random.normal(AvgVel,sqrt(Variance[index1]))

			WorkRealization = SystemFriction*Velocity*Velocity*ProtocolTime

			WorkTracker.append(WorkRealization)

		WorkAvg[index2] = sum(WorkTracker)/len(WorkTracker)

	filename = 'WorkAnalytic_Var_' + str(Variance[index1]) + '.dat'

	file1 = open(filename,'w')
	for index4 in range(len(WorkAvg)):
		file1.write('%lf\t%lf\n' % (WorkAvg[index4], TauTrack[index4]))
	file1.close()
