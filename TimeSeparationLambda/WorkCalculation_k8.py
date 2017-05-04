#This module calculates the work associated with time-separated dynamics
#
#Steven Large
#February 15th 2017

import os
import random
from math import *
from Parameters8 import *
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
		#PositionTrack.append(position)
		#CPTrack.append(CP)

	return WorkAcc#, PositionTrack#, CPTrack

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

NumberTrajectories = 50
NumberRepeats = 10
TimeRange = 20

path = 'Trajectories_Smooth_a25/'
WritePath = 'Output/'

filename_base = 'CP_Trajectory_'
filename_base_write = 'WorkTotal' + '_k' + str(k) + '.dat'

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

		CPVel = []

		for index1 in range(len(CP)-1):
			CPVel.append(float(CP[index1+1]-CP[index1])/float(dt))

		WorkAcc = 0

		for index3 in range(NumberRepeats):

			WorkTemp = WorkPropogator(CPVel)
			WorkAcc = WorkAcc + WorkTemp

		WorkTraj = WorkTraj + WorkAcc/float(NumberRepeats)

	WorkTot.append(float(WorkTraj)/float(NumberTrajectories))
	Tau.append(ProtocolTime)

WriteData(filename_base_write,WritePath,WorkTot,Tau)


