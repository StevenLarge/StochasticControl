#This module contains the Langevin integrator algorithm
#
#Steven Large
#June 21st 2016

from math import *
from Potential import *
from Parameters import *

def LangevinCP(time, CPVel, CP, CPVelD):

	Min = time*CPVelD

	Init = CP

	CPVel = sqrt(a)*CPVel + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	CPVel = CPVel + 0.5*dt*ForceOUCP(CP,Min)/m
	CP = CP + 0.5*dt*CPVel
		
	time += dt

	MinOld = Min

	Min = time*CPVelD

	CP = CP + 0.5*dt*CPVel 

	CPVel = CPVel + 0.5*dt*ForceOUCP(CP,Min)/m
	CPVel = sqrt(a)*CPVel + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	Deter = dt*CPVelD

	Stoch = (CP - Init) - Deter

	return CP, Stoch, CPVel, Min

def Langevin(time, position, velocity, CP, CPVel, CPVelD):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m

	Force = ForceOU(position,CP)
	
	position = position + 0.5*dt*velocity
																					
	time += dt

	CPOld = CP

	CP, CPFluct, CPVel, TrapPosition = LangevinCP(time, CPVel, CP, CPVelD) 		#Langevin update to control paramter position

	WorkStep = CPWorkTotal(CPOld,CP,position)

	position = position + 0.5*dt*velocity

	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)
	
	return time, position, velocity, CP, CPVel, WorkStep

