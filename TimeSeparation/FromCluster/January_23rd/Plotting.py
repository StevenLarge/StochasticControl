#Plotting script for January 23rd Time Separation data
#
#Steven Large
#January 24th 2017

import matplotlib.pyplot as plt

def ReadData(filename):

	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	Time = []
	Work = []

	for index in range(len(data)-2):
		parsed = data[index+2].split()
		Time.append(parsed[0])
		Work.append(parsed[1])

	return Time, Work


filename1 = 'WorkTotal_TS_1_k1.dat'
filename2 = 'WorkTotal_TS_2_k1.dat'
filename3 = 'WorkTotal_TS_4_k1.dat'
filename4 = 'WorkTotal_TS_8_k1.dat'
filename5 = 'WorkTotal_TS_16_k1.dat'
filename6 = 'WorkTotal_TS_32_k1.dat'
filename7 = 'WorkTotal_TS_64_k1.dat'

Time = []
Work = []

files = [filename1,filename2,filename3,filename4,filename5,filename6,filename7]

for index in range(len(files)):

	TimeTemp, WorkTemp = ReadData(files[index])

	Time.append(TimeTemp)
	Work.append(WorkTemp)

	plt.plot(Time[index],Work[index])

plt.show()
plt.close()

filename1 = 'WorkTheoryS_TS_1.dat'
filename2 = 'WorkTheoryS_TS_2.dat'
filename3 = 'WorkTheoryS_TS_4.dat'
filename4 = 'WorkTheoryS_TS_8.dat'
filename5 = 'WorkTheoryS_TS_16.dat'
filename6 = 'WorkTheoryS_TS_32.dat'
filename7 = 'WorkTheoryS_TS_64.dat'

Time = []
Work = []

files = [filename1,filename2,filename3,filename4,filename5,filename6,filename7]

for index in range(len(files)):

	TimeTemp, WorkTemp = ReadData(files[index])

	Time.append(TimeTemp)
	Work.append(WorkTemp)

	plt.plot(Time[index],Work[index])

plt.show()
plt.close()
