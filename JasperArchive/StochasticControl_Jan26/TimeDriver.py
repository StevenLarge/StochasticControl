#This module contains all of the Driving routines for the realization of a Stochastic control protocol
#
#Steven Large
#December 17th 2017

from math import *
from Potential import *
from Parameters import *
from LangevinPropogator import *
import random
import numpy

def Propogator(ProtocolTime,TimeSeparation):

	time = 0
	position = 0
	velocity = 0
	WorkAccD = 0
	WorkAccS = 0

	CP = 0
	CPVel = 0

	CPVelD = float(Dist)/float(ProtocolTime)

	Equilibration = 100 							 			# Number of equilibration steps before taking running averages

	InternalTime = 0

	ProtocolTime = ProtocolTime + Equilibration

	PoissonTime = numpy.random.poisson(TimeSeparation)+1

	counter = 0

	while time < Equilibration:
		
		if (counter%PoissonTime) == 0:
			(time, position, velocity, WorkStep, WorkS, CP, CPVel) = LangevinCPChange(time, position, velocity, CP, CPVel, CPVelD)
			InternalTime = InternalTime + dt
			PoissonTime = numpy.random.poisson(TimeSeparation)+1

		else:
			(InternalTime, position, velocity) = LangevinNoCPChange(InternalTime, position, velocity, CP, CPVel,CPVelD)

		counter = counter + 1

	while time < ProtocolTime:

		if (counter%PoissonTime) == 0:
			(time, position, velocity, WorkStep, WorkS, CP, CPVel) = LangevinCPChange(time, position, velocity, CP, CPVel, CPVelD)
			WorkAccD = WorkAccD + WorkStep
			WorkAccS = WorkAccS + WorkS
			InternalTime = InternalTime + dt
			PoissonTime = numpy.random.poisson(TimeSeparation)+1

		else:
			(InternalTime, position, velocity) = LangevinNoCPChange(InternalTime, position, velocity, CP, CPVel, CPVelD)

		counter = counter + 1

	return WorkAccD, WorkAccS, time, InternalTime 				#Put these into Driver routine to calcualte variance and other stats


