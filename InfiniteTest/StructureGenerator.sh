#!/bin/bash
#This shell script creates the file structure for the infinite-time-separation limit of stochastic protocol work

mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64

cp *.tar k1
cp *.tar k2
cp *.tar k4
cp *.tar k8
cp *.tar k16
cp *.tar k32
cp *.tar k64

cd k1
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

cd k2
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

cd k4
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

cd k8
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

cd k16
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

cd k32
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

cd k64
tar -xvf *.tar
rm *.tar
rm ParameterMasterGenerator.py
python GeneratePBS.py
cd ..

python ParameterMasterGenerator.py

python GeneratePBS.py
