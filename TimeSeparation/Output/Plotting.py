#Plotting script for Time Separation Work Results
#
#Steven Large
#January 13th 2016

import matplotlib.pyplot as plt

def Plot16():

	filename1 = 'WorkTotal_TS_1_k16.dat'
	filename2 = 'WorkTheoryD_TS_1_k16.dat'
	filename3 = 'WorkTheoryS_TS_1_k16.dat'
	filename4 = 'WorkTheorySLag_TS_1_k16.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 16')

	plt.savefig('TotalWork_16.png')

	plt.show()
	plt.close()

def Plot8():

	filename1 = 'WorkTotal_TS_1_k8.dat'
	filename2 = 'WorkTheoryD_TS_1_k8.dat'
	filename3 = 'WorkTheoryS_TS_1_k8.dat'
	filename4 = 'WorkTheorySLag_TS_1_k8.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 8')

	plt.savefig('TotalWork_8.png')

	plt.show()
	plt.close()

def Plot32():

	filename1 = 'WorkTotal_TS_1_k32.dat'
	filename2 = 'WorkTheoryD_TS_1_k32.dat'
	filename3 = 'WorkTheoryS_TS_1_k32.dat'
	filename4 = 'WorkTheorySLag_TS_1_k32.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 32')

	plt.savefig('TotalWork_32.png')

	plt.show()
	plt.close()

def Plot64():

	filename1 = 'WorkTotal_TS_1_k64.dat'
	filename2 = 'WorkTheoryD_TS_1_k64.dat'
	filename3 = 'WorkTheoryS_TS_1_k64.dat'
	filename4 = 'WorkTheorySLag_TS_1_k64.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 64')

	plt.savefig('TotalWork_64.png')

	plt.show()
	plt.close()

def Plot128():

	filename1 = 'WorkTotal_TS_1_k128.dat'
	filename2 = 'WorkTheoryD_TS_1_k128.dat'
	filename3 = 'WorkTheoryS_TS_1_k128.dat'
	filename4 = 'WorkTheorySLag_TS_1_k128.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 128')

	plt.savefig('TotalWork_128.png')

	plt.show()
	plt.close()

def Plot1():

	filename1 = 'WorkTotal_TS_1_k1.dat'
	filename2 = 'WorkTheoryD_TS_1_k1.dat'
	filename3 = 'WorkTheoryS_TS_1_k1.dat'
	filename4 = 'WorkTheorySLag_TS_1_k1.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 1, Sigma = 0.1')

	plt.savefig('TotalWork_1_Sigma.png')

	plt.show()
	plt.close()

def Plot01():

	filename1 = 'WorkTotal_TS_1_k0.1.dat'
	filename2 = 'WorkTheoryD_TS_1_k0.1.dat'
	filename3 = 'WorkTheoryS_TS_1_k0.1.dat'
	filename4 = 'WorkTheorySLag_TS_1_k0.1.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 0.1')

	plt.savefig('TotalWork_01.png')

	plt.show()
	plt.close()

def Plot005():

	filename1 = 'WorkTotal_TS_1_k0.05.dat'
	filename2 = 'WorkTheoryD_TS_1_k0.05.dat'
	filename3 = 'WorkTheoryS_TS_1_k0.05.dat'
	filename4 = 'WorkTheorySLag_TS_1_k0.05.dat'

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
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions for k = 0.5')

	plt.savefig('TotalWork_005.png')

	plt.show()
	plt.close()

def PlotAll2():

	filename1 = 'WorkTotal_TS_2.dat'
	filename2 = 'WorkTheoryD_TS_2.dat'
	filename3 = 'WorkTheoryS_TS_2.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 2')

	plt.savefig('TotalWork_TS_2.png')

	plt.show()
	plt.close()


def PlotAll1():


	filename1 = 'WorkTotal_TS_1.dat'
	filename2 = 'WorkTheoryD_TS_1.dat'
	filename3 = 'WorkTheoryS_TS_1.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 1')

	plt.savefig('TotalWork_TS_1.png')

	plt.show()
	plt.close()


def PlotAll4(modifier):

	filename1 = 'WorkTotal_TS_4_k' + modifier + '.dat'
	filename2 = 'WorkTheoryD_TS_4_k' + modifier + '.dat'
	filename3 = 'WorkTheoryS_TS_4_k' + modifier + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))

	Plot1 = plt.plot(Time1,Work1,label='Total Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Time Separation = 4')

	plt.savefig('TotalWork_TS_4.png')

	plt.show()
	plt.close()




