#This module writes the work and work variance data to file
#
#Steven Large
#January 17th 2017

import os

def WriteWork(AvgWork,Tau):

	WritePath = 'Output/'
	Filename = 'AvgWork.dat'
	CompleteName = os.path.join(WritePath,Filename)

	file1 = open(CompleteName,'w')

	file1.write('Tau\tWork\n\n')

	for index in range(len(AvgWork)):
		file1.write('%lf\t%lf\n' % (Tau[index],AvgWork[index]))

	file1.close()


def WriteWorkVariance(WorkVar,Tau):

	WritePath = 'Output/'
	Filename = 'WorkVariance.dat'
	CompleteName = os.path.join(WritePath,Filename)

	file1 = open(CompleteName,'w')

	file1.write('Tau\tWorkVariance\n\n')

	for index in range(len(WorkVar)):
		file1.write('%lf\t%lf\n' % (Tau[index],WorkVar[index]))

	file1.close()


