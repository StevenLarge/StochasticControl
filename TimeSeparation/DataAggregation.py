#This module reads and extracts the work contributions from the 10 repetitions and averages them
#
#Steven Large
#February 9th 2017

import os

Paths = ['Repetition1/','Repetition2/','Repetition3/','Repetition4/','Repetition5/','Repetition6/','Repetition7/','Repetition8/','Repetition9/','Repetition10/']

TimeSeparations = ['TimeSeparation2_512/','TimeSeparation2_1024/','TimeSeparation_2048/','TimeSeparation_4096/','TimeSeparation_8192/']

TS = ['512', '1024', '2048', '4096', '8192']

FileTotalBase = 'WorkTotal_TS_'
FileStochasticBase = 'WorkTheoryS_TS_'
FileDeterministicBase = 'WorkTheoryD_TS_'
FileStochasticLagBase = 'WorkTheorySLag_TS_'

for index1 in range(len(TimeSeparations)):

	FinalFileTotal = 'WorkTotal_' + TS[index1] + '.dat'
	FinalFileDeterministic = 'WorkTotal_' + TS[index1] + '.dat'
	FinalFileStochastic = 'WorkStochastic_' + TS[index1] + '.dat'
	FinalFileStochasticLag = 'WorkStochasticLag_' + TS[index1] + '.dat'

	CompleteNameTotal = os.path.join(TimeSeparations[index1],FinalFileTotal)
	CompleteNameDeterministic = os.path.join(TimeSeparations[index1],FinalFileDeterministic)
	CompleteNameStochastic = os.path.join(TimeSeparations[index],FinalFileStochastic)
	CompleteNameStochasticLag = os.path.join(TimeSeparations[index],FinalFileStochasticLag)

	MasterTotal = []
	MasterDeterministic = []
	MasterStochastic = []
	MasterStochasticLag = []

	for index2 in range(len(Paths)):

		FilenamePrimitive = os.path.join(TimeSeparations[index1],Paths[index2])

		FileTotal = FileTotalBase + TS[index2] + '.0' + '_k1.dat'
		FileStochastic = FileStochasticBase + TS[index2] + '.0' + '_k1.dat'
		FileDeterministic = FileDeterministicBase + TS[index2] + '.0' + '_k1.dat'
		FileStochasticLag = FileStochasticLagBase + TS[index2] + '.0' + '_k1.dat'

		FilenameTotal = os.path.join(FilenamePrimitive,FileTotal)
		FilenameDeterministic = os.path.join(FilenamePrimitive,FileDeterministic)
		FilenameStochastic = os.path.join(FilenamePrimitive,FileStochastic)
		FilenameStochasticLag = os.path.join(FilenamePrimitive,FileStochasticLag)

		file1 = open(FilenameTotal,'r')
		data1 = file1.readlines()
		file1.close()

		file2 = open(FilenameDeterministic,'r')
		data2 = file2.readlines()
		file2.close()

		file3 = open(FilenameStochastic,'r')
		data3 = file3.readlines()
		file3.close()

		file4 = open(FilenameStochasticLag,'r')
		data4 = file4.readlines()
		file4.close()

		TimeT = []
		WorkT = []
		TimeD = []
		WorkD = []
		TimeS = []
		WorkS = []
		TimeSL = []
		WorkSL = []

		for index3 in range(len(data1)-2):

			parsed1 = data1[index3+2].split()
			parsed2 = data2[index3+2].split()
			parsed3 = data3[index3+2].split()
			parsed4 = data3[index3+2].split()

			TimeT.append(eval(parsed1[0]))
			WorkT.append(eval(parsed1[1]))
			TimeD.append(eval(parsed2[0]))
			WorkD.append(eval(parsed2[1]))
			TimeS.append(eval(parsed3[0]))
			WorkS.append(eval(parsed3[1]))
			TimeSL.append(eval(parsed4[0]))
			WorkSL.append(eval(parsed4[1]))

		MasterTotal.append(WorkT)
		MasterDeterministic.append(WorkD)
		MasterStochastic.append(WorkS)
		MasterStochasticLag.append(WorkSL)

	TotalWork = []
	DeterministicWork = []
	StochasticWork = []
	StochasticLagWork = []

	for index4 in range(len(MasterTotal[1])):

		AccT = 0.0
		AccS = 0.0
		AccD = 0.0
		AccSL = 0.0

		for index5 in range(len(MasterTotal)):

			AccT = AccT + MasterTotal[index5][index4]
			AccD = AccD + MasterDeterministic[index5][index4]
			AccS = AccS + MasterStochastic[index5][index4]
			AccSL = AccSL + MasterStochasticLag[index5][index4]

		TotalWork.append(AccT/float(len(MasterTotal)))
		DeterministicWork.append(AccT/float(len(MasterTotal)))
		StochasticWork.append(AccT/float(len(MasterTotal)))
		StochasticLagWork.append(AccT/float(len(MasterTotal)))

	file1 = open(CompleteNameTotal,'w')
	file1.write('Tau\tWork\n\n')

	for index6 in range(len(TotalWork)):
		file1.write('%lf\t%lf\n' % (TimeT[index6],TotalWork[index6]))
	file1.close()

	file1 = open(CompleteNameDeterministic,'w')
	file1.write('Tau\tWork\n\n')

	for index6 in range(len(DeterministicWork)):
		file1.write('%lf\t%lf\n' % (TimeD[index6],DeterministicWork[index6]))
	file1.close()

	file1 = open(CompleteNameStochastic,'w')
	file1.write('Tau\tWork\n\n')

	for index6 in range(len(StochasticWork)):
		file1.write('%lf\t%lf\n' % (TimeS[index6],StochasticWork[index6]))
	file1.close()

	file1 = open(CompleteNameStochasticLag,'w')
	file1.write('Tau\tWork\n\n')

	for index6 in range(len(StochasticLagWork)):
		file1.write('%lf\t%lf\n' % (TimeSL[index6],StochasticLagWork[index6]))
	file1.close()





