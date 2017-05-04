#This is the second iteration of the TimeSeparationPrimary Routine
#
#Steven Large
#January 23rd 2017

import TimeDriverLocal
from math import *
from Parameters import *
from TimeParameters import *
import random
import WriteData
import WorkTheoryModule 

NumberTrajectories = 75						
TimeRange = 20

WorkTot = []
WorkTheory1 = []
WorkTheorySLag = []
WorkTheoryS = []

WorkTotal = []
VelVarArray = []

Tau = []

filename_T = 'WorkTotal_SHORT_TS_' + str(TimeSeparation) + '_k' + str(k) + '.dat'
filename_T1 = 'WorkTheoryD_SHORT_TS_' + str(TimeSeparation) + '_k' + str(k) + '.dat'
filename_TS = 'WorkTheoryS_SHORT_TS_' +str(TimeSeparation) + '_k' + str(k) + '.dat'

path = 'Output/'

for index in range(TimeRange):

	ProtocolTime = 5 + 10*index 					
	
	Tau.append(ProtocolTime)

	WorkTot.append(0.0)
	WorkTheory1.append(0.0)
	WorkTheoryS.append(0.0)
	VelVarAcc = 0.0

	DistAcc = 0

	for Realizations in range(NumberTrajectories):

		Work, VelVar = TimeDriverLocal.StationaryPropogator(ProtocolTime,TimeSeparation)

		WorkTot[index] = WorkTot[index] + Work
		VelVarAcc = VelVarAcc + VelVar

	AvgDist = DistAcc/float(Realizations)

	VelVarAcc = VelVarAcc/float(NumberTrajectories)

	WorkTheory1[index] = WorkTheoryModule.CalculateDeterministicWork(ProtocolTime)
	WorkTheoryS[index] = WorkTheoryModule.CalculateStochasticWork(ProtocolTime,VelVarAcc)

for index in range(len(WorkTot)):
	WorkTotal.append(WorkTot[index]/float(NumberTrajectories))

WriteData.WorkWrite(WorkTotal,Tau,filename_T,path)
WriteData.WorkWrite(WorkTheory1,Tau,filename_T1,path)
WriteData.WorkWrite(WorkTheoryS,Tau,filename_TS,path)



