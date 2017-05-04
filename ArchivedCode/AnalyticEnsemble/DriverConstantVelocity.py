#This module calcualtes the average work done in driving a harmonic trap at a constant velocity, where the dynamics are governed by a Langevin Equation
#
#Steven Large
#November 17th 2016

from LangevinPropogatorBare import *
from math import *
import numpy

def CalculateWork(CPVelocity,ProtocolTime):

	Realizations = 100000				#Number of Langevin Trajectories to find the Work

	WorkRealization = []

	for k in range(Realizations):

		#PositionTrack = []
		#VelocityTrack = []
		#CPTrack = []
		WorkAcc = 0

		time = 0 							#Initial Conditions for the particle, where we are assuming that any transient behaviour will not effect the overall outcome significantly.
		position = 0
		velocity = 0

		EqTime = 0
		Equilibration = 100

		CP = 0

		while time < ProtocolTime:

			if EqTime < Equilibration:

				EqTime,position,velocity,CP,Work = LangevinBones(EqTime,position,velocity,CP,CPVelocity)

			else:

				time,position,velocity,CP,Work = LangevinBones(time,position,velocity,CP,CPVelocity)

				WorkAcc = WorkAcc + Work
				#PositionTrack.append(position)
				#VelocityTrack.append(velocity)
				#CPTrack.append(CP)

		WorkRealization.append(WorkAcc)

	AvgWork = sum(WorkRealization)/float(Realizations) 
	VarianceWork = numpy.var(WorkRealization)

	return AvgWork,VarianceWork


def CalcualteStochasticWork(CPVelocityDet,ProtocolTime):


	Realizations = 100000				#Number of Langevin Trajectories to find the Work

	WorkRealization = []

	for k in range(Realizations):

		#PositionTrack = []
		#VelocityTrack = []
		#CPTrack = []
		WorkAcc = 0

		time = 0 							#Initial Conditions for the particle, where we are assuming that any transient behaviour will not effect the overall outcome significantly.
		DummyTime = 0
		position = 0
		velocity = 0

		EqTime = 0
		Equilibration = 100

		CP = 0

		CPCounter = 0

		counter = 0

		while time < ProtocolTime:

			#Poiss = numpy.random.poisson(TimeDifference)

			if EqTime < Equilibration:

				EqTime,position,velocity,CP,Work = LangevinBones(EqTime,position,velocity,CP,CPVelocity)

			else:

				if (counter%TimeDifference == 0):

					time,position,velocity,CP,Work = LangevinBones(time,position,velocity,CP,CPVelocity)

				else:
					DummyTime,position,velocity,CP = LangevinNoCP(DummyTime,position,velocity,CP,CPVelocity)


				WorkAcc = WorkAcc + Work
				#PositionTrack.append(position)
				#VelocityTrack.append(velocity)
				#CPTrack.append(CP)

		WorkRealization.append(WorkAcc)

	AvgWork = sum(WorkRealization)/float(Realizations) 
	VarianceWork = numpy.var(WorkRealization)

	return AvgWork,VarianceWork



