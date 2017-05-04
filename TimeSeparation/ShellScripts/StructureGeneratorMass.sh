#!/bin/bash
#Structure Generator sript for varying CP Mass in stochastic control simulations February 11th 2017

mkdir MassTest
cd MassTest
mkdir MASS_1
mkdir MASS_2
mkdir MASS_4
mkdir MASS_8
mkdir MASS_16
mkdir MASS_32
cd ..

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

mv Scripts.tar MassTest/Scripts.tar

cd MassTest

cp Scripts.tar MASS_1/Scripts.tar
cp Scripts.tar MASS_2/Scripts.tar
cp Scripts.tar MASS_4/Scripts.tar
cp Scripts.tar MASS_8/Scripts.tar
cp Scripts.tar MASS_16/Scripts.tar
cp Scripts.tar MASS_32/Scripts.tar

cd MASS_1
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd MASS_2
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd MASS_4
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd MASS_8
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd MASS_16
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

cd MASS_32
tar -xvf *.tar
mkdir Output
python GeneratePBS.py
cd ..

python ParameterMasterWriteMass.py

echo ""
echo ""
echo ""
echo ""
echo ""
echo "-------------Structure Generated-------------"
echo ""
echo ""
echo ""
echo ""
echo ""








