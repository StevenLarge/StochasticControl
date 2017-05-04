#!/bin/bash
#This is the submission script for Time Separation simualtions submitted on January 23rd 2017

cd TimeSeparation_1
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_2
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_4
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_8
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_16
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_32
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_64
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_128
qsub -l walltime=34:00:00 SubmissionScript.pbs
cd ..


cd TimeSeparation_1
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_2
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_4
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_8
qsub -l walltime=15:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_16
qsub -l walltime=20:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_32
qsub -l walltime=20:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_64
qsub -l walltime=24:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation_128
qsub -l walltime=24:00:00 SubmissionScriptFriction.pbs
cd ..

