#!/bin/bash
#StructureGenerator for Time Separation Simulations January 23rd 2017

mkdir TimeSeparation_1
mkdir TimeSeparation_2
mkdir TimeSeparation_4
mkdir TimeSeparation_8
mkdir TimeSeparation_16
mkdir TimeSeparation_32
mkdir TimeSeparation_64
mkdir TimeSeparation_128

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

cp Scripts.tar TimeSeparation_1/Scripts.tar
cp Scripts.tar TimeSeparation_2/Scripts.tar
cp Scripts.tar TimeSeparation_4/Scripts.tar
cp Scripts.tar TimeSeparation_8/Scripts.tar
cp Scripts.tar TimeSeparation_16/Scripts.tar
cp Scripts.tar TimeSeparation_32/Scripts.tar
cp Scripts.tar TimeSeparation_64/Scripts.tar
cp Scripts.tar TimeSeparation_128/Scripts.tar

rm *.tar

cd TimeSeparation_1
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_2
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_4
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_8
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_16
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_32
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_64
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..

cd TimeSeparation_128
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
