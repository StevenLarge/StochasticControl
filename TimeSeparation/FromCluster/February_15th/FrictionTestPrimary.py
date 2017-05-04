#This script rewrites the work data as work/friction
#
#Steven Large
#February 15th 2017

def ReadData(filename):

	Tau = []
	Work = []

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()

		Tau.append(eval(parsed[0]))
		Work.append(eval(parsed[1]))

	return Tau, Work

def WriteData(filename,Time,Work):

	file1 = open(filename,'w')

	file1.write('Time\tWork\n\n')

	for index in range(len(Work)):
		file1.write('%lf\t%lf\n' % (Time[index],Work[index]))
	file1.close()


Filenames = ['WorkTotal_2_2.dat','WorkTotal_4_2.dat','WorkTotal_8_2.dat','WorkTotal_16_2.dat','WorkTotal_32_2.dat','WorkTotal_64_2.dat','WorkTotal_128_2.dat','WorkTotal_256_2.dat']

WriteNames = ['WorkTotalN_2.dat','WorkTotalN_4.dat','WorkTotalN_8.dat','WorkTotalN_16.dat','WorkTotalN_32.dat','WorkTotalN_64.dat','WorkTotalN_128.dat','WorkTotalN_256.dat']

Separations = [2,4,8,16,32,64,128,256]

for index2 in range(len(Filenames)):

	Tau, Work = ReadData(Filenames[index2])

	Friction = 12*Separations[index2]

	for index3 in range(len(Work)):
		Work[index3] = Work[index3]/float(Friction)

	WriteData(Writename[index2],Tau,Work)




