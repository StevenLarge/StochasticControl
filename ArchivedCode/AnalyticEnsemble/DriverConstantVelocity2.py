#This module calcualtes the average work done in driving a harmonic trap at a constant velocity, where the dynamics are governed by a Langevin Equation
#
#Steven Large
#November 17th 2016

from LangevinPropogatorBare import *
from math import *
import numpy

def CalculateWork1(CPVelD,ProtocolTime,TimeDifference):

	Realizations = 100000					#Number of Langevin Trajectories to find the Work

	WorkRealization = []

	for k in range(Realizations):

		WorkAcc = 0

		time = 0 							#Initial Conditions for the particle, where we are assuming that any transient behaviour will not effect the overall outcome significantly.
		position = 0
		velocity = 0

		EqTime = 0
		Equilibration = 100

		CP = 0
		CPVelocity = 0

		counter = 1

		while time < ProtocolTime:

			if EqTime < Equilibration:

				EqTime,position,velocity,CP,CPVelocity,Work = LangevinCPStoch(EqTime,position,velocity,CP,CPVelocity,CPVelD)

			else:

				if(TimeDifference%counter == 0):

					time,position,velocity,CP,CPVelocity,Work = LangevinCPStoch(time,position,velocity,CP,CPVelocity,CPVelD)

				else:
					time,position,velocity,CP,Work = LangevinCPConstVel(time,position,velocity,CP,CPVelocity)

				counter = counter + 1

				WorkAcc = WorkAcc + Work

		WorkRealization.append(WorkAcc)

	AvgWork = sum(WorkRealization)/float(Realizations) 
	VarianceWork = numpy.var(WorkRealization)

	return AvgWork,VarianceWork


def CalculateWork2(CPVelD,ProtocolTime,TimeDifference):

	Realizations = 100000					#Number of Langevin Trajectories to find the Work

	WorkRealization = []

	for k in range(Realizations):

		WorkAcc = 0

		time = 0 							#Initial Conditions for the particle, where we are assuming that any transient behaviour will not effect the overall outcome significantly.
		position = 0
		velocity = 0

		EqTime = 0
		Equilibration = 100

		CP = 0
		CPVelocity = 0

		counter = 1

		while time < ProtocolTime:

			if EqTime < Equilibration:

				EqTime,position,velocity,CP,CPVelocity,Work = LangevinCPStoch(EqTime,position,velocity,CP,CPVelocity,CPVelD)

			else:

				if(TimeDifference%counter == 0):

					time,position,velocity,CP,CPVelocity,Work = LangevinCPStoch(time,position,velocity,CP,CPVelocity,CPVelD)

				else:
					time,position,velocity,CP = LangevinNoCP(time,position,velocity,CP,CPVelocity)

				counter = counter + 1

				WorkAcc = WorkAcc + Work

		WorkRealization.append(WorkAcc)

	AvgWork = sum(WorkRealization)/float(Realizations) 
	VarianceWork = numpy.var(WorkRealization)

	return AvgWork,VarianceWork


