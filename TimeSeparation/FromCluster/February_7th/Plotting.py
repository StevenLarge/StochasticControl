#This is a Plotting Script for the Feb 7th Time Separation Stocahstic Control Data 
#
#Steven Large
#February 8th 2017

import matplotlib.pyplot as plt


def PlotAll1():

	filename1 = 'WorkTotal_1.dat'
	filename2 = 'WorkTheoryD_1.dat'
	filename3 = 'WorkTheoryS_1.dat'
	filename4 = 'WorkTheorySLag_1.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 1')
	
	plt.savefig('TimeSeparation_1.png')
	
	plt.show()
	plt.close()

	
def PlotAll2():

	filename1 = 'WorkTotal_2.dat'
	filename2 = 'WorkTheoryD_2.dat'
	filename3 = 'WorkTheoryS_2.dat'
	filename4 = 'WorkTheorySLag_2.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 2')
	
	plt.savefig('TimeSeparation_2.png')
	
	plt.show()
	plt.close()

	
def PlotAll4():

	filename1 = 'WorkTotal_4.dat'
	filename2 = 'WorkTheoryD_4.dat'
	filename3 = 'WorkTheoryS_4.dat'
	filename4 = 'WorkTheorySLag_4.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 4')
	
	plt.savefig('TimeSeparation_4.png')
	
	plt.show()
	plt.close()

	
def PlotAll8():

	filename1 = 'WorkTotal_8.dat'
	filename2 = 'WorkTheoryD_8.dat'
	filename3 = 'WorkTheoryS_8.dat'
	filename4 = 'WorkTheorySLag_8.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 8')
	
	plt.savefig('TimeSeparation_8.png')
	
	plt.show()
	plt.close()

	
def PlotAll16():

	filename1 = 'WorkTotal_16.dat'
	filename2 = 'WorkTheoryD_16.dat'
	filename3 = 'WorkTheoryS_16.dat'
	filename4 = 'WorkTheorySLag_16.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 16')
	
	plt.savefig('TimeSeparation_16.png')
	
	plt.show()
	plt.close()

	
def PlotAll32():

	filename1 = 'WorkTotal_32.dat'
	filename2 = 'WorkTheoryD_32.dat'
	filename3 = 'WorkTheoryS_32.dat'
	filename4 = 'WorkTheorySLag_32.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 32')
	
	plt.savefig('TimeSeparation_32.png')
	
	plt.show()
	plt.close()

	
def PlotAll64():

	filename1 = 'WorkTotal_64.dat'
	filename2 = 'WorkTheoryD_64.dat'
	filename3 = 'WorkTheoryS_64.dat'
	filename4 = 'WorkTheorySLag_64.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 64')
	
	plt.savefig('TimeSeparation_64.png')
	
	plt.show()
	plt.close()

	
def PlotAll128():

	filename1 = 'WorkTotal_128.dat'
	filename2 = 'WorkTheoryD_128.dat'
	filename3 = 'WorkTheoryS_128.dat'
	filename4 = 'WorkTheorySLag_128.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 128')
	
	plt.savefig('TimeSeparation_128.png')
	
	plt.show()
	plt.close()


def PlotAll256():

	filename1 = 'WorkTotal_256.dat'
	filename2 = 'WorkTheoryD_256.dat'
	filename3 = 'WorkTheoryS_256.dat'
	filename4 = 'WorkTheorySLag_256.dat'

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

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])		

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 256')
	
	plt.savefig('TimeSeparation_256.png')
	
	plt.show()
	plt.close()
	


