#!/bin/bash
#Master structure generator for constant velocity ensemble simulations

mkdir dLambda_5
mkdir dLambda_10
mkdir dLambda_20
mkdir dLambda_40
mkdir dLambda_80


mkdir dLambda_5/k1
mkdir dLambda_5/k2
mkdir dLambda_5/k4
mkdir dLambda_5/k8
mkdir dLambda_5/k16

mkdir dLambda_10/k1
mkdir dLambda_10/k2
mkdir dLambda_10/k4
mkdir dLambda_10/k8
mkdir dLambda_10/k16

mkdir dLambda_20/k1
mkdir dLambda_20/k2
mkdir dLambda_20/k4
mkdir dLambda_20/k8
mkdir dLambda_20/k16

mkdir dLambda_40/k1
mkdir dLambda_40/k2
mkdir dLambda_40/k4
mkdir dLambda_40/k8
mkdir dLambda_40/k16

mkdir dLambda_80/k1
mkdir dLambda_80/k2
mkdir dLambda_80/k4
mkdir dLambda_80/k8
mkdir dLambda_80/k16


mkdir dLambda_5/k1/Output
mkdir dLambda_5/k2/Output
mkdir dLambda_5/k4/Output
mkdir dLambda_5/k8/Output
mkdir dLambda_5/k16/Output

mkdir dLambda_10/k1/Output
mkdir dLambda_10/k2/Output
mkdir dLambda_10/k4/Output
mkdir dLambda_10/k8/Output
mkdir dLambda_10/k16/Output

mkdir dLambda_20/k1/Output
mkdir dLambda_20/k2/Output
mkdir dLambda_20/k4/Output
mkdir dLambda_20/k8/Output
mkdir dLambda_20/k16/Output

mkdir dLambda_40/k1/Output
mkdir dLambda_40/k2/Output
mkdir dLambda_40/k4/Output
mkdir dLambda_40/k8/Output
mkdir dLambda_40/k16/Output

mkdir dLambda_80/k1/Output
mkdir dLambda_80/k2/Output
mkdir dLambda_80/k4/Output
mkdir dLambda_80/k8/Output
mkdir dLambda_80/k16/Output



tar -cvf SuperScripts.tar GeneratePBS.py ConstantVelocityPrimary.py LangevinPropogator.py WriteData.py ConstantDriver.py StructureGenerator.sh VelocityParameterMasterGenerator.py

cp SuperScripts.tar dLambda_5/k1/SuperScripts.tar
cp SuperScripts.tar dLambda_5/k2/SuperScripts.tar
cp SuperScripts.tar dLambda_5/k4/SuperScripts.tar
cp SuperScripts.tar dLambda_5/k8/SuperScripts.tar
cp SuperScripts.tar dLambda_5/k16/SuperScripts.tar

cp SuperScripts.tar dLambda_10/k1/SuperScripts.tar
cp SuperScripts.tar dLambda_10/k2/SuperScripts.tar
cp SuperScripts.tar dLambda_10/k4/SuperScripts.tar
cp SuperScripts.tar dLambda_10/k8/SuperScripts.tar
cp SuperScripts.tar dLambda_10/k16/SuperScripts.tar

cp SuperScripts.tar dLambda_20/k1/SuperScripts.tar
cp SuperScripts.tar dLambda_20/k2/SuperScripts.tar
cp SuperScripts.tar dLambda_20/k4/SuperScripts.tar
cp SuperScripts.tar dLambda_20/k8/SuperScripts.tar
cp SuperScripts.tar dLambda_20/k16/SuperScripts.tar

cp SuperScripts.tar dLambda_40/k1/SuperScripts.tar
cp SuperScripts.tar dLambda_40/k2/SuperScripts.tar
cp SuperScripts.tar dLambda_40/k4/SuperScripts.tar
cp SuperScripts.tar dLambda_40/k8/SuperScripts.tar
cp SuperScripts.tar dLambda_40/k16/SuperScripts.tar

cp SuperScripts.tar dLambda_80/k1/SuperScripts.tar
cp SuperScripts.tar dLambda_80/k2/SuperScripts.tar
cp SuperScripts.tar dLambda_80/k4/SuperScripts.tar
cp SuperScripts.tar dLambda_80/k8/SuperScripts.tar
cp SuperScripts.tar dLambda_80/k16/SuperScripts.tar

python ParameterMasterGenerator.py

cd dLambda_5
cd k1
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k2
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k4
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k8
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k16
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd ..


cd dLambda_10
cd k1
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k2
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k4
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k8
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k16
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd ..


cd dLambda_20
cd k1
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k2
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k4
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k8
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k16
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd ..


cd dLambda_40
cd k1
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k2
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k4
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k8
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k16
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd ..


cd dLambda_80
cd k1
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k2
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k4
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k8
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd k16
tar -xvf SuperScripts.tar
rm *.tar
./StructureGenerator.sh
cd ..
cd ..



