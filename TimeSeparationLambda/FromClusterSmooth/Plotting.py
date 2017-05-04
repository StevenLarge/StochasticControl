#Plotting Script for March 8th Smoothed-Stochastic Control simulations
#
#Steven Large
#March 8th 2017

import matplotlib.pyplot as plt


def PlotAllTau1():

	filename1 = 'WorkTotal_T1_k1.dat'
	filename2 = 'WorkTotal_T1_k2.dat'
	filename3 = 'WorkTotal_T1_k4.dat'
	filename4 = 'WorkTotal_T1_k8.dat'
	filename5 = 'WorkTotal_T1_k15.dat'
	filename6 = 'WorkTotal_T1_k32.dat'
	filename7 = 'WorkTotal_T1_k64.dat'
	filename8 = 'WorkTotal_T1_k75.dat'

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
	Time2 = []
	Time3 = []
	Time4 = []
	Time5 = []
	Time6 = []
	Time7 = []
	Time8 = []

	Work1 = []
	Work2 = []
	Work3 = []
	Work4 = []
	Work5 = []
	Work6 = []
	Work7 = []
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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))
		Time8.append(eval(parsed8[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='K = 1')
	Plot2 = plt.plot(Time2,Work2,label='K = 2')
	Plot3 = plt.plot(Time3,Work3,label='K = 4')
	Plot4 = plt.plot(Time4,Work4,label='K = 8')
	Plot5 = plt.plot(Time5,Work5,label='K = 16')
	Plot6 = plt.plot(Time6,Work6,label='K = 32')
	Plot7 = plt.plot(Time7,Work7,label='K = 64')
	Plot8 = plt.plot(Time8,Work8,label='K = 75')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Tau = 1')

	plt.savefig('WorkTotal_Tau1.png')

	plt.show()
	plt.close()


def PlotAllTau2():

	filename1 = 'WorkTotal_T2_k1.dat'
	filename2 = 'WorkTotal_T2_k2.dat'
	filename3 = 'WorkTotal_T2_k4.dat'
	filename4 = 'WorkTotal_T2_k8.dat'
	filename5 = 'WorkTotal_T2_k15.dat'
	filename6 = 'WorkTotal_T2_k32.dat'
	filename7 = 'WorkTotal_T2_k64.dat'
	filename8 = 'WorkTotal_T2_k75.dat'

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
	Time2 = []
	Time3 = []
	Time4 = []
	Time5 = []
	Time6 = []
	Time7 = []
	Time8 = []

	Work1 = []
	Work2 = []
	Work3 = []
	Work4 = []
	Work5 = []
	Work6 = []
	Work7 = []
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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))
		Time8.append(eval(parsed8[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='K = 1')
	Plot2 = plt.plot(Time2,Work2,label='K = 2')
	Plot3 = plt.plot(Time3,Work3,label='K = 4')
	Plot4 = plt.plot(Time4,Work4,label='K = 8')
	Plot5 = plt.plot(Time5,Work5,label='K = 16')
	Plot6 = plt.plot(Time6,Work6,label='K = 32')
	Plot7 = plt.plot(Time7,Work7,label='K = 64')
	Plot8 = plt.plot(Time8,Work8,label='K = 75')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Tau = 2')

	plt.savefig('WorkTotal_Tau2.png')

	plt.show()
	plt.close()


def PlotAllTau4():

	filename1 = 'WorkTotal_T4_k1.dat'
	filename2 = 'WorkTotal_T4_k2.dat'
	filename3 = 'WorkTotal_T4_k4.dat'
	filename4 = 'WorkTotal_T4_k8.dat'
	filename5 = 'WorkTotal_T4_k15.dat'
	filename6 = 'WorkTotal_T4_k32.dat'
	filename7 = 'WorkTotal_T4_k64.dat'
	filename8 = 'WorkTotal_T4_k75.dat'

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
	Time2 = []
	Time3 = []
	Time4 = []
	Time5 = []
	Time6 = []
	Time7 = []
	Time8 = []

	Work1 = []
	Work2 = []
	Work3 = []
	Work4 = []
	Work5 = []
	Work6 = []
	Work7 = []
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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))
		Time8.append(eval(parsed8[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='K = 1')
	Plot2 = plt.plot(Time2,Work2,label='K = 2')
	Plot3 = plt.plot(Time3,Work3,label='K = 4')
	Plot4 = plt.plot(Time4,Work4,label='K = 8')
	Plot5 = plt.plot(Time5,Work5,label='K = 16')
	Plot6 = plt.plot(Time6,Work6,label='K = 32')
	Plot7 = plt.plot(Time7,Work7,label='K = 64')
	Plot8 = plt.plot(Time8,Work8,label='K = 75')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Tau = 4')

	plt.savefig('WorkTotal_Tau4.png')

	plt.show()
	plt.close()


def PlotAllTau8():

	filename1 = 'WorkTotal_T8_k1.dat'
	filename2 = 'WorkTotal_T8_k2.dat'
	filename3 = 'WorkTotal_T8_k4.dat'
	filename4 = 'WorkTotal_T8_k8.dat'
	filename5 = 'WorkTotal_T8_k15.dat'
	filename6 = 'WorkTotal_T8_k32.dat'
	filename7 = 'WorkTotal_T8_k64.dat'
	filename8 = 'WorkTotal_T8_k75.dat'

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
	Time2 = []
	Time3 = []
	Time4 = []
	Time5 = []
	Time6 = []
	Time7 = []
	Time8 = []

	Work1 = []
	Work2 = []
	Work3 = []
	Work4 = []
	Work5 = []
	Work6 = []
	Work7 = []
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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))
		Time8.append(eval(parsed8[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='K = 1')
	Plot2 = plt.plot(Time2,Work2,label='K = 2')
	Plot3 = plt.plot(Time3,Work3,label='K = 4')
	Plot4 = plt.plot(Time4,Work4,label='K = 8')
	Plot5 = plt.plot(Time5,Work5,label='K = 16')
	Plot6 = plt.plot(Time6,Work6,label='K = 32')
	Plot7 = plt.plot(Time7,Work7,label='K = 64')
	Plot8 = plt.plot(Time8,Work8,label='K = 75')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Tau = 8')

	plt.savefig('WorkTotal_Tau8.png')

	plt.show()
	plt.close()


def PlotAllTau16():

	filename1 = 'WorkTotal_T16_k1.dat'
	filename2 = 'WorkTotal_T16_k2.dat'
	filename3 = 'WorkTotal_T16_k4.dat'
	filename4 = 'WorkTotal_T16_k8.dat'
	filename5 = 'WorkTotal_T16_k15.dat'
	filename6 = 'WorkTotal_T16_k32.dat'
	filename7 = 'WorkTotal_T16_k64.dat'
	filename8 = 'WorkTotal_T16_k75.dat'

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
	Time2 = []
	Time3 = []
	Time4 = []
	Time5 = []
	Time6 = []
	Time7 = []
	Time8 = []

	Work1 = []
	Work2 = []
	Work3 = []
	Work4 = []
	Work5 = []
	Work6 = []
	Work7 = []
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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))
		Time8.append(eval(parsed8[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='K = 1')
	Plot2 = plt.plot(Time2,Work2,label='K = 2')
	Plot3 = plt.plot(Time3,Work3,label='K = 4')
	Plot4 = plt.plot(Time4,Work4,label='K = 8')
	Plot5 = plt.plot(Time5,Work5,label='K = 16')
	Plot6 = plt.plot(Time6,Work6,label='K = 32')
	Plot7 = plt.plot(Time7,Work7,label='K = 64')
	Plot8 = plt.plot(Time8,Work8,label='K = 75')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Tau = 16')

	plt.savefig('WorkTotal_Tau16.png')

	plt.xscale('log')
	plt.yscale('log')

	plt.show()
	plt.close()

