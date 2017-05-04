#This module contains all of the Driving routines for the realization of a Stochastic control protocol
#
#Steven Large
#June 21st 2016

from math import *
from Potential import *
from Parameters import *
from LangevinPropogator import *
import random
import numpy

def Propogator(ProtocolTime):

	time = 0
	position = 0
	velocity = 0
	WorkAccD = 0
	WorkAccS = 0

	TimeSeparation = 10

	PositionTrack = []
	CPTrack = []
	VelocityTrack = []

	CP = 0
	CPVel = 0

	CPVelD = float(Dist)/float(ProtocolTime)

#	Equilibration = 10000 							 			# Number of equilibration steps before taking running averages

#	while time < Equilibration:

#		(time, position, velocity, WorkStep, WorkS, CP, CPVel) = Langevin(time, position, velocity, CP, sigma, CPVel, CPVelD)

#	position = position - CPVelD*Equilibration
#	CP = CP - CPVelD*Equilibration

#	time = 0

	counter = 0

	while time < ProtocolTime:

		if (counter%TimeSeparation) == 0:
			(time, position, velocity, WorkStep, WorkS, CP, CPVel) = LangevinCPChange(time, position, velocity, CP, sigma, CPVel, CPVelD)
			WorkAccD = WorkAccD + WorkStep
			WorkAccS = WorkAccS + WorkS

		else:
			(time, position, velocity) = LangevinNoCPChange(time, position, velocity, CP, sigma, CPVel, CPVelD)

		PositionTrack.append(position)
		VelocityTrack.append(velocity)
		CPTrack.append(CP)

		counter = counter + 1

	return WorkAccD, WorkAccS, PositionTrack, VelocityTrack, CPTrack 				#Put these into Driver routine to calcualte variance and other stats


def PropogatorConstantVelocity(ProtocolTime,VelocityVariance):

	time = 0
	position = 0
	velocity = 0
	WorkAcc  = 0
	
	PositionTrack = []
	CPTrack = []
	VelocityTrack = []

	CP = 0

	AvgVel = float(Dist)/float(ProtocolTime)

	CPVel = abs(numpy.random.normal(loc=AvgVel, scale=sqrt(VelocityVariance)))		#Generates an actual velocity which is drawn from a Gaussian distributed selection around the


#	Equilibration = 10000 							 								#Number of equilibration steps before taking running averages

#	while time < Equilibration:

#		(time, position, velocity, Work, CP) = LangevinConstantVelocity(time, position, velocity, CP, CPVel)

#	position = position - CPVel*Equilibration
#	CP = CP - CPVel*Equilibration

#	time = 0
	
	while time < ProtocolTime:

		(time, position, velocity, Work, CP) = LangevinConstantVelocity(time, position, velocity, CP, CPVel)

		WorkAcc = WorkAcc + Work

		PositionTrack.append(position)
		VelocityTrack.append(velocity)
		CPTrack.append(CP)

	return WorkAcc, PositionTrack, VelocityTrack, CPTrack




