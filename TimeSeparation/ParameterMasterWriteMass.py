#This is a master module which writes the Parameters.py file to the correct susbstructure for Stochastic Control 
#simulations
#
#Steven Large
#January 4th 2017

import os

MassCP = [1, 2, 4, 8, 16, 32]

MassPath = ['MASS_1/','MASS_2/','MASS_4/','MASS_8/','MASS_16/','MASS_32/']

filename_base = 'Parameters.py'

for index1 in range(len(Springs)):

	CompleteName = os.path.join(MassPath[index1],filename_base)

	file1 = open(CompleteName,'w')
	file1.write('#Langevin Parameters for Stochastic Control Simulation\n\n')
	file1.write('k=1\n')
	file1.write('a=0.25\nbeta=1\nm=1\nmCP=%d\n\ndt=0.1\n\nkCP=4\n' % MassCP[index1])
	file1.write('Dist=10\n')
	file1.write('sigma=1\n\n')
	file1.close()



