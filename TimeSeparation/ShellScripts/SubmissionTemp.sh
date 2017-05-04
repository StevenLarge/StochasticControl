#!/bin/bash
#temporary submission script

cd kCP_1
qsub -l walltime=16:00:00 SubmissionScript.pbs
cd ..

cd kCP_2
qsub -l walltime=16:00:00 SubmissionScript.pbs
cd ..

cd kCP_4
qsub -l walltime=16:00:00 SubmissionScript.pbs
cd ..

cd kCP_8
qsub -l walltime=16:00:00 SubmissionScript.pbs
cd ..

cd kCP_16
qsub -l walltime=16:00:00 SubmissionScript.pbs
cd ..

cd kCP_32
qsub -l walltime=16:00:00 SubmissionScript.pbs
cd ..

