#Plotting script for results from Time Separation Stochastic Control Simulations
#
#Steven Large
#January 6th 2017

import matplotlib.pyplot as plt

def PlotWork1(Time,Spring):

	filename1 = 'WorkDeterministic_TS_' +str(Time) + '_k' + str(Spring) + '.dat'
	filename2 = 'WorkStochastic_TS_' +str(Time) + '_k' + str(Spring) + '.dat'
	filename3 = 'WorkTotal_TS_' +str(Time) + '_k' + str(Spring) + '.dat'

	file1 = open(filename1,'r')
	file2 = open(filename2,'r')
	file3 = open(filename3,'r')

	data1 = file1.readlines()
	data2 = file2.readlines()
	data3 = file3.readlines()

	file1.close()
	file2.close()
	file3.close()

	TimeD = []
	WorkD = []
	TimeS = []
	WorkS = []
	TimeT = []
	WorkT = []

	for index1 in range(len(data1)-2):
		Parsed = data1[index1+2].split()
		TimeD.append(Parsed[0])
		WorkD.append(Parsed[1])

	for index2 in range(len(data2)-2):
		Parsed = data2[index2+2].split()
		TimeS.append(Parsed[0])
		WorkS.append(Parsed[1])

	for index3 in range(len(data3)-2):
		Parsed = data3[index3+2].split()
		TimeT.append(Parsed[0])
		WorkT.append(Parsed[1])

	plt.plot(TimeD,WorkD)
	plt.plot(TimeS,WorkS)
	plt.plot(TimeT,WorkT)
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.show()
	plt.close()






