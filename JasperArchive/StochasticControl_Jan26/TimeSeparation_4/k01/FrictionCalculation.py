#This module calculates the generalized friction from the autocorrelation function analytically
#
#Steven Large
#January 3rd 2017

import random
import math
import numpy
from Parameters import *
import os

def WriteData(Correlation,filename):

	Completename = os.path.join('AutoCorrelation/' + filename)

	file1 = open(Completename,'w')

	file1.write('Time\tAutoCorrelation\n\n')

	Time = 0.0

	for index in range(len(Correlation)):

		file1.write('%lf\t%lf\n' % (Time,Correlation[index]))
		Time = Time + dt

	file1.close()

def Correlator(Trajectory,filename):

	MAXLAG = 500

	AutoCorr = []

	for index1 in range(MAXLAG):

		AutoCorr.append(0.0)

		for index2 in range(len(Trajectory)-index1):

			AutoCorr[index1] = AutoCorr[index1] + Trajectory[index2]*Trajectory[index2+index1]

		AutoCorr[index1] = AutoCorr[index1]/float(len(Trajectory)-index1)

	WriteData(AutoCorr,filename)

	Friction = 0

	for index3 in range(len(AutoCorr)):
		Friction = Friction + AutoCorr[index3]*dt

	return Friction,AutoCorr


def ReadData(filename):

	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	Trajectory = []

	for index in range(len(data)):
		Trajectory.append(-1*eval(data[index]))		#-1 gives the force, becuase k=1

	return Trajectory

def Primary(PositionTrack,TimeSeparation):

	ForceTrack = []

	WriteName = 'AutoCorrelation_' + str(TimeSeparation) + '.dat'

	for index in range(len(PositionTrack)):
		ForceTrack.append(-k*PositionTrack[index])

	Friction,AutoCorr = Correlator(ForceTrack,WriteName)

	return Friction,AutoCorr

