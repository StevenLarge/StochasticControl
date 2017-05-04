#!/bin/bash
#This shell script submits the jobs for each parameter value of sigma (0.25,0.5,1,2,4) and (5,10,20,40,80,160) for kLambda subdirectories

echo "..."
echo "Submitting jobs..."
echo "..."

cd kLambda

cd k1

cd Tau_1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_4
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_8
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_16
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_32
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_64
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_128
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..
cd ..

cd k2

cd Tau_1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_4
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_8
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_16
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_32
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_64
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_128
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..
cd ..

cd k4

cd Tau_1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_4
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_8
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_16
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_32
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_64
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_128
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..
cd ..


cd k4

cd Tau_1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_4
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_8
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_16
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_32
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_64
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_128
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..
cd ..


cd k8

cd Tau_1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_4
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_8
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_16
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_32
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_64
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_128
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..
cd ..


cd k16

cd Tau_1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd Tau_4
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_8
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_16
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_32
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_64
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..

cd Tau_128
qsub -l walltime=47:00:00 MasterSubScript.pbs
cd ..
cd ..
cd ..

echo "..."
echo "Submission finished"
echo "..."
echo ""
echo ""


