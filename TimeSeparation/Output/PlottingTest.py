#Plotting Script for stochastic control tests
#
#Steven Large
#January 18th 2017

import matplotlib.pyplot as plt

filename1 = 'WorkTheoryS_TS_64.dat'
filename2 = 'WorkTheoryS_TS_32.dat'

filename3 = 'WorkTotal_TS_64_k1.dat'
filename4 = 'WorkTotal_TS_32_k1.dat'

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
Time2 = []
Time3 = []
Time4 = []

Work1 = []
Work2 = []
Work3 = []
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

plt.plot(Time1,Work1,'b')
plt.plot(Time2,Work2,'r')


plt.plot(Time3,Work3,'g')
plt.plot(Time4,Work4,'k')

plt.show()
plt.close()


