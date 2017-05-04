#This script generates the Parameter files for each of the different parameter subdirectories
#
#Steven Large
#August 23rd 2016

import os

def ParameterGenerator(TimeSeparation,kCP,path):

	filename = "Parameters.py"
	CompleteName = os.path.join(path + filename)

	file1 = open(CompleteName,'w')

	file1.write("#Parameter File for Langevin Simulations of Stochastic Work\n#\n#Steven Large\n#August 23rd 2016\n\n")
	file1.write("k = 1\n")
	file1.write("a = 0.25\nbeta = 1\nm=1\n\ndt = 0.1\n\n")
	file1.write("kCP = %d\n" % kCP)
	file1.write("Dist = 50\nsigma = 1\n\n")
	file1.write("TimeSeparation = %d" % TimeSeparation)

kLambda = [1,2,4,8,16]
TimeSeparation = [1,2,4,8,16,32,64,120]

basePath_Lambda = 'kLambda/k'
basePath_TimeSeparation = 'TimeSeparation/Tau_'

for index in range(len(kLambda)):

	for index2 in range(len(TimeSeparation)):

		path = basePath_Lambda + str(kLambda[index]) + '/' + basePath_TimeSeparation + str(TimeSeparation[index2])

		ParameterGenerator(TimeSeparation[index2],kLambda[index],path)

