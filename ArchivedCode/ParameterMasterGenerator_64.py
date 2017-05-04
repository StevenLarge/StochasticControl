#This script generates the Parameter files for each of the different parameter subdirectories
#
#Steven Large
#August 23rd 2016

import os

def ParameterGenerator(kSys,kCP,path):

	filename = "Parameters.py"
	CompleteName = os.path.join(path + filename)

	file1 = open(CompleteName,'w')

	file1.write("#Parameter File for Langevin Simulations of Stochastic Work\n#\n#Steven Large\n#August 23rd 2016\n\n")
	file1.write("k = %d\n" % kSys)
	file1.write("a = 0.25\nbeta = 1\nm=1\n\ndt = 0.1\n\n")
	file1.write("kCP = %d\n" % kCP)
	file1.write("Dist = 50\nsigma = 1\n\n")

kLambda = [1,2,4,8,16,32,64]
kSystem = [1,2,4,8,16,32,64]

kLambda_Default = 4
kSystem_Default = 1

basePath_Lambda = 'kLambda/k'
basePath_System = 'kSystem/k'

for index in range(len(kLambda)):

	path = basePath_Lambda + str(kLambda[index]) + '/'

	ParameterGenerator(kSystem_Default,kLambda[index],path)

for index in range(len(kSystem)):

	path = basePath_System + str(kSystem[index]) + '/'

	ParameterGenerator(kSystem[index],kLambda_Default,path)




