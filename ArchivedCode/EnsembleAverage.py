#This module calculates the average work from a distribution of protocols which each have a constant velocity with a constant velocity variance
#
#Steven Large
#November 17th 2016

from math import *
import numpy

SystemFriction = [1,2,4,8,16] 			#These are viscous friction values for the underlying system
Distance = 50							#Distance travelled
kTrap = 1

Realizations = 1000
TimeRange = 100

Variance = 4

for index1 in range(len(SystemFriction)):

	WorkAvg = []
	TauTrack = []

	for index2 in range(TimeRange):

		ProtocolTime = 100 + index2*10
		AvgVel = float(Dist)/float(ProtocolTime)
		WorkTracker = []

		WorkAvg.append(0.0)
		TauTrack.append(ProtocolTime)

		for index3 in range(Realizations):

			Velocity = numpy.random.normal(AvgVel,Variance)

			WorkRealization = SystemFriction[index1]*Velocity*Velocity*ProtocolTime

			WorkTracker.append(Workrealization)

		WorkAvg(index2) = sum(WorkTracker)/len(WorkTracker)

	filename = 'WorkAnalytic_' + str(SystemFriction[index1]) + '.dat'

	file1 = open(filename,'w')
	for index4 in range(len(WorkAvg)):
		file1.write('%lf\t%lf\n' % (WorkAvg[index4], TauTrack[index4]))
	file1.close()
