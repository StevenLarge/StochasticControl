#!/bin/bash
#This is a submission script for friction calculation routines of Time separation dynamics

cd TimeSeparation2_1
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_2
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_4
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_8
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_16
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_32
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_64
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..

cd TimeSeparation2_128
qsub -l walltime=4:00:00 SubmissionScriptFriction.pbs
cd ..



