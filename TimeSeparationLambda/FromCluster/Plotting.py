#Plotting script for February 21st fixed-end-point data
#
#Steven Large
#February 22nd 2017

import matplotlib.pyplot as plt

def ReadData(filename):

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()
	
	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))


def LogPlotAllA25():

	filename1 = 'WorkTotal_a25_k2.dat'
	filename2 = 'WorkTotal_a25_k4.dat'
	filename3 = 'WorkTotal_a25_k8.dat'
	filename4 = 'WorkTotal_a25_k15.dat'
	filename5 = 'WorkTotal_a25_k32.dat'
	filename6 = 'WorkTotal_a25_k64.dat'
	filename7 = 'WorkTotal_a25_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork25.png')

	plt.show()
	plt.close()


def LogPlotAllA50():

	filename1 = 'WorkTotal_a50_k2.dat'
	filename2 = 'WorkTotal_a50_k4.dat'
	filename3 = 'WorkTotal_a50_k8.dat'
	filename4 = 'WorkTotal_a50_k15.dat'
	filename5 = 'WorkTotal_a50_k32.dat'
	filename6 = 'WorkTotal_a50_k64.dat'
	filename7 = 'WorkTotal_a50_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork50.png')

	plt.show()
	plt.close()


def LogPlotAllA75():

	filename1 = 'WorkTotal_a75_k2.dat'
	filename2 = 'WorkTotal_a75_k4.dat'
	filename3 = 'WorkTotal_a75_k8.dat'
	filename4 = 'WorkTotal_a75_k15.dat'
	filename5 = 'WorkTotal_a75_k32.dat'
	filename6 = 'WorkTotal_a75_k64.dat'
	filename7 = 'WorkTotal_a75_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork75.png')

	plt.show()
	plt.close()


def LogPlotAllA90():

	filename1 = 'WorkTotal_a90_k2.dat'
	filename2 = 'WorkTotal_a90_k4.dat'
	filename3 = 'WorkTotal_a90_k8.dat'
	filename4 = 'WorkTotal_a90_k15.dat'
	filename5 = 'WorkTotal_a90_k32.dat'
	filename6 = 'WorkTotal_a90_k64.dat'
	filename7 = 'WorkTotal_a90_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork90.png')

	plt.show()
	plt.close()


def LogPlotAllA95():

	filename1 = 'WorkTotal_a95_k2.dat'
	filename2 = 'WorkTotal_a95_k4.dat'
	filename3 = 'WorkTotal_a95_k8.dat'
	filename4 = 'WorkTotal_a95_k15.dat'
	filename5 = 'WorkTotal_a95_k32.dat'
	filename6 = 'WorkTotal_a95_k64.dat'
	filename7 = 'WorkTotal_a95_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork95.png')

	plt.show()
	plt.close()


def LogPlotAllA99():

	filename1 = 'WorkTotal_a99_k2.dat'
	filename2 = 'WorkTotal_a99_k4.dat'
	filename3 = 'WorkTotal_a99_k8.dat'
	filename4 = 'WorkTotal_a99_k15.dat'
	filename5 = 'WorkTotal_a99_k32.dat'
	filename6 = 'WorkTotal_a99_k64.dat'
	filename7 = 'WorkTotal_a99_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))
		Time7.append(eval(parsed7[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))
		Work7.append(eval(parsed7[1]))

	Plot1 = plt.plot(Time1,Work1,label='k = 1')
	Plot2 = plt.plot(Time2,Work2,label='k = 2')
	Plot3 = plt.plot(Time3,Work3,label='k = 4')
	Plot4 = plt.plot(Time4,Work4,label='k = 8')
	Plot5 = plt.plot(Time5,Work5,label='k = 16')
	Plot6 = plt.plot(Time6,Work6,label='k = 32')
	Plot7 = plt.plot(Time7,Work7,label='k = 64')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork99.png')

	plt.show()
	plt.close()


def LogPlotAllK2():

	filename1 = 'WorkTotal_a25_k2.dat'
	filename2 = 'WorkTotal_a50_k2.dat'
	filename3 = 'WorkTotal_a75_k2.dat'
	filename4 = 'WorkTotal_a90_k2.dat'
	filename5 = 'WorkTotal_a95_k2.dat'
	filename6 = 'WorkTotal_a99_k2.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K2.png')

	plt.show()
	plt.close()


def LogPlotAllK4():

	filename1 = 'WorkTotal_a25_k4.dat'
	filename2 = 'WorkTotal_a50_k4.dat'
	filename3 = 'WorkTotal_a75_k4.dat'
	filename4 = 'WorkTotal_a90_k4.dat'
	filename5 = 'WorkTotal_a95_k4.dat'
	filename6 = 'WorkTotal_a99_k4.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K4.png')

	plt.show()
	plt.close()


def LogPlotAllK8():

	filename1 = 'WorkTotal_a25_k8.dat'
	filename2 = 'WorkTotal_a50_k8.dat'
	filename3 = 'WorkTotal_a75_k8.dat'
	filename4 = 'WorkTotal_a90_k8.dat'
	filename5 = 'WorkTotal_a95_k8.dat'
	filename6 = 'WorkTotal_a99_k8.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K8.png')

	plt.show()
	plt.close()


def LogPlotAllK16():

	filename1 = 'WorkTotal_a25_k15.dat'
	filename2 = 'WorkTotal_a50_k15.dat'
	filename3 = 'WorkTotal_a75_k15.dat'
	filename4 = 'WorkTotal_a90_k15.dat'
	filename5 = 'WorkTotal_a95_k15.dat'
	filename6 = 'WorkTotal_a99_k15.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K16.png')

	plt.show()
	plt.close()


def LogPlotAllK32():

	filename1 = 'WorkTotal_a25_k32.dat'
	filename2 = 'WorkTotal_a50_k32.dat'
	filename3 = 'WorkTotal_a75_k32.dat'
	filename4 = 'WorkTotal_a90_k32.dat'
	filename5 = 'WorkTotal_a95_k32.dat'
	filename6 = 'WorkTotal_a99_k32.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K32.png')

	plt.show()
	plt.close()


def LogPlotAllK64():


	filename1 = 'WorkTotal_a25_k64.dat'
	filename2 = 'WorkTotal_a50_k64.dat'
	filename3 = 'WorkTotal_a75_k64.dat'
	filename4 = 'WorkTotal_a90_k64.dat'
	filename5 = 'WorkTotal_a95_k64.dat'
	filename6 = 'WorkTotal_a99_k64.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K64.png')

	plt.show()
	plt.close()


def LogPlotAllK75():

	filename1 = 'WorkTotal_a25_k75.dat'
	filename2 = 'WorkTotal_a50_k75.dat'
	filename3 = 'WorkTotal_a75_k75.dat'
	filename4 = 'WorkTotal_a90_k75.dat'
	filename5 = 'WorkTotal_a95_k75.dat'
	filename6 = 'WorkTotal_a99_k75.dat'

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
		Time2.append(eval(parsed2[0]))
		Time3.append(eval(parsed3[0]))
		Time4.append(eval(parsed4[0]))
		Time5.append(eval(parsed5[0]))
		Time6.append(eval(parsed6[0]))

		Work1.append(eval(parsed1[1]))
		Work2.append(eval(parsed2[1]))
		Work3.append(eval(parsed3[1]))
		Work4.append(eval(parsed4[1]))
		Work5.append(eval(parsed5[1]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='a = 25')
	Plot2 = plt.plot(Time2,Work2,label='a = 50')
	Plot3 = plt.plot(Time3,Work3,label='a = 75')
	Plot4 = plt.plot(Time4,Work4,label='a = 90')
	Plot5 = plt.plot(Time5,Work5,label='a = 95')
	Plot6 = plt.plot(Time6,Work6,label='a = 99')

	WorkD,WorkS,WorkT = WorkTheory(Time1)
	Plot8 = plt.plot(Time1,WorkT,label='Theory')

	plt.yscale('log')
	plt.xscale('log')

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.legend()
	plt.savefig('LogWork_K75.png')

	plt.show()
	plt.close()




def WorkTheory(Time):

	friction = 12.0
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

