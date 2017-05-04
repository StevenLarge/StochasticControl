#Plotting script for constant velocity ensemble results, from February 22nd starting from equilibrium distribution
#
#Steven Large
#February 22nd 2017

import matplotlib.pyplot as plt

def PlotAll():

	filename1 = 'WorkTotal_01.dat'
	filename2 = 'WorkTotal_05.dat'
	filename3 = 'WorkTotal_1.dat'
	filename4 = 'WorkTotal_2.dat'
	filename5 = 'WorkTotal_4.dat'
	filename6 = 'WorkTotal_8.dat'

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


	Plot1 = plt.plot(Time1,Work1,label='Variance = 0.1')
	Plot2 = plt.plot(Time2,Work2,label='Variance = 0.5')
	Plot3 = plt.plot(Time3,Work3,label='Variance = 1')
	Plot4 = plt.plot(Time4,Work4,label='Variance = 2')
	Plot5 = plt.plot(Time5,Work5,label='Variance = 4')
	Plot6 = plt.plot(Time6,Work6,label='Variance = 8')

	WorkD_01,WorkS_01,WorkT_01 = WorkTheory(Time1,0.1)
	WorkD_05,WorkS_05,WorkT_05 = WorkTheory(Time1,0.5)
	WorkD_1,WorkS_1,WorkT_1 = WorkTheory(Time1,1.0)
	WorkD_2,WorkS_2,WorkT_2 = WorkTheory(Time1,2.0)
	WorkD_4,WorkS_4,WorkT_4 = WorkTheory(Time1,4.0)
	WorkD_8,WorkS_8,WorkT_8 = WorkTheory(Time1,8.0)	

	Plot7 = plt.plot(Time1,WorkT_01,label='Total Work Theory 0.1')
	Plot8 = plt.plot(Time1,WorkT_05,label='Total Work Theory 0.5')
	Plot9 = plt.plot(Time1,WorkT_1,label='Total Work Theory 1')
	Plot10 = plt.plot(Time1,WorkT_2,label='Total Work Theory 2')
	Plot11 = plt.plot(Time1,WorkT_4,label='Total Work Theory 4')
	Plot12 = plt.plot(Time1,WorkT_8,label='Total Work Theory 8')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.savefig('ConstantVelocityPlot.png')

	plt.show()
	plt.close()


def LogPlotAll():

	filename1 = 'WorkTotal_01.dat'
	filename2 = 'WorkTotal_05.dat'
	filename3 = 'WorkTotal_1.dat'
	filename4 = 'WorkTotal_2.dat'
	filename5 = 'WorkTotal_4.dat'
	filename6 = 'WorkTotal_8.dat'

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


	Plot1 = plt.plot(Time1,Work1,label='Variance = 0.1')
	Plot2 = plt.plot(Time2,Work2,label='Variance = 0.5')
	Plot3 = plt.plot(Time3,Work3,label='Variance = 1')
	Plot4 = plt.plot(Time4,Work4,label='Variance = 2')
	Plot5 = plt.plot(Time5,Work5,label='Variance = 4')
	Plot6 = plt.plot(Time6,Work6,label='Variance = 8')

	WorkD_01,WorkS_01,WorkT_01 = WorkTheory(Time1,0.1)
	WorkD_05,WorkS_05,WorkT_05 = WorkTheory(Time1,0.5)
	WorkD_1,WorkS_1,WorkT_1 = WorkTheory(Time1,1.0)
	WorkD_2,WorkS_2,WorkT_2 = WorkTheory(Time1,2.0)
	WorkD_4,WorkS_4,WorkT_4 = WorkTheory(Time1,4.0)
	WorkD_8,WorkS_8,WorkT_8 = WorkTheory(Time1,8.0)	

	Plot7 = plt.plot(Time1,WorkT_01,label='Total Work Theory 0.1')
	Plot8 = plt.plot(Time1,WorkT_05,label='Total Work Theory 0.5')
	Plot9 = plt.plot(Time1,WorkT_1,label='Total Work Theory 1')
	Plot10 = plt.plot(Time1,WorkT_2,label='Total Work Theory 2')
	Plot11 = plt.plot(Time1,WorkT_4,label='Total Work Theory 4')
	Plot12 = plt.plot(Time1,WorkT_8,label='Total Work Theory 8')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocityPlot.png')

	plt.show()
	plt.close()


def PlotVar01():

	filename = 'WorkTotal_01.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,0.1)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 0.1')

	plt.savefig('ConstantVelocity_01.png')

	plt.show()
	plt.close()


def PlotVar05():

	filename = 'WorkTotal_05.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,0.5)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 0.5')

	plt.savefig('ConstantVelocity_05.png')

	plt.show()
	plt.close()


def PlotVar1():

	filename = 'WorkTotal_1.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,1)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 1')

	plt.savefig('ConstantVelocity_1.png')

	plt.show()
	plt.close()


def PlotVar2():

	filename = 'WorkTotal_2.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,2)

	Plot1 = plt.plot(Time,Work,label='Simulation Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 2')

	plt.savefig('ConstantVelocity_2.png')

	plt.show()
	plt.close()


def PlotVar4():

	filename = 'WorkTotal_4.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,4)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 4')

	plt.savefig('ConstantVelocity_4.png')

	plt.show()
	plt.close()


def PlotVar8():

	filename = 'WorkTotal_8.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,8)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 8')

	plt.savefig('ConstantVelocity_8.png')

	plt.show()
	plt.close()


def LogPlotVar01():

	filename = 'WorkTotal_01.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,0.1)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 0.1')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocity_01.png')

	plt.show()
	plt.close()


def LogPlotVar05():

	filename = 'WorkTotal_05.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,0.5)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 0.5')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocity_05.png')

	plt.show()
	plt.close()


def LogPlotVar1():

	filename = 'WorkTotal_1.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,1)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 1')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocity_1.png')

	plt.show()
	plt.close()


def LogPlotVar2():

	filename = 'WorkTotal_2.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,2)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 2')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocity_2.png')

	plt.show()
	plt.close()


def LogPlotVar4():

	filename = 'WorkTotal_4.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,4)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 4')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocity_4.png')

	plt.show()
	plt.close()


def LogPlotVar8():

	filename = 'WorkTotal_8.dat'

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	WorkD,WorkS,WorkT = WorkTheory(Time,8)

	Plot1 = plt.plot(Time,Work,label='Simualtion Results')
	Plot2 = plt.plot(Time,WorkD,label='Determinstic Theory')
	Plot3 = plt.plot(Time,WorkS,label='Stochastic Theory')
	Plot4 = plt.plot(Time,WorkT,label='Total Work Theory')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Constant Velocity Ensemble Var = 8')

	plt.xscale('log')
	plt.yscale('log')

	plt.savefig('LogConstantVelocity_8.png')

	plt.show()
	plt.close()




def WorkTheory(Time,VelVar):

	Dist = 50.0
	friction = 12.0

	WorkDeterministic = []
	WorkStochastic = []
	WorkTotal = []

	for index in range(len(Time)):

		WorkDTemp = Dist*Dist*friction/Time[index]
		WorkSTemp = VelVar*friction*Time[index]

		WorkDeterministic.append(WorkDTemp)
		WorkStochastic.append(WorkSTemp)
		WorkTotal.append(WorkDTemp + WorkSTemp)

	return WorkDeterministic,WorkStochastic,WorkTotal

