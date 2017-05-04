#Plotting Script for March 16th data
#
#Steven Large
#March 16th 2017

import matplotlib.pyplot as plt

def Plot95():

	filename = 'WorkTotal_a95_k64.dat'
	file1 = open(filename,'r')
	data1 = file1.readlines()

	Time1 = []
	Work1 = []

	Friction = 12
	Variance = 1

	Dist = 25

	Deterministic = []
	Stochastic = []
	Total = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time1.append(eval(parsed[0]))
		Work1.append(eval(parsed[1]))
		Deterministic.append(Friction*Dist*Dist/float(Time1[index]))
		Stochastic.append(Friction*Variance*Time1[index])
		Total.append(Deterministic[index] + Stochastic[index])

	plt.plot(Time1,Work1,'o')
	plt.plot(Time1,Deterministic)
	plt.plot(Time1,Stochastic)
	plt.plot(Time1,Total)

	plt.show()
	plt.close()


def Plot99():


	filename = 'WorkTotal_a99_k64.dat'
	file1 = open(filename,'r')
	data1 = file1.readlines()

	Time1 = []
	Work1 = []

	Friction = 12
	Variance = 1

	Dist = 25

	Deterministic = []
	Stochastic = []
	Total = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Time1.append(eval(parsed[0]))
		Work1.append(eval(parsed[1]))
		Deterministic.append(Friction*Dist*Dist/float(Time1[index]))
		Stochastic.append(Friction*Variance*Time1[index])
		Total.append(Deterministic[index] + Stochastic[index])

	plt.plot(Time1,Work1,'o')
	plt.plot(Time1,Deterministic)
	plt.plot(Time1,Stochastic)
	plt.plot(Time1,Total)

	plt.show()
	plt.close()

#def PlotAll():





