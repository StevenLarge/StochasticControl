#This module provides the main script for various time separations of the underlying system dynamics and the control parameter
#
#Steven Large
#December17th 2016

import TimeDriver
import TimeDriverLocal
from math import *
from Parameters import *
from TimeParameters import *
import random
import WriteData

import WorkTheoryModule

import numpy as np

#NumberTrajectories = 300
#TimeRange = 75

NumberTrajectories = 50						#Local Tests
TimeRange = 25

WorkDTot = []
WorkSTot = []
WorkTot = []
WorkTheory = []
WorkTheoryD = []
WorkDeterministic = []
WorkStochastic = []
WorkTotal = []
Tau = []

CPTime = []
InternalTime = []

#filename_D = 'WorkDeterministic_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
#filename_S = 'WorkStochastic_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
filename_T = 'WorkTotal_TS_' + str(TimeSeparation) + '_k' + str(kCP) +'.dat'
filename_Theory = 'WorkTheory_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
filename_TheoryD = 'WorkTheoryD_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'

filenamePos = 'PositionTrack_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
filenameCP = 'CPTrack_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'

path = 'Output/'

filename_Times = 'Times_' + str(TimeSeparation) + '.dat'

for index in range(TimeRange):

#	ProtocolTime = 25 + 25*index

	ProtocolTime = 25 + 20*index 					#Local Tests

	print "Protocol Time --> %lf" % ProtocolTime

	Tau.append(ProtocolTime)

#	WorkDTot.append(0.0)
#	WorkSTot.append(0.0)

	WorkTot.append(0.0)
	WorkTheory.append(0.0)
	WorkTheoryD.append(0.0)

	for Realizations in range(NumberTrajectories):

#		WorkD, WorkS, OuterTime, InnerTime = TimeDriver.Propogator(ProtocolTime,TimeSeparation)

		Work,OuterTime,InnerTime,WorkAccTheory,PositionTrack,CPTrack = TimeDriverLocal.Propogator(ProtocolTime,TimeSeparation)

#		WorkDTot[index] = WorkDTot[index] + WorkD
#		WorkSTot[index] = WorkSTot[index] + WorkS
		if (Realizations==1 && index==20):
			WriteData.TrajectoryWrite(CPTrack,PositionTrack,filenameCP,filenamePos,path)

		WorkTheory[index] = WorkTheory[index] + WorkAccTheory
		WorkTot[index] = WorkTot[index] + Work

	WorkTheoryD[index] = WorkTheoryModule.CalculateDeterministicWork(ProtocolTime)
		
	CPTime.append(OuterTime)
	InternalTime.append(InnerTime)

#for index in range(len(WorkDTot)):

#	WorkDeterministic.append(WorkDTot[index]/float(NumberTrajectories))
#	WorkStochastic.append(WorkSTot[index]/float(NumberTrajectories))
	
#	WorkTotal.append(WorkDeterministic[index] + WorkStochastic[index])

for index in range(len(WorkTot)):
	WorkTotal.append(WorkTot[index]/float(NumberTrajectories))
	WorkTheory[index] = WorkTheory[index]/float(NumberTrajectories)

#WriteData.WorkWrite(WorkDeterministic,Tau,filename_D,path)
#WriteData.WorkWrite(WorkStochastic,Tau,filename_S,path)
WriteData.WorkWrite(WorkTotal,Tau,filename_T,path)
WriteData.WorkWrite(WorkTheory,Tau,filename_Theory,path)
WriteData.WorkWrite(WorkTheoryD,Tau,filename_TheoryD,path)

WriteData.TimeWrite(CPTime,InternalTime,filename_Times,path)


