#This script reads in the deterministic and stochastic works and plots them as a function of Protocol Time
#
#Steven Large
#August30th 2016

import numpy
import matplotlib.pyplot as plt

def ReadData(filename):

	file1 = open(filename,'r')
	temp = file1.readlines()

	Time = []
	Work = []

	for k in range(len(temp) - 2):

		parsed = temp[k+2].split()
		Time.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	return Time,Work


filenames = ['WorkNew.dat','WorkDeterministic.dat']

TimeD,WorkD = ReadData(filenames[1])

TimeS,WorkS = ReadData(filenames[0])

plt.plot(TimeD,WorkD)
plt.title('DeterministicWork')
plt.show()
plt.close()

plt.plot(TimeD,WorkD)
plt.plot(TimeS,WorkS)
plt.title('BothWorks')
plt.show()

plt.close()









