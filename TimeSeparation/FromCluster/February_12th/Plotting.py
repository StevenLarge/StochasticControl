#Plotting script for February 12th stochastic control simualtions
#
#Steven Large
#February 13th 2017

import matplotlib.pyplot as plt

def PlotAll1():

	filename1 = 'WorkTotal_1.dat'
	filename2 = 'WorkTheoryD_1.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))

		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 1')
	plt.savefig('WorkPlot_1.png')

	plt.show()
	plt.close()


def PlotAll2():

	filename1 = 'WorkTotal_2.dat'
	filename2 = 'WorkTheoryD_2.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))

		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 2')
	plt.savefig('WorkPlot_2.png')

	plt.show()
	plt.close()


def PlotAll4():

	filename1 = 'WorkTotal_4.dat'
	filename2 = 'WorkTheoryD_4.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))

		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 4')
	plt.savefig('WorkPlot_4.png')

	plt.show()
	plt.close()


def PlotAll8():


	filename1 = 'WorkTotal_8.dat'
	filename2 = 'WorkTheoryD_8.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))

		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 8')
	plt.savefig('WorkPlot_8.png')

	plt.show()
	plt.close()


def PlotAll16():


	filename1 = 'WorkTotal_16.dat'
	filename2 = 'WorkTheoryD_16.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))

		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 16')
	plt.savefig('WorkPlot_16.png')

	plt.show()
	plt.close()


def PlotAll32():


	filename1 = 'WorkTotal_32.dat'
	filename2 = 'WorkTheoryD_32.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))

		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 32')
	plt.savefig('WorkPlot_32.png')

	plt.show()
	plt.close()




