#!/bin/bash
#This is the master submission script for the constant velocity ensemble

cd VelVar_01
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd VelVar_05
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd VelVar_1
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd VelVar_2
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd VelVar_4
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd VelVar_8
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

