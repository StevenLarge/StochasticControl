#This module contains all routines related to calculations of energies and forces as well as work contributions
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

def CalculateWork(CP,CPOld,position):

	E1 = 0.5*float(k)*((position - CPOld)**2)
	E2 = 0.5*float(k)*((position - CP)**2)

	dE = E2 - E1

	return dE


def DeterministicWorkOU(state,time,CPVel):

	x01 = CPVel*time
	x02 = CPVel*(time+dt)

	dE = 0.5*k*(state - x02)**2 - 0.5*k*(state - x01)**2			

	return dE

def StochasticWorkOU(position,CP,CPFluct):

	dE = 0.5*k*(position - CP)**2 - 0.5*k*(position - (CP-CPFluct))**2

	return dE

def WorkConstantVelocity(position,CP,CPVel):

	E1 = 0.5*k*(position - CP)**2

	E2 = 0.5*k*(position - (CP + CPVel*dt))**2

	dE = E2 - E1

	return dE

def CPWorkTotal(CPOld,CP,position):

	E1 = 0.5*k*(position - CPOld)**2
	E2 = 0.5*k*(position - CP)**2
	dE = E2 - E1

	return dE
