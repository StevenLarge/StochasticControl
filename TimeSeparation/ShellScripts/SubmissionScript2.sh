#!/bin/bash
#This is the submission script for Time Separation simualtions submitted on January 23rd 2017

cd TimeSeparation_1
cd k01
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_2
cd k01
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_4
cd k01
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_8
cd k01
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_16
cd k01
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_32
cd k01
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=23:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_64
cd k01
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=32:00:00 SubmissionScript.pbs
cd ..
cd ..

cd TimeSeparation_128
cd k01
qsub -l walltime=50:00:00 SubmissionScript.pbs
cd ..
cd k001
qsub -l walltime=50:00:00 SubmissionScript.pbs
cd ..
cd ..
