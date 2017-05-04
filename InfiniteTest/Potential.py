#This module contains all routines related to calcualtions of energies and forces as well as work contributions
#
#Steven Large
#June 21st 2016

from math import *
from Parameters import *
import random

def ForceOU(position, x0):

	F = -k*(position - x0)

	return F

def ForceOUCP(position, x0):

	F = -kCP*(position - x0)

	return F

def ForceConstantVelocity(position, CP):

	F = -k*(position - CP)

	return F


def InfiniteWorkOU(OldMin,NewMin): 									#Calculates the work required by the controller to move the equilibrium distributions

	dE = 0.5*k*(NewMin - OldMin)**2

	return dE

def DeterministicWorkOU(state,time,CPVel):

	x01 = CPVel*time
	x02 = CPVel*(time+dt)

	dE = 0.5*k*(state - x02)**2 - 0.5*k*(state - x01)**2			#Extra Factor accounts for distance over which force is being applied.

	return dE

def StochasticWorkOU(position,CP,CPFluct):

	dE = 0.5*k*(position - CP)**2 - 0.5*k*(position - (CP-CPFluct))**2

	return dE

def StochasticWorkOU2(Force,velocity):

	StochWork = Force*velocity*dt;
	
	return StochWork
	
def StochasticWork2(CP, TrapPosition):						#New iteration calculates the work done by the CP trap, or the instantaneous energy input from teh CP trap configuration

	Energy = kCP*(CP - TrapPosition)**2 		   			#Note this is the same as a work, where we take the work to be a force times a distance, the force is kCP*(x - TrapPosition) and the distance it is applied over is ~kCP*(x - TrapPostion)*dt^2 

	Energy = Energy*dt*dt

	return Energy

def StochasticWork3(CP,TrapPosition,position):

	Energy = k*(CP - position)**2

	return Energy

def WorkGeneral(CP,Min,MinOld):

	dE = kCP*(Min - CP)**2 - kCP*(MinOld - CP)**2

	return dE

def WorkConstantVelocity(position,CP,CPVel):

	E1 = 0.5*k*(position - CP)**2

	E2 = 0.5*k*(position - (CP + CPVel*dt))**2

	dE = E2 - E1

	return dE

