#This module contains teh primary logic code for generating a distribution of constant velocity protocols with a specificed velocity variance
#
#Steven Large
#November 16th 2016


import Driver
from math import *
from Parameters import *
import random
import WriteData

NumberTrajectories = 200
TimeRange = 72

#NumberTrajectories = 2
#TimeRange = 2

WorkTot = []
WorkTotal = []
Tau = []
PositionTracking = []
VelocityTracking = []
CPTracking = []

filename_Work = 'WorkConstantVelocity.dat'

for index in range(TimeRange):

	ProtocolTime = 50 + 100*index

	Tau.append(ProtocolTime)
	WorkTot.append(0.0)

	for Realizations in range(NumberTrajectories):

		Work, PositionTrack, VelocityTrack, CPTrack = Driver.PropogatorConstantVelocity(ProtocolTime,3)

		WorkTot[index] = WorkTot[index] + Work
		
#		if Realizations == 1:
#			PositionTracking.append(PositionTrack)
#			CPTracking.append(CPTrack)
#			VelocityTracking.append(VelocityTrack)

for index in range(len(WorkTot)):
	WorkTotal.append(WorkTot[index]/float(NumberTrajectories))
	

WriteData.WorkWrite(WorkTotal,Tau,filename_Work)

#file1 = open('TrajectoryTrack.dat','w')
#file1.write('Position\tControl Parameter\tVelocity\tTime\n\n')
#for index2 in range(len(PositionTracking[1])):
#	file1.write("%lf\t%lf\t%lf\n" % (PositionTracking[1][index2], CPTracking[1][index2], VelocityTracking[1][index2]))
#file1.close()






