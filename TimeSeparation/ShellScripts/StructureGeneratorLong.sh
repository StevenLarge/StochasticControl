#!/bin/bash
#StructureGenerator for Time Separation Simulations January 23rd 2017

mkdir TimeSeparation_1050
mkdir TimeSeparation_1100
mkdir TimeSeparation_1150
mkdir TimeSeparation_1200
mkdir TimeSeparation_1250
mkdir TimeSeparation_1300
mkdir TimeSeparation_1350
mkdir TimeSeparation_1400
mkdir TimeSeparation_1450
mkdir TimeSeparation_1500

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

cp Scripts.tar TimeSeparation_1050/Scripts.tar
cp Scripts.tar TimeSeparation_1100/Scripts.tar
cp Scripts.tar TimeSeparation_1150/Scripts.tar
cp Scripts.tar TimeSeparation_1200/Scripts.tar
cp Scripts.tar TimeSeparation_1250/Scripts.tar
cp Scripts.tar TimeSeparation_1300/Scripts.tar
cp Scripts.tar TimeSeparation_1350/Scripts.tar
cp Scripts.tar TimeSeparation_1400/Scripts.tar
cp Scripts.tar TimeSeparation_1450/Scripts.tar
cp Scripts.tar TimeSeparation_1500/Scripts.tar

rm *.tar

cd TimeSeparation_1050
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1100
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1150
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1200
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1250
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1300
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1350
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1400
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd TimeSeparation_1450
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..


cd TimeSeparation_1500
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..


python TimeParameterMasterWriteLong.py


echo ""
echo ""
echo ""
echo ""
echo ""
echo "-----File Structure generated-----"
echo ""
echo ""
echo ""
echo ""
echo ""
