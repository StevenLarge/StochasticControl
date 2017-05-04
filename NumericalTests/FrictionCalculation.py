#This module calculates the generalized friction from the autocorrelation function analytically
#
#Steven Large
#January 3rd 2017

import random
import math
from Parameters import *
import LangevinPropogator
import numpy
import matplotlib.pyplot as plt

def WriteData(Correlation):

	file1 = open('AutoCorrelation.dat','w')

	file1.write('Time\tAutoCorrelation\n\n')

	Time = 0.0

	for index in range(len(Correlation)):

		file1.write('%lf\t%lf\n' % (Time,Correlation[index]))
		Time = Time + dt

	file1.close()

def Correlator(Trajectory):

	MAXLAG = 1000

	AutoCorr = []

	for index1 in range(MAXLAG):

		AutoCorr.append(0.0)

		for index2 in range(len(Trajectory)-index1):

			AutoCorr[index1] = AutoCorr[index1] + Trajectory[index2]*Trajectory[index2+index1]

		AutoCorr[index1] = AutoCorr[index1]/float(len(Trajectory)-index1)

	WriteData(AutoCorr)

	plt.plot(AutoCorr)
	plt.show()
	plt.close()

	Friction = 0

	for index3 in range(len(AutoCorr)):
		Friction = Friction + AutoCorr[index3]*dt

	return Friction

CP = 0
position = 0
velocity = 0

Equilibration = 100
TrajectoryTime = 100000

ForceTrack = []

time = 0

while time < Equilibration:

	(time,position,velocity) = LangevinPropogator.LangevinTrajectory(time,position,velocity)
		
time = 0

while time < TrajectoryTime:

	(time,position,velocity) = LangevinPropogator.LangevinTrajectory(time,position,velocity)
	ForceTrack.append(-k*(position))
		
Friction = Correlator(ForceTrack)

print "\n\n"
print ("Friction \t\t-->%lf" % Friction)
print "\n\n"
