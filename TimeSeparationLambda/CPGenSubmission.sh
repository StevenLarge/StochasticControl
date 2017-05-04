#!/bin/bash
#CPGenerator Submission script

cp RunCPGen.pbs dLambda_5/Trajectories_a30
cp RunCPGen.pbs dLambda_5/Trajectories_a50
cp RunCPGen.pbs dLambda_5/Trajectories_a70
cp RunCPGen.pbs dLambda_5/Trajectories_a80
cp RunCPGen.pbs dLambda_5/Trajectories_a90
cp RunCPGen.pbs dLambda_5/Trajectories_a95
cp RunCPGen.pbs dLambda_5/Trajectories_a99

cp RunCPGen.pbs dLambda_10/Trajectories_a30
cp RunCPGen.pbs dLambda_10/Trajectories_a50
cp RunCPGen.pbs dLambda_10/Trajectories_a70
cp RunCPGen.pbs dLambda_10/Trajectories_a80
cp RunCPGen.pbs dLambda_10/Trajectories_a90
cp RunCPGen.pbs dLambda_10/Trajectories_a95
cp RunCPGen.pbs dLambda_10/Trajectories_a99

cp RunCPGen.pbs dLambda_20/Trajectories_a30
cp RunCPGen.pbs dLambda_20/Trajectories_a50
cp RunCPGen.pbs dLambda_20/Trajectories_a70
cp RunCPGen.pbs dLambda_20/Trajectories_a80
cp RunCPGen.pbs dLambda_20/Trajectories_a90
cp RunCPGen.pbs dLambda_20/Trajectories_a95
cp RunCPGen.pbs dLambda_20/Trajectories_a99

cp RunCPGen.pbs dLambda_40/Trajectories_a30
cp RunCPGen.pbs dLambda_40/Trajectories_a50
cp RunCPGen.pbs dLambda_40/Trajectories_a70
cp RunCPGen.pbs dLambda_40/Trajectories_a80
cp RunCPGen.pbs dLambda_40/Trajectories_a90
cp RunCPGen.pbs dLambda_40/Trajectories_a95
cp RunCPGen.pbs dLambda_40/Trajectories_a99

cp RunCPGen.pbs dLambda_80/Trajectories_a30
cp RunCPGen.pbs dLambda_80/Trajectories_a50
cp RunCPGen.pbs dLambda_80/Trajectories_a70
cp RunCPGen.pbs dLambda_80/Trajectories_a80
cp RunCPGen.pbs dLambda_80/Trajectories_a90
cp RunCPGen.pbs dLambda_80/Trajectories_a95
cp RunCPGen.pbs dLambda_80/Trajectories_a99



cd dLambda_5
cd Trajectories_a30
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a50
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a70
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a80
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a90
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a95
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a99
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd ..

cd dLambda_10
cd Trajectories_a30
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a50
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a70
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a80
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a90
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a95
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a99
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd ..

cd dLambda_20
cd Trajectories_a30
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a50
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a70
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a80
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a90
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a95
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a99
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd ..

cd dLambda_40
cd Trajectories_a30
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a50
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a70
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a80
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a90
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a95
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a99
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd ..

cd dLambda_80
cd Trajectories_a30
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a50
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a70
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a80
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a90
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a95
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd Trajectories_a99
qsub -l walltime=20:00:00 RunCPGen.pbs
cd ..
cd ..

