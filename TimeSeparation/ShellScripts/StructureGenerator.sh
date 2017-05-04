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
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_2
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_4
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_8
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_16
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_32
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

cd TimeSeparation_64
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..


cd TimeSeparation_128
mkdir k01
mkdir k001
cp Scripts.tar k01/Scripts.tar
cp Scripts.tar k001/Scripts.tar
cd k01
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd k001
mkdir Output
mkdir Trajectories
mkdir AutoCorrelation
tar -xvf *.tar
python GeneratePBS.py
python GeneratePBSFriction.py
rm *.tar
cd ..
cd ..

python TimeParameterMasterWrite.py

cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k01/TimeParameters.py
cp TimeSeparation_1/TimeParameters.py TimeSeparation_1/k001/TimeParameters.py

cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k01/TimeParameters.py
cp TimeSeparation_2/TimeParameters.py TimeSeparation_2/k001/TimeParameters.py

cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k01/TimeParameters.py
cp TimeSeparation_4/TimeParameters.py TimeSeparation_4/k001/TimeParameters.py

cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k01/TimeParameters.py
cp TimeSeparation_8/TimeParameters.py TimeSeparation_8/k001/TimeParameters.py

cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k01/TimeParameters.py
cp TimeSeparation_16/TimeParameters.py TimeSeparation_16/k001/TimeParameters.py

cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k01/TimeParameters.py
cp TimeSeparation_32/TimeParameters.py TimeSeparation_32/k001/TimeParameters.py

cp TimeSeparation_64/TimeParameters.py TimeSeparation_64/k01/TimeParameters.py
cp TimeSeparation_64/TimeParameters.py TimeSeparation_64/k001/TimeParameters.py

cp TimeSeparation_128/TimeParameters.py TimeSeparation_128/k01/TimeParameters.py
cp TimeSeparation_128/TimeParameters.py TimeSeparation_128/k001/TimeParameters.py

rm TimeSeparation_1/TimeParameters.py
rm TimeSeparation_2/TimeParameters.py
rm TimeSeparation_4/TimeParameters.py
rm TimeSeparation_8/TimeParameters.py
rm TimeSeparation_16/TimeParameters.py
rm TimeSeparation_32/TimeParameters.py
rm TimeSeparation_64/TimeParameters.py
rm TimeSeparation_128/TimeParameters.py

cp ParameterMasterWrite.py TimeSeparation_1/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_2/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_4/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_8/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_16/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_32/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_64/ParameterMasterWrite.py
cp ParameterMasterWrite.py TimeSeparation_128/ParameterMasterWrite.py

cd TimeSeparation_1
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_2
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_4
python ParameterMasterWrite.py
cd ..

cd TimeSeparation_8
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

cd TimeSeparation_128
python ParameterMasterWrite.py
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
