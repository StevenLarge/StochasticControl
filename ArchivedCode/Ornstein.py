#This module contains the main logic structure of the Langevin simulation of an Ornstein-Uhlenbeck process
#
#Steven Large
#June 21st 2016

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
WorkS1Tot = []
WorkS2Tot = []
WorkDeterministic = []
WorkStochastic = []
WorkStochastic2 = []
WorkTotal = []
Tau = []

filename_D = 'WorkDeterministic.dat'
filename_S = 'WorkStochastic.dat'
filename_T = 'WorkTotal.dat'
filename_S2 = 'WorkStochastic_New.dat'

filename_BasePosition = 'PosTrack_'
filename_BaseVelocity = 'VelTrack_'
filename_BaseCP = 'CPTrack_'

for index in range(TimeRange):

	ProtocolTime = 100 + 100*index

	Tau.append(ProtocolTime)

	WorkDTot.append(0.0)
	WorkS1Tot.append(0.0)

	for Realizations in range(NumberTrajectories):

		WorkD, WorkS1, WorkS2, PositionTrack, VelocityTrack, CPTrack = Driver.Propogator(ProtocolTime)

		WorkDTot[index] = WorkDTot[index] + WorkD
		WorkS1Tot[index] = WorkS1Tot[index] + WorkS1
		WorkS2Tot[index] = WorkS2Tot[index] + WorkS2
		
		#if Realizations == 1:

		#	filename_position = filename_BasePosition + str(ProtocolTime) + '.dat'
		#	filename_velocity = filename_BaseVelocity + str(ProtocolTime) + '.dat'
		#	filename_CP = filename_BaseCP + str(ProtocolTime) + '.dat'

		#	file1 = open(filename_position,'w')
		#	file2 = open(filename_velocity,'w')
		#	file3 = open(filename_CP,'w')

		#	for k in range(len(PositionTrack)):
		#		file1.write('%lf\n' % PositionTrack[k])
		#		file2.write('%lf\n' % VelocityTrack[k])
		#		file3.write('%lf\n' % CPTrack[k])

		#	file1.close()
		#	file2.close()
		#	file3.close()

for index in range(len(WorkDTot)):

	WorkDeterministic.append(WorkDTot[index]/float(NumberTrajectories))
	WorkStochastic.append(WorkS1Tot[index]/float(NumberTrajectories))
	WorkStochastic2.append(WorkS2Tot[index]/float(NumberTrajectories))
	
	WorkTotal.append(WorkDeterministic[index] + WorkStochastic[index])

WriteData.WorkWrite(WorkDeterministic,Tau,filename_D)
WriteData.WorkWrite(WorkStochastic,Tau,filename_S)
WriteData.WorkWrite(WorkStochastic2,Tau,filename_S2)
WriteData.WorkWrite(WorkTotal,Tau,filename_T)

#plt.plot(Tau,WorkStochastic)
#plt.show()
#plt.close

#end = TM.time()

#print "\n\n"
#print end - begin
#print "\n\n"

