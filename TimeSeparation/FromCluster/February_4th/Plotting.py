#Plotting routine for data from Feb 2nd on time separation simulations
#
#Steven Large
#February 3rd 2017

import matplotlib.pyplot as plt

def PlotAll550():

	filename1 = 'WorkTotal_550.dat'
	filename2 = 'WorkTheoryD_550.dat'
	filename3 = 'WorkTheoryS_550.dat'
	filename4 = 'WorkTheorySLag_550.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 550')

	plt.show()
	plt.close()

def PlotAll600():

	filename1 = 'WorkTotal_600.dat'
	filename2 = 'WorkTheoryD_600.dat'
	filename3 = 'WorkTheoryS_600.dat'
	filename4 = 'WorkTheorySLag_600.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 600')

	plt.show()
	plt.close()

def PlotAll650():

	filename1 = 'WorkTotal_650.dat'
	filename2 = 'WorkTheoryD_650.dat'
	filename3 = 'WorkTheoryS_650.dat'
	filename4 = 'WorkTheorySLag_650.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 650')

	plt.show()
	plt.close()

def PlotAll700():

	filename1 = 'WorkTotal_700.dat'
	filename2 = 'WorkTheoryD_700.dat'
	filename3 = 'WorkTheoryS_700.dat'
	filename4 = 'WorkTheorySLag_700.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 700')

	plt.show()
	plt.close()

def PlotAll750():

	filename1 = 'WorkTotal_750.dat'
	filename2 = 'WorkTheoryD_750.dat'
	filename3 = 'WorkTheoryS_750.dat'
	filename4 = 'WorkTheorySLag_750.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 750')

	plt.show()
	plt.close()

def PlotAll800():

	filename1 = 'WorkTotal_800.dat'
	filename2 = 'WorkTheoryD_800.dat'
	filename3 = 'WorkTheoryS_800.dat'
	filename4 = 'WorkTheorySLag_800.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 800')

	plt.show()
	plt.close()

def PlotAll850():

	filename1 = 'WorkTotal_850.dat'
	filename2 = 'WorkTheoryD_850.dat'
	filename3 = 'WorkTheoryS_850.dat'
	filename4 = 'WorkTheorySLag_850.dat'

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
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 850')

	plt.show()
	plt.close()

def PlotAll900():

	filename1 = 'WorkTotal_900.dat'
	filename2 = 'WorkTheoryD_900.dat'
	filename3 = 'WorkTheoryS_900.dat'
	filename4 = 'WorkTheorySLag_900.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 900')

	plt.show()
	plt.close()

def PlotAll950():

	filename1 = 'WorkTotal_950.dat'
	filename2 = 'WorkTheoryD_950.dat'
	filename3 = 'WorkTheoryS_950.dat'
	filename4 = 'WorkTheorySLag_950.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 950')

	plt.show()
	plt.close()

def PlotAll1000():

	filename1 = 'WorkTotal_1000.dat'
	filename2 = 'WorkTheoryD_1000.dat'
	filename3 = 'WorkTheoryS_1000.dat'
	filename4 = 'WorkTheorySLag_1000.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1000')

	plt.show()
	plt.close()

def PlotAll1050():

	filename1 = 'WorkTotal_1050.dat'
	filename2 = 'WorkTheoryD_1050.dat'
	filename3 = 'WorkTheoryS_1050.dat'
	filename4 = 'WorkTheorySLag_1050.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1050')

	plt.show()
	plt.close()

def PlotAll1100():

	filename1 = 'WorkTotal_1100.dat'
	filename2 = 'WorkTheoryD_1100.dat'
	filename3 = 'WorkTheoryS_1100.dat'
	filename4 = 'WorkTheorySLag_1100.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1100')

	plt.show()
	plt.close()

def PlotAll1150():

	filename1 = 'WorkTotal_1150.dat'
	filename2 = 'WorkTheoryD_1150.dat'
	filename3 = 'WorkTheoryS_1150.dat'
	filename4 = 'WorkTheorySLag_1150.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1150')

	plt.show()
	plt.close()

def PlotAll1200():

	filename1 = 'WorkTotal_1200.dat'
	filename2 = 'WorkTheoryD_1200.dat'
	filename3 = 'WorkTheoryS_1200.dat'
	filename4 = 'WorkTheorySLag_1200.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1200')

	plt.show()
	plt.close()

def PlotAll1250():

	filename1 = 'WorkTotal_1250.dat'
	filename2 = 'WorkTheoryD_1250.dat'
	filename3 = 'WorkTheoryS_1250.dat'
	filename4 = 'WorkTheorySLag_1250.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1250')

	plt.show()
	plt.close()

def PlotAll1300():

	filename1 = 'WorkTotal_1300.dat'
	filename2 = 'WorkTheoryD_1300.dat'
	filename3 = 'WorkTheoryS_1300.dat'
	filename4 = 'WorkTheorySLag_1300.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1300')

	plt.show()
	plt.close()

def PlotAll1350():

	filename1 = 'WorkTotal_1350.dat'
	filename2 = 'WorkTheoryD_1350.dat'
	filename3 = 'WorkTheoryS_1350.dat'
	filename4 = 'WorkTheorySLag_1350.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1350')

	plt.show()
	plt.close()

def PlotAll1400():

	filename1 = 'WorkTotal_1400.dat'
	filename2 = 'WorkTheoryD_1400.dat'
	filename3 = 'WorkTheoryS_1400.dat'
	filename4 = 'WorkTheorySLag_1400.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1400')

	plt.show()
	plt.close()

def PlotAll1450():

	filename1 = 'WorkTotal_1450.dat'
	filename2 = 'WorkTheoryD_1450.dat'
	filename3 = 'WorkTheoryS_1450.dat'
	filename4 = 'WorkTheorySLag_1450.dat'

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

	Plot1 = plt.plot(Time1,Work1,label='Simulation Work')
	Plot2 = plt.plot(Time2,Work2,label='Deterministic Work')
	Plot3 = plt.plot(Time3,Work3,label='Stochastic Work')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag Work')

	plt.legend()

	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Work Contributions')

	plt.savefig('Work Contributions, TS = 1450')

	plt.show()
	plt.close()





