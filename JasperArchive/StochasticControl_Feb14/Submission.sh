#!/bin/bash

cd TimeSeparation_2
qsub -l walltime=5:00:00 SubmissionScript.pbs
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
qsub -l walltime=15:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_64
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_128
qsub -l walltime=25:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_256
qsub -l walltime=35:00:00 SubmissionScript.pbs
cd ..
