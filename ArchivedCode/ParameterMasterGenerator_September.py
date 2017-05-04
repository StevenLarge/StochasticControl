#This script generates the Parameter files for each of the different parameter subdirectories
#
#Steven Large
#August 23rd 2016

import os

def ParameterGenerator(sigma,kCP,path):

	filename = "Parameters.py"
	CompleteName = os.path.join(path + filename)

	file1 = open(CompleteName,'w')

	file1.write("#Parameter File for Langevin Simulations of Stochastic Work\n#\n#Steven Large\n#August 23rd 2016\n\n")
	file1.write("k = 1\n")
	file1.write("a = 0.25\nbeta = 1\nm=1\n\ndt = 0.1\n\n")
	file1.write("kCP = %d\n" % kCP)
	file1.write("Dist = 50\nsigma = %lf\n\n" % sigma)

kLambda = [1,2,5,10,20,40]

sigma = [0.25, 0.5, 1.0, 2.0, 4.0]

sigmaLabel = ['025','05','1','2','4']

basepathSigma = 'sigma'
basePath_Lambda = 'kLambda/k'

for primeindex in range(len(sigma)):

	BasePath = basepathSigma + sigmaLabel[primeindex] + '/'

	for index in range(len(kLambda)):

		path = BasePath + basePath_Lambda + str(kLambda[index]) + '/'

		ParameterGenerator(sigma[primeindex],kLambda[index],path)



