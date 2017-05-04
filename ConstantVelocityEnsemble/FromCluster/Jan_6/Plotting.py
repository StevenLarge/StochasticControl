#Plotting script for constant velocity protocol ensemble January 6th
#
#Steven Large
#January 6th 2017

import matplotlib.pyplot as plt

def PlotWork1(modifier):

	filename = 'WorkTotal_' + str(modifier) + '.dat'

	file1 = open(filename,'r')

	data = file1.readlines()
	file1.close()

	Time = []
	Data = []

	for index in range(len(data)-2):

		parsed = data[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	plt.plot(Time,Work)
	plt.show()
	plt.close()

def PlotWorkAll():

	modifiers = ['01','05','1','2','4','8']

	for index1 in range(len(modifiers)):

		filename = 'WorkTotal_' + modifiers[index1] + '.dat'

		file1 = open(filename,'r')

		data = file1.readlines()
		file1.close()

		Time = []
		Work = []

		for index in range(len(data)-2):

			parsed = data[index+2].split()

			Time.append(eval(parsed[0]))
			Work.append(eval(parsed[1]))

		plt.plot(Time,Work)

	plt.show()
	plt.close()







