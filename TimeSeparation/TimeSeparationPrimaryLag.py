#This module provides the main script for various time separations of the underlying system dynamics and the control parameter
#
#Steven Large
#December17th 2016

import TimeDriver
import TimeDriverLag
from math import *
from Parameters import *
from TimeParameters import *
import random
import WriteData

import numpy as np

#NumberTrajectories = 300
#TimeRange = 75

NumberTrajectories = 25						#Local Tests
TimeRange = 25

WorkDTot = []
WorkSTot = []
WorkTot = []
WorkDeterministic = []
WorkStochastic = []
WorkTotal = []
Tau = []

CPTime = []
InternalTime = []

#filename_D = 'WorkDeterministic_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
#filename_S = 'WorkStochastic_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
filename_T = 'WorkTotal_TS_' + str(TimeSeparation) + '_k' + str(kCP) +'.dat'

path = 'Output/'

filename_Times = 'Times_' + str(TimeSeparation) + '.dat'

for index in range(TimeRange):

#	ProtocolTime = 25 + 25*index

	ProtocolTime = 25 + 100*index 					#Local Tests

	print "Protocol Time --> %lf" % ProtocolTime

	Tau.append(ProtocolTime)

#	WorkDTot.append(0.0)
#	WorkSTot.append(0.0)

	WorkTot.append(0.0)

	for Realizations in range(NumberTrajectories):

#		WorkD, WorkS, OuterTime, InnerTime = TimeDriver.Propogator(ProtocolTime,TimeSeparation)

		Work,OuterTime,InnerTime = TimeDriverLag.Propogator(ProtocolTime,TimeSeparation)

#		WorkDTot[index] = WorkDTot[index] + WorkD
#		WorkSTot[index] = WorkSTot[index] + WorkS

		WorkTot[index] = WorkTot[index] + Work
		
	CPTime.append(OuterTime)
	InternalTime.append(InnerTime)

#for index in range(len(WorkDTot)):

#	WorkDeterministic.append(WorkDTot[index]/float(NumberTrajectories))
#	WorkStochastic.append(WorkSTot[index]/float(NumberTrajectories))
	
#	WorkTotal.append(WorkDeterministic[index] + WorkStochastic[index])

for index in range(len(WorkTot)):
	WorkTotal.append(WorkTot[index]/float(NumberTrajectories))

#WriteData.WorkWrite(WorkDeterministic,Tau,filename_D,path)
#WriteData.WorkWrite(WorkStochastic,Tau,filename_S,path)
WriteData.WorkWrite(WorkTotal,Tau,filename_T,path)

WriteData.TimeWrite(CPTime,InternalTime,filename_Times,path)


