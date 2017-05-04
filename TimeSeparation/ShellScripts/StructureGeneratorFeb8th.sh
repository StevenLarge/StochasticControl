#!/bin/bash
#StructureGenerator for Time Separation Simulations February 8th 2017

mkdir TimeSeparation_256
mkdir TimeSeparation_512
mkdir TimeSeparation_1024

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

cp Scripts.tar TimeSeparation_256/Scripts.tar
cp Scripts.tar TimeSeparation_512/Scripts.tar
cp Scripts.tar TimeSeparation_1024/Scripts.tar

rm *.tar

cd TimeSeparation_256
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_512
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_1024
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..


python TimeParameterMasterWrite.py


echo ""
echo ""
echo ""
echo ""
echo ""
echo "-----File Structure genrated-----"
echo ""
echo ""
echo ""
echo ""
echo ""







