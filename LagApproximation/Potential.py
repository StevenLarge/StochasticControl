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

def CPWorkTotal(CPOld,CP,position):

	E1 = 0.5*k*(position - CPOld)**2
	E2 = 0.5*k*(position - CP)**2
	dE = E2 - E1

	return dE
