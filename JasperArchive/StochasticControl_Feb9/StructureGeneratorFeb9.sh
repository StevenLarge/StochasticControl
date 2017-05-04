#!/bin/bash
#This script generates the file structure for simulations at variable kCP values for stochastic control


mkdir TimeSeparation_1
mkdir TimeSeparation_2
mkdir TimeSeparation_4
mkdir TimeSeparation_8
mkdir TimeSeparation_16
mkdir TimeSeparation_32
mkdir TimeSeparation_64

cd TimeSeparation_1
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

cd TimeSeparation_2
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

cd TimeSeparation_4
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

cd TimeSeparation_8
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

cd TimeSeparation_16
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

cd TimeSeparation_32
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

cd TimeSeparation_64
mkdir kCP_1
mkdir kCP_2
mkdir kCP_4
mkdir kCP_8
mkdir kCP_16
mkdir kCP_32
cd ..

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

cp Scripts.tar TimeSeparation_1/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_1/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_1/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_1/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_1/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_1/kCP_32/Scripts.tar

cp Scripts.tar TimeSeparation_2/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_2/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_2/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_2/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_2/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_2/kCP_32/Scripts.tar

cp Scripts.tar TimeSeparation_4/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_4/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_4/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_4/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_4/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_4/kCP_32/Scripts.tar

cp Scripts.tar TimeSeparation_8/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_8/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_8/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_8/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_8/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_8/kCP_32/Scripts.tar

cp Scripts.tar TimeSeparation_16/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_16/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_16/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_16/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_16/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_16/kCP_32/Scripts.tar

cp Scripts.tar TimeSeparation_32/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_32/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_32/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_32/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_32/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_32/kCP_32/Scripts.tar

cp Scripts.tar TimeSeparation_64/kCP_1/Scripts.tar
cp Scripts.tar TimeSeparation_64/kCP_2/Scripts.tar
cp Scripts.tar TimeSeparation_64/kCP_4/Scripts.tar
cp Scripts.tar TimeSeparation_64/kCP_8/Scripts.tar
cp Scripts.tar TimeSeparation_64/kCP_16/Scripts.tar
cp Scripts.tar TimeSeparation_64/kCP_32/Scripts.tar

rm *.tar

cd TimeSeparation_1
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_2
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_4
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_8
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_16
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_32
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..


cd TimeSeparation_64
cd kCP_1
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_2
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_4
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_8
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_16
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd kCP_32
mkdir Output
tar -xvf *.tar
python GeneratePBS.py
rm *.tar
cd ..
cd ..

python TimeParameterMasterWrite.py

cp ParameterMasterWrite.py TimeSeparation_1/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_2/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_4/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_8/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_16/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_32/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_64/ParameterMasterWrite.py

cd TimeSeparation_1
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_2
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_4
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_16
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_32
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_64
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_1
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

cd TimeSeparation_2
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

cd TimeSeparation_4
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

cd TimeSeparation_8
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

cd TimeSeparation_16
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

cd TimeSeparation_32
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

cd TimeSeparation_64
cp TimeParameters.py kCP_1/TimeParameters.py
cp TimeParameters.py kCP_2/TimeParameters.py
cp TimeParameters.py kCP_4/TimeParameters.py
cp TimeParameters.py kCP_8/TimeParameters.py
cp TimeParameters.py kCP_16/TimeParameters.py
cp TimeParameters.py kCP_32/TimeParameters.py
cd ..

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





