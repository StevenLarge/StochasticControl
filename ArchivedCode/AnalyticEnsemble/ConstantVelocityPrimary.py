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

NumberTrajectories = 1
TimeRange = 1

WorkTotal = []
Tau = []

WorkDTot = []

filename_T = 'WorkTotal_' + str(VelocityVariance) + '.dat'

for index in range(TimeRange):

	ProtocolTime = 10 + 50*index

	Tau.append(ProtocolTime)

	WorkDTot.append(0.0)

	for Realizations in range(NumberTrajectories):

		WorkTrajectory = ConstantDriver.Propogator(ProtocolTime,VelocityVariance)

		WorkDTot[index] = WorkDTot[index] + WorkTrajectory
		
for index in range(len(WorkDTot)):

	WorkTotal.append(WorkDTot[index]/float(NumberTrajectories))

WriteData.WorkWrite(WorkTotal,Tau,filename_T)
