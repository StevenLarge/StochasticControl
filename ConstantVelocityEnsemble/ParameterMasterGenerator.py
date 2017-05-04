#This is the master parameter file generator for Constant velocity ensemble simulations
#
#Steven Large
#April 10th 2017

import os

dLambda = [5,10,20,40,80]

kVals = [1,2,4,8,16]

Dists = ['5','10','20','40','80']
Springs = ['1','2','4','8','16']

filename = 'Parameters.py'

for index in range(len(Dists)):

	SuperPath = 'dLambda_' + Dists[index] + '/'

	for index2 in range(len(Springs)):

		SubPath = 'k' + Springs[index2] + '/'

		SecondaryName = os.path.join(SubPath,filename)

		CompleteName = os.path.join(SuperPath,SecondaryName)

		file1 = open(CompleteName,'w')
		file1.write('#Parameter file for Constant velocity ensemble\n\n')
		file1.write('k = %d\n' % kVals[index2])
		file1.write('a=0.25\nbeta=1\nm=1\n\ndt=0.1\n\nkCP=4\n')
		file1.write('Dist=%d\n' % dLambda[index])
		file1.write('sigma=1\n\n')
		file1.close()


