#!/bin/bash
#This is the submission script for Time Separation simualtions submitted on January 23rd 2017

cd TimeSeparation_1050
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1100
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1150
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1200
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1250
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1300
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1350
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1400
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1450
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_1500
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..


