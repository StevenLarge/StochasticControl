#Time Parameter Master Generator for February 15th simulations
#
#Steven Large
#February 15th 2017

import os


StringSprings = ['1','2','4','8','16','32','64','75']
Springs = [1,2,4,8,15,32,64,75]

for index1 in range(len(Springs)):

	filename = 'Parameters' + StringSprings[index1] + '.py'

	file1 = open(filename,'w')
	file1.write('#Parameter File For Work Calculation\n\n')
	file1.write('k = %d\n' % Springs[index1])
	file1.write('beta = 1\nm = 1\ndt = 0.1\na = 0.25\n')
	file1.close()




