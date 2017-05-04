#This is a plotting routine for the Autocorrelation function of different Time Separation Values
#
#Steven Large
#January 23rd 2017

import matplotlib.pyplot as plt

def ReadData(filename):

	file1 = open(filename,'r')
	data = file1.readlines()

	Time = []
	AutoCorr = []

	for index in range(len(data)-2):
		parsed = data[index+2].split()
		Time.append(eval(parsed[0]))
		AutoCorr.append(eval(parsed[1]))

	return Time, AutoCorr


filename_1 = 'AutoCorrelation_1.dat'
filename_5 = 'AutoCorrelation_5.dat'
filename_10 = 'AutoCorrelation_10.dat'
filename_20 = 'AutoCorrelation_20.dat'
filename_40 = 'AutoCorrelation_40.dat'

Time1,AutoCorr1 = ReadData(filename_1)
Time5,AutoCorr5 = ReadData(filename_5)
Time10,AutoCorr10 = ReadData(filename_10)
Time20,AutoCorr20 = ReadData(filename_20)
Time40,AutoCorr40 = ReadData(filename_40)

plt.plot(Time1,AutoCorr1,'r')
plt.plot(Time5,AutoCorr5,'g')
plt.plot(Time10,AutoCorr10,'b')
plt.plot(Time20,AutoCorr20,'m')
plt.plot(Time40,AutoCorr40,'k')

plt.show()
plt.close()



