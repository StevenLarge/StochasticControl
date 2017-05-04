#This module simulates the work required to move a harmonic trap a fixed distance in a fixed finite time
#and also measures the variance of the work values, this is then compared with two theoretical metrics
#
#Steven Large
#January 17th 2017

import os
import numpy as np
import WriteData
import VarianceDriver

NumTrajectories = 10000

TimeRange = 50

AvgWork = []
WorkVar = []
Tau = []

for index1 in range(TimeRange):

	ProtocolTime = 10 + 10*index1

	WorkAcc = 0
	WorkTrack = []

	for index in range(NumTrajectories):

		Work = VarianceDriver.Propogator(ProtocolTime)

		WorkAcc = WorkAcc + Work
		WorkTrack.append(Work)

	Tau.append(ProtocolTime)
	AvgWork.append(WorkAcc/float(NumTrajectories))
	WorkVar.append(np.var(WorkTrack))


WriteData.WriteWork(AvgWork,Tau)
WriteData.WriteWorkVariance(WorkVar,Tau)

















