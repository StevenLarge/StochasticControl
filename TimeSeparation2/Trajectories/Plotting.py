#Test plotting routine for CP Generator
#
#Steven Large
#February 15th 2017

import matplotlib.pyplot as plt

def Plotting(mod1,mod2):

	filename = 'CP_Trajectory_' + mod1 + '_' + mod2 + '.dat'
	
	file1 = open(filename,'r')	
	data1 = file1.readlines()
	file1.close()

	Time = []
	Position = []

	for index in range(len(data1)):
		parsed = data1[index].split()
		Time.append(eval(parsed[0]))
		Position.append(eval(parsed[1]))

	plt.plot(Time,Position)
	plt.show()
	plt.close()



