#This python script generates a 'path parameter' file that tells individual simulation realizations what thje path they need to draw data from is
#
#Steven Large
#April 12th 2017

import os

dLambdaVals = [5,10,20,40,80]
kVals = [1,2,4,8,16,32,64,128]
aVals = [30,50,70,80,90,95,99]

for index1 in range(len(dLambdaVals)):

	for index2 in range(len(kVals)):

		for index3 in range(len(aVals)):

			filename = 'PathParameters' + str(aVals[index3]) + '.py'
			WritePath = 'dLambda_' + str(dLambdaVals[index1]) + '/k' + kVals[index2] + '/'

			CompleteName = os.path.join(WritePath,filename)

			file1 = open(CompleteName,'w')
			file1.write('#Thie parameter file contains the read path for the stochastic control simualtions contained in this file\n\n')
			file1.write('READPATH = \'/home/slarge/StochasticControlApril12/dLambda_%d/Trajectories_a%s/\'' % (dLambdaVals[index1],aVals[index3]))
			file1.close()
