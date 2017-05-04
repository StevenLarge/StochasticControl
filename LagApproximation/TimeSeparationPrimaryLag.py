#This module provides the main script for various time separations of the underlying system dynamics and the control parameter
#
#Steven Large
#December17th 2016

import TimeDriverLag
from math import *
from Parameters import *
import random
import WriteData

import numpy as np

NumberTrajectories = 25						#Local Tests
TimeRange = 25

WorkTot = []
WorkTotTheory = []
WorkTotTheory2 = []
WorkTotTheoryOld = []

WorkTotal = []
WorkTotalTheory = []
WorkTotalTheory2 = []
WorkTotalTheoryOld = []

Tau = []

CPTime = []

filename_T = 'WorkTotal' + '_k' + str(kCP) + '.dat'
filename_T2 = 'WorkTotalTheory' + '_k' + str(kCP) + '.dat'
filename_T3 = 'WorkTotalTheory2' + '_k' + str(kCP) + '.dat'
filename_T4 = 'WorkTotalTheoryOld' + '_k' + str(kCP) + '.dat'

path = 'Output/'

for index in range(TimeRange):

	ProtocolTime = 25 + 25*index 					#Local Tests

	print "Protocol Time --> %lf" % ProtocolTime

	Tau.append(ProtocolTime)

	WorkTot.append(0.0)
	WorkTotTheory.append(0.0)
	#WorkTotTheory2.append(0.0)
	#WorkTotTheoryOld.append(0.0)

	for Realizations in range(NumberTrajectories):

		Work, WorkTheory = TimeDriverLag.Propogator(ProtocolTime)

		WorkTot[index] = WorkTot[index] + Work
		WorkTotTheory[index] = WorkTotTheory[index] + WorkTheory
		#WorkTotTheory2[index] = WorkTotTheory2[index] + WorkTheory2
		#WorkTotTheoryOld[index] = WorkTotTheoryOld[index] + WorkTheoryOld

for index in range(len(WorkTot)):
	WorkTotal.append(WorkTot[index]/float(NumberTrajectories))
	WorkTotalTheory.append(WorkTotTheory[index]/float(NumberTrajectories))
	#WorkTotalTheory2.append(WorkTotTheory2[index]/float(NumberTrajectories))
	#WorkTotalTheoryOld.append(WorkTotTheoryOld[index]/float(NumberTrajectories))

WriteData.WorkWrite(WorkTotal,Tau,filename_T,path)
WriteData.WorkWrite(WorkTotalTheory,Tau,filename_T2,path)
#WriteData.WorkWrite(WorkTotalTheory2,Tau,filename_T3,path)
#WriteData.WorkWrite(WorkTotalTheoryOld,Tau,filename_T4,path)

