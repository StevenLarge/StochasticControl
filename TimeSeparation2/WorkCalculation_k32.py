#This module calculates the work associated with time-separated dynamics
#
#Steven Large
#February 15th 2017

import os
import random
from math import *
#from TimeParameters import *
import numpy as np

#import matplotlib.pyplot as plt

def ReadData(filename,path):

	CompleteName = os.path.join(path,filename)

	file1 = open(CompleteName,'r')
	data1 = file1.readlines()
	file1.close()

	Time = []
	CP = []

	for index in range(len(data1)):
		
		parsed = data1[index].split()

		Time.append(eval(parsed[0]))
		CP.append(eval(parsed[1]))

	return Time,CP

def WriteData(filename,path,Work,Time):

	CompleteName = os.path.join(path,filename)

	file1 = open(CompleteName,'w')
	file1.write('Time\tWork\n\n')

	for index in range(len(Work)):
		file1.write('%lf\t%lf\n' % (Time[index],Work[index]))

	file1.close()

def WorkPropogator(CPVel):

	Equilibration = 500

	time = 0
	position = 0
	velocity = 0
	CP = 0

	WorkAcc = 0
	PositionTrack = []
	CPTrack = []

	EqVel = np.mean(CPVel)

	while time < Equilibration:

		(time,position,velocity,CP,Work) = Langevin(time,position,velocity,CP,EqVel)
		#PositionTrack.append(position)
		#CPTrack.append(CP)

	for index in range(len(CPVel)):

		(time,position,velocity,CP,Work) = Langevin(time,position,velocity,CP,CPVel[index])
		WorkAcc = WorkAcc + Work
		PositionTrack.append(position)
		#CPTrack.append(CP)

	return WorkAcc, PositionTrack#, CPTrack

def Langevin(time,position,velocity,CP,CPVel):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	CPOld = CP

	CP = CP + CPVel*dt

	Work = CalculateWork(CP,CPOld,position)

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time,position,velocity,CP,Work

def ForceConstantVelocity(position,CP):

	F = -k*(position - CP)

	return F

def CalculateWork(CP,CPOld,position):

	E1 = 0.5*k*((position - CPOld)**2)
	E2 = 0.5*k*((position - CP)**2)
	dE = E2 - E1

	return dE

k = 32
beta = 1
m = 1
dt=0.1
a = 0.25

#a = exp(log(0.25)/float(TimeSeparation))			#New a value so that the friction remains constant

NumberTrajectories = 100
NumberRepeats = 50
TimeRange = 20

path = 'Trajectories/'
WritePath = 'Output/'

filename_base = 'CP_Trajectory_'
filename_base_write = 'WorkTotal_k32.dat'

WorkTot = []
Tau = []

for indexOuter in range(TimeRange):

	ProtocolTime = 10 + 5*indexOuter

	filenameInner = filename_base + str(ProtocolTime) + '_'

	WorkTraj = 0

	#print 'Protocol Time --> %d' % ProtocolTime

	for indexInner in range(NumberTrajectories):

		filename = filenameInner + str(indexInner) + '.dat'

		Time,CP = ReadData(filename,path)

		#plt.plot(Time,CP)
		#plt.show()
		#plt.close()

		CPVel = []
		CPTrack = []
		TimeMod = []

		#EffectiveLength = int(floor(len(CP)/TimeSeparation))

		#print 'CP Length --> %d\n' % len(CP)
		#print 'Reduced Length --> %d\n' % EffectiveLength

		#for index in range(len(CP)):
		#	CP[index] = TimeSeparation*CP[index]

		#plt.plot(Time,CP)
		#plt.show()
		#plt.close()

		counter = 0

		for index1 in range(len(CP)-1):
			#for index2 in range(TimeSeparation):
			CPVel.append(float(CP[index1+1]-CP[index1])/float(dt))
				#CPTrack.append(CP[index1])
			#TimeMod.append(Time[counter])
			#counter = counter + 1

		#plt.plot(CPVel)
		#plt.show()
		#plt.close()

		WorkAcc = 0

		for index3 in range(NumberRepeats):

			WorkTemp, PositionTrack = WorkPropogator(CPVel)

			WorkAcc = WorkAcc + WorkTemp

		WorkTraj = WorkTraj + WorkAcc/float(NumberRepeats)

#		Plot1 = plt.plot(PositionTrack,label='Position')
#		Plot2 = plt.plot(CPTrack,label='CP')
#		plt.legend()
#		plt.show()
#		plt.close()

	WorkTot.append(float(WorkTraj)/float(NumberTrajectories))
	Tau.append(ProtocolTime)

WriteData(filename_base_write,WritePath,WorkTot,Tau)

#plt.plot(Tau,WorkTot)
#plt.show()
#lt.close()


