#Plotting Script for Local Tests of Lag-Time Approximation
#
#Steven Large
#January 18th 2017

import matplotlib.pyplot as plt

filename1 = 'WorkTotalTheory_k16.dat'
filename2 = 'WorkTotalTheory_k2.dat'
#filename3 = 'WorkTotal_k2.dat'

file1 = open(filename1,'r')
file2 = open(filename2,'r')
#file3 = open(filename3,'r')

data1 = file1.readlines()
data2 = file2.readlines()
#data3 = file3.readlines()

file1.close()
file2.close()
#file3.close()

Time1 = []
Time2 = []
#Time3 = []
Work1 = []
Work2 = []
#Work3 = []

for index in range(len(data1)-2):

	parsed1 = data1[index+2].split()
	parsed2 = data2[index+2].split()
#	parsed3 = data3[index+2].split()

	Time1.append(eval(parsed1[0]))
	Work1.append(eval(parsed1[1]))
	Time2.append(eval(parsed2[0]))
	Work2.append(eval(parsed2[1]))
#	Time3.append(eval(parsed3[0]))
#	Work3.append(eval(parsed3[1]))


plt.plot(Time1,Work1,'r')
plt.plot(Time2,Work2,'b')
#plt.plot(Time3,Work3,'g')
plt.show()

plt.close()

