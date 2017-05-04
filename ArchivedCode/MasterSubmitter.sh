#!/bin/bash
#This shell script submits the jobs for each parameter value of sigma (0.25,0.5,1,2,4) and (5,10,20,40,80,160) for kLambda subdirectories

echo "..."
echo "Submitting jobs..."
echo "..."


cd sigma025
cd kLambda

cd k1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k5
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k10
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k20
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k40
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..
cd ..
cd ..

cd sigma05
cd kLambda

cd k1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k5
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k10
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k20
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k40
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..
cd ..
cd ..

cd sigma1
cd kLambda

cd k1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k5
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k10
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k20
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k40
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..
cd ..
cd ..

cd sigma2
cd kLambda

cd k1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k5
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k10
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k20
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k40
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..
cd ..
cd ..

cd sigma4
cd kLambda

cd k1
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k2
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k5
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k10
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k20
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..

cd k40
qsub -l walltime=23:00:00 MasterSubScript.pbs
cd ..
cd ..
cd ..

echo "..."
echo "Submission finished"
echo "..."
echo ""
echo ""


