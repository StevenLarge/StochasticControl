#This script generates a langevin trajectory in a stationary potential and then calculates the velocity distribution
#
#Steven Large
#February 9th 2017

from math import *
import random
import numpy as np
import matplotlib.pyplot as plt

def LangevinTrajectory(time,position,velocity,CP,CPVel,k):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP,k)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	CPOld = CP

	CP = CP + CPVel*dt

	WorkStep = CalcWork(position,CPOld,CP)

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP,k)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP, WorkStep

def CalcWork(position,CPOld,CP):

	E1 = 0.5*k*((position - CPOld)**2)
	E2 = 0.5*k*((position - CP)**2)

	dE = E2 - E1

	return dE

def ForceConstantVelocity(position,CP,k):

	F = -k*(position - CP)

	return F

def ReadData(filename):

	file1 = open(filename,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	Track = []

	for index in range(len(data1)-2):

		parsed = data1[index+2].split()
		Time.append(eval(parsed[0]))
		Track.append(eval(parsed[1]))

	return Time, Track


a = 0.25  									# a=1 is no friction limit, a=0 is high friction limit
beta = 1 									# Inverse temperature, kT, is set to 1
m = 1

dt = 0.05					 				# Time step
	
kCP = 4										# Trap strength confining the control parameter
Dist = 10 									# Distance that the control paramter travels
sigma = 1 									# Variance of control parameter velocity fluctuations

SampleTime = 20

CPVel = 5.0

Springs = [1,2,4,8,16,32]
filenames = ['Tracking_1.dat','Tracking_2.dat','Tracking_4.dat','Tracking_8.dat','Tracking_16.dat','Tracking_32.dat']

NumberTrajectories = 100

for index in range(len(Springs)):

	time = 0
	
	TrajectoryTrack = []

	while time < SampleTime:
		TrajectoryTrack.append(0.0)
		time = time +dt

	for index2 in range(NumberTrajectories):

		time = 0
		position = 0
		velocity = 0
		CP = 0

		k = Springs[index]

		counter = 0

		while time < SampleTime:

			(time,position,velocity,CP,Power) = LangevinTrajectory(time,position,velocity,k,CP,CPVel)
			TrajectoryTrack[counter] = TrajectoryTrack[counter] + Power
			counter = counter + 1

	for index4 in range(len(TrajectoryTrack)):
		TrajectoryTrack[index] = TrajectoryTrack[index]/float(NumberTrajectories)

	time = 0

	file1 = open(filenames[index],'w')
	file1.write('Time\tPosition\n\n')
	for index5 in range(len(TrajectoryTrack)):
		time = time + dt
		file1.write('%lf\t%lf\n' % (time,TrajectoryTrack[index5]))
	file1.close()


Time1,Track1 = ReadData(filenames[0])
Time2,Track2 = ReadData(filenames[1])
Time3,Track3 = ReadData(filenames[2])
Time4,Track4 = ReadData(filenames[3])
Time5,Track5 = ReadData(filenames[4])
Time6,Track6 = ReadData(filenames[5])

Plot1 = plt.plot(Time1,Track1,label='k = 1')
Plot2 = plt.plot(Time2,Track2,label='k = 2')
Plot3 = plt.plot(Time3,Track3,label='k = 4')
Plot4 = plt.plot(Time4,Track4,label='k = 8')
Plot5 = plt.plot(Time5,Track5,label='k = 16')
Plot6 = plt.plot(Time6,Track6,label='k = 32')

plt.legend()

plt.xlabel('Time')
plt.ylabel('Difference, CP - position')
plt.title('Comparison of Relaxation for different k values')

plt.savefig('RelaxCompare.png')

plt.show()
plt.close()




