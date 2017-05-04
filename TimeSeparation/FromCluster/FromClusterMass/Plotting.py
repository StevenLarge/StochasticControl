#Plotting script for February 11th stochastic control data
#
#Steven Large
#February 12th 2017

import matplotlib.pyplot as plt

def PlotAllM1():

	filename1 = 'WorkTotal_1_M1.dat'
	filename2 = 'WorkTheoryD_1_M1.dat'
	filename3 = 'WorkTheoryS_1_M1.dat'
	filename4 = 'WorkTheorySLag_1_M1.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(eval(parsed1[0]))
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for CPMass = 1')

	plt.savefig('Work_M1.png')

	plt.show()
	plt.close()


def PlotAllM2():

	filename1 = 'WorkTotal_1_M2.dat'
	filename2 = 'WorkTheoryD_1_M2.dat'
	filename3 = 'WorkTheoryS_1_M2.dat'
	filename4 = 'WorkTheorySLag_1_M2.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(eval(parsed1[0]))
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for CPMass = 2')

	plt.savefig('Work_M2.png')

	plt.show()
	plt.close()
	

def PlotAllM4():

	filename1 = 'WorkTotal_1_M4.dat'
	filename2 = 'WorkTheoryD_1_M4.dat'
	filename3 = 'WorkTheoryS_1_M4.dat'
	filename4 = 'WorkTheorySLag_1_M4.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(eval(parsed1[0]))
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for CPMass = 4')

	plt.savefig('Work_M4.png')

	plt.show()
	plt.close()
	

def PlotAllM8():

	filename1 = 'WorkTotal_1_M8.dat'
	filename2 = 'WorkTheoryD_1_M8.dat'
	filename3 = 'WorkTheoryS_1_M8.dat'
	filename4 = 'WorkTheorySLag_1_M8.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(eval(parsed1[0]))
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for CPMass = 8')

	plt.savefig('Work_M8.png')

	plt.show()
	plt.close()
	

def PlotAllM16():

	filename1 = 'WorkTotal_1_M16.dat'
	filename2 = 'WorkTheoryD_1_M16.dat'
	filename3 = 'WorkTheoryS_1_M16.dat'
	filename4 = 'WorkTheorySLag_1_M16.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(eval(parsed1[0]))
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for CPMass = 16')

	plt.savefig('Work_M16.png')

	plt.show()
	plt.close()
	

def PlotAllM32():

	filename1 = 'WorkTotal_1_M32.dat'
	filename2 = 'WorkTheoryD_1_M32.dat'
	filename3 = 'WorkTheoryS_1_M32.dat'
	filename4 = 'WorkTheorySLag_1_M32.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(eval(parsed1[0]))
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for CPMass = 32')

	plt.savefig('Work_M32.png')

	plt.show()
	plt.close()
	



