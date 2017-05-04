#This module calculates the deterministic prediction for the excess work
#
#Steven Large
#January 22nd 2016

from Parameters import *
from TimeParameters import *
import math

def CalculateDeterministicWork(ProtocolTime):

	friction = 12/float(TimeSeparation)

	DeterministicWork = friction*Dist*Dist/float(ProtocolTime)

	return DeterministicWork

def CalculateStochasticWork(ProtocolTime,VelVar):

	friction = 12/float(TimeSeparation)

	StochasticWork = math.sqrt(friction*VelVar)*ProtocolTime

	return StochasticWork



