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

SampleTime = 200000

path = 'Trajectories/'
CorrPath = 'AutoCorrelation/'

filename_CP = 'CPTrack_TS_' + str(TimeSeparation) + '.dat'
filename_Pos = 'PositionTrack_TS_' + str(TimeSeparation) + '.dat'
filename_Corr = 'AutoCorrelation_TS_' + str(TimeSeparation) + '.dat'

PositionTrack = TimeDriverLocal.FrictionPropogator(SampleTime,TimeSeparation)
CPTrack = TimeDriverLocal.FrictionPropogatorCP(SampleTime,TimeSeparation)
WriteData.TrajectoryWrite(PositionTrack,filename_Pos,path)
WriteData.TrajectoryWrite(CPTrack,filename_CP,path)

WriteName = 'AutoCorrelation_' + str(TimeSeparation) + '.dat'
WriteNameCP = 'AutoCorrelationCP_' + str(TimeSeparation) + '.dat'

Friction,AutoCorr = FrictionCalculation.Primary(PositionTrack,TimeSeparation,WriteName)
CPFriction,AutoCorrCP = FrictionCalculation.Primary(CPTrack,TimeSeparation,WriteNameCP)

FrictionName = os.path.join(CorrPath,'Friction.dat')
FrictionCPName = os.path.join(CorrPath,'FrictionCP.dat')

file1 = open(FrictionName,'w')
file1.write('Friction\tTimeSeparation\n\n')
file1.write('%lf\t%d\n' % (Friction, TimeSeparation))
file1.close()

file2 = open(FrictionCPName,'w')
file2.write('Friction\tTimeSeparation\n\n')
file2.write('%lf\t%d\n' % (FrictionCP, TimeSeparation))
file2.close()





