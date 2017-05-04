#This module tests the quantitative predictions of the work required to drive a harmonic trap at constant velocity
#
#Steven Large
#December 28th 2016

import LangevinPropogator
import math
from Parameters import *
import numpy as np
import random

NumberRepeats = 100
TotalTime = 10
Equilibration = 500

TotalWorkAcc = []

CPVel = float(Dist)/float(TotalTime)

VelVarTrack = []

for index in range(NumberRepeats):

	time = 0
	position = 0
	velocity = 0
	CP = 0
	WorkAcc = 0.0

	index = 0

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


