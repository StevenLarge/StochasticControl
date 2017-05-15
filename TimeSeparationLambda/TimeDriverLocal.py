#TimeDriver For local tests, calculating the total work only
#
#Steven Large
#January 18th 2017

from math import *
import random
import numpy as np
from DampingParameter import *
from dLambdaParameter import *


k=1
beta=1

m = 1

dt=0.1

kCP=1
sigma=1

def CPPropogator(ProtocolTime):

	time = 0
	position = 0
	velocity = 0

	PositionTrack = []
	TimeTrack = []
	CPTrack = []
	VelocityTrack = []

	CP = 0
	CPVel = float(Dist)/float(ProtocolTime) 					#This is the effective deterministic velocity of the control parameter

	Equilibration = 500 							 			#Number of equilibration steps before taking running averages

	ProtocolTime = ProtocolTime + Equilibration

	while time < Equilibration:
		
		(time, position, velocity, CP) = LangevinCPGenerator(time, position, velocity, CP, CPVel)

	PosInit = position
	CPInit = CP

	while (position-PosInit) < Dist:

		(time, position, velocity, CP) = LangevinCPGenerator(time, position, velocity, CP, CPVel)
		PositionTrack.append(position - PosInit)
		CPTrack.append(CP - CPInit)
		TimeTrack.append(time)

	return TimeTrack,PositionTrack,CPTrack

def LangevinCPGenerator(time, position, velocity, CP, CPVel):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	CP = CP + CPVel*dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP

def ForceConstantVelocity(position, CP):

	F = -k*(position - CP)

	return F

