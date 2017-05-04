#Generates an ensemble of control parameter trajectories
#
#Steven Large
#February 15th 2017

import TimeDriverLocal
import WriteData
import numpy as np

#import matplotlib.pyplot as plt

NumberTrajectories = 100						
TimeRange = 40

#NumberTrajectories = 1
#TimeRange = 1

filename_base = 'CP_Trajectory_'

path = 'Trajectories/'
	
Tau = []
Variance = []

for index in range(TimeRange):

	ProtocolTime = 12.5 + 5*index 	
	#ProtocolTime = 100

	print 'Protocol Time --> %d\n' % ProtocolTime				

	filename_time = filename_base + str(ProtocolTime)

	DistAcc = 0
	VarAcc = 0

	for Realizations in range(NumberTrajectories):

		filename_tot = filename_time + '_' + str(Realizations) + '.dat'

		Time,Tracker,CPTrack = TimeDriverLocal.CPPropogator(ProtocolTime)

		#plt.plot(CPTrack)
		#plt.plot(Tracker)
		#plt.show()
		#plt.close()

		WriteData.CPTrajectoryWrite(Tracker,Time,filename_tot,path)

	#print "Done Realizations\n\n"

	#Tau.append(ProtocolTime)

	#plt.plot(CPTrack)
	#plt.plot(Tracker)
	#plt.show()
	#lt.close()


