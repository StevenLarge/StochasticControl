#Time Parameter Master Generator for February 15th simulations
#
#Steven Large
#February 15th 2017

import os

baseNames = ['TimeSeparation_','TimeSeparation_a75_','TimeSeparation_a95_']

StringSeparations = ['1','2','4','8','16','32','64']
TimeSeparations = [1,2,4,8,15,32,64]
filename = 'TimeParameters.py'

for index1 in range(len(TimeSeparations)):

	for index2 in range(len(baseNames)):

		WritePath = baseNames[index2] + StringSeparations[index1] + '/'
		CompleteName = os.path.join(WritePath,filename)

		file1 = open(CompleteName,'w')
		file1.write('TimeSeparation = %d' % TimeSeparations[index1])
		file1.close()



