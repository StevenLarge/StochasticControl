#!/bin/bash
#Submission Script for February 11th simulations

cd TimeSeparation_1
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_2
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_4
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_8
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_16
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_32
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_64
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..







