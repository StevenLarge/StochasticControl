#!/bin/bash
#Structure Generator script for CPGenerator simulations at various distances and damping strengths

mkdir dLambda_5
mkdir dLambda_10
mkdir dLambda_20
mkdir dLambda_40
mkdir dLambda_80

cd dLambda_5
mkdir Trajectories_a30
mkdir Trajectories_a50
mkdir Trajectories_a70
mkdir Trajectories_a80
mkdir Trajectories_a90
mkdir Trajectories_a95
mkdir Trajectories_a99
cd ..

cd dLambda_10
mkdir Trajectories_a30
mkdir Trajectories_a50
mkdir Trajectories_a70
mkdir Trajectories_a80
mkdir Trajectories_a90
mkdir Trajectories_a95
mkdir Trajectories_a99
cd ..

cd dLambda_20
mkdir Trajectories_a30
mkdir Trajectories_a50
mkdir Trajectories_a70
mkdir Trajectories_a80
mkdir Trajectories_a90
mkdir Trajectories_a95
mkdir Trajectories_a99
cd ..

cd dLambda_40
mkdir Trajectories_a30
mkdir Trajectories_a50
mkdir Trajectories_a70
mkdir Trajectories_a80
mkdir Trajectories_a90
mkdir Trajectories_a95
mkdir Trajectories_a99
cd ..

cd dLambda_80
mkdir Trajectories_a30
mkdir Trajectories_a50
mkdir Trajectories_a70
mkdir Trajectories_a80
mkdir Trajectories_a90
mkdir Trajectories_a95
mkdir Trajectories_a99
cd ..

python dLambdaParameterGenerator.py
python DampingParameterGenerator.py

cp CPGenScripts.tar dLambda_5/Trajectories_a30/CPGenScripts.tar
cp CPGenScripts.tar dLambda_5/Trajectories_a50/CPGenScripts.tar
cp CPGenScripts.tar dLambda_5/Trajectories_a70/CPGenScripts.tar
cp CPGenScripts.tar dLambda_5/Trajectories_a80/CPGenScripts.tar
cp CPGenScripts.tar dLambda_5/Trajectories_a90/CPGenScripts.tar
cp CPGenScripts.tar dLambda_5/Trajectories_a95/CPGenScripts.tar
cp CPGenScripts.tar dLambda_5/Trajectories_a99/CPGenScripts.tar


cp CPGenScripts.tar dLambda_10/Trajectories_a30/CPGenScripts.tar
cp CPGenScripts.tar dLambda_10/Trajectories_a50/CPGenScripts.tar
cp CPGenScripts.tar dLambda_10/Trajectories_a70/CPGenScripts.tar
cp CPGenScripts.tar dLambda_10/Trajectories_a80/CPGenScripts.tar
cp CPGenScripts.tar dLambda_10/Trajectories_a90/CPGenScripts.tar
cp CPGenScripts.tar dLambda_10/Trajectories_a95/CPGenScripts.tar
cp CPGenScripts.tar dLambda_10/Trajectories_a99/CPGenScripts.tar


cp CPGenScripts.tar dLambda_20/Trajectories_a30/CPGenScripts.tar
cp CPGenScripts.tar dLambda_20/Trajectories_a50/CPGenScripts.tar
cp CPGenScripts.tar dLambda_20/Trajectories_a70/CPGenScripts.tar
cp CPGenScripts.tar dLambda_20/Trajectories_a80/CPGenScripts.tar
cp CPGenScripts.tar dLambda_20/Trajectories_a90/CPGenScripts.tar
cp CPGenScripts.tar dLambda_20/Trajectories_a95/CPGenScripts.tar
cp CPGenScripts.tar dLambda_20/Trajectories_a99/CPGenScripts.tar


cp CPGenScripts.tar dLambda_40/Trajectories_a30/CPGenScripts.tar
cp CPGenScripts.tar dLambda_40/Trajectories_a50/CPGenScripts.tar
cp CPGenScripts.tar dLambda_40/Trajectories_a70/CPGenScripts.tar
cp CPGenScripts.tar dLambda_40/Trajectories_a80/CPGenScripts.tar
cp CPGenScripts.tar dLambda_40/Trajectories_a90/CPGenScripts.tar
cp CPGenScripts.tar dLambda_40/Trajectories_a95/CPGenScripts.tar
cp CPGenScripts.tar dLambda_40/Trajectories_a99/CPGenScripts.tar


cp CPGenScripts.tar dLambda_80/Trajectories_a30/CPGenScripts.tar
cp CPGenScripts.tar dLambda_80/Trajectories_a50/CPGenScripts.tar
cp CPGenScripts.tar dLambda_80/Trajectories_a70/CPGenScripts.tar
cp CPGenScripts.tar dLambda_80/Trajectories_a80/CPGenScripts.tar
cp CPGenScripts.tar dLambda_80/Trajectories_a90/CPGenScripts.tar
cp CPGenScripts.tar dLambda_80/Trajectories_a95/CPGenScripts.tar
cp CPGenScripts.tar dLambda_80/Trajectories_a99/CPGenScripts.tar



cd dLambda_5
cd Trajectories_a30
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a50
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a70
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a80
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a90
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a95
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a99
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd ..


cd dLambda_10
cd Trajectories_a30
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a50
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a70
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a80
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a90
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a95
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a99
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd ..


cd dLambda_20
cd Trajectories_a30
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a50
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a70
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a80
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a90
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a95
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a99
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd ..


cd dLambda_40
cd Trajectories_a30
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a50
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a70
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a80
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a90
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a95
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a99
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd ..


cd dLambda_80
cd Trajectories_a30
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a50
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a70
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a80
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a90
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a95
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd Trajectories_a99
tar -xvf CPGenScripts.tar
rm *.tar
cd ..
cd ..
