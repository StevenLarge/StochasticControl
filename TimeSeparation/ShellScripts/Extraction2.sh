#!/bin/bash
#This is the master submission script for the time separation simulations of Stochastic Control


cd Times_80
cd k1
qsub -l walltime=60:00:00 SubmissionScript.pbs
cd ..
cd k2
qsub -l walltime=60:00:00 SubmissionScript.pbs
cd ..
cd k4
qsub -l walltime=60:00:00 SubmissionScript.pbs
cd ..
cd k8
qsub -l walltime=60:00:00 SubmissionScript.pbs
cd ..
cd k16
qsub -l walltime=60:00:00 SubmissionScript.pbs
cd ..
cd ..

cd Times_160
cd k1
qsub -l walltime=71:00:00 SubmissionScript.pbs
cd ..
cd k2
qsub -l walltime=71:00:00 SubmissionScript.pbs
cd ..
cd k4
qsub -l walltime=71:00:00 SubmissionScript.pbs
cd ..
cd k8
qsub -l walltime=71:00:00 SubmissionScript.pbs
cd ..
cd k16
qsub -l walltime=71:00:00 SubmissionScript.pbs
cd ..
cd ..
