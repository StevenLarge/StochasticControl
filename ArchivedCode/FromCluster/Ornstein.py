#This module contains the main logic structure of the Langevin simulation of an Ornstein-Uhlenbeck process
#
#Steven Large
#June 21st 2016

import Driver
from math import *
from Parameters import *
import random
import WriteData

#NumberTrajectories = 100
#TimeRange = 72

WorkTot = []
WorkSTot = []
WorkDeterministic = []
WorkStochastic = []
WorkTotal = []
Tau = []

filename_S = 'WorkStochastic.dat'
filename_T = 'WorkTotal.dat'

for index in range(TimeRange):

	ProtocolTime = 100 + 100*index

	Tau.append(ProtocolTime)

	WorkTot.append(0.0)
	WorkSTot.append(0.0)

	for Realizations in range(NumberTrajectories):

		WorkT, WorkS, PositionTrack, VelocityTrack, CPTrack = Driver.Propogator(ProtocolTime)

		WorkTot[index] = WorkTot[index] + WorkT
		WorkSTot[index] = WorkSTot[index] + WorkS
		
for index in range(len(WorkTot)):

	WorkTotal.append(WorkTot[index]/float(NumberTrajectories))
	WorkStochastic.append(WorkSTot[index]/float(NumberTrajectories))
	
WriteData.WorkWrite(WorkStochastic,Tau,filename_S)
WriteData.WorkWrite(WorkTotal,Tau,filename_T)

