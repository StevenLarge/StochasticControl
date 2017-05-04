#This is a plotting script for data on Time Separation simulations from the cluster on January 13th
#
#Steven Large
#January 15th 2016

import matplotlib.pyplot as plt

def ReadDeterministicWork(modifier,spring):

	filename = 'WorkDeterministic_TS_' + str(modifier) + '_k' + str(spring) + '.dat'

	file1 = open(filename,'r')

	data = file1.readlines()

	file1.close()

	Time = []
	Work = []

	for index in range(len(data)-2):

		parsed = data[index+2].split()
		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	return Time,Work

def PlotWorks(modifier):
	
	springs = [1,2,4,8,16]

	TimeTot = []
	WorkTot = []

	for index in range(len(springs)):

		Time,Work = ReadDeterministicWork(modifier,springs[index])

		TimeTot.append(Time)
		WorkTot.append(Work)


	k1 = plt.plot(Time[0],Work[0],label='k=1')
	k2 = plt.plot(Time[1],Work[1],label='k=2')
	k3 = plt.plot(Time[2],Work[2],label='k=4')
	k4 = plt.plot(Time[3],Work[3],label='k=8')
	k5 = plt.plot(Time[4],Work[4],label='k=16')
	plt.legend([k1,k2,k3,k4,k5])

	plt.xlabel('Time')
	plt.ylabel('Work')

	plt.show()
	plt.close()


filename1 = 'WorkDeterministic_TS_1_k1.dat'
filename2 = 'WorkDeterministic_TS_1_k2.dat'
filename3 = 'WorkDeterministic_TS_1_k4.dat'
filename4 = 'WorkDeterministic_TS_1_k8.dat'
filename5 = 'WorkDeterministic_TS_1_k16.dat'

file1 = open(filename1,'r')
data = file1.readlines()
file1.close()

Time = []
Work = []
for index in range(len(data)-2):
	parsed = data[index+2].split()
	Time.append(eval(parsed[0]))
	Work.append(eval(parsed[1]))

k1, = plt.plot(Time,Work,label='k1')

file1 = open(filename2,'r')
data = file1.readlines()
file1.close()

Time = []
Work = []
for index in range(len(data)-2):
	parsed = data[index+2].split()
	Time.append(eval(parsed[0]))
	Work.append(eval(parsed[1]))

k2, = plt.plot(Time,Work,label='k2')

file1 = open(filename3,'r')
data = file1.readlines()
file1.close()

Time = []
Work = []
for index in range(len(data)-2):
	parsed = data[index+2].split()
	Time.append(eval(parsed[0]))
	Work.append(eval(parsed[1]))

k3, = plt.plot(Time,Work,label='k4')

file1 = open(filename4,'r')
data = file1.readlines()
file1.close()

Time = []
Work = []
for index in range(len(data)-2):
	parsed = data[index+2].split()
	Time.append(eval(parsed[0]))
	Work.append(eval(parsed[1]))

k4, = plt.plot(Time,Work,label='k8')

file1 = open(filename5,'r')
data = file1.readlines()
file1.close()

Time = []
Work = []
for index in range(len(data)-2):
	parsed = data[index+2].split()
	Time.append(eval(parsed[0]))
	Work.append(eval(parsed[1]))

k5, = plt.plot(Time,Work,label='k16')
plt.legend([k1,k2,k3,k4,k5])
plt.xlabel('Time')
plt.ylabel('Work')

plt.show()
plt.close()



