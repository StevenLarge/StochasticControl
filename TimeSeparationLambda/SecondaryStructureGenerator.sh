#!/bin/bash
#Secondary Structure Generator script for stochastic control simulations

cd dLambda_5
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64
mkdir k128
cd ..

cd dLambda_10
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64
mkdir k128
cd ..

cd dLambda_20
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64
mkdir k128
cd ..

cd dLambda_40
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64
mkdir k128
cd ..


cd dLambda_80
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64
mkdir k128
cd ..


cp SimulationScripts.tar dLambda_5/k1
cp SimulationScripts.tar dLambda_5/k2
cp SimulationScripts.tar dLambda_5/k4
cp SimulationScripts.tar dLambda_5/k8
cp SimulationScripts.tar dLambda_5/k16
cp SimulationScripts.tar dLambda_5/k32
cp SimulationScripts.tar dLambda_5/k64
cp SimulationScripts.tar dLambda_5/k128

cp SimulationScripts.tar dLambda_10/k1
cp SimulationScripts.tar dLambda_10/k2
cp SimulationScripts.tar dLambda_10/k4
cp SimulationScripts.tar dLambda_10/k8
cp SimulationScripts.tar dLambda_10/k16
cp SimulationScripts.tar dLambda_10/k32
cp SimulationScripts.tar dLambda_10/k64
cp SimulationScripts.tar dLambda_10/k128

cp SimulationScripts.tar dLambda_20/k1
cp SimulationScripts.tar dLambda_20/k2
cp SimulationScripts.tar dLambda_20/k4
cp SimulationScripts.tar dLambda_20/k8
cp SimulationScripts.tar dLambda_20/k16
cp SimulationScripts.tar dLambda_20/k32
cp SimulationScripts.tar dLambda_20/k64
cp SimulationScripts.tar dLambda_20/k128

cp SimulationScripts.tar dLambda_40/k1
cp SimulationScripts.tar dLambda_40/k2
cp SimulationScripts.tar dLambda_40/k4
cp SimulationScripts.tar dLambda_40/k8
cp SimulationScripts.tar dLambda_40/k16
cp SimulationScripts.tar dLambda_40/k32
cp SimulationScripts.tar dLambda_40/k64
cp SimulationScripts.tar dLambda_40/k128

cp SimulationScripts.tar dLambda_80/k1
cp SimulationScripts.tar dLambda_80/k2
cp SimulationScripts.tar dLambda_80/k4
cp SimulationScripts.tar dLambda_80/k8
cp SimulationScripts.tar dLambda_80/k16
cp SimulationScripts.tar dLambda_80/k32
cp SimulationScripts.tar dLambda_80/k64
cp SimulationScripts.tar dLambda_80/k128


cd dLambda_5
cd k1
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k2
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k4
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k8
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k16
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k32
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k64
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k128
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd ..

cd dLambda_10
cd k1
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k2
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k4
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k8
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k16
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k32
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k64
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k128
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd ..

cd dLambda_20
cd k1
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k2
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k4
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k8
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k16
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k32
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k64
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k128
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd ..

cd dLambda_40
cd k1
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k2
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k4
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k8
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k16
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k32
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k64
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k128
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd ..

cd dLambda_80
cd k1
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k2
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k4
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k8
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k16
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k32
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k64
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd k128
mkdir Output
tar -xvf SimulationScripts.tar
cd ..
cd ..

cp SecondaryParameterMasterGenerator.py dLambda_5
cp SecondaryParameterMasterGenerator.py dLambda_10
cp SecondaryParameterMasterGenerator.py dLambda_20
cp SecondaryParameterMasterGenerator.py dLambda_40
cp SecondaryParameterMasterGenerator.py dLambda_80

cd dLambda_5
python SecondaryParameterMasterGenerator.py
cd ..
cd dLambda_10
python SecondaryParameterMasterGenerator.py
cd ..
cd dLambda_20
python SecondaryParameterMasterGenerator.py
cd ..
cd dLambda_40
python SecondaryParameterMasterGenerator.py
cd ..
cd dLambda_80
python SecondaryParameterMasterGenerator.py
cd ..


