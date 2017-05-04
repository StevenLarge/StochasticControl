#!/bin/bash
#Structure generator for fixed end-point protocol ensembles

mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16
mkdir k32
mkdir k64
mkdir k75

tar -cvf Script.tar WorkCalculation.py PBSGenerator.py

cp Scripts.tar k1/Scripts.tar
cp Scripts.tar k2/Scripts.tar
cp Scripts.tar k4/Scripts.tar
cp Scripts.tar k8/Scripts.tar
cp Scripts.tar k16/Scripts.tar
cp Scripts.tar k32/Scripts.tar
cp Scripts.tar k64/Scripts.tar
cp Scripts.tar k75/Scripts.tar

python ParameterMasterGenerator.py

cd k1
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k2
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k4
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k8
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k16
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k32
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k64
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..
cd k75
mkdir Output
tar -xvf *.tar
python GeneratorPBS.py
cd ..

