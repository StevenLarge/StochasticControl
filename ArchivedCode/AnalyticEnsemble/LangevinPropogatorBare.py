#This module is a stripped down Langevin Propogator Routine
#
#Steven Large
#November 17th 2016

from math import *
import random

beta = 1
a = 0.1	
m = 1
dt = 0.1151 				#Fixed so that gamma = 20 at a = 0.1
TrapStrength = 5

def LangevinNoCP(time, position, velocity, CP, CPVelocity): 					#This routine runs the Langevin dynamics of the system at a FIXED control parameter value

	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	position = position+0.5*dt*velocity
		
	time += dt

	position = position+0.5*dt*velocity 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP

def LangevinCPConstVel(time, position, velocity, CP, CPVelocity): 				#This may be mroe physical in the sense that the control parameter is never truly static, however, the acounting for average velocities and what not may get skewed?

	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	position = position+0.5*dt*velocity
		
	CPOld = CP

	time += dt

	CP = CPOld + CPVelocity*dt

	Work = WorkCalc(position,CP,CPOld)

	position = position+0.5*dt*velocity 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP, Work

def LangevinCPStoch(time, position, velocity, CP, CPVelocity, CPVelD): 			#This routine runs a langevin step in which the control parameter also feels a stochastic kick 
	
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	position = position+0.5*dt*velocity
		
	CPOld = CP

	time += dt

	CP, CPVelocity = LangevinCP(time,CP,CPVelocity,CPVelD)

	Work = WorkCalc(position,CP,CPOld)

	position = position+0.5*dt*velocity 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1)
	
	return time, position, velocity, CP, Work, CPVelocity

def LangevinCP(time,CP,CPVelocity,CPVelD): 										#This routine propogates the Langevin dynamics of the control parameter

	Min = CPVelD*time

	CPVelocity = sqrt(a)*CPVelocity+sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	CPVelocity = CPVelocity+0.5*dt*ForceParticle(CP,Min)/m
	CP = CP+0.5*dt*CPVelocity
		
	time += dt
	
	Min = Min + CPVelD*dt

	CP = CP+0.5*dt*CPVelocity 
	CPVelocity = CPVelocity+0.5*dt*ForceParticle(CP,Min)/m
	CPVelocity = sqrt(a)*CPVelocity+sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return CP,CPVelocity

def LangevinBones(time, position, velocity, CP, CPVelocity):

	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	position = position+0.5*dt*velocity
		
	time += dt

	CP_Old = CP
	CP = CP + CPVelocity*dt

	Work = WorkCalc(position,CP,CP_Old)

	position = position+0.5*dt*velocity 
	velocity = velocity+0.5*dt*ForceParticle(position,CP)/m
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP, Work

def ForceParticle(position,CP):

	Force = -TrapStrength*(position - CP)

	return Force

def WorkCalc(position,CP,CP_Old):

	E1 = 0.5*TrapStrength*(position - CP_Old)**2
	E2 = 0.5*TrapStrength*(position - CP)**2 

	dE = (E2 - E1)

	return dE

