#TimeDriver For local tests, calculating the total work only
#
#Steven Large
#January 18th 2017


from math import *
from Potential import *
from Parameters import *
import LangevinPropogator
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
	CPInner = 0
	CPVel = 0
	CPVelD = float(Dist)/float(ProtocolTime) 	# This is the effective deterministic velocity of the control parameter

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	InternalTime = 0

	ProtocolTime = ProtocolTime + Equilibration

	PoissonTime = np.random.poisson(TimeSeparation)+1

	InnerDT = dt/float(PoissonTime)

	counter = 1

	while time < Equilibration:
		
		if (counter%PoissonTime) == 0:
#			PoissonTime = np.random.poisson(TimeSeparation)+1
			PoissonTime = TimeSeparation
			InnerDT = dt/float(PoissonTime)
			(time, position, velocity, CP, CPInner, CPVel, Work) = LangevinPropogator.LangevinStationary(time, position, velocity, CP, CPVel, CPVelD, InnerDT)
			InternalTime = InternalTime + InnerDT
			counter = 1

		else:
			(InternalTime, position, velocity, CPInner, CPVel, Work) = LangevinPropogator.LangevinStationaryNoCP(InternalTime, position, velocity, CPInner, CPVel, InnerDT)

		counter = counter + 1

	CPInit = CP

	while time < ProtocolTime:

		if (counter%PoissonTime) == 0:
#			PoissonTime = np.random.poisson(TimeSeparation)+1
			PoissonTime = TimeSeparation
			InnerDT = dt/float(PoissonTime)
			(time, position, velocity, CP, CPInner, CPVel, Work) = LangevinPropogator.LangevinStationary(time, position, velocity, CP, CPVel, CPVelD, InnerDT)
			counter = 1
			InternalTime = InternalTime + InnerDT
			WorkAcc = WorkAcc + Work
			CPVelTrack.append(CPVel)

		else:
			(InternalTime, position, velocity, CPInner, CPVel, Work) = LangevinPropogator.LangevinStationaryNoCP(InternalTime, position, velocity, CPInner, CPVel, InnerDT)
			WorkAcc = WorkAcc + Work

		counter = counter + 1

	CPDiff = CP - CPInit

	VarAcc = 0.0

	for index in range(len(CPVelTrack)):
		VarAcc = VarAcc + CPVelTrack[index]*CPVelTrack[index]

	VelVar = (VarAcc/float(len(CPVelTrack))) - np.mean(CPVelTrack)*np.mean(CPVelTrack)

	return WorkAcc, VelVar			#Put these into Driver routine to calculate variance and other stats



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


def FrictionPropogatorCP(ProtocolTime,TimeSeparation):

	time = 0
	position = 0
	velocity = 0

	PositionTrack = []

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	ProtocolTime = ProtocolTime + Equilibration

	while time < Equilibration:
		
		(time, position, velocity) = LangevinTrajectoryCPFric(time, position, velocity)
		
	while time < ProtocolTime:

		(time, position, velocity) = LangevinTrajectoryCPFric(time, position, velocity)
		PositionTrack.append(position)

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










