#This is a master module which writes the TimeParameter.py files to the correct substructure for stochastic control 
#simulations
#
#Steven Large
#January 4th 2017

import os

Times = ['TimeSeparation2_512/','TimeSeparation2_1024/','TimeSeparation2_2048/','TimeSeparation2_4096/','TimeSeparation2_8192/']

NumberTimes = [512, 1024, 2048, 4096, 8192]

filename_base = 'TimeParameters.py'

for index1 in range(len(Times)):

	CompleteName = os.path.join(Times[index1],filename_base)

	file1 = open(CompleteName,'w')
	file1.write('#Time Separation Parameter for Stochastic Control Simulation\n')
	file1.write('TimeSeparation = %lf' % NumberTimes[index1])
	file1.close()



