#!/bin/bash
#This is a structure generator for a trivially parallelizable implementation of stochastic control, 
#where we average over a small number of trajectories

mkdir TimeSeparation2_512
mkdir TimeSeparation2_1024
mkdir TimeSeparation2_2048
mkdir TimeSeparation2_4096
mkdir TimeSeparation2_8192

tar -cvf Scripts.tar TimePrimary.py Parameters.py GeneratePBS.py GeneratePBSFriction.py TimeDriverLocal.py WriteData.py WorkTheoryModule.py Potential.py LangevinPropogator.py FrictionCalculation.py FrictionTestPrimary.py

cd TimeSeparation2_512
mkdir Repetition1
cd Repetition1
mkdir Output
cd ..
mkdir Repetition2
cd Repetition2
mkdir Output
cd ..
mkdir Repetition3
cd Repetition3
mkdir Output
cd ..
mkdir Repetition4
cd Repetition4
mkdir Output
cd ..
mkdir Repetition5
cd Repetition5
mkdir Output
cd ..
mkdir Repetition6
cd Repetition6
mkdir Output
cd ..
mkdir Repetition7
cd Repetition7
mkdir Output
cd ..
mkdir Repetition8
cd Repetition8
mkdir Output
cd ..
mkdir Repetition9
cd Repetition9
mkdir Output
cd ..
mkdir Repetition10
cd Repetition10
mkdir Output
cd ..
cd ..

cd TimeSeparation2_1024
mkdir Repetition1
cd Repetition1
mkdir Output
cd ..
mkdir Repetition2
cd Repetition2
mkdir Output
cd ..
mkdir Repetition3
cd Repetition3
mkdir Output
cd ..
mkdir Repetition4
cd Repetition4
mkdir Output
cd ..
mkdir Repetition5
cd Repetition5
mkdir Output
cd ..
mkdir Repetition6
cd Repetition6
mkdir Output
cd ..
mkdir Repetition7
cd Repetition7
mkdir Output
cd ..
mkdir Repetition8
cd Repetition8
mkdir Output
cd ..
mkdir Repetition9
cd Repetition9
mkdir Output
cd ..
mkdir Repetition10
cd Repetition10
mkdir Output
cd ..
cd ..

cd TimeSeparation2_2048
mkdir Repetition1
cd Repetition1
mkdir Output
cd ..
mkdir Repetition2
cd Repetition2
mkdir Output
cd ..
mkdir Repetition3
cd Repetition3
mkdir Output
cd ..
mkdir Repetition4
cd Repetition4
mkdir Output
cd ..
mkdir Repetition5
cd Repetition5
mkdir Output
cd ..
mkdir Repetition6
cd Repetition6
mkdir Output
cd ..
mkdir Repetition7
cd Repetition7
mkdir Output
cd ..
mkdir Repetition8
cd Repetition8
mkdir Output
cd ..
mkdir Repetition9
cd Repetition9
mkdir Output
cd ..
mkdir Repetition10
cd Repetition10
mkdir Output
cd ..
cd ..

cd TimeSeparation2_4096
mkdir Repetition1
cd Repetition1
mkdir Output
cd ..
mkdir Repetition2
cd Repetition2
mkdir Output
cd ..
mkdir Repetition3
cd Repetition3
mkdir Output
cd ..
mkdir Repetition4
cd Repetition4
mkdir Output
cd ..
mkdir Repetition5
cd Repetition5
mkdir Output
cd ..
mkdir Repetition6
cd Repetition6
mkdir Output
cd ..
mkdir Repetition7
cd Repetition7
mkdir Output
cd ..
mkdir Repetition8
cd Repetition8
mkdir Output
cd ..
mkdir Repetition9
cd Repetition9
mkdir Output
cd ..
mkdir Repetition10
cd Repetition10
mkdir Output
cd ..
cd ..

cd TimeSeparation2_8192
mkdir Repetition1
cd Repetition1
mkdir Output
cd ..
mkdir Repetition2
cd Repetition2
mkdir Output
cd ..
mkdir Repetition3
cd Repetition3
mkdir Output
cd ..
mkdir Repetition4
cd Repetition4
mkdir Output
cd ..
mkdir Repetition5
cd Repetition5
mkdir Output
cd ..
mkdir Repetition6
cd Repetition6
mkdir Output
cd ..
mkdir Repetition7
cd Repetition7
mkdir Output
cd ..
mkdir Repetition8
cd Repetition8
mkdir Output
cd ..
mkdir Repetition9
cd Repetition9
mkdir Output
cd ..
mkdir Repetition10
cd Repetition10
mkdir Output
cd ..
cd ..

cp Scripts.tar TimeSeparation2_512/Repetition1/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition2/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition3/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition4/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition5/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition6/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition7/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition8/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition9/Scripts.tar
cp Scripts.tar TimeSeparation2_512/Repetition10/Scripts.tar

cp Scripts.tar TimeSeparation2_1024/Repetition1/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition2/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition3/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition4/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition5/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition6/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition7/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition8/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition9/Scripts.tar
cp Scripts.tar TimeSeparation2_1024/Repetition10/Scripts.tar

cp Scripts.tar TimeSeparation2_2048/Repetition1/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition2/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition3/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition4/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition5/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition6/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition7/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition8/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition9/Scripts.tar
cp Scripts.tar TimeSeparation2_2048/Repetition10/Scripts.tar

cp Scripts.tar TimeSeparation2_4096/Repetition1/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition2/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition3/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition4/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition5/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition6/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition7/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition8/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition9/Scripts.tar
cp Scripts.tar TimeSeparation2_4096/Repetition10/Scripts.tar

cp Scripts.tar TimeSeparation2_8192/Repetition1/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition2/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition3/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition4/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition5/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition6/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition7/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition8/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition9/Scripts.tar
cp Scripts.tar TimeSeparation2_8192/Repetition10/Scripts.tar

cd TimeSeparation2_512
cd Repetition1
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition2
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition3
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition4
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition5
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition6
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition7
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition8
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition9
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition10
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

cd TimeSeparation2_1024
cd Repetition1
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition2
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition3
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition4
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition5
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition6
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition7
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition8
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition9
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition10
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

cd TimeSeparation2_2048
cd Repetition1
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition2
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition3
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition4
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition5
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition6
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition7
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition8
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition9
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition10
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

cd TimeSeparation2_4096
cd Repetition1
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition2
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition3
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition4
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition5
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition6
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition7
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition8
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition9
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition10
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

cd TimeSeparation2_8192
cd Repetition1
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition2
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition3
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition4
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition5
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition6
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition7
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition8
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition9
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd Repetition10
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

rm Scripts.tar

python TimeParameterMasterWriteParallel.py

cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition1/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition2/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition3/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition4/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition5/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition6/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition7/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition8/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition9/TimeParameters.py
cp TimeSeparation2_512/TimeParameters.py TimeSeparation2_512/Repetition10/TimeParameters.py

cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition1/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition2/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition3/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition4/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition5/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition6/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition7/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition8/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition9/TimeParameters.py
cp TimeSeparation2_1024/TimeParameters.py TimeSeparation2_1024/Repetition10/TimeParameters.py

cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition1/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition2/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition3/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition4/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition5/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition6/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition7/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition8/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition9/TimeParameters.py
cp TimeSeparation2_2048/TimeParameters.py TimeSeparation2_2048/Repetition10/TimeParameters.py

cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition1/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition2/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition3/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition4/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition5/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition6/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition7/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition8/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition9/TimeParameters.py
cp TimeSeparation2_4096/TimeParameters.py TimeSeparation2_4096/Repetition10/TimeParameters.py

cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition1/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition2/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition3/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition4/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition5/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition6/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition7/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition8/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition9/TimeParameters.py
cp TimeSeparation2_8192/TimeParameters.py TimeSeparation2_8192/Repetition10/TimeParameters.py


rm TimeSeparation2_512/TimeParameters.py
rm TimeSeparation2_1024/TimeParameters.py
rm TimeSeparation2_2048/TimeParameters.py
rm TimeSeparation2_4096/TimeParameters.py
rm TimeSeparation2_8192/TimeParameters.py


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



