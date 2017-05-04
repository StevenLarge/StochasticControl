#This module tests the quantitative predictions of the work required to drive a harmonic trap at constant velocity
#
#Steven Large
#December 28th 2016

import LangevinPropogator
import math
from Parameters import *
import numpy as np
import random

def AnalyticalCalculation(TotalTime):

	Friction = -math.log(a)/dt

	WorkAnalytical = Friction*(float(Dist)**2)/float(TotalTime)

	return WorkAnalytical

NumberRepeats = 100

TotalTime = 100

Equilibration = 100

TotalWorkAcc = []

CPVel = float(Dist)/float(TotalTime)

for index in range(NumberRepeats):

	time = 0
	position = 0
	velocity = 0
	CP = 0
	WorkAcc = 0.0

	while time < Equilibration:

		(time,position,velocity,WorkStep,CP) = LangevinPropogator.LangevinConstantVelocity(time,position,velocity,CP,CPVel)

	time = 0
	CP = 0
	position = position - CPVel*Equilibration

	mu = -(-math.log(a)/dt)*CPVel/k
	sigma = math.sqrt(1/(beta*k))

	position = random.gauss(mu,sigma)

	while time < TotalTime:

		(time,position,velocity,WorkStep,CP) = LangevinPropogator.LangevinConstantVelocity(time,position,velocity,CP,CPVel)
		WorkAcc += WorkStep

	TotalWorkAcc.append(WorkAcc)


AnalyticalWork = AnalyticalCalculation(TotalTime)

SimulationWork = np.mean(TotalWorkAcc)

SimulationVariance = np.var(TotalWorkAcc)

StdDevMean = math.sqrt(SimulationVariance)/math.sqrt(len(TotalWorkAcc))

print ("\n\nAnalyticalWork\t-->\t%lf\n\n" % AnalyticalWork)
print ("SimulationWork\t-->\t%lf\n" % SimulationWork)
print ("Simulation Error\t-->\t%lf\n\n" % StdDevMean)


