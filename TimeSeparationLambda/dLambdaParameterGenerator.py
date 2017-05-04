#This pythin script generates the different dLambda parameter files to be read into CPGenerator routine
#
#Steven Large
#April 12th 2017

import os

dLambdaVals = ['5','10','20','40','80']
aVals = ['30','50','70','80','90','95','99']

dLambdaValsNum = [5,10,20,40,80]

filename = 'dLambdaParameter.py'

for index1 in range(len(dLambdaVals)):

	for index2 in range(len(aVals)):

		Path = 'dLambda_' + dLambdaVals[index1] + '/Trajectories_a' + aVals[index2] + '/'
		CompleteName = os.path.join(Path,filename)
		file1 = open(CompleteName,'w')

		file1.write("#dLambda parameter value\n\n")
		file1.write("Dist = %d\n" % dLambdaValsNum[index1])
		file1.close()




