#Plotting script for Januray 25th Time Separation data
#
#Steven Large
#January 25th 2017

import matplotlib.pyplot as plt

def PlotStochastic():

	filename1 = 'WorkTheoryS_TS_1.dat'
	filename2 = 'WorkTheoryS_TS_2.dat'
	filename3 = 'WorkTheoryS_TS_4.dat'
	filename4 = 'WorkTheoryS_TS_8.dat'
	filename5 = 'WorkTheoryS_TS_16.dat'
	filename6 = 'WorkTheoryS_TS_32.dat'
	filename7 = 'WorkTheoryS_TS_64.dat'
	#filename8 = 'WorkTheoryS_TS_128.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	file1 = open(filename7,'r')
	data7 = file1.readlines()
	file1.close()

	#file1 = open(filename8,'r')
	#data8 = file1.readlines()
	#file1.close()

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
	#Time8 = []
	#Work8 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		#parsed8 = data8[index+2].split()

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
		#Time8.append(eval(parsed8[0]))
		#Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	#Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Work')

	plt.show()
	plt.close()

def PlotTotal():

	filename1 = 'WorkTotal_TS_1.dat'
	filename2 = 'WorkTotal_TS_2.dat'
	filename3 = 'WorkTotal_TS_4.dat'
	filename4 = 'WorkTotal_TS_8.dat'
	filename5 = 'WorkTotal_TS_16.dat'
	filename6 = 'WorkTotal_TS_32.dat'
	filename7 = 'WorkTotal_TS_64.dat'
	#filename8 = 'WorkTotal_TS_128.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	file1 = open(filename7,'r')
	data7 = file1.readlines()
	file1.close()

	#file1 = open(filename8,'r')
	#data8 = file1.readlines()
	#file.close()

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
	#Time8 = []
	#Work8 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		#parsed8 = data8[index+2].split()

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
		#Time8.append(eval(parsed8[0]))
		#Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	#Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work')

	plt.show()
	plt.close()

def PlotDeterministic():

	filename1 = 'WorkTheoryD_TS_1.dat'
	filename2 = 'WorkTheoryD_TS_2.dat'
	filename3 = 'WorkTheoryD_TS_4.dat'
	filename4 = 'WorkTheoryD_TS_8.dat'
	filename5 = 'WorkTheoryD_TS_16.dat'
	filename6 = 'WorkTheoryD_TS_32.dat'
	filename7 = 'WorkTheoryD_TS_64.dat'
	#filename8 = 'WorkTheoryD_TS_128.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	file1 = open(filename7,'r')
	data7 = file1.readlines()
	file1.close()

	#file1 = open(filename8,'r')
	#data8 = file8.readlines()
	#file1.close()

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
	#Time8 = []
	#Work8 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		#parsed8 = data8[index+2].split()

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
		#Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	#Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Work')

	plt.show()
	plt.close()

def PlotStochasticLag():


	filename1 = 'WorkTheorySLag_TS_1.dat'
	filename2 = 'WorkTheorySLag_TS_2.dat'
	filename3 = 'WorkTheorySLag_TS_4.dat'
	filename4 = 'WorkTheorySLag_TS_8.dat'
	filename5 = 'WorkTheorySLag_TS_16.dat'
	filename6 = 'WorkTheorySLag_TS_32.dat'
	filename7 = 'WorkTheorySLag_TS_64.dat'
	#filename8 = 'WorkTheorySLag_TS_128.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	file1 = open(filename7,'r')
	data7 = file1.readlines()
	file1.close()

	#file1 = open(filename8,'r')
	#data8 = file1.readlines()
	#file1.close()

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
	#Time8 = []
	#Work8 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		#parsed8 = data8[index+2].split()

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
		#Time8.append(eval(parsed8[0]))
		#Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	#Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Lag Work')

	plt.show()
	plt.close()

def PlotAll1():

	filename1 = 'WorkTotal_TS_1.dat'
	filename2 = 'WorkTheoryS_TS_1.dat'
	filename3 = 'WorkTheoryD_TS_1.dat'
	filename4 = 'WorkTheorySLag_TS_1.dat'

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
	data4 = file3.readlines()
	file3.close()

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


	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 1')

	plt.show()

	plt.close()

def PlotAll2():

	filename1 = 'WorkTotal_TS_2.dat'
	filename2 = 'WorkTheoryS_TS_2.dat'
	filename3 = 'WorkTheoryD_TS_2.dat'
	filename4 = 'WorkTheorySLag_TS_2.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 2')

	plt.show()

	plt.close()

def PlotAll4():

	filename1 = 'WorkTotal_TS_4.dat'
	filename2 = 'WorkTheoryS_TS_4.dat'
	filename3 = 'WorkTheoryD_TS_4.dat'
	filename4 = 'WorkTheorySLag_TS_4.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 4')

	plt.show()

	plt.close()

def PlotAll8():

	filename1 = 'WorkTotal_TS_8.dat'
	filename2 = 'WorkTheoryS_TS_8.dat'
	filename3 = 'WorkTheoryD_TS_8.dat'
	filename4 = 'WorkTheorySLag_TS_8.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 8')

	plt.show()

	plt.close()

def PlotAll16():

	filename1 = 'WorkTotal_TS_16.dat'
	filename2 = 'WorkTheoryS_TS_16.dat'
	filename3 = 'WorkTheoryD_TS_16.dat'
	filename4 = 'WorkTheorySLag_TS_16.dat'

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


	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 16')

	plt.show()

	plt.close()

def PlotAll32():

	filename1 = 'WorkTotal_TS_32.dat'
	filename2 = 'WorkTheoryS_TS_32.dat'
	filename3 = 'WorkTheoryD_TS_32.dat'
	filename4 = 'WorkTheorySLag_TS_32.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(TIme4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 32')

	plt.show()

	plt.close()

def PlotAll64():

	filename1 = 'WorkTotal_TS_64.dat'
	filename2 = 'WorkTheoryS_TS_64.dat'
	filename3 = 'WorkTheoryD_TS_64.dat'
	filename4 = 'WorkTheorySLag_TS_64.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 64')
	plt.show()

	plt.close()

def PlotAll128():

	filename1 = 'WorkTotal_TS_128.dat'
	filename2 = 'WorkTheoryS_TS_128.dat'
	filename3 = 'WorkTheoryD_TS_128.dat'
	filename4 = 'WorkTheorySLag_TS_128.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title('TS = 128')
	plt.show()

	plt.close()






