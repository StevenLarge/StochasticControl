#This module is the main driving routine for the work variance simulations
#
#Steven Large
#January 17th 2017

from Parameters import *
import LangevinPropogator

def Propogator(ProtocolTime):

	CPVel = float(Dist)/float(ProtocolTime)

	Equilibration = 500

	ProtocolTime = ProtocolTime + Equilibration

	time = 0
	position = 0
	velocity = 0
	CP = 0

	while time < Equilibration:

		(time,position,velocity,Work,CP) = LangevinPropogator.Langevin(time,position,velocity,CP,CPVel)

	WorkAcc = 0

	while time < ProtocolTime:

		(time,position,velocity,Work,CP) = LangevinPropogator.Langevin(time,position,velocity,CP,CPVel)
		WorkAcc = WorkAcc + Work

	return WorkAcc


