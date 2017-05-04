#Plotting Script for February 19th Data
#
#Steven Large
#February 22nd 2017

import matplotlib.pyplot as plt

def PlotAllK1():

	filename1 = 'WorkTotal_25_k1.dat'
	filename2 = 'WorkTotal_50_k1.dat'
	filename3 = 'WorkTotal_75_k1.dat'
	filename4 = 'WorkTotal_90_k1.dat'
	filename5 = 'WorkTotal_95_k1.dat'
	filename6 = 'WorkTotal_99_k1.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work k = 1')

	plt.savefig('WorkTotals_k1.png')

	plt.show()
	plt.close()


def PlotAllK2():

	filename1 = 'WorkTotal_25_k2.dat'
	filename2 = 'WorkTotal_50_k2.dat'
	filename3 = 'WorkTotal_75_k2.dat'
	filename4 = 'WorkTotal_90_k2.dat'
	filename5 = 'WorkTotal_95_k2.dat'
	filename6 = 'WorkTotal_99_k2.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 2')

	plt.savefig('WorkTotals_k2.png')

	plt.show()
	plt.close()


def PlotAllK4():


	filename1 = 'WorkTotal_25_k4.dat'
	filename2 = 'WorkTotal_50_k4.dat'
	filename3 = 'WorkTotal_75_k4.dat'
	filename4 = 'WorkTotal_90_k4.dat'
	filename5 = 'WorkTotal_95_k4.dat'
	filename6 = 'WorkTotal_99_k4.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 4')

	plt.savefig('WorkTotals_k4.png')

	plt.show()
	plt.close()


def PlotAllK8():


	filename1 = 'WorkTotal_25_k8.dat'
	filename2 = 'WorkTotal_50_k8.dat'
	filename3 = 'WorkTotal_75_k8.dat'
	filename4 = 'WorkTotal_90_k8.dat'
	filename5 = 'WorkTotal_95_k8.dat'
	filename6 = 'WorkTotal_99_k8.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 8')

	plt.savefig('WorkTotals_k8.png')

	plt.show()
	plt.close()


def PlotAllK16():


	filename1 = 'WorkTotal_25_k16.dat'
	filename2 = 'WorkTotal_50_k16.dat'
	filename3 = 'WorkTotal_75_k16.dat'
	filename4 = 'WorkTotal_90_k16.dat'
	filename5 = 'WorkTotal_95_k16.dat'
	filename6 = 'WorkTotal_99_k16.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 16')

	plt.savefig('WorkTotals_k16.png')

	plt.show()
	plt.close()


def PlotAllK32():


	filename1 = 'WorkTotal_25_k32.dat'
	filename2 = 'WorkTotal_50_k32.dat'
	filename3 = 'WorkTotal_75_k32.dat'
	filename4 = 'WorkTotal_90_k32.dat'
	filename5 = 'WorkTotal_95_k32.dat'
	filename6 = 'WorkTotal_99_k32.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 32')

	plt.savefig('WorkTotals_k32.png')

	plt.show()
	plt.close()


def PlotAllK64():


	filename1 = 'WorkTotal_25_k64.dat'
	filename2 = 'WorkTotal_50_k64.dat'
	filename3 = 'WorkTotal_75_k64.dat'
	filename4 = 'WorkTotal_90_k64.dat'
	filename5 = 'WorkTotal_95_k64.dat'
	filename6 = 'WorkTotal_99_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 64')

	plt.savefig('WorkTotals_k64.png')

	plt.show()
	plt.close()


def PlotAllA25():


	filename1 = 'WorkTotal_25_k1.dat'
	filename2 = 'WorkTotal_25_k2.dat'
	filename3 = 'WorkTotal_25_k4.dat'
	filename4 = 'WorkTotal_25_k8.dat'
	filename5 = 'WorkTotal_25_k16.dat'
	filename6 = 'WorkTotal_25_k32.dat'
	filename7 = 'WorkTotal_25_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.25')

	plt.savefig('WorkTotals_a25.png')

	plt.show()
	plt.close()


def PlotAllA50():


	filename1 = 'WorkTotal_50_k1.dat'
	filename2 = 'WorkTotal_50_k2.dat'
	filename3 = 'WorkTotal_50_k4.dat'
	filename4 = 'WorkTotal_50_k8.dat'
	filename5 = 'WorkTotal_50_k16.dat'
	filename6 = 'WorkTotal_50_k32.dat'
	filename7 = 'WorkTotal_50_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.50')

	plt.savefig('WorkTotals_a50.png')

	plt.show()
	plt.close()


def PlotAllA75():

	filename1 = 'WorkTotal_75_k1.dat'
	filename2 = 'WorkTotal_75_k2.dat'
	filename3 = 'WorkTotal_75_k4.dat'
	filename4 = 'WorkTotal_75_k8.dat'
	filename5 = 'WorkTotal_75_k16.dat'
	filename6 = 'WorkTotal_75_k32.dat'
	filename7 = 'WorkTotal_75_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.75')

	plt.savefig('WorkTotals_a75.png')

	plt.show()
	plt.close()


def PlotAllA90():

	filename1 = 'WorkTotal_90_k1.dat'
	filename2 = 'WorkTotal_90_k2.dat'
	filename3 = 'WorkTotal_90_k4.dat'
	filename4 = 'WorkTotal_90_k8.dat'
	filename5 = 'WorkTotal_90_k16.dat'
	filename6 = 'WorkTotal_90_k32.dat'
	filename7 = 'WorkTotal_90_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.90')

	plt.savefig('WorkTotals_a90.png')

	plt.show()
	plt.close()


def PlotAllA95():

	filename1 = 'WorkTotal_95_k1.dat'
	filename2 = 'WorkTotal_95_k2.dat'
	filename3 = 'WorkTotal_95_k4.dat'
	filename4 = 'WorkTotal_95_k8.dat'
	filename5 = 'WorkTotal_95_k16.dat'
	filename6 = 'WorkTotal_95_k32.dat'
	filename7 = 'WorkTotal_95_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.95')

	plt.savefig('WorkTotals_a95.png')

	plt.show()
	plt.close()


def PlotAllA99():

	filename1 = 'WorkTotal_99_k1.dat'
	filename2 = 'WorkTotal_99_k2.dat'
	filename3 = 'WorkTotal_99_k4.dat'
	filename4 = 'WorkTotal_99_k8.dat'
	filename5 = 'WorkTotal_99_k16.dat'
	filename6 = 'WorkTotal_99_k32.dat'
	filename7 = 'WorkTotal_99_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.99')

	plt.savefig('WorkTotals_a99.png')

	plt.show()
	plt.close()




def LogPlotAllK1():

	filename1 = 'WorkTotal_25_k1.dat'
	filename2 = 'WorkTotal_50_k1.dat'
	filename3 = 'WorkTotal_75_k1.dat'
	filename4 = 'WorkTotal_90_k1.dat'
	filename5 = 'WorkTotal_95_k1.dat'
	filename6 = 'WorkTotal_99_k1.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work k = 1')

	plt.savefig('LogWorkTotals_k1.png')

	plt.show()
	plt.close()


def LogPlotAllK2():

	filename1 = 'WorkTotal_25_k2.dat'
	filename2 = 'WorkTotal_50_k2.dat'
	filename3 = 'WorkTotal_75_k2.dat'
	filename4 = 'WorkTotal_90_k2.dat'
	filename5 = 'WorkTotal_95_k2.dat'
	filename6 = 'WorkTotal_99_k2.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 2')

	plt.savefig('LogWorkTotals_k2.png')

	plt.show()
	plt.close()


def LogPlotAllK4():


	filename1 = 'WorkTotal_25_k4.dat'
	filename2 = 'WorkTotal_50_k4.dat'
	filename3 = 'WorkTotal_75_k4.dat'
	filename4 = 'WorkTotal_90_k4.dat'
	filename5 = 'WorkTotal_95_k4.dat'
	filename6 = 'WorkTotal_99_k4.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 4')

	plt.savefig('LogWorkTotals_k4.png')

	plt.show()
	plt.close()


def LogPlotAllK8():


	filename1 = 'WorkTotal_25_k8.dat'
	filename2 = 'WorkTotal_50_k8.dat'
	filename3 = 'WorkTotal_75_k8.dat'
	filename4 = 'WorkTotal_90_k8.dat'
	filename5 = 'WorkTotal_95_k8.dat'
	filename6 = 'WorkTotal_99_k8.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 8')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_k8.png')

	plt.show()
	plt.close()


def LogPlotAllK16():


	filename1 = 'WorkTotal_25_k16.dat'
	filename2 = 'WorkTotal_50_k16.dat'
	filename3 = 'WorkTotal_75_k16.dat'
	filename4 = 'WorkTotal_90_k16.dat'
	filename5 = 'WorkTotal_95_k16.dat'
	filename6 = 'WorkTotal_99_k16.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 16')

	plt.yscale('log')
	plt.xscale('log')

	plt.savefig('LogWorkTotals_k16.png')

	plt.show()
	plt.close()


def LogPlotAllK32():


	filename1 = 'WorkTotal_25_k32.dat'
	filename2 = 'WorkTotal_50_k32.dat'
	filename3 = 'WorkTotal_75_k32.dat'
	filename4 = 'WorkTotal_90_k32.dat'
	filename5 = 'WorkTotal_95_k32.dat'
	filename6 = 'WorkTotal_99_k32.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 32')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_k32.png')

	plt.show()
	plt.close()


def LogPlotAllK64():


	filename1 = 'WorkTotal_25_k64.dat'
	filename2 = 'WorkTotal_50_k64.dat'
	filename3 = 'WorkTotal_75_k64.dat'
	filename4 = 'WorkTotal_90_k64.dat'
	filename5 = 'WorkTotal_95_k64.dat'
	filename6 = 'WorkTotal_99_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for k = 64')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_k64.png')

	plt.show()
	plt.close()


def LogPlotAllA25():


	filename1 = 'WorkTotal_25_k1.dat'
	filename2 = 'WorkTotal_25_k2.dat'
	filename3 = 'WorkTotal_25_k4.dat'
	filename4 = 'WorkTotal_25_k8.dat'
	filename5 = 'WorkTotal_25_k16.dat'
	filename6 = 'WorkTotal_25_k32.dat'
	filename7 = 'WorkTotal_25_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.25')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_a25.png')

	plt.show()
	plt.close()


def LogPlotAllA50():


	filename1 = 'WorkTotal_50_k1.dat'
	filename2 = 'WorkTotal_50_k2.dat'
	filename3 = 'WorkTotal_50_k4.dat'
	filename4 = 'WorkTotal_50_k8.dat'
	filename5 = 'WorkTotal_50_k16.dat'
	filename6 = 'WorkTotal_50_k32.dat'
	filename7 = 'WorkTotal_50_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.50')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_a50.png')

	plt.show()
	plt.close()


def LogPlotAllA75():

	filename1 = 'WorkTotal_75_k1.dat'
	filename2 = 'WorkTotal_75_k2.dat'
	filename3 = 'WorkTotal_75_k4.dat'
	filename4 = 'WorkTotal_75_k8.dat'
	filename5 = 'WorkTotal_75_k16.dat'
	filename6 = 'WorkTotal_75_k32.dat'
	filename7 = 'WorkTotal_75_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.75')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_a75.png')

	plt.show()
	plt.close()


def LogPlotAllA90():

	filename1 = 'WorkTotal_90_k1.dat'
	filename2 = 'WorkTotal_90_k2.dat'
	filename3 = 'WorkTotal_90_k4.dat'
	filename4 = 'WorkTotal_90_k8.dat'
	filename5 = 'WorkTotal_90_k16.dat'
	filename6 = 'WorkTotal_90_k32.dat'
	filename7 = 'WorkTotal_90_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')


	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.90')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_a90.png')

	plt.show()
	plt.close()


def LogPlotAllA95():

	filename1 = 'WorkTotal_95_k1.dat'
	filename2 = 'WorkTotal_95_k2.dat'
	filename3 = 'WorkTotal_95_k4.dat'
	filename4 = 'WorkTotal_95_k8.dat'
	filename5 = 'WorkTotal_95_k16.dat'
	filename6 = 'WorkTotal_95_k32.dat'
	filename7 = 'WorkTotal_95_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.95')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_a95.png')

	plt.show()
	plt.close()


def LogPlotAllA99():

	filename1 = 'WorkTotal_99_k1.dat'
	filename2 = 'WorkTotal_99_k2.dat'
	filename3 = 'WorkTotal_99_k4.dat'
	filename4 = 'WorkTotal_99_k8.dat'
	filename5 = 'WorkTotal_99_k16.dat'
	filename6 = 'WorkTotal_99_k32.dat'
	filename7 = 'WorkTotal_99_k64.dat'

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

	for index in range(len(data1)-2):

		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()

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

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkTheoryD, WorkTheoryS, WorkTheoryTotal = TheoryWork(Time1)
	Plot8 = plt.plot(Time1,WorkTheoryD,label='Deterministic Theory')
	Plot9 = plt.plot(Time1,WorkTheoryS,label='Stochastic Theory')
	Plot10 = plt.plot(Time1,WorkTheoryTotal,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work for a = 0.99')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogWorkTotals_a99.png')

	plt.show()
	plt.close()


def TheoryWork(Time):

	friction = 12.86
	Dist = 25.0
	VelVar = 1.0

	WorkD = []
	WorkS = []
	WorkTot = []

	for index in range(len(Time)):

		TempWorkD = Dist*Dist*friction/float(Time[index])
		TempWorkS = friction*VelVar*Time[index]

		WorkD.append(TempWorkD)
		WorkS.append(TempWorkS)
		WorkTot.append(TempWorkD+TempWorkS)

	return WorkD, WorkS, WorkTot






