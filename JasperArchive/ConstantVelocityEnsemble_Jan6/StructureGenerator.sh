#!/bin/bash
#This shell script generates the file structure for different velocity variances

mkdir VelVar_01
mkdir VelVar_05
mkdir VelVar_1
mkdir VelVar_2
mkdir VelVar_4
mkdir VelVar_8

tar -cvf Scripts.tar GeneratePBS.py ConstantVelocityPrimary.py LangevinPropogator.py WriteData.py ConstantDriver.py Parameters.py

cp Scripts.tar VelVar_01/Scripts.tar
cp Scripts.tar VelVar_05/Scripts.tar
cp Scripts.tar VelVar_1/Scripts.tar
cp Scripts.tar VelVar_2/Scripts.tar
cp Scripts.tar VelVar_4/Scripts.tar
cp Scripts.tar VelVar_8/Scripts.tar

python VelocityParameterMasterGenerator.py

cd VelVar_01
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd VelVar_05
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd VelVar_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd VelVar_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd VelVar_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd VelVar_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

