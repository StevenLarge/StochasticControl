#This script calculates the numerical quantities associated with the LangevinSimulation routines
#
#Steven Large
#June 17th 2016

import numpy

def Variance(position,velocity,CP):

	meanPos = numpy.mean(position[0])
	meanVel = numpy.mean(velocity[0])
	meanCP  = numpy.mean(CP[0])

	VarAcc = 0.0

	for k in range(len(position[0])):

		VarAcc = VarAcc + (position[0][k] - meanPos)**2

	varPos = VarAcc/float(len(position[0]))

	VarAcc = 0.0

	for k in range(len(velocity[0])):

		VarAcc = VarAcc + (velocity[0][k] - meanVel)**2

	varVel = VarAcc/float(len(velocity[0]))

	VarAcc = 0.0

	for k in range(len(CP[0])):

		VarAcc = VarAcc + (CP[0][k] - meanCP)**2

	varCP = VarAcc/float(len(CP[0]))

	return varPos, varVel, varCP

