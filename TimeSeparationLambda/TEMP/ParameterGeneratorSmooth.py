#Generates SmoothParameter.py files for different local file locations
#
#Steven Large
#March 6th 2017

import os

Separations = [1,2,4,8,16]

WritePaths = ['Smoothing_Tau_1/','Smoothing_Tau_2/','Smoothing_Tau_4/','Smoothing_Tau_8/','Smoothing_Tau_16/']

filename = 'SmoothParameter.py'

for index in range(len(WritePaths)):

	filenameWrite = os.path.join(WritePaths[index],filename)

	file1 = open(filenameWrite,'w')

	file1.write('#Smoothing Parameter\n\n')
	file1.write('Smooth = %d' % Separations[index])
	file1.close()







