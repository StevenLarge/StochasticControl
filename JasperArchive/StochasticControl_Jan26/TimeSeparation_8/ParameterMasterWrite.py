#This is a master module which writes the Parameters.py file to the correct susbstructure for Stochastic Control 
#simulations
#
#Steven Large
#January 4th 2017

import os

NumberSprings = [0.1, 0.01]

Springs = ['k01/','k001/']

filename_base = 'Parameters.py'

for index2 in range(len(Springs)):

	CompleteName = os.path.join(Springs[index2],filename_base)

	file1 = open(CompleteName,'w')
	file1.write('#Langevin Parameters for Stochastic Control Simulation\n\n')
	file1.write('k=1\na=0.25\nbeta=1\nm=1\n\ndt=0.1\n\n')
	file1.write('kCP=%lf\n' % NumberSprings[index2])
	file1.write('Dist=10\nsigma=1\n\n')
	file1.close()



