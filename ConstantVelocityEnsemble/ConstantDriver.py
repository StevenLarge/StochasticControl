#This is the driver routine for the constant velocity simualtions
#
#Steven Large
#January 4th 2016

from math import *
from Parameters import *
from LangevinPropogator import *
import random
import numpy

def Propogator(ProtocolTime, VelocityVariance):

	time = 0
	position = 0
	velocity = 0
	WorkAcc = 0

	CP = 0

	PositionTrack = []
	CPTrack = []

	CPVel_MEAN = float(Dist)/float(ProtocolTime)

	CPVel = random.gauss(CPVel_MEAN, sqrt(VelocityVariance))

	Equilibration = 50							 			

	ProtocolTime = ProtocolTime + Equilibration

	while time < Equilibration:

		(time, position, velocity, WorkStep, CP) = LangevinConstantCPVelocity(time, position, velocity, CP, CPVel)

	while time < ProtocolTime:

			(time, position, velocity, WorkStep, CP) = LangevinConstantCPVelocity(time, position, velocity, CP, CPVel)
			WorkAcc = WorkAcc + WorkStep

			CPTrack.append(CP)
			PositionTrack.append(position)

	return WorkAcc, CPVel, PositionTrack, CPTrack

def Propogator2(ProtocolTime,VelocityVariance):

	time = 0
	position = random.gauss(0,float(1)/float(k))
	velocity = 0
	WorkAcc = 0

	CP = 0

	CPVel_MEAN = float(Dist)/float(ProtocolTime)

	CPVel = random.gauss(CPVel_MEAN, sqrt(VelocityVariance))

	while time < ProtocolTime:

			(time, position, velocity, WorkStep, CP) = LangevinConstantCPVelocity(time, position, velocity, CP, CPVel)
			WorkAcc = WorkAcc + WorkStep

	return WorkAcc



