#Generates an ensemble of control parameter trajectories
#
#Steven Large
#February 15th 2017

import TimeDriverLocal
import WriteData
import numpy as np

NumberTrajectories = 100						
TimeRange = 80

filename_base = 'CP_Trajectory_'
	
Tau = []
Variance = []

for index in range(TimeRange):

	ProtocolTime = 5 + 2.5*index 	

	filename_time = filename_base + str(ProtocolTime)

	DistAcc = 0
	VarAcc = 0

	for Realizations in range(NumberTrajectories):

		filename_tot = filename_time + '_' + str(Realizations) + '.dat'

		Time,Tracker,CPTrack = TimeDriverLocal.CPPropogator(ProtocolTime)

		WriteData.CPTrajectoryWrite2(Tracker,Time,filename_tot)


