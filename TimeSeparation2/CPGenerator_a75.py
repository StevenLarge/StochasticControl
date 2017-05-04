#Generates an ensemble of control parameter trajectories
#
#Steven Large
#February 15th 2017

import TimeDriverLocal_a75
import WriteData
import numpy as np

import matplotlib.pyplot as plt

NumberTrajectories = 100						
TimeRange = 40

filename_base = 'CP_Trajectory_'

path = 'Trajectories/'

Tau = []
Variance = []

for index in range(TimeRange):

	ProtocolTime = 10 + 5*index 	

	#print 'Protocol Time --> %d\n' % ProtocolTime				

	filename_time = filename_base + str(ProtocolTime)

	DistAcc = 0
	VarAcc = 0

	for Realizations in range(NumberTrajectories):

		filename_tot = filename_time + '_' + str(Realizations) + '.dat'

		Time,Tracker,VelTrack = TimeDriverLocal_a75.CPPropogator(ProtocolTime)

		VarAcc = VarAcc + np.var(VelTrack)

		WriteData.CPTrajectoryWrite(Tracker,Time,filename_tot,path)

	Variance.append(VarAcc/float(NumberTrajectories))
	Tau.append(ProtocolTime)

#print 'Avg Variance --> %lf' % np.mean(Variance)




