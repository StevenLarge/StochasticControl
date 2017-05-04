#This module generates the Parameters.py file for each of hte different kCP values
#
#Steven Large
#December 27th 2016

import os

def WriteParameterFile(WritePath,kCP):

	filename = 'Parameters.py'
	CompleteName = os.path.join(WritePath,filename)

	file1 = open(CompleteName,'w')
	file1.write('#Parameters File\n\nk=1\na=0.25\nbeta=1\nm=1\n\ndt=0.1\n\nkCP=%lf\nDist=50\nsigma=1\n' % kCP)
	file1.close()

	return None

WritePaths = ['k1/','k2/','k4/','k8/','k16/','k32/','k64/']
Springs = [1,2,4,8,16,32,64]

for k in range(len(WritePaths)):

	WriteParameterFile(WritePaths[k],Springs[k])



