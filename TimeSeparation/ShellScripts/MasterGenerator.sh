#!/bin/bash
#This is a structure generator script for parameter variation scripts of Time Separation stochastic control simulations

mkdir TimeSeparation_1
mkdir TimeSeparation_2
mkdir TimeSeparation_4
mkdir TimeSeparation_8
mkdir TimeSeparation_16
mkdir TimeSeparation_32

cd TimeSeparation_1
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
cd ..

cd TimeSeparation_2
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
cd ..

cd TimeSeparation_4
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
cd ..

cd TimeSeparation_8
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
cd ..

cd TimeSeparation_16
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
cd ..

cd TimeSeparation_32
mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
cd ..


cd TimeSeparation_1
cd k1
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k2
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k4
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k8
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k16
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd ..

cd TimeSeparation_2
cd k1
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k2
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k4
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k8
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k16
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd ..

cd TimeSeparation_4
cd k1
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k2
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k4
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k8
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k16
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd ..

cd TimeSeparation_8
cd k1
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k2
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k4
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k8
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k16
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd ..

cd TimeSeparation_16
cd k1
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k2
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k4
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k8
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k16
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd ..

cd TimeSeparation_32
cd k1
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k2
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k4
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k8
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd k16
mkdir sigma1
mkdir sigma05
mkdir sigma01
cd ..
cd ..

python TimeParameterMasterWrite.py

cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k1/sigma1/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k1/sigma05/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k1/sigma01/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k2/sigma1/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k2/sigma05/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k2/sigma01/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k4/sigma1/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k4/sigma05/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k4/sigma01/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k8/sigma1/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k8/sigma05/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k8/sigma01/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k16/sigma1/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k16/sigma05/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k16/sigma01/TimeParameters.py

cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k1/sigma1/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k1/sigma05/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k1/sigma01/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k2/sigma1/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k2/sigma05/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k2/sigma01/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k4/sigma1/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k4/sigma05/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k4/sigma01/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k8/sigma1/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k8/sigma05/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k8/sigma01/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k16/sigma1/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k16/sigma05/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k16/sigma01/TimeParameters.py

cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k1/sigma1/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k1/sigma05/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k1/sigma01/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k2/sigma1/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k2/sigma05/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k2/sigma01/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k4/sigma1/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k4/sigma05/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k4/sigma01/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k8/sigma1/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k8/sigma05/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k8/sigma01/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k16/sigma1/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k16/sigma05/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k16/sigma01/TimeParameters.py

cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k1/sigma1/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k1/sigma05/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k1/sigma01/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k2/sigma1/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k2/sigma05/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k2/sigma01/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k4/sigma1/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k4/sigma05/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k4/sigma01/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k8/sigma1/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k8/sigma05/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k8/sigma01/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k16/sigma1/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k16/sigma05/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k16/sigma01/TimeParameters.py

cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k1/sigma1/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k1/sigma05/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k1/sigma01/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k2/sigma1/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k2/sigma05/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k2/sigma01/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k4/sigma1/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k4/sigma05/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k4/sigma01/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k8/sigma1/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k8/sigma05/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k8/sigma01/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k16/sigma1/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k16/sigma05/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k16/sigma01/TimeParameters.py

cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k1/sigma1/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k1/sigma05/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k1/sigma01/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k2/sigma1/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k2/sigma05/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k2/sigma01/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k4/sigma1/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k4/sigma05/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k4/sigma01/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k8/sigma1/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k8/sigma05/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k8/sigma01/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k16/sigma1/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k16/sigma05/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k16/sigma01/TimeParameters.py

cp ParameterMasterWrite.py TimeSeparation_1/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_2/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_4/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_8/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_16/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_32/ParameterMasterWrite.py

cd TimeSeparation_1
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_2
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_4
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_8
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_16
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_32
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_1
cd k1
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k2
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k4
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k8
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k16
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..
cd ..


cd TimeSeparation_2
cd k1
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k2
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k4
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k8
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k16
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..
cd ..


cd TimeSeparation_4
cd k1
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k2
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k4
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k8
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k16
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..
cd ..


cd TimeSeparation_8
cd k1
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k2
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k4
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k8
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k16
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..
cd ..


cd TimeSeparation_16
cd k1
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k2
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k4
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k8
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k16
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..
cd ..


cd TimeSeparation_32
cd k1
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k2
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k4
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k8
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..

cd k16
cd sigma1
mkdir Output
cd ..
cd sigma05
mkdir Output
cd ..
cd sigma01
mkdir Output
cd ..
cd ..
cd ..

tar -cvf Scripts.tar TimePrimary.py TimeDriverLocal.py LangevinPropogator.py WriteData.py Potential.py GeneratePBS.py WorkTheoryModule.py

cp Scripts.tar TimeSeparation_1/k1/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_1/k1/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_1/k1/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_1/k2/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_1/k2/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_1/k2/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_1/k4/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_1/k4/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_1/k4/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_1/k8/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_1/k8/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_1/k8/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_1/k16/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_1/k16/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_1/k16/sigma01/Scripts.tar


cp Scripts.tar TimeSeparation_2/k1/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_2/k1/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_2/k1/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_2/k2/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_2/k2/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_2/k2/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_2/k4/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_2/k4/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_2/k4/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_2/k8/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_2/k8/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_2/k8/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_2/k16/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_2/k16/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_2/k16/sigma01/Scripts.tar


cp Scripts.tar TimeSeparation_4/k1/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_4/k1/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_4/k1/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_4/k2/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_4/k2/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_4/k2/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_4/k4/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_4/k4/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_4/k4/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_4/k8/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_4/k8/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_4/k8/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_4/k16/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_4/k16/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_4/k16/sigma01/Scripts.tar

cp Scripts.tar TimeSeparation_8/k1/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_8/k1/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_8/k1/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_8/k2/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_8/k2/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_8/k2/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_8/k4/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_8/k4/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_8/k4/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_8/k8/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_8/k8/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_8/k8/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_8/k16/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_8/k16/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_8/k16/sigma01/Scripts.tar


cp Scripts.tar TimeSeparation_16/k1/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_16/k1/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_16/k1/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_16/k2/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_16/k2/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_16/k2/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_16/k4/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_16/k4/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_16/k4/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_16/k8/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_16/k8/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_16/k8/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_16/k16/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_16/k16/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_16/k16/sigma01/Scripts.tar


cp Scripts.tar TimeSeparation_32/k1/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_32/k1/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_32/k1/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_32/k2/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_32/k2/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_32/k2/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_32/k4/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_32/k4/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_32/k4/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_32/k8/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_32/k8/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_32/k8/sigma01/Scripts.tar
cp Scripts.tar TimeSeparation_32/k16/sigma1/Scripts.tar
cp Scripts.tar TimeSeparation_32/k16/sigma05/Scripts.tar
cp Scripts.tar TimeSeparation_32/k16/sigma01/Scripts.tar

cd TimeSeparation_1
cd k1
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k2
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k4
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k8
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k16
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd ..

cd TimeSeparation_2
cd k1
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k2
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k4
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k8
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k16
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd ..

cd TimeSeparation_4
cd k1
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k2
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k4
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k8
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k16
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd ..

cd TimeSeparation_8
cd k1
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k2
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k4
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k8
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k16
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd ..

cd TimeSeparation_16
cd k1
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k2
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k4
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k8
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k16
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd ..

cd TimeSeparation_32
cd k1
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k2
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k4
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k8
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd k16
cd sigma1
tar -xvf Scripts.tar
cd ..
cd sigma05
tar -xvf Scripts.tar
cd ..
cd sigma01
tar -xvf Scripts.tar
cd ..
cd ..
cd ..

cd TimeSeparation_1
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..



cd TimeSeparation_2
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..


cd TimeSeparation_4
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..


cd TimeSeparation_8
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..


cd TimeSeparation_8
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..


cd TimeSeparation_16
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..



cd TimeSeparation_32
cd k1
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k2
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k4
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k8
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd k16
cd sigma1
python GeneratePBS.py
cd ..
cd sigma05
python GeneratePBS.py
cd ..
cd sigma01
python GeneratePBS.py
cd ..
cd ..
cd ..

