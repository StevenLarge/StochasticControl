#Plotting script for Januray 25th Time Separation data
#
#Steven Large
#January 25th 2017

import matplotlib.pyplot as plt

def PlotStochastic(modifier):

	filename1 = 'WorkTheoryS_TS_1_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_2_k' + modifier + '.dat'
	filename3 = 'WorkTheoryS_TS_4_k' + modifier + '.dat'
	filename4 = 'WorkTheoryS_TS_8_k' + modifier + '.dat'
	filename5 = 'WorkTheoryS_TS_16_k' + modifier + '.dat'
	filename6 = 'WorkTheoryS_TS_32_k' + modifier + '.dat'
	filename7 = 'WorkTheoryS_TS_64_k' + modifier + '.dat'
	filename8 = 'WorkTheoryS_TS_128_k' + modifier + '.dat'

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

	file1 = open(filename8,'r')
	data8 = file1.readlines()
	file1.close()

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

	for index in range(len(data8)-2):
		parsed8 = data8[index+2].split()

		Time8.append(eval(parsed8[0]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Work')

	plt.savefig('WorkStochastic.png')

	plt.show()
	plt.close()

def PlotTotal(modifier):

	filename1 = 'WorkTotal_TS_1_k' + modifier + '.dat'
	filename2 = 'WorkTotal_TS_2_k' + modifier + '.dat'
	filename3 = 'WorkTotal_TS_4_k' + modifier + '.dat'
	filename4 = 'WorkTotal_TS_8_k' + modifier + '.dat'
	filename5 = 'WorkTotal_TS_16_k' + modifier + '.dat'
	filename6 = 'WorkTotal_TS_32_k' + modifier + '.dat'
	filename7 = 'WorkTotal_TS_64_k' + modifier + '.dat'
	filename8 = 'WorkTotal_TS_128_k' + modifier + '.dat'

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

	file1 = open(filename8,'r')
	data8 = file1.readlines()
	file.close()

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

	for index in range(len(data8)-2):
		parsed8 = data8[index+2].split()

		Time8.append(eval(parsed8[0]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work')

	plt.savefig('WorkTotal.png')

	plt.show()
	plt.close()

def PlotDeterministic(modifier):

	filename1 = 'WorkTheoryD_TS_1_k' + modifier + '.dat'
	filename2 = 'WorkTheoryD_TS_2_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_4_k' + modifier + '.dat'
	filename4 = 'WorkTheoryD_TS_8_k' + modifier + '.dat'
	filename5 = 'WorkTheoryD_TS_16_k' + modifier + '.dat'
	filename6 = 'WorkTheoryD_TS_32_k' + modifier + '.dat'
	filename7 = 'WorkTheoryD_TS_64_k' + modifier + '.dat'
	filename8 = 'WorkTheoryD_TS_128_k' + modifier + '.dat'

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

	file1 = open(filename8,'r')
	data8 = file1.readlines()
	file1.close()

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

	for index in range(len(data8)-2):

		parsed8 = data8[index+2].split()

		Time8.append(eval(parsed8[0]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Work')

	plt.savefig('WorkDeterministic.png')

	plt.show()
	plt.close()

def PlotStochasticLag(modifier):

	filename1 = 'WorkTheorySLag_TS_1_k' + modifier + '.dat'
	filename2 = 'WorkTheorySLag_TS_2_k' + modifier + '.dat'
	filename3 = 'WorkTheorySLag_TS_4_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_8_k' + modifier + '.dat'
	filename5 = 'WorkTheorySLag_TS_16_k' + modifier + '.dat'
	filename6 = 'WorkTheorySLag_TS_32_k' + modifier + '.dat'
	filename7 = 'WorkTheorySLag_TS_64_k' + modifier + '.dat'
	filename8 = 'WorkTheorySLag_TS_128_k' + modifier + '.dat'

	print filename1

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

	file1 = open(filename8,'r')
	data8 = file1.readlines()
	file1.close()

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

	for index in range(len(data8)-2):

		parsed8 = data8[index+2].split()

		Time8.append(eval(parsed8[0]))
		Work8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')
	Plot7 = plt.plot(Time7,Work7,label='64')
	Plot8 = plt.plot(Time8,Work8,label='128')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Lag Work')

	plt.savefig('WorkStochasticLag.png')

	plt.show()
	plt.close()

def PlotAll1(modifier):

	filename1 = 'WorkTotal_TS_1_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_1_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_1_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_1_k' + modifier + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file3 = open(filename4,'r')
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

	plt.savefig('WorkAll_1.png')

	plt.show()

	plt.close()

def PlotAll2(modifier):

	filename1 = 'WorkTotal_TS_2_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_2_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_2_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_2_k' + modifier + '.dat'

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

	plt.savefig('WorkAll_2.png')

	plt.show()

	plt.close()

def PlotAll4(modifier):

	filename1 = 'WorkTotal_TS_4_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_4_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_4_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_4_k' + modifier + '.dat'

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

	plt.savefig('WorkAll_4.png')

	plt.show()

	plt.close()

def PlotAll8(modifier):

	filename1 = 'WorkTotal_TS_8_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_8_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_8_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_8_k' + modifier + '.dat'

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

	plt.savefig('WorkAll_8.png')

	plt.show()

	plt.close()

def PlotAll16(modifier):

	filename1 = 'WorkTotal_TS_16_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_16_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_16_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_16_k' + modifier + '.dat'

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

	plt.savefig('WorkAll_16.png')

	plt.show()

	plt.close()

def PlotAll32(modifier):

	filename1 = 'WorkTotal_TS_32_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_32_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_32_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_32_k' + modifier + '.dat'

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

	plt.title('TS = 32')

	plt.savefig('WorkAll_32.png')

	plt.show()

	plt.close()

def PlotAll64(modifier):

	filename1 = 'WorkTotal_TS_64_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_64_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_64_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_64_k' + modifier + '.dat'

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

	plt.savefig('WorkAll_64.png')

	plt.show()

	plt.close()

def PlotAll128(modifier):

	filename1 = 'WorkTotal_TS_128_k' + modifier + '.dat'
	filename2 = 'WorkTheoryS_TS_128_k' + modifier + '.dat'
	filename3 = 'WorkTheoryD_TS_128_k' + modifier + '.dat'
	filename4 = 'WorkTheorySLag_TS_128_k' + modifier + '.dat'

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
	
	plt.savefig('WorkAll_128.png')

	plt.show()

	plt.close()

def PlotAutoCorr():

	filename1 = 'AutoCorrelation_1.dat'
	filename2 = 'AutoCorrelation_2.dat'
	filename3 = 'AutoCorrelation_4.dat'
	filename4 = 'AutoCorrelation_8.dat'
	filename5 = 'AutoCorrelation_16.dat'
	filename6 = 'AutoCorrelation_32.dat'
	filename7 = 'AutoCorrelation_64.dat'
	filename8 = 'AutoCorrelation_128.dat'

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
	Corr1 = []
	Time2 = []
	Corr2 = []
	Time3 = []
	Corr3 = []
	Time4 = []
	Corr4 = []
	Time5 = []
	Corr5 = []
	Time6 = []
	Corr6 = []
	Time7 = []
	Corr7 = []
	Time8 = []
	Corr8 = []

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
		Corr1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Corr2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Corr3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Corr4.append(eval(parsed4[1]))
		Time5.append(eval(parsed5[0]))
		Corr5.append(eval(parsed5[1]))
		Time6.append(eval(parsed6[0]))
		Corr6.append(eval(parsed6[1]))
		Time7.append(eval(parsed7[0]))
		Corr7.append(eval(parsed7[1]))
		Time8.append(eval(parsed8[0]))
		Corr8.append(eval(parsed8[1]))

	Plot1 = plt.plot(Time1,Corr1,label='TS = 1')
	Plot2 = plt.plot(Time2,Corr2,label='TS = 2')
	Plot3 = plt.plot(Time3,Corr3,label='TS = 4')
	Plot4 = plt.plot(Time4,Corr4,label='TS = 8')
	Plot5 = plt.plot(Time5,Corr5,label='TS = 16')
	Plot6 = plt.plot(Time6,Corr6,label='TS = 32')
	Plot7 = plt.plot(Time7,Corr7,label='TS = 64')
	Plot8 = plt.plot(Time8,Corr8,label='TS = 128')
	
	plt.legend()
	plt.xlabel('Lag Time')
	plt.ylabel('Force AutoCorrelation')
	plt.title('AutoCorrelation for Different Time Lags')

	plt.savefig('AutoCorrelations.png')

	plt.show()
	plt.close()

def PlotFrictions():

	filename1 = 'Friction_1.dat'
	filename2 = 'Friction_2.dat'
	filename3 = 'Friction_4.dat'
	filename4 = 'Friction_8.dat'
	filename5 = 'Friction_16.dat'
	filename6 = 'Friction_32.dat'
	filename7 = 'Friction_64.dat'
	filename8 = 'Friction_128.dat'

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

	TimeSep = [1,2,4,8,16,32,64,128]

	Friction = []

	Friction.append((data1[2].split())[0])
	Friction.append((data2[2].split())[0])
	Friction.append((data3[2].split())[0])
	Friction.append((data4[2].split())[0])
	Friction.append((data5[2].split())[0])
	Friction.append((data6[2].split())[0])
	Friction.append((data7[2].split())[0])
	Friction.append((data8[2].split())[0])

	plt.plot(TimeSep,Friction,'ro')
	plt.plot(TimeSep,Friction,'b')
	plt.xlabel('Time Separation')
	plt.ylabel('Friction')
	plt.title('Comparison of Generalized Friction Values for Different Time Separations')

	plt.savefig('Frictions.png')

	plt.show()
	plt.close()

	plt.loglog(TimeSep,Friction,'ro')
	plt.loglog(TimeSep,Friction,'b')
	plt.xlabel('Time Separation')
	plt.ylabel('Friction')
	plt.title('Comparison of Generalized Friction Values for Different Time Separations')

	plt.savefig('LogFrictions.png')

	plt.show()
	plt.close()

def PlotStochasticLagCompare(modifier):

	filename1 = 'WorkTheorySLag_TS_' + modifier + '_k1.dat'
	filename2 = 'WorkTheorySLag_TS_' + modifier + '_k01.dat'
	filename3 = 'WorkTheorySLag_TS_' + modifier + '_k001.dat'

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
	Time2 = []
	Time3 = []
	Work1 = []
	Work2 = []
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

	Plot1 = plt.plot(Time1,Work1,label='kCP = 1')
	Plot2 = plt.plot(Time2,Work2,label='kCP = 0.1')
	Plot3 = plt.plot(Time3,Work3,label='kCP = 0.01')

	plt.legend()
	plt.title('Comparison of Stocahstic Works for different kCP')
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')


	plt.show()









