#This module contains all of the parameters necessary to perform Langevin simulations
#
#Steven Large
#June 21st 2016


k = 1 										# Harmonic trap strength confining system
a = 0.25  									# a=1 is no friction limit, a=0 is high friction limit
beta = 1 									# Inverse temperature, kT, is set to 1
m = 1

dt = 0.1					 				# Time step
	
kCP = 4 									# Trap strength confining teh control parameter
Dist = 75 									# Distance that the control paramter travels
sigma = 1 									# Variance of control parameter velocity fluctuations



