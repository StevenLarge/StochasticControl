#Thie is the python reformatting script for April data, Stochastic Contorl simulations
#
#Steven Large
#April 13th 2017

dLambda = [5,10,20,40,80]
kVals = [1,2,4,8,16,32,64,128]
aVals = [30,50,70,80,90,95,99]

for index1 in range(len(dLambda)):

	for index2 in range(len(kVals)):

		for index3 in range(len(aVals)):

			filename = 'WorkTotal_L' + str(dLambda[index1]) + '_k' + str(kVals[index2]) + '_a' + str(aVals[index3]) + '.dat'
			file1 = open(filename,'r')
			DataTemp = file1.readlines()
			file1.close()

			file2 = open(filename,'w')
			for index4 in range(len(DataTemp)-2):
				parsed = DataTemp[index4+2].split()
				file2.write("%lf\t%lf\n" % (eval(parsed[0]),eval(parsed[1])))
			file2.close()



