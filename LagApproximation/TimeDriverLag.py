#This is the Time Driver that calculates the lag-time theoretical predictions from the theory of Stochastic Control
#
#Steven Large
#January 18th 2017


#This module contains all of the Driving routines for the realization of a Stochastic control protocol
#
#Steven Large
#December 17th 2017

from math import *
from Potential import *
from Parameters import *
from LangevinPropogator import *
import random
import numpy

import matplotlib.pyplot as plt

def Propogator(ProtocolTime):

	friction = 12

	time = 0
	position = 0
	velocity = 0
	WorkAcc = 0
	WorkAccTheory = 0
	WorkAccTheoryOld = 0
	WorkAccTheory2 = 0

	CP = 0
	CPVel = 0

	CPVelD = float(Dist)/float(ProtocolTime)

	Equilibration = 100 							 			# Number of equilibration steps before taking running averages

	ProtocolTime = ProtocolTime + Equilibration

	while time < Equilibration:
		
		(time, position, velocity, CP, CPVel, WorkStep) = Langevin(time, position, velocity, CP, CPVel, CPVelD)

	while time < ProtocolTime:

		CPVelOld = CPVel
		(time, position, velocity, CP, CPVel, WorkStep) = Langevin(time, position, velocity, CP, CPVel, CPVelD)

		WorkAcc = WorkAcc + WorkStep

		WorkTheory = float(friction)*(CPVelD*CPVelD + (CPVel-CPVelD)*(CPVelOld-CPVelD))*dt
		WorkAccTheory = WorkAccTheory + WorkTheory

#		WorkTheory = float(friction)*dCP*dCP_Old
#		WorkAccTheory = WorkAccTheory + WorkTheory

#		WorkTheoryOld = float(friction)*dCP*abs(dCP)
#		WorkAccTheoryOld = WorkAccTheoryOld + WorkTheoryOld

#		WorkTheory2 = float(friction)*CPVel*abs(CPVel)
#		WorkAccTheory2 = WorkAccTheory2 + WorkTheory2

	return WorkAcc, WorkAccTheory 								#Put these into Driver routine to calculate variance and other stats






