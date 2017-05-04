#TimeDriver For local tests, calculating the total work only
#
#Steven Large
#January 18th 2017

from math import *
import random
import numpy as np
from SmoothParameter import *

#import matplotlib.pyplot as plt

k=1
a=0.95
beta=1

m = 1

dt=0.1

kCP=1
Dist=25
sigma=1

Tau = Smooth*dt

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

	Equilibration = 100 							 			# Number of equilibration steps before taking running averages

	ProtocolTime = ProtocolTime + Equilibration

	VelTrack = [0,0,0,0,0,0,0,0,0,0]

	#print "Entering Equilibration\n\n"

	while time < Equilibration:
		
		(time, position, velocity, CP) = LangevinCPGenerator(time, position, velocity, CP, CPVel,VelTrack)

	PosInit = position
	CPInit = CP

	#print "Entering Data Gathering\n\n"

	while (position-PosInit) < Dist:

		(time, position, velocity, CP) = LangevinCPGenerator(time, position, velocity, CP, CPVel,VelTrack)
		PositionTrack.append(position - PosInit)
		CPTrack.append(CP - CPInit)
		TimeTrack.append(time)

	return TimeTrack,PositionTrack,CPTrack

def LangevinCPGenerator(time, position, velocity, CP, CPVel, VelTrack):

	#velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = VelocitySmoothed(velocity,VelTrack)
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	position = position + 0.5*dt*velocity
		
	VelTrack.insert(0,velocity)
	VelTrack = VelTrack[0:len(VelTrack)-1]

	time += dt

	CP = CP + CPVel*dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	#velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)
	velocity = VelocitySmoothed(velocity,VelTrack)

	VelTrack.insert(0,velocity)
	VelTrack = VelTrack[0:len(VelTrack)-1]

	return time, position, velocity, CP

def ForceConstantVelocity(position, CP):

	F = -k*(position - CP)

	return F

def VelocitySmoothed(velocity,VelTrack):

	Acc = 0.0

	for index in range(len(VelTrack)):

		Acc = Acc + exp(-index*dt/Tau)*(sqrt(a)*VelTrack[index] + sqrt((1-a)/(beta*m))*random.gauss(0,1))*dt

	return Acc/Tau






