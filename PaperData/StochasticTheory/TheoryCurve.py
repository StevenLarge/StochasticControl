#This script generates the theoretical predictions for the Stochastic, Deterministic, and Total Work for input distance and k values
#
#Steven Large
#April 10th 2017

import math

def CalculateTheory(dLambda,kVal):

	Friction = 12

	VelVar = 1

	ProtocolTime = []
	TimeVal = 0.02
	dT = 0.02

	while TimeVal < 200:

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

	filename1 = "WorkStochastic_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"
	filename2 = "WorkDeterministic_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"
	filename3 = "WorkTotalTheory_" + str(dLambda) + "_k" + str(kVal) + "_Var_" + str(VelVar) + ".dat"

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

