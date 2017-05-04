#This is a Plotting script for Time Separation Data from January 30th
#
#Steven Large
#January 31st 2017

import matplotlib.pyplot as plt


def PlotSigma(k,TS):

	filename1 = 'WorkTotal_' + TS + '_k' + k + '_1.dat'
	filename2 = 'WorkTotal_' + TS + '_k' + k + '_05.dat'
	filename3 = 'WorkTotal_' + TS + '_k' + k + '_01.dat'

	filename4 = 'WorkTheoryS_' + TS + '_k' + k + '_1.dat'
	filename5 = 'WorkTheoryS_' + TS + '_k' + k + '_05.dat'
	filename6 = 'WorkTheoryS_' + TS + '_k' + k + '_01.dat'

	filename7 = 'WorkTheoryD_' + TS + '_k' + k + '_1.dat'
	filename8 = 'WorkTheoryD_' + TS + '_k' + k + '_05.dat'
	filename9 = 'WorkTheoryD_' + TS + '_k' + k + '_01.dat'

	filename10 = 'WorkTheorySLag_' + TS + '_k' + k + '_1.dat'
	filename11 = 'WorkTheorySLag_' + TS + '_k' + k + '_05.dat'
	filename12 = 'WorkTheorySLag_' + TS + '_k' + k + '_01.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	file5 = open(filename5,'r')
	data5 = file5.readlines()
	file5.close()

	file6 = open(filename6,'r')
	data6 = file6.readlines()
	file6.close()

	file7 = open(filename7,'r')
	data7 = file7.readlines()
	file7.close()

	file8 = open(filename8,'r')
	data8 = file8.readlines()
	file8.close()

	file9 = open(filename9,'r')
	data9 = file9.readlines()
	file9.close()

	file10 = open(filename10,'r')
	data10 = file10.readlines()
	file10.close()

	file11 = open(filename11,'r')
	data11 = file11.readlines()
	file11.close()

	file12 = open(filename12,'r')
	data12 = file12.readlines()
	file12.close()


	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []
	Time7 = []
	Work7 = []
	Time8 = []
	Work8 = []
	Time9 = []
	Work9 = []
	Time10 = []
	Work10 = []
	Time11 = []
	Work11 = []
	Time12 = []
	Work12 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		parsed8 = data8[index+2].split()
		parsed9 = data9[index+2].split()
		parsed10 = data10[index+2].split()
		parsed11 = data11[index+2].split()
		parsed12 = data12[index+2].split()

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])
		Time5.append(parsed5[0])
		Work5.append(parsed5[1])
		Time6.append(parsed6[0])
		Work6.append(parsed6[1])
		Time7.append(parsed7[0])
		Work7.append(parsed7[1])
		Time8.append(parsed8[0])
		Work8.append(parsed8[1])
		Time9.append(parsed9[0])
		Work9.append(parsed9[1])
		Time10.append(parsed10[0])
		Work10.append(parsed10[1])
		Time11.append(parsed11[0])
		Work11.append(parsed11[1])
		Time12.append(parsed12[0])
		Work12.append(parsed12[1])


	Plot1 = plt.plot(Time1,Work1,label='Total, sigma = 1')
	Plot2 = plt.plot(Time2,Work2,label='Total, sigma = 0.5')
	Plot3 = plt.plot(Time3,Work3,label='Total, sigma = 0.1')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Total Work as a function of sigma')
	filename = 'WorkTotal_' + TS + '_k' + k + '_SIGMA.png'
	plt.savefig(filename)
	plt.show()
	plt.close()

	Plot4 = plt.plot(Time4,Work4,label='Stochastic, sigma = 1')
	Plot5 = plt.plot(Time5,Work5,label='Stochastic, sigma = 0.5')
	Plot6 = plt.plot(Time6,Work6,label='Stochastic, sigma = 0.1')
	
	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Stochastic Work as a function of sigma')
	filename = 'WorkStochastic_' + TS + '_k' + k + '_SIGMA.png'
	plt.savefig(filename)
	plt.show()
	plt.close()

	Plot7 = plt.plot(Time7,Work7,label='Deterministic, sigma = 1')
	Plot8 = plt.plot(Time8,Work8,label='Deterministic, sigma = 0.5')
	Plot9 = plt.plot(Time9,Work9,label='Deterministic, sigma = 0.1')
	
	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Deterministic Work as a function of sigma')
	filename = 'WorkDeterministic_' + TS + '_k' + k + '_SIGMA.png'
	plt.savefig(filename)
	plt.show()
	plt.close()

	Plot10 = plt.plot(Time10,Work10,label='StochasticLag, sigma = 1')
	Plot11 = plt.plot(Time11,Work11,label='StochasticLag, sigma = 0.5')
	Plot12 = plt.plot(Time12,Work12,label='StochasticLag, sigma = 0.1')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Stochastic Lag Work as a function of sigma')
	filename = 'WorkStochasticLag_' + TS + '_k' + k + '_SIGMA.png'
	plt.savefig(filename)
	plt.show()
	plt.close()


def PlotKTotal(sigma,TS):


	filename1 = 'WorkTotal_' + TS + '_k1_' + sigma + '.dat'
	filename2 = 'WorkTotal_' + TS + '_k2_' + sigma + '.dat'
	filename3 = 'WorkTotal_' + TS + '_k4_' + sigma + '.dat'
	filename4 = 'WorkTotal_' + TS + '_k8_' + sigma + '.dat'
	filename5 = 'WorkTotal_' + TS + '_k16_' + sigma + '.dat'

	filename6 = 'WorkTheoryS_' + TS + '_k1_' + sigma + '.dat'
	filename7 = 'WorkTheoryS_' + TS + '_k2_' + sigma + '.dat'
	filename8 = 'WorkTheoryS_' + TS + '_k4_' + sigma + '.dat'
	filename9 = 'WorkTheoryS_' + TS + '_k8_' + sigma + '.dat'
	filename10 = 'WorkTheoryS_' + TS + '_k16_' + sigma + '.dat'

	filename11 = 'WorkTheoryD_' + TS + '_k1_' + sigma + '.dat'
	filename12 = 'WorkTheoryD_' + TS + '_k2_' + sigma + '.dat'
	filename13 = 'WorkTheoryD_' + TS + '_k4_' + sigma + '.dat'
	filename14 = 'WorkTheoryD_' + TS + '_k8_' + sigma + '.dat'
	filename15 = 'WorkTheoryD_' + TS + '_k16_' + sigma + '.dat'

	filename16 = 'WorkTheorySLag_' + TS + '_k1_' + sigma + '.dat'
	filename17 = 'WorkTheorySLag_' + TS + '_k2_' + sigma + '.dat'
	filename18 = 'WorkTheorySLag_' + TS + '_k4_' + sigma + '.dat'
	filename19 = 'WorkTheorySLag_' + TS + '_k8_' + sigma + '.dat'
	filename20 = 'WorkTheorySLag_' + TS + '_k16_' + sigma + '.dat'


	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file4 = open(filename4,'r')
	data4 = file4.readlines()
	file4.close()

	file5 = open(filename5,'r')
	data5 = file5.readlines()
	file5.close()

	file6 = open(filename6,'r')
	data6 = file6.readlines()
	file6.close()

	file7 = open(filename7,'r')
	data7 = file7.readlines()
	file7.close()

	file8 = open(filename8,'r')
	data8 = file8.readlines()
	file8.close()

	file9 = open(filename9,'r')
	data9 = file9.readlines()
	file9.close()

	file10 = open(filename10,'r')
	data10 = file10.readlines()
	file10.close()

	file11 = open(filename11,'r')
	data11 = file11.readlines()
	file11.close()

	file12 = open(filename12,'r')
	data12 = file12.readlines()
	file12.close()

	file13 = open(filename13,'r')
	data13 = file13.readlines()
	file13.close()

	file14 = open(filename14,'r')
	data14 = file14.readlines()
	file14.close()

	file15 = open(filename15,'r')
	data15 = file15.readlines()
	file15.close()

	file16 = open(filename16,'r')
	data16 = file16.readlines()
	file16.close()

	file17 = open(filename17,'r')
	data17 = file17.readlines()
	file17.close()

	file18 = open(filename18,'r')
	data18 = file18.readlines()
	file18.close()

	file19 = open(filename19,'r')
	data19 = file19.readlines()
	file19.close()

	file20 = open(filename20,'r')
	data20 = file20.readlines()
	file20.close()


	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []
	Time7 = []
	Work7 = []
	Time8 = []
	Work8 = []
	Time9 = []
	Work9 = []
	Time10 = []
	Work10 = []
	Time11 = []
	Work11 = []
	Time12 = []
	Work12 = []
	Time13 = []
	Work13 = []
	Time14 = []
	Work14 = []
	Time15 = []
	Work15 = []
	Time16 = []
	Work16 = []
	Time17 = []
	Work17 = []
	Time18 = []
	Work18 = []
	Time19 = []
	Work19 = []
	Time20 = []
	Work20 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()
		parsed7 = data7[index+2].split()
		parsed8 = data8[index+2].split()
		parsed9 = data9[index+2].split()
		parsed10 = data10[index+2].split()
		parsed11 = data11[index+2].split()
		parsed12 = data12[index+2].split()
		parsed13 = data13[index+2].split()
		parsed14 = data14[index+2].split()
		parsed15 = data15[index+2].split()
		parsed16 = data16[index+2].split()
		parsed17 = data17[index+2].split()
		parsed18 = data18[index+2].split()
		parsed19 = data19[index+2].split()
		parsed20 = data20[index+2].split()

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])
		Time5.append(parsed5[0])
		Work5.append(parsed5[1])
		Time6.append(parsed6[0])
		Work6.append(parsed6[1])
		Time7.append(parsed7[0])
		Work7.append(parsed7[1])
		Time8.append(parsed8[0])
		Work8.append(parsed8[1])
		Time9.append(parsed9[0])
		Work9.append(parsed9[1])
		Time10.append(parsed10[0])
		Work10.append(parsed10[1])
		Time11.append(parsed11[0])
		Work11.append(parsed11[1])
		Time12.append(parsed12[0])
		Work12.append(parsed12[1])
		Time13.append(parsed13[0])
		Work13.append(parsed13[1])
		Time14.append(parsed14[0])
		Work14.append(parsed14[1])
		Time15.append(parsed15[0])
		Work15.append(parsed15[1])
		Time16.append(parsed16[0])
		Work16.append(parsed16[1])
		Time17.append(parsed17[0])
		Work17.append(parsed17[1])
		Time18.append(parsed18[0])
		Work18.append(parsed18[1])
		Time19.append(parsed19[0])
		Work19.append(parsed19[1])
		Time20.append(parsed20[0])
		Work20.append(parsed20[1])

	Plot1 = plt.plot(Time1,Work1,label='Total, K = 1')
	Plot2 = plt.plot(Time2,Work2,label='Total, K = 2')
	Plot3 = plt.plot(Time3,Work3,label='Total, K = 4')
	Plot4 = plt.plot(Time4,Work4,label='Total, K = 8')
	Plot5 = plt.plot(Time5,Work5,label='Total, K = 16')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Total Work as a function of K')
	filename = 'WorkTotal_' + TS + '_K_' + sigma + '.png'
	plt.savefig(filename)
	plt.show()
	plt.close()

	Plot6 = plt.plot(Time6,Work6,label='Stochastic, K = 1')
	Plot7 = plt.plot(Time7,Work7,label='Stochastic, K = 2')
	Plot8 = plt.plot(Time8,Work8,label='Stochastic, K = 4')
	Plot9 = plt.plot(Time9,Work9,label='Stochastic, K = 8')
	Plot10 = plt.plot(Time10,Work10,label='Stochastic, K = 16')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Stocahstic Work as a function of K')
	filename = 'WorkStochastic_' + TS + '_K_' + sigma + '.png'
	plt.savefig(filename)
	plt.show()
	plt.close()

	Plot11 = plt.plot(Time11,Work11,label='Deterministic, K = 1')
	Plot12 = plt.plot(Time12,Work12,label='Deterministic, K = 2')
	Plot13 = plt.plot(Time13,Work13,label='Deterministic, K = 4')
	Plot14 = plt.plot(Time14,Work14,label='Deterministic, K = 8')
	Plot15 = plt.plot(Time15,Work15,label='Deterministic, K = 16')

	
	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Deterministic Work as a function of K')
	filename = 'WorkDeterministic_' + TS + '_K_' + sigma + '.png'
	plt.savefig(filename)
	plt.show()
	plt.close()

	Plot16 = plt.plot(Time16,Work16,label='StochasticLag, K = 1')
	Plot17 = plt.plot(Time17,Work17,label='StochasticLag, K = 2')
	Plot18 = plt.plot(Time18,Work18,label='StochasticLag, K = 4')
	Plot19 = plt.plot(Time19,Work19,label='StochasticLag, K = 8')
	Plot20 = plt.plot(Time20,Work20,label='StochasticLag, K = 16')

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')
	plt.title('Stochastic Lag Work as a function of K')
	filename = 'WorkStochasticLag_' + TS + '_K_' + sigma + '.png'
	plt.savefig(filename)
	plt.show()
	plt.close()


def PlotAll(sigma,k,TS):

	filename1 = 'WorkTotal_' + TS + '_k' + k + '_' + sigma + '.dat'
	filename2 = 'WorkTheoryS_' + TS + '_k' + k + '_' + sigma + '.dat'
	filename3 = 'WorkTheoryD_' + TS + '_k' + k + '_' + sigma + '.dat'
	filename4 = 'WorkTheorySLag_' + TS + '_k' + k + '_' + sigma + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file2 = open(filename2,'r')
	data2 = file2.readlines()
	file2.close()

	file3 = open(filename3,'r')
	data3 = file3.readlines()
	file3.close()

	file3 = open(filename4,'r')
	data4 = file3.readlines()
	file3.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()

		Time1.append(parsed1[0])
		Work1.append(parsed1[1])
		Time2.append(parsed2[0])
		Work2.append(parsed2[1])
		Time3.append(parsed3[0])
		Work3.append(parsed3[1])
		Time4.append(parsed4[0])
		Work4.append(parsed4[1])


	Plot1 = plt.plot(Time1,Work1,label='Total')
	Plot2 = plt.plot(Time2,Work2,label='Stochastic')
	Plot3 = plt.plot(Time3,Work3,label='Deterministic')
	Plot4 = plt.plot(Time4,Work4,label='Stochastic Lag')

	filename = 'WorkAll_' + TS + '_k' + k + '_' + sigma + '.png'
	title = 'TimeSepation = ' + TS

	plt.legend()
	plt.xlabel('ProtocolTime')
	plt.ylabel('Work')

	plt.title(title)

	plt.savefig(filename)

	plt.show()

	plt.close()


def PlotTotal(sigma,k):

	filename1 = 'WorkTotal_1_k' + k + '_' + sigma + '.dat'
	filename2 = 'WorkTotal_2_k' + k + '_' + sigma + '.dat'
	filename3 = 'WorkTotal_4_k' + k + '_' + sigma + '.dat'
	filename4 = 'WorkTotal_8_k' + k + '_' + sigma + '.dat'
	filename5 = 'WorkTotal_16_k' + k + '_' + sigma + '.dat'
	filename6 = 'WorkTotal_32_k' + k + '_' + sigma + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))				
		Time5.append(eval(parsed5[0]))
		Work5.append(eval(parsed5[1]))
		Time6.append(eval(parsed6[0]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Total Work')

	plt.savefig('WorkTotal.png')

	plt.show()
	plt.close()


def PlotStochastic(sigma,k):

	filename1 = 'WorkTheoryS_1_k' + k + '_' + sigma + '.dat'
	filename2 = 'WorkTheoryS_2_k' + k + '_' + sigma + '.dat'
	filename3 = 'WorkTheoryS_4_k' + k + '_' + sigma + '.dat'
	filename4 = 'WorkTheoryS_8_k' + k + '_' + sigma + '.dat'
	filename5 = 'WorkTheoryS_16_k' + k + '_' + sigma + '.dat'
	filename6 = 'WorkTheoryS_32_k' + k + '_' + sigma + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))				
		Time5.append(eval(parsed5[0]))
		Work5.append(eval(parsed5[1]))
		Time6.append(eval(parsed6[0]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Work')

	plt.savefig('WorkStochastic.png')

	plt.show()
	plt.close()


def PlotStochasticLag(sigma,k):

	filename1 = 'WorkTheorySLag_1_k' + k + '_' + sigma + '.dat'
	filename2 = 'WorkTheorySLag_2_k' + k + '_' + sigma + '.dat'
	filename3 = 'WorkTheorySLag_4_k' + k + '_' + sigma + '.dat'
	filename4 = 'WorkTheorySLag_8_k' + k + '_' + sigma + '.dat'
	filename5 = 'WorkTheorySLag_16_k' + k + '_' + sigma + '.dat'
	filename6 = 'WorkTheorySLag_32_k' + k + '_' + sigma + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))				
		Time5.append(eval(parsed5[0]))
		Work5.append(eval(parsed5[1]))
		Time6.append(eval(parsed6[0]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Stochastic Lag Work')

	plt.savefig('WorkStochasticLag.png')

	plt.show()
	plt.close()


def PlotDeterministic(sigma,k):

	filename1 = 'WorkTheoryD_1_k' + k + '_' + sigma + '.dat'
	filename2 = 'WorkTheoryD_2_k' + k + '_' + sigma + '.dat'
	filename3 = 'WorkTheoryD_4_k' + k + '_' + sigma + '.dat'
	filename4 = 'WorkTheoryD_8_k' + k + '_' + sigma + '.dat'
	filename5 = 'WorkTheoryD_16_k' + k + '_' + sigma + '.dat'
	filename6 = 'WorkTheoryD_32_k' + k + '_' + sigma + '.dat'

	file1 = open(filename1,'r')
	data1 = file1.readlines()
	file1.close()

	file1 = open(filename2,'r')
	data2 = file1.readlines()
	file1.close()

	file1 = open(filename3,'r')
	data3 = file1.readlines()
	file1.close()

	file1 = open(filename4,'r')
	data4 = file1.readlines()
	file1.close()

	file1 = open(filename5,'r')
	data5 = file1.readlines()
	file1.close()

	file1 = open(filename6,'r')
	data6 = file1.readlines()
	file1.close()

	Time1 = []
	Work1 = []
	Time2 = []
	Work2 = []
	Time3 = []
	Work3 = []
	Time4 = []
	Work4 = []
	Time5 = []
	Work5 = []
	Time6 = []
	Work6 = []

	for index in range(len(data1)-2):
		parsed1 = data1[index+2].split()
		parsed2 = data2[index+2].split()
		parsed3 = data3[index+2].split()
		parsed4 = data4[index+2].split()
		parsed5 = data5[index+2].split()
		parsed6 = data6[index+2].split()

		Time1.append(eval(parsed1[0]))
		Work1.append(eval(parsed1[1]))
		Time2.append(eval(parsed2[0]))
		Work2.append(eval(parsed2[1]))
		Time3.append(eval(parsed3[0]))
		Work3.append(eval(parsed3[1]))
		Time4.append(eval(parsed4[0]))
		Work4.append(eval(parsed4[1]))				
		Time5.append(eval(parsed5[0]))
		Work5.append(eval(parsed5[1]))
		Time6.append(eval(parsed6[0]))
		Work6.append(eval(parsed6[1]))

	Plot1 = plt.plot(Time1,Work1,label='1')
	Plot2 =	plt.plot(Time2,Work2,label='2')
	Plot3 = plt.plot(Time3,Work3,label='4')
	Plot4 = plt.plot(Time4,Work4,label='8')
	Plot5 = plt.plot(Time5,Work5,label='16')
	Plot6 = plt.plot(Time6,Work6,label='32')

	plt.legend()
	plt.xlabel('Protocol Time')
	plt.ylabel('Work')
	plt.title('Deterministic Work')

	plt.savefig('WorkDeterministic.png')

	plt.show()
	plt.close()


