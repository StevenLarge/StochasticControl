#!/bin/bash
#This shell script generates the complete file structure for Time Separation simulations of stochastic control

mkdir Times_1
mkdir Times_5
mkdir Times_10
mkdir Times_20
mkdir Times_40
mkdir Times_80

cd Times_1
mkdir k1
cd k1
mkdir Output
cd ..
mkdir k2
cd k2
mkdir Output
cd ..
mkdir k4
cd k4
mkdir Output
cd ..
mkdir k8
cd k8
mkdir Output
cd ..
mkdir k16
cd k16
mkdir Output
cd ..
cd ..

cd Times_5
mkdir k1
cd k1
mkdir Output
cd ..
mkdir k2
cd k2
mkdir Output
cd ..
mkdir k4
cd k4
mkdir Output
cd ..
mkdir k8
cd k8
mkdir Output
cd ..
mkdir k16
cd k16
mkdir Output
cd ..
cd ..

cd Times_10
mkdir k1
cd k1
mkdir Output
cd ..
mkdir k2
cd k2
mkdir Output
cd ..
mkdir k4
cd k4
mkdir Output
cd ..
mkdir k8
cd k8
mkdir Output
cd ..
mkdir k16
cd k16
mkdir Output
cd ..
cd ..

cd Times_20
mkdir k1
cd k1
mkdir Output
cd ..
mkdir k2
cd k2
mkdir Output
cd ..
mkdir k4
cd k4
mkdir Output
cd ..
mkdir k8
cd k8
mkdir Output
cd ..
mkdir k16
cd k16
mkdir Output
cd ..
cd ..

cd Times_40
mkdir k1
cd k1
mkdir Output
cd ..
mkdir k2
cd k2
mkdir Output
cd ..
mkdir k4
cd k4
mkdir Output
cd ..
mkdir k8
cd k8
mkdir Output
cd ..
mkdir k16
cd k16
mkdir Output
cd ..
cd ..

cd Times_80
mkdir k1
cd k1
mkdir Output
cd ..
mkdir k2
cd k2
mkdir Output
cd ..
mkdir k4
cd k4
mkdir Output
cd ..
mkdir k8
cd k8
mkdir Output
cd ..
mkdir k16
cd k16
mkdir Output
cd ..
cd ..


tar -cvf Scripts.tar GeneratePBS.py LangevinPropogator.py TimeDriver.py Potential.py TimeSeparationPrimary.py WriteData.py

cp Scripts.tar Times_1/k1/Scripts.tar
cp Scripts.tar Times_1/k2/Scripts.tar
cp Scripts.tar Times_1/k4/Scripts.tar
cp Scripts.tar Times_1/k8/Scripts.tar
cp Scripts.tar Times_1/k16/Scripts.tar

cp Scripts.tar Times_5/k1/Scripts.tar
cp Scripts.tar Times_5/k2/Scripts.tar
cp Scripts.tar Times_5/k4/Scripts.tar
cp Scripts.tar Times_5/k8/Scripts.tar
cp Scripts.tar Times_5/k16/Scripts.tar

cp Scripts.tar Times_10/k1/Scripts.tar
cp Scripts.tar Times_10/k2/Scripts.tar
cp Scripts.tar Times_10/k4/Scripts.tar
cp Scripts.tar Times_10/k8/Scripts.tar
cp Scripts.tar Times_10/k16/Scripts.tar

cp Scripts.tar Times_20/k1/Scripts.tar
cp Scripts.tar Times_20/k2/Scripts.tar
cp Scripts.tar Times_20/k4/Scripts.tar
cp Scripts.tar Times_20/k8/Scripts.tar
cp Scripts.tar Times_20/k16/Scripts.tar

cp Scripts.tar Times_40/k1/Scripts.tar
cp Scripts.tar Times_40/k2/Scripts.tar
cp Scripts.tar Times_40/k4/Scripts.tar
cp Scripts.tar Times_40/k8/Scripts.tar
cp Scripts.tar Times_40/k16/Scripts.tar

cp Scripts.tar Times_80/k1/Scripts.tar
cp Scripts.tar Times_80/k2/Scripts.tar
cp Scripts.tar Times_80/k4/Scripts.tar
cp Scripts.tar Times_80/k8/Scripts.tar
cp Scripts.tar Times_80/k16/Scripts.tar


cd Times_1
cd k1
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k2
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k4
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k8
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k16
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd Times_5
cd k1
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k2
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k4
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k8
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k16
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd Times_10
cd k1
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k2
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k4
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k8
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k16
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd Times_20
cd k1
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k2
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k4
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k8
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k16
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd Times_40
cd k1
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k2
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k4
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k8
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k16
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd Times_80
cd k1
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k2
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k4
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k8
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd k16
tar -xvf Scripts.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..


python TimeParameterMasterWrite.py
python ParameterMasterWrite.py

echo ""
echo ""
echo ""
echo ""
echo ""
echo "----------- File Structure Generated -----------"
echo ""
echo ""
echo ""
