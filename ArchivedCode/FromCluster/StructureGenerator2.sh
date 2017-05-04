#!/bin/bash
#This shell script generates the primitive file structure for simulations regarding Time Separations

echo "..."
echo "Script Beginning"
echo "..."

mkdir kLambda

cd kLambda

mkdir k1
mkdir k2
mkdir k4
mkdir k8
mkdir k16

cd k1
mkdir Tau_1
mkdir Tau_2
mkdir Tau_4
mkdir Tau_8
mkdir Tau_16
mkdir Tau_32
mkdir Tau_64
mkdir Tau_128
cd ..

cd k2
mkdir Tau_1
mkdir Tau_2
mkdir Tau_4
mkdir Tau_8
mkdir Tau_16
mkdir Tau_32
mkdir Tau_64
mkdir Tau_128
cd ..

cd k4
mkdir Tau_1
mkdir Tau_2
mkdir Tau_4
mkdir Tau_8
mkdir Tau_16
mkdir Tau_32
mkdir Tau_64
mkdir Tau_128
cd ..

cd k8
mkdir Tau_1
mkdir Tau_2
mkdir Tau_4
mkdir Tau_8
mkdir Tau_16
mkdir Tau_32
mkdir Tau_64
mkdir Tau_128
cd ..

cd k16
mkdir Tau_1
mkdir Tau_2
mkdir Tau_4
mkdir Tau_8
mkdir Tau_16
mkdir Tau_32
mkdir Tau_64
mkdir Tau_128
cd ..

cd ..

tar -cvf Executables.tar Driver.py LangevinPropogator.py Ornstein.py Potential.py WriteData.py GeneratePBS.py

cp Executables.tar kLambda/k1/Tau_1/Executables.tar
cp Executables.tar kLambda/k1/Tau_2/Executables.tar
cp Executables.tar kLambda/k1/Tau_4/Executables.tar
cp Executables.tar kLambda/k1/Tau_8/Executables.tar
cp Executables.tar kLambda/k1/Tau_16/Executables.tar
cp Executables.tar kLambda/k1/Tau_32/Executables.tar
cp Executables.tar kLambda/k1/Tau_64/Executables.tar
cp Executables.tar kLambda/k1/Tau_128/Executables.tar

cp Executables.tar kLambda/k2/Tau_1/Executables.tar
cp Executables.tar kLambda/k2/Tau_2/Executables.tar
cp Executables.tar kLambda/k2/Tau_4/Executables.tar
cp Executables.tar kLambda/k2/Tau_8/Executables.tar
cp Executables.tar kLambda/k2/Tau_16/Executables.tar
cp Executables.tar kLambda/k2/Tau_32/Executables.tar
cp Executables.tar kLambda/k2/Tau_64/Executables.tar
cp Executables.tar kLambda/k2/Tau_128/Executables.tar

cp Executables.tar kLambda/k4/Tau_1/Executables.tar
cp Executables.tar kLambda/k4/Tau_2/Executables.tar
cp Executables.tar kLambda/k4/Tau_4/Executables.tar
cp Executables.tar kLambda/k4/Tau_8/Executables.tar
cp Executables.tar kLambda/k4/Tau_16/Executables.tar
cp Executables.tar kLambda/k4/Tau_32/Executables.tar
cp Executables.tar kLambda/k4/Tau_64/Executables.tar
cp Executables.tar kLambda/k4/Tau_128/Executables.tar

cp Executables.tar kLambda/k8/Tau_1/Executables.tar
cp Executables.tar kLambda/k8/Tau_2/Executables.tar
cp Executables.tar kLambda/k8/Tau_4/Executables.tar
cp Executables.tar kLambda/k8/Tau_8/Executables.tar
cp Executables.tar kLambda/k8/Tau_16/Executables.tar
cp Executables.tar kLambda/k8/Tau_32/Executables.tar
cp Executables.tar kLambda/k8/Tau_64/Executables.tar
cp Executables.tar kLambda/k8/Tau_128/Executables.tar

cp Executables.tar kLambda/k16/Tau_1/Executables.tar
cp Executables.tar kLambda/k16/Tau_2/Executables.tar
cp Executables.tar kLambda/k16/Tau_4/Executables.tar
cp Executables.tar kLambda/k16/Tau_8/Executables.tar
cp Executables.tar kLambda/k16/Tau_16/Executables.tar
cp Executables.tar kLambda/k16/Tau_32/Executables.tar
cp Executables.tar kLambda/k16/Tau_64/Executables.tar
cp Executables.tar kLambda/k16/Tau_128/Executables.tar

python ParameterMasterGenerator2.py

cd kLambda

cd k1
cd Tau_1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_4
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_8
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_16
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_32
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_64
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_128
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd k2
cd Tau_1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_4
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_8
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_16
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_32
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_64
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_128
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd k4
cd Tau_1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_4
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_8
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_16
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_32
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_64
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_128
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd k8
cd Tau_1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_4
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_8
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_16
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_32
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_64
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_128
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd k16
cd Tau_1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_4
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_8
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_16
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_32
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_64
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd Tau_128
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd ..

echo "..."
echo "File Structure Generated"
echo "..."
