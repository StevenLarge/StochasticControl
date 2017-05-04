#This is the infinite time primary executable script for Stochastic control simulations in the infinite time 
#separation limit.
#
#Steven Large
#December 16th 2016

import InfiniteDriver
from math import *
from Parameters import *
import random
import WriteData


NumberTrajectories = 100
TimeRange = 100

WorkTotAccumulator = []
WorkTotal = []
Tau = []

filename_T = 'WorkTotal.dat'

filename_BaseCP = 'CPTrack_Infinite.dat'

for index in range(TimeRange):

	ProtocolTime = 100 + 50*index

	print "Protocol Time --> %lf\n" % ProtocolTime

	Tau.append(ProtocolTime)

	WorkTotAccumulator.append(0.0)

	for Realizations in range(NumberTrajectories):

		WorkProt, CPTrack = InfiniteDriver.Propogator(ProtocolTime)

		if (Realizations==2 & ProtocolTime==100):
			WriteData.CPTrajectoryWrite(CPTrack,filename_CP,'ControlParameter')

		WorkTotAccumulator[index] = WorkTotAccumulator[index] + WorkProt
		
for index in range(len(WorkTotAccumulator)):

	WorkTotal.append(WorkTotAccumulator[index]/float(NumberTrajectories))
	
WriteData.WorkWrite(WorkTotal,Tau,filename_T)






