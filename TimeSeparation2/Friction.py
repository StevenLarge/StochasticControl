from math import *
import numpy as np
import random
import os

import matplotlib.pyplot as plt

def Langevin(time,position,velocity):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time,position,velocity

def ForceConstantVelocity(position,CP):

	F = -k*(position - CP)

	return F

def Correlation(Trajectory,CP_dt):

	MAXLAG = 750

	timer = 0

	AutoCorr = []
	LagTime = []

	for index1 in range(MAXLAG):

		AutoCorr.append(0.0)
		LagTime.append(timer)

		timer = timer + CP_dt

		for index2 in range(len(Trajectory)-index1):

			AutoCorr[index1] = AutoCorr[index1] + Trajectory[index2]*Trajectory[index2+index1]

		AutoCorr[index1] = AutoCorr[index1]/float(len(Trajectory)-index1)

	Friction = 0

	for index3 in range(len(AutoCorr)):
		Friction = Friction + AutoCorr[index3]*CP_dt

	return Friction,AutoCorr, LagTime

k = 16
beta = 1
m = 1
dt=0.1
a = 0.25

#a = exp(log(0.25)/float(TimeSeparation))			#New a value so that the friction remains constant

WritePath = 'AutoCorrelation/'

filename_write = 'Correlation_95.dat'

SampleTime = 10000

time = 0
position = 0
velocity = 0 

Tracker = []
TimeTrack = []

#Equilibration = 500

#while time < Equilibration:

#	(time,position,velocity) = Langevin(time,position,velocity)

#time = 0

while time < SampleTime:

	(time,position,velocity) = Langevin(time,position,velocity)
	Tracker.append(position)
	TimeTrack.append(time)

CP_dt = TimeTrack[1]-TimeTrack[0]

plt.plot(TimeTrack,Tracker)
plt.show()
plt.close()

Friction, AutoCorr, LagTime = Correlation(Tracker,CP_dt)

CompleteName = os.path.join(WritePath,filename_write)

file1 = open(CompleteName,'w')
file1.write('Lag Time\tAutoCorrelation\n\n')

for index in range(len(AutoCorr)):
	file1.write('%lf\t%lf\n' % (LagTime[index],AutoCorr[index]))
file1.close()


plt.plot(LagTime,AutoCorr)
plt.show()
plt.close()

print '\n\nFriction --> %lf\n\n' % Friction

