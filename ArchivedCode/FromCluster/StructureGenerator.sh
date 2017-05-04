#!/bin/bash
#This shell script gernerates the file structure to run simulations at various different Parameter values for different spring constants

echo "..."
echo "Script Beginning"
echo "..."

mkdir sigma025
mkdir sigma05
mkdir sigma1
mkdir sigma2
mkdir sigma4

cd sigma025

mkdir kLambda

cd kLambda

mkdir k1
mkdir k2
mkdir k5
mkdir k10
mkdir k20
mkdir k40

cd ..
cd ..

cd sigma05

mkdir kLambda

cd kLambda

mkdir k1
mkdir k2
mkdir k5
mkdir k10
mkdir k20
mkdir k40

cd ..
cd ..

cd sigma1

mkdir kLambda

cd kLambda

mkdir k1
mkdir k2
mkdir k5
mkdir k10
mkdir k20
mkdir k40

cd ..
cd ..

cd sigma2

mkdir kLambda

cd kLambda

mkdir k1
mkdir k2
mkdir k5
mkdir k10
mkdir k20
mkdir k40

cd ..
cd ..

cd sigma4

mkdir kLambda

cd kLambda

mkdir k1
mkdir k2
mkdir k5
mkdir k10
mkdir k20
mkdir k40

cd ..
cd ..

tar -cvf Files.tar Driver.py LangevinPropogator.py Ornstein.py Potential.py WriteData.py GeneratePBS.py

cp Files.tar sigma025/kLambda/k1/Files.tar
cp Files.tar sigma025/kLambda/k2/Files.tar
cp Files.tar sigma025/kLambda/k5/Files.tar
cp Files.tar sigma025/kLambda/k10/Files.tar
cp Files.tar sigma025/kLambda/k20/Files.tar
cp Files.tar sigma025/kLambda/k40/Files.tar

cp Files.tar sigma05/kLambda/k1/Files.tar
cp Files.tar sigma05/kLambda/k2/Files.tar
cp Files.tar sigma05/kLambda/k5/Files.tar
cp Files.tar sigma05/kLambda/k10/Files.tar
cp Files.tar sigma05/kLambda/k20/Files.tar
cp Files.tar sigma05/kLambda/k40/Files.tar

cp Files.tar sigma1/kLambda/k1/Files.tar
cp Files.tar sigma1/kLambda/k2/Files.tar
cp Files.tar sigma1/kLambda/k5/Files.tar
cp Files.tar sigma1/kLambda/k10/Files.tar
cp Files.tar sigma1/kLambda/k20/Files.tar
cp Files.tar sigma1/kLambda/k40/Files.tar

cp Files.tar sigma2/kLambda/k1/Files.tar
cp Files.tar sigma2/kLambda/k2/Files.tar
cp Files.tar sigma2/kLambda/k5/Files.tar
cp Files.tar sigma2/kLambda/k10/Files.tar
cp Files.tar sigma2/kLambda/k20/Files.tar
cp Files.tar sigma2/kLambda/k40/Files.tar

cp Files.tar sigma4/kLambda/k1/Files.tar
cp Files.tar sigma4/kLambda/k2/Files.tar
cp Files.tar sigma4/kLambda/k5/Files.tar
cp Files.tar sigma4/kLambda/k10/Files.tar
cp Files.tar sigma4/kLambda/k20/Files.tar
cp Files.tar sigma4/kLambda/k40/Files.tar

python ParameterMasterGenerator_September.py

cd sigma025
cd kLambda

cd k1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k5
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k10
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k20
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k40
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..
cd ..

cd sigma05
cd kLambda

cd k1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k5
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k10
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k20
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k40
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..
cd ..

cd sigma1
cd kLambda

cd k1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..


cd k5
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k10
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k20
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k40
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..
cd ..

cd sigma2
cd kLambda

cd k1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k5
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k10
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k20
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k40
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..
cd ..

cd sigma4
cd kLambda

cd k1
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k2
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k5
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k10
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k20
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..

cd k40
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..
cd ..


echo "..."
echo "File Structure Generated"
echo "..."



