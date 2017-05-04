#This module contains all routines related to calcualtions of energies and forces as well as work contributions
#
#Steven Large
#June 21st 2016

from math import *
from Parameters import *
import random

def ForceConstantVelocity(position, CP):

	F = -k*(position - CP)

	return F

def WorkConstantVelocity(position,CP,CPVel):

	E1 = 0.5*k*((position - CP)*(position - CP))

	E2 = 0.5*k*((position - (CP + CPVel*dt))*(position - (CP + CPVel*dt)))

	dE = (E2 - E1)

	return dE

