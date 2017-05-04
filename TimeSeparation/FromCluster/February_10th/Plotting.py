#Plotting script for February 10th data
#
#Steven Large
#February 10th 2017

import matplotlib.pyplot as plt

def PlotAll(spring,TS):

	filename1 = 'WorkTotal_' + TS + '_' + spring + '.dat'
	filename2 = 'WorkTheoryD_' + TS + '_' + spring + '.dat'	 
	filename3 = 'WorkTheoryS_' + TS + '_' + spring + '.dat'
	filename4 = 'WorkTheorySLag_' + TS + '_' + spring + '.dat'

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

	TitleName = 'TimeSeparation = ' + TS + ' Spring Constant = ' + spring
	SaveName = 'WorkAll_TS_' + TS + 'K_' + spring + '.png'

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title(TitleName)

	plt.savefig(SaveName)

	plt.show()
	plt.close()

def PlotTotalKCP(TS):

	filename1 = 'WorkTotal_' + TS + '_1.dat'
	filename2 = 'WorkTotal_' + TS + '_2.dat'
	filename3 = 'WorkTotal_' + TS + '_4.dat'
	filename4 = 'WorkTotal_' + TS + '_8.dat'
	filename5 = 'WorkTotal_' + TS + '_16.dat'
	filename6 = 'WorkTotal_' + TS + '_32.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='kCP = 1')
	Plot2 = plt.plot(Time2,Work2,label='kCP = 2')
	Plot3 = plt.plot(Time3,Work3,label='kCP = 4')
	Plot4 = plt.plot(Time4,Work4,label='kCP = 8')
	Plot5 = plt.plot(Time5,Work5,label='kCP = 16')
	Plot6 = plt.plot(Time6,Work6,label='kCP = 32')

	PlotTitle = 'Simulation Work Time Separation = ' + TS

	SaveName = 'WorkCompareKCP_' + TS + '.png'

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title(PlotTitle)

	plt.savefig(SaveName)

	plt.show()
	plt.close()











