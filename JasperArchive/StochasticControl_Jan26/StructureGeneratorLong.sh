#!/bin/bash
#StructureGenerator for Time Separation Simulations January 23rd 2017

mkdir TimeSeparation_256
mkdir TimeSeparation_512

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

cp Scripts.tar TimeSeparation_256/Scripts.tar
cp Scripts.tar TimeSeparation_512/Scripts.tar

rm *.tar

cd TimeSeparation_256
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_512
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
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
