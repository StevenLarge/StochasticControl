#!/bin/bash
#Structure generator script for constatnt velocity time separation simulations

mkdir TimeSeparation_1
mkdir TimeSeparation_2
mkdir TimeSeparation_4
mkdir TimeSeparation_8
mkdir TimeSeparation_16
mkdir TimeSeparation_32
mkdir TimeSeparation_64


tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py 

cp Scripts.tar TimeSeparation_1/Scripts.tar
cp Scripts.tar TimeSeparation_2/Scripts.tar
cp Scripts.tar TimeSeparation_4/Scripts.tar
cp Scripts.tar TimeSeparation_8/Scripts.tar
cp Scripts.tar TimeSeparation_16/Scripts.tar
cp Scripts.tar TimeSeparation_32/Scripts.tar
cp Scripts.tar TimeSeparation_64/Scripts.tar

cd TimeSeparation_1
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd TimeSeparation_2
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd TimeSeparation_4
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd TimeSeparation_8
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd TimeSeparation_16
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd TimeSeparation_32
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd TimeSeparation_64
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..


python TimeParameterMasterWrite.py




