#This is a plotting script for the WorkTotal files of different velocity variances
#
#Steven Large
#January 5th 2017

import matplotlib.pyplot as plt
import numpy as np

def PlotOne(modifier):

	filename = 'WorkTotal_' + str(modifier) + '.dat'

	Time = []
	Work = []

	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	for index in range(len(data)-2):
	 	parsed = data[index+2].split()
	 	Time.append(eval(parsed[0]))
	 	Work.append(eval(parsed[1]))

	plt.plot(Time,Work)
	plt.xlabel('Time')
	plt.ylabel('Work')
	plt.show()
	plt.close()

def PlotAll():

	modifiers = ['01','05','1','2','4','8']

	for index1 in range(len(modifiers)):

		Time = []
		Work = []

		filename = 'WorkTotal_' + modifiers[index1] +'.dat'

		file1 = open(filename,'r')
		data = file1.readlines()
		file1.close()

	 	for index in range(len(data)-2):
	 		parsed = data[index+2].split()
	 		Time.append(eval(parsed[0]))
	 		Work.append(eval(parsed[1]))

	 	plt.plot(Time,Work)

	plt.xlabel('Time')
	plt.ylabel('Work')
	plt.show()
	plt.close()


