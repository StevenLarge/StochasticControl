#!/bin/bash
#This is the submission script for Time Separation simualtions submitted on January 23rd 2017

cd TimeSeparation_256
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_512
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1024
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..



cd TimeSeparation_256
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_512
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_1024
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..


