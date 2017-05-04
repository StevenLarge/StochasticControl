#This module simulates stationary dynamics at different fixed control parameter values to show the 
#differences in relaxation time
#
#Steven Large
#February 14th 2017

import TimeDriverLocal
from Parameters import *
import WriteData
import FrictionCalculation
import os
from TimeParameters import *

SampleTime = 200000

path = 'Relaxation/'

filename_base = 'Relaxation_k'
trajectory_base = 'Trajectory_k'

Springs = [1,2,3,4,5]

RelaxationTimes = []

for index in range(len(Springs)):

	print 'Springs --> %d\n' % Springs[index]

	CompleteName = trajectory_base + str(Springs[index]) + '.dat'
	PositionTrack = TimeDriverLocal.FrictionPropogator(SampleTime,1)
	WriteData.TrajectoryWrite(PositionTrack,CompleteName,path)
	Friction,AutoCorr = FrictionCalculation.Primary(PositionTrack,TimeSeparation,'NULL.dat')
	Relaxation = FrictionCalculation.RelaxationTime(AutoCorr)
	RelaxationAcc = 0

	for index2 in range(len(Relaxation)):
		RelaxationAcc = RelaxationAcc + Relaxation[index]*dt

	RelaxationName = filename_base + str(Springs[index]) + '.dat'
	RelaxationNameComplete = os.path.join(path,RelaxationName)

	file1 = open(RelaxationNameComplete,'w')
	file1.write('Relaxation\tTimeSeparation\n\n')

	Time = 0.0

	for index2 in range(len(Relaxation)):
		file1.write('%lf\t%d\n' % (Relaxation[index2], Time))
		Time = Time + dt

	file1.close()
	RelaxationTimes.append(RelaxationAcc)










