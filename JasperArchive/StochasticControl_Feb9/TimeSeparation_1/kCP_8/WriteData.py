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

def TrajectoryWrite(PositionTrack,filenamePos,WritePath):

	CompleteNamePos = os.path.join(WritePath,filenamePos)

	file2 = open(CompleteNamePos,'w')
	for index in range(len(PositionTrack)):
		file2.write('%lf\n' % PositionTrack[index])
	file2.close()



	







