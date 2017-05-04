#This python script generates the required damping parameter files in each trajectory directory
#
#Steven Large
#April 12th 2017

import os

dLambdaVals = ['5','10','20','40','80']
aVals = ['30','50','70','80','90','95','99']

aValsNum = [0.30,0.50,0.70,0.80,0.90,0.95,0.99]

filename = 'DampingParameter.py'

for index1 in range(len(dLambdaVals)):

	for index2 in range(len(aVals)):

		Path = 'dLambda_' + dLambdaVals[index1] + '/Trajectories_a' + aVals[index2] + '/'
		CompleteName = os.path.join(Path,filename)
		file1 = open(CompleteName,'w')

		file1.write("#Damping parameter value\n\n")
		file1.write("a = %lf\n" % aValsNum[index2])
		file1.close()





