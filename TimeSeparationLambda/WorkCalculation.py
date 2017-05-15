#This module calculates the work associated with time-separated dynamics
#
#Steven Large
#February 15th 2017

import os
import random
from math import *
from Parameters import *
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

def Langevin(time,position,velocity,CP,CPVel): 		#Langevin Integrator

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

def ForceConstantVelocity(position,CP): 			#Calculates the force on a particle for a given control parameter velocity

	F = -k*(position - CP)

	return F

def CalculateWork(CP,CPOld,position): 				#Calculates the work contribution for a particular change in control parameter

	E1 = 0.5*k*((position - CPOld)**2)
	E2 = 0.5*k*((position - CP)**2)
	dE = E2 - E1

	return dE

NumberTrajectories = 100
NumberRepeats = 50
TimeRange = 20

Modifiers = ['a25','a50','a75','a90','a95','a99'] 													#Trajectory distributions with different damping parameters (a)

for MasterIndex in range(len(Modifiers)):

	path = 'Trajectories_' + Modifiers[MasterIndex] + '/' 											#Directory where control parameter trajectories are stored
	WritePath = 'Output/'

	filename_base = 'CP_Trajectory_'
	filename_base_write = 'WorkTotal_' + Modifiers[MasterIndex] + '_k' + str(k) + '.dat'			#Write file for Work calculation

	WorkTot = []
	Tau = []

	for indexOuter in range(TimeRange):

		ProtocolTime = 10 + 5*indexOuter 															#Protocol times for whcih work values are calulated
		filenameInner = filename_base + str(ProtocolTime) + '_'

		WorkTraj = 0

		print 'Protocol Time --> %d' % ProtocolTime

		for indexInner in range(NumberTrajectories):

			filename = filenameInner + str(indexInner) + '.dat' 									#NOTE: There has to be a CP trajectory file with this name
			Time,CP = ReadData(filename,path)

			WorkAcc = 0

			for index3 in range(NumberRepeats):														#Number of repetitions of teh same CP trajectory

				WorkTemp = WorkPropogator(CPVel) 													#Calculate the work associated with a realzation of the protocol
				WorkAcc = WorkAcc + WorkTemp

			WorkTraj = WorkTraj + WorkAcc/float(NumberRepeats) 										#Work for particular protocol, averaged over the number of repetitions

		WorkTot.append(float(WorkTraj)/float(NumberTrajectories)) 									#Average work over different realizations of protocol as well
		Tau.append(ProtocolTime)

	WriteData(filename_base_write,WritePath,WorkTot,Tau) 											#Write work vs. protocol time data to file.


