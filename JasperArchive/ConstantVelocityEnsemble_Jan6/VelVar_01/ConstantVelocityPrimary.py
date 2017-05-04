#This is the primary module for Stochastic Control simulations of the constant velocity ensemble
#
#Steven Large
#January 4th 2017

import ConstantDriver
from math import *
from Parameters import *
from VelocityParameters import *
import random
import WriteData

NumberTrajectories = 10000
TimeRange = 60

WorkTotal = []
Tau = []

CPVel_Track = []

WorkDTot = []

filename_T = 'WorkTotal_' + str(VelocityVariance) + '.dat'

for index in range(TimeRange):

	ProtocolTime = 5 + 5*index

	#print ("ProtocolTime -->\t\t%lf\n" % ProtocolTime)

	Tau.append(ProtocolTime)

	WorkDTot.append(0.0)

	for Realizations in range(NumberTrajectories):

		#WorkTrajectory,CPVel_Realization,Position_Track,CP_Track = ConstantDriver.Propogator(ProtocolTime,VelocityVariance)

		WorkTrajectory = ConstantDriver.Propogator2(ProtocolTime,VelocityVariance)

		#CPVel_Track.append(CPVel_Realization)

		#if Realizations==1 & ProtocolTime==100:
		#	WriteData.TrajectoryWrite(Position_Track,'PositionTracking.dat','Output/')
		#	WriteData.TrajectoryWrite(CP_Track,'CPTracking.dat','Output/')

		WorkDTot[index] = WorkDTot[index] + WorkTrajectory
		
for index in range(len(WorkDTot)):

	WorkTotal.append(WorkDTot[index]/float(NumberTrajectories))

WriteData.WorkWrite(WorkTotal,Tau,filename_T,'Output/')
