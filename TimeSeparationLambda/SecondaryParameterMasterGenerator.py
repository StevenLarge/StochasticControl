#Parameter Master generator for different k values in Stochastic Control Simulations
#
#Steven Large
#April 12th 2017

import os

kVals = [1,2,4,8,16,32,64,128]

filename = 'Parameters.py'

for index in range(len(kVals)):

	Path = 'k' + str(kVals[index]) + '/'

	CompleteName = os.path.join(Path,filename)

	file1 = open(CompleteName,'w')
	file1.write('#Parameters for Stochastic Control Simulations\n\n')
	file1.write('k = %d\n' % kVals[index])
	file1.write('beta=1\nm=1\ndt=0.1\na=0.25\n\n')
	file1.close()




