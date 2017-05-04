#Thie module contains the Langevin propogator routines for the work variance calculations
#
#Steven Large
#January 17th 2017

from math import *
import random
from Parameters import *

def Langevin(time,position,velocity,CP,CPVelocity):

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

	return time, position, velocity, Work, CP


def ForceParticle(position,CP):

	F = -k*(position - CP)

	return F


def WorkCalc(position, CP, CPOld):

	E1 = 0.5*k*((position - CPOld)**2)
	E2 = 0.5*k*((position - CP)**2)

	dE = E2 - E1

	return dE
