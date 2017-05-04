#This is the master module for writing the Velocity Variance Parameter file
#
#Steven Large
#January 4th 2017

import os

VelocityVar = [0.125,0.25,0.5,1,2,4,8]

Paths = ['0125','025','05','1','2','4','8']

filename = 'VelocityParameters.py'

for index in range(len(Paths)):

	WritePath = 'VelVar_' + str(Paths[index]) + '/'

	CompleteName = os.path.join(WritePath, filename)

	file1 = open(CompleteName,'w')
	file1.write('#Velocity Varance Parameter File\n\n')
	file1.write('VelocityVariance = %lf' % VelocityVar[index])


