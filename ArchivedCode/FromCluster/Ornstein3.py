#This module readjusts teh relative time scales of teh control parameter noise and the system to better negate the effects of negative velocity moves
#
#Steven Large
#November 16th 2016

import Driver
from math import *
from Parameters import *
import random
import WriteData
#import matplotlib.pyplot as plt
#import time as TM

#begin = TM.time()

NumberTrajectories = 100
TimeRange = 72


WorkDTot = []
WorkSTot = []
WorkDeterministic = []
WorkStochastic = []
WorkStochastic2 = []
WorkTotal = []
Tau = []

filename_D = 'WorkDeterministic.dat'
filename_S = 'WorkStochastic.dat'
filename_T = 'WorkTotal.dat'

filename_BasePosition = 'PosTrack_'
filename_BaseVelocity = 'VelTrack_'
filename_BaseCP = 'CPTrack_'

for index in range(TimeRange):

	ProtocolTime = 100 + 500*index

	Tau.append(ProtocolTime)

	WorkDTot.append(0.0)
	WorkSTot.append(0.0)

	for Realizations in range(NumberTrajectories):

		WorkD, WorkS, PositionTrack, VelocityTrack, CPTrack = Driver.Propogator(ProtocolTime)

		WorkDTot[index] = WorkDTot[index] + WorkD
		WorkSTot[index] = WorkSTot[index] + WorkS
		
for index in range(len(WorkDTot)):

	WorkDeterministic.append(WorkDTot[index]/float(NumberTrajectories))
	WorkStochastic.append(WorkSTot[index]/float(NumberTrajectories))
	
	WorkTotal.append(WorkDeterministic[index] + WorkStochastic[index])

WriteData.WorkWrite(WorkDeterministic,Tau,filename_D)
WriteData.WorkWrite(WorkStochastic,Tau,filename_S)
WriteData.WorkWrite(WorkTotal,Tau,filename_T)



