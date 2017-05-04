#This script plots the data files input into the script
#
#Steven Large
#January 4th 2017

import numpy as np
import matplotlib.pyplot as plt

def PlotTotal(time,k):

	filename = 'WorkTotal_TS_' + str(time) + '_k' + str(k) + '.dat'

	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data)-2):

		parsed = data[index+2].split()

		Time.append(parsed[0])
		Work.append(parsed[1])

	plt.plot(Time,Work)
	plt.show()
	plt.xlabel('Protocol Time')
	plt.ylabel('Total Work')
	plt.close()

def PlotDeterministic(time,k):

	filename = 'WorkDeterministic_TS_' + str(time) + '_k' + str(k) + '.dat'

	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data)-2):

		parsed = data[index+2].split()

		Time.append(parsed[0])
		Work.append(parsed[1])

	plt.plot(Time,Work)
	plt.show()
	plt.xlabel('Protocol Time')
	plt.ylabel('Deterministic Work')
	plt.close()

def PlotStochastic(time,k):

	filename = 'WorkStochastic_TS_' + str(time) + '_k' + str(k) + '.dat'

	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data)-2):

		parsed = data[index+2].split()

		Time.append(parsed[0])
		Work.append(parsed[1])

	plt.plot(Time,Work)
	plt.show()
	plt.xlabel('Protocol Time')
	plt.ylabel('Stochastic Work')
	plt.close()


def PlotAll(time,k):

	filename1 = 'WorkTotal_TS_' + str(time) + '_k' + str(k) + '.dat'
	filename2 = 'WorkDeterministic_TS_' + str(time) + '_k' + str(k) + '.dat'
	filename3 = 'WorkStochastic_TS_' + str(time) + '_k' + str(k) + '.dat'

	file1 = open(filename1,'r')
	dataTotal = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	dataDeterministic = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	dataStochastic = file3.readlines()
	file3.close()

	TimeTotal = []
	WorkTotal = []

	TimeDeterministic = []
	WorkDeterministic = []

	TimeStochastic = []
	WorkStochastic = []

	for index in range(len(dataTotal)-2):
		parsed = dataTotal[index+2].split()
		TimeTotal.append(parsed[0])
		WorkTotal.append(parsed[1])

	for index in range(len(dataDeterministic)-2):
		parsed = dataDeterministic[index+2].split()
		TimeDeterministic.append(parsed[0])
		WorkDeterministic.append(parsed[1])

	for index in range(len(dataStochastic)-2):
		parsed = dataStochastic[index+2].split()
		TimeStochastic.append(parsed[0])
		WorkStochastic.append(parsed[1])



	plt.plot(TimeTotal,WorkTotal)
	plt.plot(TimeDeterministic,WorkDeterministic)
	plt.plot(TimeStochastic,WorkStochastic)
	plt.show()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.close()










