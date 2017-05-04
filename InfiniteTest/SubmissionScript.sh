#!/bin/bash
#This shell script submits the jobs for the infinite time separation on the cluster

cd k1
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd k2
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd k4
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd k8
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd k16
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd k32
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..

cd k64
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..


