#Plotting script for February 14th simulations
#
#February 15th 2017
#Steven Large

import matplotlib.pyplot as plt

def PlotAll2():

	filename1 = 'WorkTotal_2_2.dat'
	filename2 = 'WorkTheoryD_2_2.dat'
	filename3 = 'WorkTheoryS_2_2.dat'

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

	plt.savefig('WorkTS_2_k2.png')

	plt.show()
	plt.close()


def PlotAll4():

	filename1 = 'WorkTotal_4_2.dat'
	filename2 = 'WorkTheoryD_4_2.dat'
	filename3 = 'WorkTheoryS_4_2.dat'

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

	plt.savefig('WorkTS_4_k2.png')

	plt.show()
	plt.close()


def PlotAll8():

	filename1 = 'WorkTotal_8_2.dat'
	filename2 = 'WorkTheoryD_8_2.dat'
	filename3 = 'WorkTheoryS_8_2.dat'

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
	plt.title('Time Separation = 8')

	plt.savefig('WorkTS_8_k2.png')

	plt.show()
	plt.close()


def PlotAll16():

	filename1 = 'WorkTotal_16_2.dat'
	filename2 = 'WorkTheoryD_16_2.dat'
	filename3 = 'WorkTheoryS_16_2.dat'

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
	plt.title('Time Separation = 16')

	plt.savefig('WorkTS_16_k2.png')

	plt.show()
	plt.close()


def PlotAll32():

	filename1 = 'WorkTotal_32_2.dat'
	filename2 = 'WorkTheoryD_32_2.dat'
	filename3 = 'WorkTheoryS_32_2.dat'

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
	plt.title('Time Separation = 32')

	plt.savefig('WorkTS_32_k2.png')

	plt.show()
	plt.close()


def PlotAll64():

	filename1 = 'WorkTotal_64_2.dat'
	filename2 = 'WorkTheoryD_64_2.dat'
	filename3 = 'WorkTheoryS_64_2.dat'

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
	plt.title('Time Separation = 64')

	plt.savefig('WorkTS_64_k2.png')

	plt.show()
	plt.close()


def PlotAll128():

	filename1 = 'WorkTotal_128_2.dat'
	filename2 = 'WorkTheoryD_128_2.dat'
	filename3 = 'WorkTheoryS_128_2.dat'

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
	plt.title('Time Separation = 128')

	plt.savefig('WorkTS_128_k2.png')

	plt.show()
	plt.close()


def PlotAll256():

	filename1 = 'WorkTotal_256_2.dat'
	filename2 = 'WorkTheoryD_256_2.dat'
	filename3 = 'WorkTheoryS_256_2.dat'

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
	plt.title('Time Separation = 256')

	plt.savefig('WorkTS_256_k2.png')

	plt.show()
	plt.close()


def PlotTotalNorm():

	filename1 = 'WorkTotalN_2.dat'
	filename2 = 'WorkTotalN_4.dat'
	filename3 = 'WorkTotalN_8.dat'
	filename4 = 'WorkTotalN_16.dat'
	filename5 = 'WorkTotalN_32.dat'
	filename6 = 'WorkTotalN_64.dat'
	filename7 = 'WorkTotalN_128.dat'
	filename8 = 'WorkTotalN_256.dat'

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

	file5 = open(filename5,'r')
	data5 = file5.readlines()
	file5.close()

	file6 = open(filename6,'r')
	data6 = file6.readlines()
	file6.close()

	file7 = open(filename7,'r')
	data7 = file7.readlines()
	file7.close()

	file8 = open(filename8,'r')
	data8 = file8.readlines()
	file8.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []
	Time7 = []
	Work7 = []
	Time8 = []
	Work8 = []

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		parsed8 = data8[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))
		Time5.append(eval(parsed5[0]))
		Work5.append(eval(parsed5[1]))
		Time6.append(eval(parsed6[0]))
		Work6.append(eval(parsed6[1]))
		Time7.append(eval(parsed7[0]))
		Work7.append(eval(parsed7[1]))
		Time8.append(eval(parsed8[0]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='WorkTotal TS = 2')
	Plot2 = plt.plot(Time2,Work2,label='WorkTotal TS = 4')
	Plot3 = plt.plot(Time3,Work3,label='WorkTotal TS = 8')
	Plot4 = plt.plot(Time4,Work4,label='WorkTotal TS = 16')
	Plot5 = plt.plot(Time5,Work5,label='WorkTotal TS = 32')
	Plot6 = plt.plot(Time6,Work6,label='WorkTotal TS = 64')
	Plot7 = plt.plot(Time7,Work7,label='WorkTotal TS = 128')
	Plot8 = plt.plot(Time8,Work8,label='WorkTotal TS = 256')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work/Friction')
	plt.title('Normalized Friction')

	plt.savefig('WorkNorm.png')

	plt.show()
	plt.close()



