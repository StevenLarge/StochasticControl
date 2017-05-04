#This is a master module which writes the TimeParameter.py files to the correct substructure for stochastic control 
#simulations
#
#Steven Large
#January 4th 2017

import os

Times = ['TimeSeparation_1/','TimeSeparation_2/','TimeSeparation_4/','TimeSeparation_8/','TimeSeparation_16/','TimeSeparation_32/','TimeSeparation_64/','TimeSeparation_128/']

NumberTimes = [1, 2, 4, 8, 16, 32, 64, 128]

filename_base = 'TimeParameters.py'

for index1 in range(len(Times)):

	CompleteName = os.path.join(Times[index1],filename_base)

	file1 = open(CompleteName,'w')
	file1.write('#Time Separation Parameter for Stochastic Control Simulation\n')
	file1.write('TimeSeparation = %lf' % NumberTimes[index1])
	file1.close()



