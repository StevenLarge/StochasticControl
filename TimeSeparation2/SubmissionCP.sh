#!/bin/bash

cd a25
qsub -l walltime=1:00:00 CPGenerator_a25.pbs
cd ..

cd a50
qsub -l walltime=1:00:00 CPGenerator_a50.pbs
cd ..

cd a75
qsub -l walltime=1:00:00 CPGenerator_a75.pbs
cd ..

cd a90
qsub -l walltime=1:00:00 CPGenerator_a90.pbs
cd ..

cd a95
qsub -l walltime=1:00:00 CPGenerator_a95.pbs
cd ..

cd a99
qsub -l walltime=1:00:00 CPGenerator_a99.pbs
cd ..



