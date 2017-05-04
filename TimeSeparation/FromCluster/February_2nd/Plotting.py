#This is a plotting script for the Time Separation data Febuary 2nd
#
#Steven Large
#February 2nd 2017

import matplotlib.pyplot as plt

def PlotAll200():

	filename1 = 'WorkTotal_200.dat'
	filename2 = 'WorkTheoryS_200.dat'
	filename3 = 'WorkTheorySLag_200.dat'
	filename4 = 'WorkTheoryD_200.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 200')
	plt.savefig('WorkAll_200.png')

	plt.show()
	plt.close()

def PlotAll250():

	filename1 = 'WorkTotal_250.dat'
	filename2 = 'WorkTheoryS_250.dat'
	filename3 = 'WorkTheorySLag_250.dat'
	filename4 = 'WorkTheoryD_250.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 250')
	plt.savefig('WorkAll_250.png')

	plt.show()
	plt.close()

def PlotAll300():

	filename1 = 'WorkTotal_300.dat'
	filename2 = 'WorkTheoryS_300.dat'
	filename3 = 'WorkTheorySLag_300.dat'
	filename4 = 'WorkTheoryD_300.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 300')
	plt.savefig('WorkAll_300.png')

	plt.show()
	plt.close()

def PlotAll350():

	filename1 = 'WorkTotal_350.dat'
	filename2 = 'WorkTheoryS_350.dat'
	filename3 = 'WorkTheorySLag_350.dat'
	filename4 = 'WorkTheoryD_350.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 350')
	plt.savefig('WorkAll_350.png')

	plt.show()
	plt.close()

def PlotAll400():

	filename1 = 'WorkTotal_400.dat'
	filename2 = 'WorkTheoryS_400.dat'
	filename3 = 'WorkTheorySLag_400.dat'
	filename4 = 'WorkTheoryD_400.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 400')
	plt.savefig('WorkAll_400.png')

	plt.show()
	plt.close()

def PlotAll450():

	filename1 = 'WorkTotal_450.dat'
	filename2 = 'WorkTheoryS_450.dat'
	filename3 = 'WorkTheorySLag_450.dat'
	filename4 = 'WorkTheoryD_450.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 450')
	plt.savefig('WorkAll_450.png')

	plt.show()
	plt.close()

def PlotAll500():

	filename1 = 'WorkTotal_500.dat'
	filename2 = 'WorkTheoryS_500.dat'
	filename3 = 'WorkTheorySLag_500.dat'
	filename4 = 'WorkTheoryD_500.dat'

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
	Plot2 = plt.plot(Time2,Work2,label='Stochastic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Lag Work')
	Plot4 = plt.plot(Time4,Work4,label='Deterministic Work')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.title('Time Separation = 500')
	plt.savefig('WorkAll_500.png')

	plt.show()
	plt.close()















