#!/bin/bash
#SubmissionScript for February 15th data

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
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_32
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_64
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_a75_1
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a75_2
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a75_4
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a75_8
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a75_16
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a75_32
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a75_64
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..

cd TimeSeparation_a95_1
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a95_2
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a95_4
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a95_8
qsub -l walltime=10:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a95_16
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a95_32
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..
cd TimeSeparation_a95_64
qsub -l walltime=20:00:00 SubmissionScript.pbs
cd ..



