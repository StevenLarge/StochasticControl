#This script generates the theoretical predictions for the Stochastic, Deterministic, and Total Work for input distance and k values
#
#Steven Large
#April 10th 2017

import math

def CalculateTheoreticalPredictions(dLambda,kVal,VelVar):

	Friction = 12

	ProtocolTime = []
	TimeVal = 0.1
	dT = 0.1

	while TimeVal < 600:

		ProtocolTime.append(TimeVal)
		TimeVal = TimeVal + dT

	StochasticWork = []

	for index in range(len(ProtocolTime)):
		StochasticWork.append(Friction*VelVar*ProtocolTime[index])

	DeterministicWork = []

	for index in range(len(ProtocolTime)):
		ThermodynamicLengthSquared = dLambda*dLambda*Friction
		DeterministicWork.append(ThermodynamicLengthSquared/ProtocolTime[index])

	TotalWorkTheory = []

	for index in range(len(ProtocolTime)):
		TotalWorkTheory.append(DeterministicWork[index] + StochasticWork[index])

	TotalWorkExact = []

	for index in range(len(ProtocolTime)):

		ExactWork = ((dLambda**2)/(ProtocolTime[index]**2) + VelVar)*(Friction*ProtocolTime[index] + ((Friction**2)/kVal)*(math.exp(-1*kVal*ProtocolTime[index]/Friction) - 1))
		TotalWorkExact.append(ExactWork)

	LowerBound = 2*math.sqrt(Friction*VelVar*ThermodynamicLengthSquared)

	filename1 = "WorkStochastic_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"
	filename2 = "WorkDeterministic_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"
	filename3 = "WorkTotalTheory_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"
	filename4 = "WorkTotalExact_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"		
	filename5 = "WorkLowerBound_" + str(dLambda) + "_Var_" + str(VelVar) + ".dat" 

	file1 = open(filename1,'w')
	for index in range(len(ProtocolTime)):
		file1.write("%lf\t%lf\n" % (ProtocolTime[index],StochasticWork[index]))
	file1.close()

	file2 = open(filename2,'w')
	for index in range(len(ProtocolTime)):
		file2.write("%lf\t%lf\n" % (ProtocolTime[index],DeterministicWork[index]))
	file2.close()

	file3 = open(filename3,'w')
	for index in range(len(ProtocolTime)):
		file3.write("%lf\t%lf\n" % (ProtocolTime[index],TotalWorkTheory[index]))
	file3.close()

	file4 = open(filename4,'w')
	for index in range(len(ProtocolTime)):
		file4.write("%lf\t%lf\n" % (ProtocolTime[index],TotalWorkExact[index]))
	file4.close()

	file5 = open(filename5,'w')
	for index in range(len(ProtocolTime)):
		file5.write("%lf\t%lf\n" % (ProtocolTime[index],LowerBound))
	file5.close()
