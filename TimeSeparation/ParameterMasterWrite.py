#This is a master module which writes the Parameters.py file to the correct susbstructure for Stochastic Control 
#simulations
#
#Steven Large
#January 4th 2017

import os

Springs = [1, 2, 4, 8, 16, 32]

SpringsPath = ['kCP_1/','kCP_2/','kCP_4/','kCP_8/','kCP_16/','kCP_32/']

filename_base = 'Parameters.py'


for index1 in range(len(Springs)):

	CompleteName = os.path.join(SpringsPath[index1],filename_base)

	file1 = open(CompleteName,'w')
	file1.write('#Langevin Parameters for Stochastic Control Simulation\n\n')
	file1.write('k=1\n')
	file1.write('a=0.25\nbeta=1\nm=1\n\ndt=0.1\n\nkCP=%lf\n' % Springs[index1])
	file1.write('Dist=10\n')
	file1.write('sigma=1\n\n')
	file1.close()



