#!/bin/bash
#Structure Generator for February 16th data

mkdir TimeSeparation_1
mkdir TimeSeparation_2
mkdir TimeSeparation_4
mkdir TimeSeparation_8
mkdir TimeSeparation_16
mkdir TimeSeparation_32
mkdir TimeSeparation_64

mkdir TimeSeparation_a75_1
mkdir TimeSeparation_a75_2
mkdir TimeSeparation_a75_4
mkdir TimeSeparation_a75_8
mkdir TimeSeparation_a75_16
mkdir TimeSeparation_a75_32
mkdir TimeSeparation_a75_64

mkdir TimeSeparation_a95_1
mkdir TimeSeparation_a95_2
mkdir TimeSeparation_a95_4
mkdir TimeSeparation_a95_8
mkdir TimeSeparation_a95_16
mkdir TimeSeparation_a95_32
mkdir TimeSeparation_a95_64

cd TimeSeparation_1
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_2
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_4
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_8
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_16
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_32
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_64
mkdir Output
mkdir Trajectories
cd ..


cd TimeSeparation_a75_1
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a75_2
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a75_4
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a75_8
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a75_16
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a75_32
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a75_64
mkdir Output
mkdir Trajectories
cd ..


cd TimeSeparation_a95_1
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a95_2
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a95_4
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a95_8
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a95_16
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a95_32
mkdir Output
mkdir Trajectories
cd ..
cd TimeSeparation_a95_64
mkdir Output
mkdir Trajectories
cd ..

python TimeParameterMasterGenerator.py

cp WorkCalculation.py TimeSeparation_1/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_2/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_4/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_8/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_16/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_32/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_64/WorkCalculation.py

cp WorkCalculation.py TimeSeparation_a75_1/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a75_2/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a75_4/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a75_8/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a75_16/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a75_32/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a75_64/WorkCalculation.py

cp WorkCalculation.py TimeSeparation_a95_1/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a95_2/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a95_4/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a95_8/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a95_16/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a95_32/WorkCalculation.py
cp WorkCalculation.py TimeSeparation_a95_64/WorkCalculation.py

cp GeneratePBS.py TimeSeparation_1/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_2/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_4/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_8/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_16/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_32/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_64/GeneratePBS.py

cp GeneratePBS.py TimeSeparation_a75_1/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a75_2/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a75_4/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a75_8/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a75_16/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a75_32/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a75_64/GeneratePBS.py

cp GeneratePBS.py TimeSeparation_a95_1/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a95_2/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a95_4/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a95_8/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a95_16/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a95_32/GeneratePBS.py
cp GeneratePBS.py TimeSeparation_a95_64/GeneratePBS.py


cp Trajectories.tar TimeSeparation_1/Trajectories/Trajectories.tar
cp Trajectories.tar TimeSeparation_2/Trajectories/Trajectories.tar
cp Trajectories.tar TimeSeparation_4/Trajectories/Trajectories.tar
cp Trajectories.tar TimeSeparation_8/Trajectories/Trajectories.tar
cp Trajectories.tar TimeSeparation_16/Trajectories/Trajectories.tar
cp Trajectories.tar TimeSeparation_32/Trajectories/Trajectories.tar
cp Trajectories.tar TimeSeparation_64/Trajectories/Trajectories.tar

cp Trajectories75.tar TimeSeparation_a75_1/Trajectories/Trajectories.tar
cp Trajectories75.tar TimeSeparation_a75_2/Trajectories/Trajectories.tar
cp Trajectories75.tar TimeSeparation_a75_4/Trajectories/Trajectories.tar
cp Trajectories75.tar TimeSeparation_a75_8/Trajectories/Trajectories.tar
cp Trajectories75.tar TimeSeparation_a75_16/Trajectories/Trajectories.tar
cp Trajectories75.tar TimeSeparation_a75_32/Trajectories/Trajectories.tar
cp Trajectories75.tar TimeSeparation_a75_64/Trajectories/Trajectories.tar

cp Trajectories95.tar TimeSeparation_a95_1/Trajectories/Trajectories.tar
cp Trajectories95.tar TimeSeparation_a95_2/Trajectories/Trajectories.tar
cp Trajectories95.tar TimeSeparation_a95_4/Trajectories/Trajectories.tar
cp Trajectories95.tar TimeSeparation_a95_8/Trajectories/Trajectories.tar
cp Trajectories95.tar TimeSeparation_a95_16/Trajectories/Trajectories.tar
cp Trajectories95.tar TimeSeparation_a95_32/Trajectories/Trajectories.tar
cp Trajectories95.tar TimeSeparation_a95_64/Trajectories/Trajectories.tar

cd TimeSeparation_1/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_2/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_4/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_8/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_16/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_32/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_64/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

cd TimeSeparation_a75_1/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a75_2/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a75_4/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a75_8/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a75_16/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a75_32/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a75_64/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..

cd TimeSeparation_a95_1/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a95_2/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a95_4/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a95_8/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a95_16/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a95_32/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..
cd TimeSeparation_a95_64/Trajectories
tar -xvf *.tar
python GeneratePBS.py
cd ..
cd ..





