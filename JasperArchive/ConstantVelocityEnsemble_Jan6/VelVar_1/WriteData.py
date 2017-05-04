#This module contains the necessary data writing routines for calculation of Force autocorrelation functions in Langevin simulations
#of a stationary OU process to calculate the friction coefficient
#
#Steven Large
#May 10th 2015

import os

def WorkWrite(data,time,filename,WritePath):

	CompleteName = os.path.join(WritePath,filename)
	file1 = open(CompleteName,'w')
	file1.write('ProtocolTime\tWork\n\n')

	for k in range(len(data)):
		file1.write('%d\t%lf\n' % (time[k], data[k]))
	file1.close()

def TimeWrite(OuterTime,InnerTime,filename,WritePath):

	CompleteName = os.path.join(WritePath,filename)
	file1 = open(CompleteName,'w')
	file1.write('CPTime\tInternalTime\n\n')

	for k in range(len(OuterTime)):
		file1.write('%0.2lf\t%.2lf\n' % (OuterTime[k],InnerTime[k]))
	file1.close()

def TrajectoryWrite(Data,filename,WritePath):

	CompleteName = os.path.join(WritePath,filename)
	file1 = open(CompleteName,'w')
	
	for index in range(len(Data)):
		file1.write('%lf\n' % Data[index])
	file1.close()







