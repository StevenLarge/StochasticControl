#This module contains the necessary data writing routines for calculation of Force autocorrelation functions in Langevin simulations
#of a stationary OU process to calculate the friction coefficient
#
#Steven Large
#May 10th 2015


def WorkWrite(data,time,filename):

	file1 = open(filename,'w')

	file1.write('ProtocolTime\tWork\n\n')

	for k in range(len(data)):

		file1.write('%d\t%lf\n' % (time[k], data[k]))

	file1.close()

def TrajectoryWrite(data,filename,identity):

	file1 = open(filename,'w')

	file1.write(identity + '\n\n')

	for k in range(len(data)):

		file1.write('%lf\n' % data[k])

	file1.close()

def Variance(data,time,filename):

	file1 = open(filename,'w')

	file1.write('ProtocolTime\tVariance\n\n')

	for k in range(len(data)):

		file1.write('%d\t%lf\n' % (time[k], data[k]))

	file1.close()
