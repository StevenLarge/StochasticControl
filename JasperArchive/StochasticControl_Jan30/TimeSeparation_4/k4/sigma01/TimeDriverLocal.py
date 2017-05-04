#TimeDriver For local tests, calculating the total work only
#
#Steven Large
#January 18th 2017


from math import *
from Potential import *
from Parameters import *
from LangevinPropogator import *
import random
import numpy as np

def Propogator(ProtocolTime,TimeSeparation):

	time = 0
	position = 0
	velocity = 0
	WorkAcc = 0
	WorkAccTheory = 0

	CP = 0
	CPVel = 0

	CPVelD = float(Dist)/float(ProtocolTime)

	friction = float(12)/float(20)

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	InternalTime = 0

	ProtocolTime = ProtocolTime + Equilibration

	PoissonTime = numpy.random.poisson(TimeSeparation)+1

	counter = 0

	while time < Equilibration:
		
		if (counter%PoissonTime) == 0:
			(time, position, velocity, Work, CP, CPVel) = LangevinCPChangeLocal(time, position, velocity, CP, CPVel, CPVelD)
			InternalTime = InternalTime + dt
			PoissonTime = numpy.random.poisson(TimeSeparation)+1

		else:
			(InternalTime, position, velocity) = LangevinNoCPChange(InternalTime, position, velocity, CP, CPVel,CPVelD)

		counter = counter + 1

	while time < ProtocolTime:

		if (counter%PoissonTime) == 0:
			CPVelOld = CPVel
			(time, position, velocity, Work, CP, CPVel) = LangevinCPChangeLocal(time, position, velocity, CP, CPVel, CPVelD)
			WorkAcc = WorkAcc + Work
			InternalTime = InternalTime + dt
			PoissonTime = numpy.random.poisson(TimeSeparation)+1
			WorkAccTheory = WorkAccTheory + friction*CPVel*CPVelOld*dt

		else:
			(InternalTime, position, velocity) = LangevinNoCPChange(InternalTime, position, velocity, CP, CPVel, CPVelD)


		counter = counter + 1

	return WorkAcc, time, InternalTime, WorkAccTheory 				#Put these into Driver routine to calculate variance and other stats



def StationaryPropogator(ProtocolTime,TimeSeparation):

	time = 0
	position = 0
	velocity = 0
	WorkAcc = 0
	WorkAccTheory = 0
	WorkAccTheoryD = 0

	PositionTrack = []
	CPTrack = []
	CPVelTrack = []
	CPVelOldTrack = []

	CP = 0
	CPVel = 0
	CPVelD = float(Dist)/float(ProtocolTime)

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	InternalTime = 0

	ProtocolTime = ProtocolTime + Equilibration

	PoissonTime = TimeSeparation

	counter = 0

	while time < Equilibration:
		
		if (counter%PoissonTime) == 0:
			(time, position, velocity,CP,CPVel,Work) = LangevinStationary(time, position, velocity, CP, CPVel, CPVelD)
			InternalTime = InternalTime + dt
			PoissonTime = TimeSeparation

		else:
			(InternalTime, position, velocity,CP,CPVel) = LangevinStationaryNoCP(InternalTime, position, velocity, CP, CPVel)

		counter = counter + 1

	while time < ProtocolTime:

		if (counter%PoissonTime) == 0:
			CPVelOldTrack.append(CPVel)
			(time, position, velocity,CP,CPVel,Work) = LangevinStationary(time, position, velocity, CP, CPVel, CPVelD)
			InternalTime = InternalTime + dt
			PoissonTime = TimeSeparation
			WorkAcc = WorkAcc + Work
			CPVelTrack.append(CPVel)

		else:
			(InternalTime, position, velocity,CP,CPVel) = LangevinStationaryNoCP(InternalTime, position, velocity, CP, CPVel)


		counter = counter + 1

	VarAccLag = 0.0
	VarAcc = 0.0

	for index in range(len(CPVelOldTrack)):
		VarAccLag = VarAccLag + CPVelTrack[index]*CPVelOldTrack[index]
		VarAcc = VarAcc + CPVelTrack[index]*CPVelTrack[index]

	VelVarLag = (VarAccLag/float(len(CPVelOldTrack))) - np.mean(CPVelTrack)*np.mean(CPVelOldTrack)
	VelVar = (VarAcc/float(len(CPVelTrack))) - np.mean(CPVelTrack)*np.mean(CPVelTrack)

	return WorkAcc, VelVar, VelVarLag 				#Put these into Driver routine to calculate variance and other stats



def FrictionPropogator(ProtocolTime,TimeSeparation):

	time = 0
	position = 0
	velocity = 0

	PositionTrack = []

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	InternalTime = 0

	ProtocolTime = ProtocolTime + Equilibration

	PoissonTime = TimeSeparation

	counter = 0

	while time < Equilibration:
		
		if (counter%PoissonTime) == 0:
			(time, position, velocity) = LangevinTrajectory(time, position, velocity)
			InternalTime = InternalTime + dt
			PoissonTime = TimeSeparation

		else:
			(InternalTime, position, velocity) = LangevinTrajectory(InternalTime, position, velocity)

		counter = counter + 1

	while time < ProtocolTime:

		if (counter%PoissonTime) == 0:
			(time, position, velocity) = LangevinTrajectory(time, position, velocity)
			InternalTime = InternalTime + dt
			PoissonTime = TimeSeparation
			PositionTrack.append(position)

		else:
			(InternalTime, position, velocity) = LangevinTrajectory(InternalTime, position, velocity)


		counter = counter + 1


	return PositionTrack 				#Put these into Driver routine to calculate variance and other stats


def VariancePropogator(ProtocolTime):

	time = 0
	position = 0
	velocity = 0

	VelocityTrack = []

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	ProtocolTime = ProtocolTime + Equilibration

	counter = 0

	while time < Equilibration:
		
		(time, position, velocity) = LangevinTrajectory(time, position, velocity)

	while time < ProtocolTime:

		(time, position, velocity) = LangevinTrajectory(time, position, velocity)

		VelocityTrack.append(velocity)

	Variance = np.var(VelocityTrack)

	return Variance










