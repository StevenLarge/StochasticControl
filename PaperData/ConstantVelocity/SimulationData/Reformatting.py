#This python script reformats the output data for work vs protocol time for constant velocity results
#
#Steven Large
#April 11th 2017

dLambda = ['5','10','20','40','80']
kVals = ['1','2','4','8','16']
VelVar = ['0125','025','05','1','2','4','8']

for index1 in range(len(dLambda)):

	for index2 in range(len(kVals)):

		for index3 in range(len(VelVar)):

			filename = 'WorkTotal_L' + dLambda[index1] + '_k' + kVals[index2] + '_' + VelVar[index3] + '.dat'

			file1 = open(filename,'r')
			data = file1.readlines()
			file1.close()

			file2 = open(filename,'w')
			for index4 in range(len(data)-2):
				parsed = data[index4+2].split()
				file2.write("%lf\t%lf\n" % (eval(parsed[0]),eval(parsed[1])))
			file2.close()