#This module calcultes the velocity variance of stationary simulations with different kCP values
#
#Steven Large
#January 30th 2017

import WriteData
import os
from math import *
import random
import numpy as np

def VariancePropogator(ProtocolTime,Spring):

	time=0
	position = 0
	velocity = 0

	VelocityTrack = []

	Equilibration = 500 							 			# Number of equilibration steps before taking running averages

	ProtocolTime = ProtocolTime + Equilibration

	counter = 0

	while time < Equilibration:
		
		(time, position, velocity) = LangevinTrajectory(time, position, velocity, Spring)

	while time < ProtocolTime:

		(time, position, velocity) = LangevinTrajectory(time, position, velocity, Spring)

		VelocityTrack.append(velocity)

	Variance = np.var(VelocityTrack)

	return Variance

def ForceConstantVelocity(position,Min,Spring):

	Force = -Spring*(position - Min)

	return Force

def LangevinTrajectory(time,position,velocity,Spring):

	beta = 1
	a = 0.25
	dt = 0.1
	m = 1

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,2) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0,Spring)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0,Spring)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,2)

	return time, position, velocity

SampleTime = 100000

Springs = [100,200,400]
Variance = []

VarPath = 'Variance/'

filename = 'VelocityVariances'

for index in range(len(Springs)):

	print 'Springs --> %d' % Springs[index]

	VelocityVar = VariancePropogator(SampleTime,Springs[index])

	Variance.append(VelocityVar)

CompleteName = os.path.join(VarPath,filename)

file1 = open(CompleteName,'w')
file1.write('kCP\tVariance\n\n')

for index2 in range(len(Springs)):
	file1.write('%d\t%lf\n' % (Springs[index2], Variance[index2]))

file1.close()






