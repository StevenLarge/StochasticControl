#This is the primary module for calculating the friction in Time Separation Simualtions
#
#Steven Large
#January 23th 2017

import TimeDriverLocal
from Parameters import *
import WriteData
import FrictionCalculation
import os
from TimeParameters import *

SampleTime = 100000

path = 'Trajectories/'
CorrPath = 'AutoCorrelation/'

filename_CP = 'CPTrack_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
filename_Pos = 'PositionTrack_TS_' + str(TimeSeparation) + '_k' + str(kCP) + '.dat'
filename_Corr = 'AutoCorrelation_TS_' + str(TimeSeparation) + '.dat'

PositionTrack = TimeDriverLocal.FrictionPropogator(SampleTime,TimeSeparation)
WriteData.TrajectoryWrite(PositionTrack,filename_Pos,path)

Friction,AutoCorr = FrictionCalculation.Primary(PositionTrack,TimeSeparation)

FrictionName = os.path.join(CorrPath,'Friction.dat')

file1 = open(FrictionName,'w')
file1.write('Friction\tTimeSeparation\n\n')

file1.write('%lf\t%d\n' % (Friction, TimeSeparation))
file1.close()






