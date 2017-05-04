#Plotting script for Constant Velocity Ensemble Tests
#
#Steven Large
#January 5th 2017

import numpy as np
import matplotlib.pyplot as plt

def PlotTrajectory(modifier):

	filename = str(modifier) + 'Tracking.dat'

	file1 = open(filename,'r')
	data = file1.readlines()
	Traj = []
	file1.close()

	for index in range(len(data)):
		Traj.append(eval(data[index]))

	plt.plot(Traj)
	plt.show()
	plt.close()

def PlotTrajCP():

	filename1 = 'PositionTracking.dat'
	filename2 = 'CPTracking.dat'

	file1 = open(filename1,'r')
	dataPos = file1.readlines()
	TrajPos = []
	file1.close()

	file2 = open(filename2,'r')
	dataCP = file2.readlines()
	TrajCP = []
	file2.close()

	for index in range(len(dataPos)):
		TrajPos.append(eval(dataPos[index]))
		TrajCP.append(eval(dataCP[index]))

	plt.plot(TrajPos)
	plt.plot(TrajCP)
	plt.show()
	plt.close()

def PlotWork():

	filename = 'WorkTotal_1.dat'

	file1 = open(filename,'r')
	data = file1.readlines()
	Work = []
	Time = []
	file1.close()

	for index in range(len(data)-2):
		parsed = data[index+2].split()
		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	plt.plot(Time,Work)
	plt.show()
	plt.close()



