#This module contains the Langevin integrator algorithm
#
#Steven Large
#June 21st 2016

from math import *
import Potential
from Parameters import *
import random

def LangevinCP(time, CPVel, CP, CPVelD):

	Min = time*CPVelD

	Init = CP

	CPVel = sqrt(aCP)*CPVel + sqrt((1-aCP)/(beta*mCP))*random.gauss(0,1) 
	CPVel = CPVel + 0.5*dt*ForceOUCP(CP,Min)/mCP
	CP = CP + 0.5*dt*CPVel
		
	time += dt

	MinOld = Min

	Min = time*CPVelD

	CP = CP + 0.5*dt*CPVel 

	CPVel = CPVel + 0.5*dt*ForceOUCP(CP,Min)/mCP
	CPVel = sqrt(aCP)*CPVel + sqrt((1-aCP)/(beta*mCP))*random.gauss(0,1)

	Deter = dt*CPVelD

	Stoch = (CP - Init) - Deter

	return CP, Stoch, CPVel, Min


def Langevin(time, position, velocity, CP, sigma, CPVel, CPVelD): 									#Uses equation 3 in Phys.Rev.X. 3, 2013, Sivak et al. 

	velocity1 = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity1 + 0.5*dt*ForceOU(position,CP)/m
	
	DeltaV = velocity - velocity1
	
	Force = ForceOU(position,CP)
	
	position = position + 0.5*dt*velocity
																					
	StepWork = DeterministicWorkOU(position, time, CPVelD)	 									#Calculate the deterministic contribution to the work

	time += dt

	CP, CPFluct, CPVel, TrapPosition = LangevinCP(time, CPVel, sigma, CP, CPVelD) 								#Langevin update to control paramter position

	position = position + 0.5*dt*velocity

	StochasticWork1 = StochasticWorkOU(position,CP,CPFluct)

	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)
	
	return time, position, velocity, StepWork, StochasticWork1, StochasticWork2, CP, CPVel 			


def LangevinConstantVelocity(time,position,velocity,CP,CPVel):

	position = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	Work = WorkConstantVelocity(position,CP,CPVel)

	CP = time*CPVel

	position = position + 0.5*dt*velocity 

	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, Work, CP

def LangevinCPGenerator(time, position, velocity, CP, CPVel):

	position = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*Potential.ForceConstantVelocity(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	CP = time*CPVel

	position = position + 0.5*dt*velocity 

	velocity = velocity + 0.5*dt*Potential.ForceConstantVelocity(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP

def LangevinNoCPChange(time, position, velocity, CP, CPVel, CPVelD): 									#Uses equation 3 in Phys.Rev.X. 3, 2013, Sivak et al. 

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m
	
	Force = ForceOU(position,CP)
	
	position = position + 0.5*dt*velocity

	time += dt

	position = position + 0.5*dt*velocity

	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)
	
	return time, position, velocity 			

def LangevinCPChange(time, position, velocity, CP, CPVel, CPVelD): 				#Uses equation 3 in Phys.Rev.X. 3, 2013, Sivak et al. 

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m

	Force = ForceOU(position,CP)
	
	position = position + 0.5*dt*velocity
																					
	StepWork = DeterministicWorkOU(position, time, CPVelD)	 					#Calculate the deterministic contribution to the work

	time += dt

	CP, CPFluct, CPVel, TrapPosition = LangevinCP(time, CPVel, CP, CPVelD) 		#Langevin update to control paramter position

	position = position + 0.5*dt*velocity

	StochasticWork = StochasticWorkOU(position,CP,CPFluct)

	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)
	
	return time, position, velocity, StepWork, StochasticWork, CP, CPVel 			


def LangevinCPChangeLocal(time, position, velocity, CP, CPVel, CPVelD):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m

	Force = ForceOU(position,CP)
	
	position = position + 0.5*dt*velocity
																					
	time += dt

	CPOld = CP

	CP, CPFluct, CPVel, TrapPosition = LangevinCP(time, CPVel, CP, CPVelD) 		#Langevin update to control paramter position

	Work = CPWorkTotal(CPOld,CP,position)

	position = position + 0.5*dt*velocity
	velocity = velocity + 0.5*dt*ForceOU(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)
	
	return time, position, velocity, Work, CP, CPVel

def LangevinTrajectoryCP(time,position,velocity,CPVelD):

	Min = CPVelD*time

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*mCP))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*Potential.ForceOUCP(position,Min)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	Min = CPVelD*time

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*Potential.ForceOUCP(position,Min)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*mCP))*random.gauss(0,1)

	return position, velocity

def LangevinStationary(time, position, velocity, CP, CPVel, CPVelD, InnerDT):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*InnerDT*Potential.ForceOU(position,CP)/m
	position = position + 0.5*InnerDT*velocity
		
	time += dt

	CPOld = CP

	CP,CPVel = LangevinTrajectoryCP(time,CP,CPVel,CPVelD)

	CPNew = CPOld + CPVel*InnerDT

	Work = Potential.CalculateWork(CPNew,CPOld,position)

	position = position + 0.5*InnerDT*velocity 
	velocity = velocity + 0.5*InnerDT*Potential.ForceOU(position,CPNew)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP, CPNew, CPVel, Work

def LangevinStationaryNoCP(InternalTime, position, velocity, CP, CPVel, InnerDT):
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*InnerDT*Potential.ForceOU(position,CP)/m
	position = position + 0.5*InnerDT*velocity
		
	InternalTime += InnerDT

	CPOld = CP

	CP = CPOld + CPVel*InnerDT

	Work = Potential.CalculateWork(CP,CPOld,position)

	position = position + 0.5*InnerDT*velocity 
	velocity = velocity + 0.5*InnerDT*Potential.ForceOU(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return InternalTime, position, velocity, CP, CPVel, Work


def LangevinTrajectory(time,position,velocity):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity

def LangevinTrajectoryCPFric(time,position,velocity):

	velocity = sqrt(aCP)*velocity + sqrt((1-aCP)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*ForceConstantVelocity(position,0)/m
	velocity = sqrt(aCP)*velocity + sqrt((1-aCP)/(beta*m))*random.gauss(0,1)

	return time, position, velocity
