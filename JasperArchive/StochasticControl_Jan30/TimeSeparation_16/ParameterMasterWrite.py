#This is a master module which writes the Parameters.py file to the correct susbstructure for Stochastic Control 
#simulations
#
#Steven Large
#January 4th 2017

import os

Springs = [1, 2, 4, 8, 16]
Sigmas = [1,0.5,0.1]

SpringsPath = ['k1/','k2/','k4/','k8/','k16/']
SigmasPath = ['sigma1/','sigma05/','sigma01/']

filename_base = 'Parameters.py'

for index2 in range(len(Sigmas)):

	for index1 in range(len(Springs)):

		FirstName = os.path.join(SigmasPath[index2],filename_base)
		CompleteName = os.path.join(SpringsPath[index1],FirstName)

		file1 = open(CompleteName,'w')
		file1.write('#Langevin Parameters for Stochastic Control Simulation\n\n')
		file1.write('k=%lf\n' % Springs[index1])
		file1.write('a=0.25\nbeta=1\nm=1\n\ndt=0.1\n\nkCP=1\n')
		file1.write('Dist=10\n')
		file1.write('sigma=%lf\n\n' % Sigmas[index2])
		file1.close()



