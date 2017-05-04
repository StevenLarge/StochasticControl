#This script generates a langevin trajectory in a stationary potential and then calculates the velocity distribution
#
#Steven Large
#February 9th 2017

from math import *
import random
import numpy as np
import matplotlib.pyplot as plt

def LangevinTrajectory(time,position,velocity,CP,CPVel,CPVelD):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	CPOld = CP

	CP,CPVel = LangevinCP(time,CP,CPVel,CPVelD)

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP, CPVel

def LangevinCP(time,position,velocity,CPVelD):

	Min = CPVelD*time

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,Min)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	Min = CPVelD*time

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,Min)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return position, velocity

def ForceConstantVelocity(position,CP):

	F = -k*(position - CP)

	return F


k = 0.1
a = 0.25  									# a=1 is no friction limit, a=0 is high friction limit
beta = 1 									# Inverse temperature, kT, is set to 1
m = 1

dt = 0.1					 				# Time step
	
kCP = 4										# Trap strength confining the control parameter
Dist = 100 									# Distance that the control paramter travels
sigma = 1 									# Variance of control parameter velocity fluctuations

SampleTime = 1000

CPVelD = float(Dist)/float(SampleTime)

time = 0
position = 0
velocity = 0
CP = 0
CPVel = 0

PositionTrack = []
CPTrack = []
TimeTrack = []

while time < SampleTime:

	(time,position,velocity,CP,CPVel) = LangevinTrajectory(time,position,velocity,CP,CPVel,CPVelD)
	PositionTrack.append(position)
	CPTrack.append(CP)
	TimeTrack.append(time)

file1 = open('Tracking.dat','w')
file1.write('Time\tPosition\tCP\n\n')
for index in range(len(PositionTrack)):
	file1.write('%lf\t%lf\t%lf\n' % (TimeTrack[index],PositionTrack[index],CPTrack[index]))
file1.close()





