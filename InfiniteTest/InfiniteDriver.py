#This module is the driving routine for the Stochastic Control of a nested OU process, where the time scale 
#separation is taken to be infinite, so the system remains at equilibrium through the entire protocol.
#
#Steven Large
#December 16th 2016

from math import *
from Potential import *
from Parameters import *
from LangevinPropogator import *
import random
import numpy



def Propogator(ProtocolTime):

	time = 0
	WorkAcc = 0

	CPTrack = []

	CP = 0
	CPVel = 0

	CPVelD = float(Dist)/float(ProtocolTime)

	counter = 0

	while time < ProtocolTime:

		(time, WorkStep, CP, CPVel) = LangevinCPInfinite(time, CP, CPVel, CPVelD)
		WorkAcc = WorkAcc + WorkStep

		CPTrack.append(CP)

	return WorkAcc, CPTrack 


