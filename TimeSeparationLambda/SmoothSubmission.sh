#!/bin/bash
#Master Submission script for low-pass-filtered noisy protocols

cd Smoothing_Tau_1
qsub -l walltime=36:00:00 SubmissionScript_k1.pbs
qsub -l walltime=36:00:00 SubmissionScript_k2.pbs
qsub -l walltime=36:00:00 SubmissionScript_k4.pbs
qsub -l walltime=36:00:00 SubmissionScript_k8.pbs
qsub -l walltime=36:00:00 SubmissionScript_k16.pbs
qsub -l walltime=36:00:00 SubmissionScript_k32.pbs
qsub -l walltime=36:00:00 SubmissionScript_k64.pbs
qsub -l walltime=36:00:00 SubmissionScript_k75.pbs
cd ..

cd Smoothing_Tau_2
qsub -l walltime=36:00:00 SubmissionScript_k1.pbs
qsub -l walltime=36:00:00 SubmissionScript_k2.pbs
qsub -l walltime=36:00:00 SubmissionScript_k4.pbs
qsub -l walltime=36:00:00 SubmissionScript_k8.pbs
qsub -l walltime=36:00:00 SubmissionScript_k16.pbs
qsub -l walltime=36:00:00 SubmissionScript_k32.pbs
qsub -l walltime=36:00:00 SubmissionScript_k64.pbs
qsub -l walltime=36:00:00 SubmissionScript_k75.pbs
cd ..

cd Smoothing_Tau_4
qsub -l walltime=36:00:00 SubmissionScript_k1.pbs
qsub -l walltime=36:00:00 SubmissionScript_k2.pbs
qsub -l walltime=36:00:00 SubmissionScript_k4.pbs
qsub -l walltime=36:00:00 SubmissionScript_k8.pbs
qsub -l walltime=36:00:00 SubmissionScript_k16.pbs
qsub -l walltime=36:00:00 SubmissionScript_k32.pbs
qsub -l walltime=36:00:00 SubmissionScript_k64.pbs
qsub -l walltime=36:00:00 SubmissionScript_k75.pbs
cd ..

cd Smoothing_Tau_8
qsub -l walltime=36:00:00 SubmissionScript_k1.pbs
qsub -l walltime=36:00:00 SubmissionScript_k2.pbs
qsub -l walltime=36:00:00 SubmissionScript_k4.pbs
qsub -l walltime=36:00:00 SubmissionScript_k8.pbs
qsub -l walltime=36:00:00 SubmissionScript_k16.pbs
qsub -l walltime=36:00:00 SubmissionScript_k32.pbs
qsub -l walltime=36:00:00 SubmissionScript_k64.pbs
qsub -l walltime=36:00:00 SubmissionScript_k75.pbs
cd ..

cd Smoothing_Tau_16
qsub -l walltime=36:00:00 SubmissionScript_k1.pbs
qsub -l walltime=36:00:00 SubmissionScript_k2.pbs
qsub -l walltime=36:00:00 SubmissionScript_k4.pbs
qsub -l walltime=36:00:00 SubmissionScript_k8.pbs
qsub -l walltime=36:00:00 SubmissionScript_k16.pbs
qsub -l walltime=36:00:00 SubmissionScript_k32.pbs
qsub -l walltime=36:00:00 SubmissionScript_k64.pbs
qsub -l walltime=36:00:00 SubmissionScript_k75.pbs
cd ..

